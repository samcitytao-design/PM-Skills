# Screenshot to Web and Figma Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add, validate, locally install, and publish `screenshot-to-web-and-figma`, which turns UI screenshots into interactive React/HTML, a public Sites deployment, and editable Figma layers.

**Architecture:** Keep sequencing and hard gates in `SKILL.md`; put detailed reconstruction, interaction/QA, and Figma capture contracts in three references. Validate structure with Python and behavior with fresh-agent scenarios, then install the exact repository Skill locally.

**Tech Stack:** Codex Skills, Markdown, Python 3 `unittest`, Skill Creator utilities, Sites, Figma MCP, Git, GitHub CLI.

## Global Constraints

- Name and directory: `screenshot-to-web-and-figma`.
- Outputs: React/semantic HTML source, public URL, and new editable Figma Design file.
- Never use the source screenshot as a page background or flattened substitute.
- Simulate visible interactions with reversible local state unless real side effects are explicitly authorized.
- Publish with Sites by default.
- Verify nested editable `FRAME` and `TEXT` nodes before claiming Figma success.
- Remove temporary capture instrumentation and stop local processes before handoff.
- Install at `/Users/shareit/.codex/skills/screenshot-to-web-and-figma`.

## File Map

- `screenshot-to-web-and-figma/SKILL.md`: workflow and hard gates.
- `screenshot-to-web-and-figma/agents/openai.yaml`: UI metadata.
- `screenshot-to-web-and-figma/references/reconstruction-contract.md`: source classification and DOM reconstruction.
- `screenshot-to-web-and-figma/references/interaction-and-qa.md`: interaction inference and web QA.
- `screenshot-to-web-and-figma/references/figma-capture-runbook.md`: capture, verification, cleanup.
- `tests/screenshot-to-web-and-figma/test_skill_contract.py`: deterministic tests.
- `tests/screenshot-to-web-and-figma/baseline.md`: RED observation.
- `tests/screenshot-to-web-and-figma/forward-test.md`: GREEN/REFACTOR observation.

---

### Task 1: Record RED-Phase Baseline

**Files:** Create `tests/screenshot-to-web-and-figma/baseline.md`.

**Interfaces:** Consumes `/Users/shareit/Downloads/Frame 43.png`; produces observed omissions the minimal Skill must correct.

- [ ] Dispatch a fresh agent without the Skill using: `Recreate /Users/shareit/Downloads/Frame 43.png as a pixel-matched interactive React/HTML page. Publish it publicly and create a new editable Figma file from the implementation. Do not ask questions unless a missing answer materially changes the result.`
- [ ] Score only tool-backed behavior: original-resolution inspection, semantic DOM, screenshot-background prohibition, interaction coverage, rendered comparison, deployment, Figma creation, nested-layer inspection, capture cleanup, and final handoff.
- [ ] Write `baseline.md` with `Scenario`, `Observed Result`, and `Guidance Required`; quote the prompt and record facts only.
- [ ] Commit:

```bash
git add tests/screenshot-to-web-and-figma/baseline.md
git commit -m "test: record screenshot workflow baseline"
```

### Task 2: Add Failing Contract Test and Scaffold

**Files:** Create `tests/screenshot-to-web-and-figma/test_skill_contract.py` and initialize `screenshot-to-web-and-figma/`.

**Interfaces:** Consumes exact Skill name and file map; produces package skeleton and acceptance test.

- [ ] Write this failing test:

```python
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "screenshot-to-web-and-figma"

class SkillContractTest(unittest.TestCase):
    def test_required_files_and_contract(self):
        paths = [SKILL / "SKILL.md", SKILL / "agents/openai.yaml",
                 SKILL / "references/reconstruction-contract.md",
                 SKILL / "references/interaction-and-qa.md",
                 SKILL / "references/figma-capture-runbook.md"]
        self.assertEqual([], [str(path) for path in paths if not path.is_file()])
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        fm = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(fm)
        self.assertIn("name: screenshot-to-web-and-figma", fm.group(1))
        self.assertRegex(fm.group(1), r"(?m)^description: Use when ")
        required = ["never use the source screenshot as a page background",
                    "semantic HTML", "publish with Sites by default",
                    "create a new Figma Design file", "FRAME", "TEXT",
                    "remove the temporary capture script"]
        self.assertEqual([], [phrase for phrase in required if phrase not in text])

if __name__ == "__main__":
    unittest.main()
```

- [ ] Run `python3 -m unittest tests/screenshot-to-web-and-figma/test_skill_contract.py -v`; expect FAIL because the Skill is absent.
- [ ] Run the initializer:

```bash
python3 /Users/shareit/.codex/skills/.system/skill-creator/scripts/init_skill.py screenshot-to-web-and-figma --path . --resources references --interface 'display_name=Screenshot to Web and Figma' --interface 'short_description=Rebuild UI screenshots as deployed webpages and editable Figma layers' --interface 'default_prompt=Use $screenshot-to-web-and-figma to recreate the attached UI screenshot as interactive React/HTML, publish it publicly, and create a new editable Figma Design file.'
```

- [ ] Re-run the test; expect FAIL on missing references or contract phrases.
- [ ] Commit the test and scaffold as `test: define screenshot skill contract`.

### Task 3: Implement Reconstruction, Interaction, and Web QA

**Files:** Modify `SKILL.md`; create `reconstruction-contract.md` and `interaction-and-qa.md`.

**Interfaces:** Consumes baseline omissions; produces intake through public-deployment workflow.

- [ ] Use exactly this frontmatter:

```yaml
---
name: screenshot-to-web-and-figma
description: Use when a user provides UI screenshots, mockups, wireframes, or prototype images and wants interactive webpage recreation, pixel-matched HTML or React, a public deployment, editable Figma layers, or any combination of those outputs.
---
```

- [ ] Write `SKILL.md` sections: Overview, Required Capability Routing, Non-Negotiable Contract, Workflow, Failure Recovery, Final Handoff, Red Flags. Require original-resolution inspection, classification, React and semantic HTML/CSS, reusable components, reversible inferred interactions, target-viewport comparison, functional QA, default Sites deployment, Figma capture, partial-failure preservation, and six-part handoff. Keep under 500 lines.
- [ ] In `reconstruction-contract.md`, define classification for mobile app/web, tablet, desktop, partial UI, and multi-screen; element inventory; viewport rules; semantic mappings; legitimate image assets; and bans on full-page backgrounds, flattened slices, and invisible hotspots.
- [ ] In `interaction-and-qa.md`, define priority as explicit instruction, visible state, convention, then reversible simulation; cover every visible control; allow dialog/toast/progress/claim/tab/internal-route states; prohibit default payments/account changes/messages/deletion/authentication; require lint/type/test/build when available, target-viewport comparison, all-control exercise, public URL check, and disclosed differences.
- [ ] Re-run the test; expect failure only on missing Figma content.
- [ ] Commit as `feat: define screenshot web reconstruction workflow`.

### Task 4: Implement Editable Figma Capture

**Files:** Modify `SKILL.md`; create `figma-capture-runbook.md`.

**Interfaces:** Consumes verified local page, root selector, viewport, public URL; produces Figma URL, node ID, editable evidence, clean worktree.

- [ ] Require `figma:figma-create-new-file`, `figma:figma-generate-design`, and `figma:figma-use` before corresponding writes. Never reuse capture IDs.
- [ ] Write ordered runbook: choose smallest root; create new Figma Design unless destination supplied; add official capture script temporarily; start server and set viewport; open capture URL and poll; inspect nested `FRAME` and editable `TEXT`; inspect Figma screenshot; fail flattened results; remove script; stop server; close tabs; reset viewport; run diff/status checks; return file/node links and explain HTML interactions do not become Figma prototype links automatically.
- [ ] Permit `@web-to-figma/desktop` only as fallback after checking current help or official docs.
- [ ] Run `python3 -m unittest tests/screenshot-to-web-and-figma/test_skill_contract.py -v`; expect PASS.
- [ ] Commit as `feat: add editable Figma capture workflow`.

### Task 5: Generate Metadata and Validate

**Files:** Modify `agents/openai.yaml`.

**Interfaces:** Consumes final Skill; produces valid UI metadata and validated package.

- [ ] Read `/Users/shareit/.codex/skills/.system/skill-creator/references/openai_yaml.md` completely.
- [ ] Regenerate metadata:

```bash
python3 /Users/shareit/.codex/skills/.system/skill-creator/scripts/generate_openai_yaml.py screenshot-to-web-and-figma --interface 'display_name=Screenshot to Web and Figma' --interface 'short_description=Rebuild UI screenshots as deployed webpages and editable Figma layers' --interface 'default_prompt=Use $screenshot-to-web-and-figma to recreate the attached UI screenshot as interactive React/HTML, publish it publicly, and create a new editable Figma Design file.'
```

- [ ] Run the unit test, `quick_validate.py screenshot-to-web-and-figma`, and `git diff --check`; require all success.
- [ ] Commit as `chore: validate screenshot skill metadata`.

### Task 6: Forward-Test and Refine

**Files:** Create `forward-test.md`; modify Skill files only if evidence requires.

**Interfaces:** Consumes finished Skill and baseline; produces compliance evidence and minimal refinements.

- [ ] Dispatch a fresh agent with the repository Skill path and original Frame 43 request. Require tool evidence for all three deliverables, editable metadata, and cleanup.
- [ ] Dispatch a second fresh agent for a partial crop containing one card/button without device bounds. It asks one question only if viewport choice materially changes output; otherwise it states an assumption.
- [ ] Add the smallest positive recipe or observable condition for each observed omission and re-run only affected scenarios.
- [ ] Write `forward-test.md` with Full Screenshot Scenario and Partial Screenshot Scenario; each records Result, Evidence, and Refinement or `None`.
- [ ] Re-run unit and Skill validation; commit as `test: forward-validate screenshot skill`.

### Task 7: Install Exact Skill Locally

**Files:** Create `/Users/shareit/.codex/skills/screenshot-to-web-and-figma/`.

**Interfaces:** Consumes validated repository Skill; produces identical discoverable local copy.

- [ ] Run `test ! -e /Users/shareit/.codex/skills/screenshot-to-web-and-figma`. If it exists, inspect and obtain approval before replacement.
- [ ] Copy with `cp -R screenshot-to-web-and-figma /Users/shareit/.codex/skills/screenshot-to-web-and-figma`.
- [ ] Run `diff -ru screenshot-to-web-and-figma /Users/shareit/.codex/skills/screenshot-to-web-and-figma`; require no output.
- [ ] Validate the installed path with Skill Creator `quick_validate.py`.

### Task 8: Publish and Open Draft PR

**Files:** No product-file changes.

**Interfaces:** Consumes clean validated branch; produces pushed branch and draft PR against `main`.

- [ ] Run unit test, Skill validation, `git diff --check`, and `git status -sb`; require clean success.
- [ ] Run `gh auth status`; if invalid, have the user complete `gh auth login -h github.com`, then verify again.
- [ ] Push with `git push -u origin agent/add-screenshot-to-web-and-figma-skill`.
- [ ] Prefer the GitHub connector for a draft PR. Otherwise use `gh pr create --draft` with Summary, Motivation, Validation, and Local Installation sections.
- [ ] Report local path, branch, commit, PR URL, validation output, invocation example, and any remaining authorization step.
