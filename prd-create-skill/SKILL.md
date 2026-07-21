---
name: prd-create-skill
description: Use when a user provides prototype images, UI screenshots, wireframes, or a prototype-generate-skill handoff and wants a product requirements document, PRD logic scan, page requirements, experiment-variant specification, or portable Markdown specification.
---

# PRD Create Skill

## Purpose

Turn prototype evidence into one complete, maintainable Markdown PRD. Separate what is visible, what the user stated, and what is inferred; confirm both product decisions and the intended document format before formal drafting.

This skill is domain-neutral. It does not assume an industry, platform, account model, backend, payment system, fixed canvas, or implementation architecture.

This skill begins after prototype images already exist. It may inventory, classify, and reference those images, but it never creates, regenerates, redesigns, or resizes them. Do not invoke a prototype-generation workflow from this skill.

## Output Boundary

Produce only one `.md` PRD plus the prototype image files it references. Do not produce Word, PDF, Figma, production code, or redesigned prototype images unless the user separately asks for a different task.

Use portable Markdown by default. Do not require HTML, CSS, plugins, or a particular editor. When the user explicitly names a compatible Markdown editor, optional HTML may enhance presentation, but all information must remain readable without it.

## Required References

Read these references as the workflow reaches them:

- Input selection: [references/input-modes.md](references/input-modes.md)
- Direct-image intake: [references/prototype-intake.md](references/prototype-intake.md)
- Every project scan: [references/universal-scan-framework.md](references/universal-scan-framework.md)
- Domain signals found: [references/conditional-domain-modules.md](references/conditional-domain-modules.md)
- Pre-draft confirmation: [references/clarification-gate.md](references/clarification-gate.md)
- Template selection: [references/markdown-template.md](references/markdown-template.md) and [references/review-table-template.md](references/review-table-template.md) when variants or test points are present
- Formal drafting: [references/prd-content-schema.md](references/prd-content-schema.md)
- Before delivery: [references/validation-checklist.md](references/validation-checklist.md)

## Mandatory Workflow

### 1. Identify The Input Mode

Classify the input as:

- **Standard package:** output from `prototype-generate-skill`, including a manifest and per-screen evidence.
- **Direct images:** prototypes or screenshots from any other source.

If both exist, use the user's latest explicit instruction as authority and treat the other source as supporting evidence. Follow [references/input-modes.md](references/input-modes.md).

### 2. Establish A Proposed Page And Test-Point Map

For a standard package, verify that each manifest item has its expected image and stable ID.

For direct images, follow [references/prototype-intake.md](references/prototype-intake.md): inventory the files, classify page/state/overlay/fragment/variant, assign source IDs, group variants under proposed test points when applicable, and separate visual evidence from inference.

The proposed map may be included in the single pre-draft confirmation pack in Step 6. Do not draft until the complete map is explicitly confirmed. Silence is not confirmation.

If the package or images are unreadable, explain the intake process and request access. Do not simulate inspection, assign final IDs, or produce project-specific findings from a verbal label alone.

### 3. Run The Universal Scan

Read [references/universal-scan-framework.md](references/universal-scan-framework.md). Scan only from available evidence and user statements. Report:

- confirmed facts
- contradictions and missing logic
- inferred relationships with evidence
- material decisions
- optional improvements kept separate from requirements

Do not invent platforms, actors, storage, APIs, analytics, integrations, implementation layers, or states merely because they are common.

### 4. Activate Conditional Modules

Read [references/conditional-domain-modules.md](references/conditional-domain-modules.md). Activate a module only when an observable signal exists in the prototypes, source text, or user instruction.

Record the signal and activated module. Absence of a signal means the module stays inactive.

### 5. Produce The Scan Report

Before the final PRD, present:

1. input evidence and page coverage
2. confirmed product logic
3. missing or contradictory logic
4. activated conditional modules and their signals
5. decision table
6. proposed test-point and variant grouping when applicable
7. expected final PRD coverage

Follow [references/clarification-gate.md](references/clarification-gate.md).

### 6. Present One Pre-Draft Confirmation Pack

A decision is blocking when different answers change scope, user outcome, page/state behavior, permissions, workflow, key data meaning, dependency behavior, recovery, acceptance results, or the expected PRD artifact.

Before drafting, present one consolidated confirmation pack containing:

1. proposed page/test-point/variant map
2. all product and interaction decisions currently discoverable
3. applicable configuration, defaults, precedence, fallback, lifecycle, measurement, and acceptance decisions
4. document-format decisions: language, template profile, section outline, table structure, image-reference mode, acceptance detail, output path/name, and update-existing/new-file choice
5. the proposed final outline
6. one representative page/test-point table populated with actual project evidence

For each unresolved blocking decision, give 2-3 mutually exclusive options, impacts, and one recommendation with rationale. Batch all currently known questions by default so the user can answer once. Ask one at a time only when the user requests an interview-style process.

The user must approve both the product decisions and the template preview. One explicit reply may approve the entire pack. If the reply changes product behavior or format, revise only the affected portion and reconfirm it.

**Never generate the formal PRD while a blocking decision or document-format decision is unresolved.** Do not select a temporary answer and move the conflict to a final pending-questions section. User silence is not approval.

### 7. Build The Formal PRD

After the complete confirmation pack is approved or explicitly delegated:

1. build the structured content in [references/prd-content-schema.md](references/prd-content-schema.md)
2. render it with the approved profile from [references/markdown-template.md](references/markdown-template.md)
3. use the approved image-reference mode; never emit an absolute local filesystem path
4. record confirmed decisions, including delegated recommendations
5. put accepted non-blocking ideas under `后续优化`, outside current acceptance

Use the review-table profile by default when work is organized around test points, experiment variants, placement options, or alternative styles. In that profile:

- each test point or page requirement owns one table
- every visual variant under the same test point is a separate row in that table
- shared rules appear once below the table
- the right cell follows [references/review-table-template.md](references/review-table-template.md), omitting irrelevant slots
- every meaningful action states its destination, result, close behavior, or retained state

Use the full-spec profile for products better represented as independent pages, flows, states, and recovery paths.

Maintain the same Markdown file for later logic changes; do not create competing copies unless the user requests version snapshots.

### 8. Validate Before Delivery

Run [references/validation-checklist.md](references/validation-checklist.md). Use the confirmed profile and image mode, for example:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/prd-create-skill/scripts/validate_markdown.py" path/to/prd.md --profile review-table --image-mode relative --acceptance-detail concise
```

If a structured JSON model is used, generate with:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/prd-create-skill/scripts/build_prd_markdown.py" model.json --output path/to/prd.md
```

Fix content, grouping, mapping, path, structure, or portability failures before delivery.

## Evidence Priority

Use this order when sources conflict:

1. user's latest explicit decision
2. user annotations and approved requirements
3. confirmed page/test-point map or prototype manifest
4. visible prototype evidence
5. clearly labeled inference

Never silently overwrite a higher-priority source with a lower-priority one.

## Failure Conditions

The task is incomplete if any of these are true:

- a direct-image map was not confirmed
- a blocking product or document-format decision remains unresolved
- the template preview was not approved
- visual inference is presented as confirmed business logic
- an irrelevant domain module was forced onto the project
- prototype images cannot be traced to stable source IDs
- variants from one confirmed test point were split into competing tables without a stated reason
- a key action lacks a destination, result, close behavior, or retained state
- final Markdown contains unresolved placeholders or a pending-questions section
- the document requires a specific Markdown editor to remain understandable
- the user asked only for scanning or explanation, but the skill generated a formal PRD anyway

## Quick Reference

| Situation | Required action |
|---|---|
| Standard package | Verify manifest-image mapping, then scan |
| Direct images | Propose a page/test-point/variant map in the confirmation pack |
| Material ambiguity | Add it to the consolidated pre-draft confirmation pack |
| Experiment variants | Use one table per test point and one row per variant |
| Document format unknown | Preview the outline and sample table; obtain approval |
| Domain signal present | Load only the matching conditional module |
| User authorizes recommendations | Record each delegated decision |
| Later logic change | Update the same Markdown and decision record |
