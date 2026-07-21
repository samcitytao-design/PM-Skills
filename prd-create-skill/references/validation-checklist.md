# PRD Validation Checklist

## Pre-Draft Gate

- [ ] Input mode identified
- [ ] Page/test-point/variant map explicitly confirmed
- [ ] Evidence and inference separated
- [ ] All blocking decisions resolved or delegated
- [ ] Activated conditional modules have observable signals
- [ ] Document profile, outline, table structure, image mode, acceptance detail, and output target explicitly confirmed
- [ ] Representative table preview explicitly approved

## Coverage

- [ ] Every source image maps to a page/state or test-point variant
- [ ] Every visible action has a confirmed destination, result, close behavior, or retained state
- [ ] Every critical flow has a start, branches, end, and recovery/termination when applicable
- [ ] Page, flow, state, rule, data, and acceptance statements agree
- [ ] Acceptance matches the approved detail/style; Given/When/Then is used only when approved or needed for precise transitions

## Review-Table Profile

- [ ] Every test point has exactly one prototype/requirement table
- [ ] Variants of the same test point occupy separate rows in that table
- [ ] Independently controlled variables are not mixed into one test point
- [ ] Shared rules are stated once below the table
- [ ] Each variant row uses applicable stable logic slots and omits irrelevant ones
- [ ] Exact parameter keys and values are used; `/` and combined pseudo-values are not treated as experiment values

## Evidence Quality

- [ ] Visible copy and example values are not misrepresented as hidden rules
- [ ] No platform, actor, backend, storage, API, analytics, or architecture was invented
- [ ] Recommendations and future ideas are separate from current requirements
- [ ] Confirmed decisions record source and impact when a decision record is included

## Markdown

- [ ] Exactly one final `.md` document is maintained
- [ ] Title hierarchy is continuous
- [ ] Summary tables have consistent columns
- [ ] Image references match the confirmed mode; absolute local paths never appear
- [ ] Relative images exist; external images use HTTP(S)
- [ ] Page/test-point IDs are unique when IDs are included
- [ ] Mermaid fences and obvious incomplete edges pass basic validation
- [ ] The document is understandable without HTML, CSS, or a specific editor
- [ ] Detailed requirement text remains outside images

## Final Scan

```bash
rg -n 'TBD|TODO|待确认问题|暂定方案|以后补充|待补充' path/to/prd.md
```

Every match must be removed or occur in quoted historical source text explicitly labeled as non-normative.

Run the bundled validator with the confirmed modes, for example:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/prd-create-skill/scripts/validate_markdown.py" path/to/prd.md --profile review-table --image-mode relative --acceptance-detail concise
```

Do not declare completion while any validation error remains.
