#!/usr/bin/env python3
"""Validate a final portable Markdown PRD in full-spec or review-table form."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO)\b|暂定方案|以后补充|待补充", re.IGNORECASE)
PAGE_HEADING_RE = re.compile(r"^###\s+([A-Za-z0-9][A-Za-z0-9._-]*)\s+.+$", re.MULTILINE)
SECTION_HEADING_RE = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)
PAGE_SECTION_RE = re.compile(r"^##\s+(?:页面需求|Page Requirements)\s*$", re.MULTILINE | re.IGNORECASE)
IMAGE_START_RE = re.compile(r"!\[[^\]]*\]\(")
LINK_START_RE = re.compile(r"(?<!!)\[[^\]]+\]\(")
PENDING_SECTION_RE = re.compile(
    r"^#{1,6}\s+.*(?:待确认问题|待确认事项|Pending Questions|Open Questions|Unresolved Decisions).*$",
    re.MULTILINE | re.IGNORECASE,
)
PROFILE_MARKER_RE = re.compile(r"<!--\s*prd-profile:\s*(full-spec|review-table)\s*-->", re.IGNORECASE)


def _page_region(text: str) -> str:
    start_match = PAGE_SECTION_RE.search(text)
    if not start_match:
        return ""
    rest = text[start_match.end() :]
    end_match = re.search(r"^##\s+", rest, re.MULTILINE)
    return rest[: end_match.start()] if end_match else rest


def _sections(text: str, pattern: re.Pattern[str]) -> list[tuple[str, str]]:
    region = _page_region(text)
    matches = list(pattern.finditer(region))
    sections = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(region)
        sections.append((match.group(1).strip(), region[match.start() : end]))
    return sections


def _target(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and value.endswith(">"):
        return unquote(value[1:-1].strip())
    title_match = re.match(r"^(.*?)(?:\s+[\"'][^\"']*[\"'])$", value)
    return unquote((title_match.group(1) if title_match else value).strip())


def _extract_targets(text: str, image: bool) -> list[str]:
    pattern = IMAGE_START_RE if image else LINK_START_RE
    targets = []
    for match in pattern.finditer(text):
        start = match.end()
        index = start
        depth = 1
        in_angle = False
        escaped = False
        while index < len(text):
            char = text[index]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "<" and depth == 1:
                in_angle = True
            elif char == ">" and in_angle:
                in_angle = False
            elif not in_angle and char == "(":
                depth += 1
            elif not in_angle and char == ")":
                depth -= 1
                if depth == 0:
                    targets.append(text[start:index])
                    break
            index += 1
    return targets


def _target_kind(target: str) -> str:
    parsed = urlsplit(target)
    if parsed.scheme.lower() in {"http", "https"} and parsed.netloc:
        return "external"
    if parsed.scheme or parsed.netloc or target.startswith(("/", "~")) or re.match(r"^[A-Za-z]:[\\/]", target):
        return "absolute"
    return "relative"


def _split_cells(line: str) -> list[str]:
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def _count_table_cells(line: str) -> int:
    return len(_split_cells(line))


def _table_blocks(text: str) -> list[tuple[list[str], list[list[str]]]]:
    lines = text.splitlines()
    delimiter = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")
    blocks: list[tuple[list[str], list[list[str]]]] = []
    for index, line in enumerate(lines):
        if not delimiter.match(line) or index == 0 or "|" not in lines[index - 1]:
            continue
        header = _split_cells(lines[index - 1])
        rows: list[list[str]] = []
        row = index + 1
        while row < len(lines) and lines[row].strip() and "|" in lines[row]:
            rows.append(_split_cells(lines[row]))
            row += 1
        blocks.append((header, rows))
    return blocks


def _is_prototype_requirement_table(header: list[str]) -> bool:
    joined = " ".join(header).lower()
    has_prototype = any(token in joined for token in ("prototype", "原型", "页面示意", "样式"))
    has_requirement = any(token in joined for token in ("requirement", "需求", "逻辑", "规则", "说明"))
    return has_prototype and has_requirement and len(header) == 2


def _validate_headings(text: str) -> list[str]:
    issues = []
    in_fence = False
    previous_level = 0
    for line_number, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(#{1,6})\s+", line)
        if not match:
            continue
        level = len(match.group(1))
        if previous_level and level > previous_level + 1:
            issues.append(f"Heading level jumps from H{previous_level} to H{level} at line {line_number}.")
        previous_level = level
    return issues


def _validate_tables(text: str) -> list[str]:
    issues = []
    lines = text.splitlines()
    delimiter = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")
    for index, line in enumerate(lines):
        if not delimiter.match(line):
            continue
        if index == 0 or "|" not in lines[index - 1]:
            issues.append(f"Table delimiter at line {index + 1} has no header row.")
            continue
        expected = _count_table_cells(lines[index - 1])
        if _count_table_cells(line) != expected:
            issues.append(f"Table delimiter at line {index + 1} has inconsistent columns.")
        row = index + 1
        while row < len(lines) and lines[row].strip() and "|" in lines[row]:
            if _count_table_cells(lines[row]) != expected:
                issues.append(f"Table row at line {row + 1} has inconsistent columns.")
            row += 1
    return issues


def _validate_mermaid(text: str) -> list[str]:
    issues = []
    lines = text.splitlines()
    in_mermaid = False
    content: list[str] = []
    starts = 0
    for line in lines:
        if not in_mermaid and line.strip().lower() == "```mermaid":
            in_mermaid = True
            starts += 1
            content = []
        elif in_mermaid and line.strip() == "```":
            first = next((item.strip() for item in content if item.strip()), "")
            if not re.match(
                r"^(?:flowchart|graph|sequenceDiagram|stateDiagram(?:-v2)?|erDiagram|journey|gantt|timeline|classDiagram|mindmap|pie|quadrantChart|xychart)\b",
                first,
                re.IGNORECASE,
            ):
                issues.append("Mermaid syntax must start with a supported diagram declaration.")
            in_mermaid = False
        elif in_mermaid:
            content.append(line)
    if in_mermaid:
        issues.append("Mermaid code fence is not closed.")
    if starts and not re.search(r"(?:流程步骤|文字步骤|Text Steps)", text, re.IGNORECASE):
        issues.append("Mermaid flow is missing a readable text-steps fallback.")
    return issues


def _heading_anchors(text: str) -> set[str]:
    anchors = set()
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if not match:
            continue
        slug = match.group(1).strip().lower()
        slug = re.sub(r"[^\w\- ]", "", slug, flags=re.UNICODE)
        slug = re.sub(r"\s+", "-", slug)
        slug = re.sub(r"-+", "-", slug).strip("-")
        if slug:
            anchors.add(slug)
    return anchors


def _validate_full_spec(text: str, acceptance_detail: str) -> list[str]:
    issues = []
    sections = _sections(text, PAGE_HEADING_RE)
    page_ids = [page_id for page_id, _ in sections]
    for page_id, count in Counter(page_ids).items():
        if count > 1:
            issues.append(f"Duplicate page ID: {page_id}.")
    if not page_ids:
        issues.append("No full-spec page requirement headings were found.")
    for page_id, section in sections:
        if acceptance_detail != "none" and not re.search(
            r"^####\s+(?:Acceptance Criteria|验收标准)\s*$", section, re.MULTILINE | re.IGNORECASE
        ):
            issues.append(f"Page {page_id} is missing an Acceptance Criteria section.")
        if not _extract_targets(section, image=True):
            issues.append(f"Page {page_id} has no traceable prototype image.")
    return issues


def _validate_review_table(text: str) -> list[str]:
    issues = []
    sections = _sections(text, SECTION_HEADING_RE)
    names = [name for name, _ in sections]
    for name, count in Counter(names).items():
        if count > 1:
            issues.append(f"Duplicate test-point heading: {name}.")
    if not sections:
        return ["No review-table test-point headings were found."]

    for name, section in sections:
        matching = [(header, rows) for header, rows in _table_blocks(section) if _is_prototype_requirement_table(header)]
        if len(matching) != 1:
            issues.append(f"Test point {name} must contain exactly one two-column prototype/requirement table.")
            continue
        _, rows = matching[0]
        if not rows:
            issues.append(f"Test point {name} has no variant rows.")
            continue
        for index, row in enumerate(rows, 1):
            if len(row) != 2:
                continue
            if not _extract_targets(row[0], image=True):
                issues.append(f"Test point {name} variant row {index} has no prototype image.")
            if not re.search(r"\w|[\u4e00-\u9fff]", re.sub(r"<br\s*/?>", " ", row[1], flags=re.IGNORECASE)):
                issues.append(f"Test point {name} variant row {index} has no requirement logic.")
    return issues


def _detect_profile(text: str) -> str:
    marker = PROFILE_MARKER_RE.search(text)
    if marker:
        return marker.group(1).lower()
    sections = _sections(text, SECTION_HEADING_RE)
    has_review_table = False
    for _, section in sections:
        for header, rows in _table_blocks(section):
            if _is_prototype_requirement_table(header):
                has_review_table = True
                if len(rows) > 1:
                    return "review-table"
    if has_review_table and not all(
        re.search(r"^####\s+(?:Acceptance Criteria|验收标准)\s*$", section, re.MULTILINE | re.IGNORECASE)
        for _, section in sections
    ):
        return "review-table"
    return "full-spec"


def validate_markdown(
    path: Path,
    profile: str = "auto",
    image_mode: str = "relative",
    acceptance_detail: str = "concise",
) -> list[str]:
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []

    if PLACEHOLDER_RE.search(text):
        issues.append("Unresolved placeholder found in final Markdown.")
    if PENDING_SECTION_RE.search(text):
        issues.append("Final Markdown must not contain a pending-questions section.")
    if not PAGE_SECTION_RE.search(text):
        issues.append("No 页面需求 or Page Requirements section was found.")

    issues.extend(_validate_headings(text))
    issues.extend(_validate_tables(text))
    issues.extend(_validate_mermaid(text))

    selected_profile = _detect_profile(text) if profile == "auto" else profile
    if selected_profile == "review-table":
        issues.extend(_validate_review_table(text))
    else:
        issues.extend(_validate_full_spec(text, acceptance_detail))

    for raw_target in _extract_targets(text, image=True):
        target = _target(raw_target)
        kind = _target_kind(target)
        if kind == "absolute":
            issues.append(f"Prototype must not use an absolute local or unsupported path: {target}.")
        elif kind == "external":
            if image_mode not in {"external", "mixed"}:
                issues.append(f"External prototype does not match image mode {image_mode}: {target}.")
        else:
            if image_mode == "external":
                issues.append(f"Relative prototype does not match image mode external: {target}.")
            elif not (path.parent / target).resolve().is_file():
                issues.append(f"Missing image: {target}.")

    anchors = _heading_anchors(text)
    for raw_target in _extract_targets(text, image=False):
        target = _target(raw_target)
        if target.startswith("#"):
            if unquote(target[1:]).lower() not in anchors:
                issues.append(f"Broken internal link: {target}.")
            continue
        if _target_kind(target) != "relative":
            continue
        local_target = target.split("#", 1)[0]
        if local_target and not (path.parent / local_target).resolve().exists():
            issues.append(f"Broken local link: {target}.")

    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path, help="Markdown PRD path")
    parser.add_argument("--profile", choices=("auto", "full-spec", "review-table"), default="auto")
    parser.add_argument("--image-mode", choices=("relative", "external", "mixed"), default="relative")
    parser.add_argument("--acceptance-detail", choices=("none", "concise", "detailed"), default="concise")
    args = parser.parse_args(argv)

    issues = validate_markdown(args.document, args.profile, args.image_mode, args.acceptance_detail)
    if issues:
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1
    print("OK: Markdown PRD validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
