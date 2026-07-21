#!/usr/bin/env python3
"""Regression tests for the PRD renderer and validator."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def _load(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, SKILL_ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


renderer = _load("prd_renderer", "scripts/build_prd_markdown.py")
validator = _load("prd_validator", "scripts/validate_markdown.py")


class ReviewTableTests(unittest.TestCase):
    def _model(self) -> dict:
        return {
            "document_profile": "review_table",
            "delivery": {
                "language": "zh-CN",
                "image_mode": "relative",
                "acceptance_detail": "concise",
                "output_target": "Review-PRD.md",
                "update_mode": "new_file",
            },
            "meta": {"title": "Review PRD", "version": "1.0"},
            "overview": {"goal": "Compare two confirmed styles."},
            "sources": ["Confirmed prototypes"],
            "test_points": [
                {
                    "id": "T01",
                    "name": "Entry position",
                    "variants": [
                        {
                            "id": "V01",
                            "name": "Right",
                            "images": ["assets/V01.png"],
                            "applicability": ["entry_position=right"],
                            "display": ["Show the entry on the right."],
                            "interactions": ["Tap the entry → open the confirmed destination."],
                        },
                        {
                            "id": "V02",
                            "name": "Center",
                            "images": ["assets/V02.png"],
                            "applicability": ["entry_position=center"],
                            "display": ["Show the entry in the center."],
                            "interactions": ["Tap the entry → open the confirmed destination."],
                        },
                    ],
                    "shared_rules": ["Only one entry position is visible."],
                    "acceptance": ["The selected value renders the matching entry."],
                }
            ],
            "decisions": [],
            "blocking_decisions": [],
        }

    def test_review_table_preserves_variants_in_one_table(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            assets = root / "assets"
            assets.mkdir()
            (assets / "V01.png").write_bytes(b"fixture")
            (assets / "V02.png").write_bytes(b"fixture")

            output = renderer.render_prd(self._model())
            document = root / "review.md"
            document.write_text(output, encoding="utf-8")

            self.assertEqual(output.count("### T01 Entry position"), 1)
            self.assertEqual(output.count("| Prototype | Requirement summary |"), 1)
            self.assertIn("![V01 prototype](assets/V01.png)", output)
            self.assertIn("![V02 prototype](assets/V02.png)", output)
            self.assertEqual(validator.validate_markdown(document, "review-table", "relative"), [])

    def test_absolute_local_image_is_rejected(self) -> None:
        model = self._model()
        model["test_points"][0]["variants"][0]["images"] = ["/tmp/V01.png"]
        with self.assertRaisesRegex(ValueError, "absolute local path"):
            renderer.render_prd(model)

    def test_external_image_mode_is_supported_when_confirmed(self) -> None:
        model = self._model()
        model["delivery"]["image_mode"] = "external"
        model["test_points"][0]["variants"][0]["images"] = ["https://example.com/V01.png"]
        model["test_points"][0]["variants"][1]["images"] = ["https://example.com/V02.png"]
        output = renderer.render_prd(model)
        with tempfile.TemporaryDirectory() as temp_dir:
            document = Path(temp_dir) / "external.md"
            document.write_text(output, encoding="utf-8")
            self.assertEqual(validator.validate_markdown(document, "review-table", "external"), [])

    def test_review_table_rejects_two_tables_for_one_test_point(self) -> None:
        markdown = """# Example

## 页面需求

### Position

| Prototype | Requirement summary |
|---|---|
| ![A](https://example.com/A.png) | Logic A |

| Prototype | Requirement summary |
|---|---|
| ![B](https://example.com/B.png) | Logic B |
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            document = Path(temp_dir) / "invalid.md"
            document.write_text(markdown, encoding="utf-8")
            issues = validator.validate_markdown(document, "review-table", "external")
        self.assertTrue(any("exactly one" in issue for issue in issues), issues)

    def test_full_spec_profile_still_renders_and_validates(self) -> None:
        model = {
            "document_profile": "full_spec",
            "delivery": {
                "language": "en",
                "image_mode": "relative",
                "acceptance_detail": "concise",
                "output_target": "Full-PRD.md",
                "update_mode": "new_file",
            },
            "meta": {"title": "Full Spec"},
            "overview": {"goal": "Describe one page."},
            "sources": ["Confirmed prototype"],
            "pages": [
                {
                    "id": "P01",
                    "name": "Home",
                    "image": "assets/P01.png",
                    "purpose": "Start the confirmed flow.",
                    "interactions": ["Tap Start → open the confirmed destination."],
                    "acceptance": ["The Start action opens the confirmed destination."],
                }
            ],
            "decisions": [],
            "blocking_decisions": [],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            assets = root / "assets"
            assets.mkdir()
            (assets / "P01.png").write_bytes(b"fixture")
            document = root / "full.md"
            document.write_text(renderer.render_prd(model), encoding="utf-8")
            self.assertEqual(validator.validate_markdown(document, "full-spec", "relative"), [])

    def test_full_spec_can_omit_acceptance_when_confirmed(self) -> None:
        model = {
            "document_profile": "full_spec",
            "delivery": {
                "language": "en",
                "image_mode": "external",
                "acceptance_detail": "none",
                "output_target": "Full-PRD.md",
                "update_mode": "new_file",
            },
            "meta": {"title": "Full Spec Without Acceptance"},
            "overview": {"goal": "Describe one page."},
            "sources": ["Confirmed prototype"],
            "pages": [
                {
                    "id": "P01",
                    "name": "Home",
                    "image": "https://example.com/P01.png",
                    "purpose": "Start the confirmed flow.",
                    "interactions": ["Tap Start → open the confirmed destination."],
                }
            ],
            "decisions": [],
            "blocking_decisions": [],
        }
        output = renderer.render_prd(model)
        self.assertNotIn("#### Acceptance Criteria", output)
        with tempfile.TemporaryDirectory() as temp_dir:
            document = Path(temp_dir) / "full-none.md"
            document.write_text(output, encoding="utf-8")
            self.assertEqual(validator.validate_markdown(document, "auto", "external", "none"), [])

    def test_auto_detects_single_variant_review_table_from_marker(self) -> None:
        model = self._model()
        model["test_points"][0]["variants"] = model["test_points"][0]["variants"][:1]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            assets = root / "assets"
            assets.mkdir()
            (assets / "V01.png").write_bytes(b"fixture")
            document = root / "single-review.md"
            document.write_text(renderer.render_prd(model), encoding="utf-8")
            self.assertEqual(validator.validate_markdown(document, "auto", "relative"), [])


if __name__ == "__main__":
    unittest.main()
