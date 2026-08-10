from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "screenshot-to-web-and-figma"


class SkillContractTest(unittest.TestCase):
    def test_required_files_and_contract(self):
        paths = [
            SKILL / "SKILL.md",
            SKILL / "agents/openai.yaml",
            SKILL / "references/reconstruction-contract.md",
            SKILL / "references/interaction-and-qa.md",
            SKILL / "references/figma-capture-runbook.md",
        ]
        self.assertEqual([], [str(path) for path in paths if not path.is_file()])

        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(frontmatter)
        self.assertIn("name: screenshot-to-web-and-figma", frontmatter.group(1))
        self.assertRegex(frontmatter.group(1), r"(?m)^description: Use when ")

        required = [
            "never use the source screenshot as a page background",
            "semantic html",
            "publish with sites by default",
            "create a new figma design file",
            "frame",
            "text",
            "remove the temporary capture script",
        ]
        text_lower = text.lower()
        self.assertEqual([], [phrase for phrase in required if phrase not in text_lower])


if __name__ == "__main__":
    unittest.main()
