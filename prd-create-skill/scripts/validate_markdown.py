#!/usr/bin/env python3
"""Validate a final portable Markdown PRD."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO)\b|暂定方案|以后补充|待补充", re.IGNORECASE)
PAGE_HEADING_RE = re.compile(r"^###\s+([A-Za-z0-9][A-Za-z0-9._-]*)\s+.+$", re.MULTILINE)
PAGE_SECTION_RE = re.compile(r"^##\s+(?:页面需求|Page Requirements)\s*$", re.MULTILINE | re.IGNORECASE)
IMAGE_START_RE = re.compile(r"!\[[^\]]*\]\(")
LINK_START_RE = re.compile(r"(?<!!)\[[^\]]+\]\(")
PENDING_SECTION_RE = re.compile(
    r"^#{1,6}\s+.*(?:待确认问题|待确认事项|Pending Questions|Open Questions|Unresolved Decisions).*$",
    re.MULTILINE | re.IGNORECASE,
)


def _page_region(text: str) -> str:
    start_match = PAGE_SECTION_RE.search(text)
    if not start_match:
        return ""
    rest = text[start_match.end() :]
    end_match = re.search(r"^##\s+", rest, re.MULTILINE)
    return rest[: end_match.start()] if end_match else rest


def _page_sections(text: str) -> list[tuple[str, str]]:
    region = _page_region(text)
    matches = list(PAGE_HEADING_RE.finditer(region))
    sections = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(region)
        sections.append((match.group(1), region[match.start() : end]))
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


def _is_external_or_absolute(target: str) -> bool:
    parsed = urlsplit(target)
    return bool(parsed.scheme or parsed.netloc or target.startswith(("/", "~")) or re.match(r"^[A-Za-z]:[\\/]", target))


def _count_table_cells(line: str) -> int:
    content = line.strip().strip("|")
    return len(re.split(r"(?<!\\)\|", content))


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
        if row < len(lines) and lines[row].strip() and "|" not in lines[row]:
            issues.append(f"Table row at line {row + 1} has no column separators.")
        while row < len(lines) and lines[row].strip() and "|" in lines[row]:
            if _count_table_cells(lines[row]) != expected:
                issues.append(f"Table row at line {row + 1} has inconsistent columns.")
            row += 1
    return issues


def _validate_mermaid(text: str) -> list[str]:
    issues = []
    lines = text.splitlines()
    in_mermaid = False
    starts = 0
    content: list[str] = []
    for line_number, line in enumerate(lines, 1):
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
            elif re.match(r"^(?:flowchart|graph)\b", first, re.IGNORECASE):
                for statement in content[1:]:
                    candidate = statement.strip()
                    if not candidate or candidate.startswith("%%"):
                        continue
                    edge = re.split(r"(?:-->|---|-\.->|==>)", candidate, maxsplit=1)
                    if len(edge) == 2:
                        right = re.sub(r"^\|[^|]*\|\s*", "", edge[1].strip())
                        if not right or not re.match(r"^[A-Za-z0-9_]", right):
                            issues.append("Mermaid syntax contains an incomplete flow edge.")
                            break
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


def validate_markdown(path: Path) -> list[str]:
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []

    if PLACEHOLDER_RE.search(text):
        issues.append("Unresolved placeholder found in final Markdown.")
    if PENDING_SECTION_RE.search(text):
        issues.append("Final Markdown must not contain 待确认问题 or any pending questions section.")

    issues.extend(_validate_headings(text))
    issues.extend(_validate_tables(text))
    issues.extend(_validate_mermaid(text))

    page_ids = PAGE_HEADING_RE.findall(_page_region(text))
    duplicates = sorted(page_id for page_id, count in Counter(page_ids).items() if count > 1)
    for page_id in duplicates:
        issues.append(f"Duplicate page ID: {page_id}.")
    if not page_ids:
        issues.append("No page requirement headings were found.")

    for page_id, section in _page_sections(text):
        if not re.search(r"^####\s+(?:Acceptance Criteria|验收标准)\s*$", section, re.MULTILINE | re.IGNORECASE):
            issues.append(f"Page {page_id} is missing an Acceptance Criteria section.")
        if not _extract_targets(section, image=True):
            issues.append(f"Page {page_id} has no traceable prototype image.")

    for raw_target in _extract_targets(text, image=True):
        target = _target(raw_target)
        if _is_external_or_absolute(target):
            issues.append(f"Prototype must use a relative image path: {target}.")
            continue
        image_path = (path.parent / target).resolve()
        if not image_path.is_file():
            issues.append(f"Missing image: {target}.")

    anchors = _heading_anchors(text)
    for raw_target in _extract_targets(text, image=False):
        target = _target(raw_target)
        if target.startswith("#"):
            if unquote(target[1:]).lower() not in anchors:
                issues.append(f"Broken internal link: {target}.")
            continue
        if _is_external_or_absolute(target):
            continue
        local_target = target.split("#", 1)[0]
        if local_target and not (path.parent / local_target).resolve().exists():
            issues.append(f"Broken local link: {target}.")

    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path, help="Markdown PRD path")
    args = parser.parse_args(argv)

    issues = validate_markdown(args.document)
    if issues:
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1
    print("OK: Markdown PRD validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
