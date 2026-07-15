# PRD Validation Checklist

## Gate

- [ ] Input mode identified
- [ ] Direct-image page map explicitly confirmed when applicable
- [ ] Evidence and inference separated
- [ ] All blocking decisions resolved or explicitly delegated
- [ ] Activated conditional modules have observable signals
- [ ] Inactive modules did not add irrelevant requirements

## Coverage

- [ ] Every confirmed page/state has a stable unique ID
- [ ] Every page has a valid prototype mapping or documented reason for none
- [ ] Every visible action has a confirmed result or a resolved decision
- [ ] Every critical flow has a start, branches, end, and recovery/termination
- [ ] Page, flow, state, rule, data, and acceptance statements agree
- [ ] Given/When/Then criteria cover normal and applicable failure paths

## Evidence Quality

- [ ] Visible copy and example values are not misrepresented as hidden rules
- [ ] No platform, actor, backend, storage, API, analytics, or technical architecture was invented
- [ ] Recommendations and future ideas are separate from current requirements
- [ ] Confirmed decisions record their source and impact

## Markdown

- [ ] Exactly one final `.md` document is maintained
- [ ] Title hierarchy is continuous
- [ ] Summary tables have consistent columns
- [ ] Image paths are relative and exist
- [ ] Page IDs are unique
- [ ] Mermaid fences, declarations, and obvious incomplete flow edges pass basic validation
- [ ] Mermaid is rendered when a compatible renderer is available; a text flow is present when renderer support is unknown
- [ ] The document is understandable without HTML, CSS, or a specific editor
- [ ] Detailed requirement text remains outside images

## Final Scan

Search for unresolved markers and forbidden final sections:

```bash
rg -n 'TBD|TODO|待确认问题|暂定方案|以后补充|待补充' path/to/prd.md
```

Every match must either be removed or occur in quoted historical source text explicitly labeled as non-normative.

Run the bundled validator when available:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/prd-create-skill/scripts/validate_markdown.py" path/to/prd.md
```

Do not declare completion while any validation error remains.
