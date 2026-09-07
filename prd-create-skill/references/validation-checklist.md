# PRD Validation Checklist

## Pre-Draft Gate

- [ ] Input mode identified
- [ ] Page/test-point/variant map explicitly confirmed
- [ ] Evidence and inference separated
- [ ] All blocking decisions resolved or delegated
- [ ] Activated conditional modules have observable signals
- [ ] Document profile, outline, table structure, review-table logic placement, document/UI-copy languages, image mode, acceptance detail, and output target explicitly confirmed
- [ ] Format resolved by explicit instruction, approved reference/preview, or standing preference; no redundant approval round

## Coverage

- [ ] Every source image maps to a page/state or test-point variant
- [ ] Every visible action has a confirmed destination, result, close behavior, or retained state
- [ ] Every critical flow has a start, branches, end, and recovery/termination when applicable
- [ ] Eligibility-gated content defines qualified and unqualified visibility; externally resolved eligibility also defines loading/failure and pre-action recheck behavior when applicable, without silently disabling the base capability
- [ ] Page, flow, state, rule, data, and acceptance statements agree
- [ ] Acceptance matches the approved detail/style; Given/When/Then is used only when approved or needed for precise transitions

## Review-Table Profile

- [ ] Every test point has exactly one prototype/requirement table
- [ ] Variants of the same test point occupy separate rows in that table
- [ ] Independently controlled variables are not mixed into one test point
- [ ] Logic placement matches the approved preview: `row_complete` or `shared_below`
- [ ] In `row_complete`, every row is independently understandable, implementable, and testable; all applicable common rules are repeated in-row and no “same as above” or table-external display/interaction/copy/acceptance lookup is required
- [ ] In `shared_below`, rows contain variant differences and genuinely common rules plus test-point acceptance are stated once below the table
- [ ] Each variant row uses applicable stable logic slots and omits irrelevant ones
- [ ] Configuration depth matches the request: product control responsibilities by default; exact keys only for requested implementation/experiment details

## Evidence Quality

- [ ] Visible copy and example values are not misrepresented as hidden rules
- [ ] Confirmed UI strings retain their approved language and are tied to the correct element, state, and display condition
- [ ] No platform, actor, backend, storage, API, analytics, or architecture was invented
- [ ] Recommendations and future ideas are separate from current requirements
- [ ] Confirmed decisions record source and impact when a decision record is included

## Markdown

- [ ] Exactly one final `.md` document is maintained
- [ ] The final section outline matches the approved outline; removed sections were not recreated under new names
- [ ] Title hierarchy is continuous
- [ ] Summary tables have consistent columns
- [ ] Image references match the confirmed mode; absolute local paths never appear
- [ ] Relative images exist; external images use HTTP(S)
- [ ] Page/test-point IDs are unique when IDs are included
- [ ] Mermaid fences and obvious incomplete edges pass basic validation
- [ ] The document is understandable without HTML, CSS, or a specific editor
- [ ] Detailed requirement text remains outside images
- [ ] Background and goals use one clear idea per bullet; page rules, eligibility, state transitions, configuration effects, and exceptions are not buried in the overview

## Format-Change Regression Checks

- [ ] Only the approved top-level modules appear, in order; the standing format has exactly five.
- [ ] A module-list edit has not changed table columns, grouping, or image placement.
- [ ] “分层分点 / 精简” was applied inside the right cell: bold short labels, numbered short points, no detached prose replacement.
- [ ] Condensing removed repetition, not conditions, action destinations, close behavior, or recovery.
- [ ] Reference files were actually read; structure was separated from their business examples.
- [ ] Configuration summaries contain no unsolicited JSON or exhaustive key/type matrix; proposed tracking is not presented as observed logs.
- [ ] Internal evidence/decision bookkeeping has not leaked into unrequested modules.

## Final Scan

```bash
rg -n 'TBD|TODO|待确认问题|暂定方案|以后补充|待补充' path/to/prd.md
```

Every match must be removed or occur in quoted historical source text explicitly labeled as non-normative.

Run the bundled validator with the confirmed modes, for example:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/prd-create-skill/scripts/validate_markdown.py" path/to/prd.md --profile review-table --outline five-section --image-mode relative --acceptance-detail none
```

Do not declare completion while any validation error remains.
