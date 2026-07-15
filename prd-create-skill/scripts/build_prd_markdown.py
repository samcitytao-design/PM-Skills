#!/usr/bin/env python3
"""Render a portable Markdown PRD from the documented JSON model."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Iterable


SECTION_NAMES = {
    "sources": "来源与页面映射",
    "actors": "角色与权限",
    "flows": "核心流程",
    "states": "全局状态",
    "rules": "业务规则与配置",
    "data": "数据与内容规则",
    "dependencies": "外部依赖",
    "risks": "异常、恢复与约束",
    "measurement": "分析与度量",
}


def _text(value: Any) -> str:
    return str(value or "").strip()


def _items(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [_text(item) for item in value if _text(item)]
    text = _text(value)
    return [text] if text else []


def _escape_cell(value: Any) -> str:
    return _text(value).replace("|", "\\|").replace("\n", "<br>")


def _numbered_cell(label: str, values: Iterable[str]) -> str:
    clean = [_escape_cell(value) for value in values if _text(value)]
    if not clean:
        return ""
    entries = "<br>".join(f"{index}. {value}" for index, value in enumerate(clean, 1))
    return f"**{label}**<br>{entries}"


def _bullet_section(title: str, values: Any, level: int = 3) -> list[str]:
    items = _items(values)
    if not items:
        return []
    lines = [f"{'#' * level} {title}", ""]
    lines.extend(f"- {item}" for item in items)
    lines.append("")
    return lines


def _label(key: str) -> str:
    return key.replace("_", " ").strip().title()


def _render_structured(value: Any, heading_level: int = 3) -> list[str]:
    if value is None or value == [] or value == {} or value == "":
        return []
    if isinstance(value, (str, int, float, bool)):
        return [_text(value), ""]
    if isinstance(value, list):
        if all(not isinstance(item, (dict, list)) for item in value):
            return [*(f"- {_text(item)}" for item in value if _text(item)), ""]
        lines: list[str] = []
        for index, item in enumerate(value, 1):
            if isinstance(item, dict):
                title = _text(item.get("name") or item.get("title") or item.get("id")) or f"Item {index}"
                lines.extend([f"{'#' * heading_level} {title}", ""])
                for key, child in item.items():
                    if key in {"name", "title", "id"}:
                        continue
                    if isinstance(child, list) and all(not isinstance(entry, (dict, list)) for entry in child):
                        joined = "; ".join(_text(entry) for entry in child if _text(entry))
                        if joined:
                            lines.append(f"- **{_label(key)}:** {joined}")
                    elif not isinstance(child, (dict, list)):
                        if _text(child):
                            lines.append(f"- **{_label(key)}:** {_text(child)}")
                    else:
                        lines.extend([f"{'#' * min(heading_level + 1, 6)} {_label(key)}", ""])
                        lines.extend(_render_structured(child, min(heading_level + 2, 6)))
                lines.append("")
            else:
                lines.extend(_render_structured(item, heading_level))
        return lines
    if isinstance(value, dict):
        lines = []
        for key, child in value.items():
            if child is None or child == [] or child == {} or child == "":
                continue
            lines.extend([f"{'#' * heading_level} {_label(key)}", ""])
            lines.extend(_render_structured(child, min(heading_level + 1, 6)))
        return lines
    return [_text(value), ""]


def _markdown_image_target(raw_path: str) -> str:
    if not raw_path:
        return ""
    if re.match(r"^(?:[a-z][a-z0-9+.-]*:|/|~|[A-Za-z]:[\\/])", raw_path, re.IGNORECASE):
        raise ValueError(f"prototype image path must be relative: {raw_path}")
    if "<" in raw_path or ">" in raw_path:
        raise ValueError(f"prototype image path contains unsupported angle brackets: {raw_path}")
    return f"<{raw_path}>" if any(char.isspace() for char in raw_path) or any(char in "()" for char in raw_path) else raw_path


def _render_page(page: dict[str, Any]) -> list[str]:
    page_id = _text(page.get("id"))
    name = _text(page.get("name"))
    if not page_id or not name:
        raise ValueError("each page requires non-empty id and name")

    image_path = _text(page.get("image"))
    image_target = _markdown_image_target(image_path)
    image = f"![{page_id} prototype]({image_target})" if image_target else "No prototype image"
    summary_parts = [
        f"**Purpose**<br>{_escape_cell(page.get('purpose'))}" if _text(page.get("purpose")) else "",
        _numbered_cell("Key elements", _items(page.get("elements"))),
        _numbered_cell("Interactions", _items(page.get("interactions"))),
    ]
    summary = "<br><br>".join(part for part in summary_parts if part) or "Confirmed details are provided below."

    lines = [
        f"### {page_id} {name}",
        "",
        f"> Type: {_text(page.get('type')) or 'Page'} | Source: `{image_path or 'Not provided'}`",
        "",
        "| Prototype | Requirement summary |",
        "|---|---|",
        f"| {image} | {summary} |",
        "",
    ]
    lines.extend(_bullet_section("Elements", page.get("elements"), 4))
    lines.extend(_bullet_section("Interactions", page.get("interactions"), 4))
    lines.extend(_bullet_section("States", page.get("states"), 4))
    lines.extend(_bullet_section("Exceptions And Recovery", page.get("exceptions"), 4))
    lines.extend(_bullet_section("Acceptance Criteria", page.get("acceptance"), 4))
    return lines


def render_prd(model: dict[str, Any]) -> str:
    if "blocking_decisions" not in model or not isinstance(model["blocking_decisions"], list):
        raise ValueError("blocking_decisions must be present as a list")
    if model["blocking_decisions"]:
        raise ValueError("formal PRD cannot be rendered while blocking decisions remain unresolved")

    if not isinstance(model.get("overview"), dict) or not model["overview"]:
        raise ValueError("overview must be present as a non-empty object")
    if not isinstance(model.get("sources"), (list, dict)) or not model["sources"]:
        raise ValueError("sources must be present and non-empty")

    meta = model.get("meta") or {}
    title = _text(meta.get("title"))
    if not title:
        raise ValueError("meta.title is required")

    lines = [f"# {title}", ""]
    for key in ("version", "date", "status", "source_mode"):
        if _text(meta.get(key)):
            lines.append(f"- {_label(key)}: {_text(meta.get(key))}")
    lines.append("")

    overview = model.get("overview") or {}
    if overview:
        lines.extend(["## 产品概述", ""])
        lines.extend(_render_structured(overview, 3))

    for key in ("sources", "actors", "flows", "states"):
        if model.get(key):
            lines.extend([f"## {SECTION_NAMES[key]}", ""])
            lines.extend(_render_structured(model[key], 3))

    pages = model.get("pages")
    if not isinstance(pages, list) or not pages:
        raise ValueError("pages must be a non-empty list")
    lines.extend(["## 页面需求", ""])
    for page in pages:
        if not isinstance(page, dict):
            raise ValueError("each page must be an object")
        lines.extend(_render_page(page))

    for key in ("rules", "data", "dependencies", "risks", "measurement"):
        if model.get(key):
            lines.extend([f"## {SECTION_NAMES[key]}", ""])
            lines.extend(_render_structured(model[key], 3))

    decisions = model.get("decisions")
    if not isinstance(decisions, list):
        raise ValueError("decisions must be a list")
    lines.extend(["## 已确认决策记录", "", "| ID | Decision | Source | Impact |", "|---|---|---|---|"])
    if decisions:
        for decision in decisions:
            impact = ", ".join(_items(decision.get("impact")))
            lines.append(
                "| {id} | {decision} | {source} | {impact} |".format(
                    id=_escape_cell(decision.get("id")),
                    decision=_escape_cell(decision.get("resolution") or decision.get("title")),
                    source=_escape_cell(decision.get("source")),
                    impact=_escape_cell(impact),
                )
            )
    else:
        lines.append("| - | No material decisions were required beyond the confirmed input. | Confirmed input | All pages |")
    lines.append("")

    future = _items(model.get("future"))
    if future:
        lines.extend(["## 后续优化", "", "> The following items are outside current acceptance.", ""])
        lines.extend(f"- {item}" for item in future)
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path, help="UTF-8 JSON PRD model")
    parser.add_argument("--output", required=True, type=Path, help="Output Markdown path")
    args = parser.parse_args(argv)

    if args.output.suffix.lower() != ".md":
        raise ValueError("output path must use the .md suffix")

    model = json.loads(args.model.read_text(encoding="utf-8"))
    output = render_prd(model)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
