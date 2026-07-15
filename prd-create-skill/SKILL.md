---
name: prd-create-skill
description: Use when a user provides prototype images, UI screenshots, wireframes, or a prototype-generate-skill handoff and wants a product requirements document, PRD logic scan, page requirements, or portable Markdown specification.
---

# PRD Create Skill

## Purpose

Turn prototype evidence into one complete, maintainable Markdown PRD. Separate what is visible, what the user stated, and what is inferred; resolve material ambiguity before formal drafting.

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
- Any ambiguity found: [references/clarification-gate.md](references/clarification-gate.md)
- Formal drafting: [references/prd-content-schema.md](references/prd-content-schema.md) and [references/markdown-template.md](references/markdown-template.md)
- Before delivery: [references/validation-checklist.md](references/validation-checklist.md)

## Mandatory Workflow

### 1. Identify The Input Mode

Classify the input as:

- **Standard package:** output from `prototype-generate-skill`, including a manifest and per-screen evidence.
- **Direct images:** prototypes or screenshots from any other source.

If both exist, use the user's latest explicit instruction as authority and treat the other source as supporting evidence. Follow [references/input-modes.md](references/input-modes.md).

### 2. Establish A Confirmed Page Map

For a standard package, verify that each manifest item has its expected image and stable ID.

For direct images, follow [references/prototype-intake.md](references/prototype-intake.md): inventory the files, classify page/state/overlay/fragment, assign proposed IDs, separate visual evidence from inference, and present the page map for confirmation.

**Do not proceed to formal scanning or drafting until a direct-image page map is explicitly confirmed.** Silence is not confirmation.

If the actual package or images are not readable in the current context, explain the intake process and request access to the evidence. Do not simulate inspection, assign final IDs, or produce project-specific findings from a verbal label alone.

### 3. Run The Universal Scan

Read [references/universal-scan-framework.md](references/universal-scan-framework.md). Scan only from available evidence and user statements. Report:

- confirmed facts
- contradictions and missing logic
- inferred relationships with evidence
- material decisions
- optional improvements kept separate from requirements

Do not invent platforms, actors, storage, APIs, analytics, integrations, implementation layers, or states merely because they are common.

Do not turn a universal scan heading into a project-specific risk without evidence. Lifecycle, for example, does not prove browsers, background execution, local storage, devices, or network behavior exist.

### 4. Activate Conditional Modules

Read [references/conditional-domain-modules.md](references/conditional-domain-modules.md). Activate a module only when an observable signal exists in the prototypes, source text, or user instruction.

Record the signal and activated module. Absence of a signal means the module stays inactive. Never ask payment questions for a non-transactional tool, account questions for a product without identity, or backend questions when no remote system is evidenced.

### 5. Produce The Scan Report

Before the final PRD, present:

1. input evidence and page coverage
2. confirmed product logic
3. missing or contradictory logic
4. activated conditional modules and their signals
5. decision table
6. expected final PRD coverage

Follow [references/clarification-gate.md](references/clarification-gate.md).

### 6. Resolve Blocking Decisions

A decision is blocking when different answers change scope, user outcome, page/state behavior, permissions, workflow, key data meaning, dependency behavior, recovery, or acceptance results.

For each decision, give 2-3 mutually exclusive options, impacts, and one recommendation with rationale. Ask one blocking question at a time unless the user explicitly requests a batch or authorizes recommended answers.

**Never generate the formal PRD while a blocking decision is unresolved.** Do not select a temporary answer and move the conflict to a final "pending questions" section. User silence is not approval.

### 7. Build The Formal PRD

After all blocking decisions are confirmed or explicitly delegated:

1. build the structured content described in [references/prd-content-schema.md](references/prd-content-schema.md)
2. render it using [references/markdown-template.md](references/markdown-template.md)
3. keep images on relative paths with stable names
4. record confirmed decisions, including delegated recommendations
5. put non-blocking future ideas under `后续优化`, clearly outside current acceptance

The final document must not contain a `待确认问题` section. Update this same Markdown file for later logic changes; do not create competing copies unless the user requests version snapshots.

### 8. Validate Before Delivery

Run [references/validation-checklist.md](references/validation-checklist.md). When available, use:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/prd-create-skill/scripts/validate_markdown.py" path/to/prd.md
```

If a structured JSON model is used, generate with:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/prd-create-skill/scripts/build_prd_markdown.py" model.json --output path/to/prd.md
```

Fix content, mapping, path, structure, or portability failures before delivery.

## Evidence Priority

Use this order when sources conflict:

1. user's latest explicit decision
2. user annotations and approved requirements
3. confirmed page map or standard prototype manifest
4. visible prototype evidence
5. clearly labeled inference

Never silently overwrite a higher-priority source with a lower-priority one.

## Failure Conditions

The task is incomplete if any of these are true:

- a direct-image page map was not confirmed
- a blocking decision remains unresolved
- visual inference is presented as confirmed business logic
- an irrelevant domain module was forced onto the project
- prototype images cannot be traced to stable page IDs
- a key action lacks a result or a key failure lacks recovery/termination
- final Markdown contains unresolved placeholders or a pending-questions section
- the document requires a specific Markdown editor to remain understandable
- the user asked only for scanning or explanation, but the skill generated a formal PRD anyway

## Quick Reference

| Situation | Required action |
|---|---|
| Standard package | Verify manifest-image mapping, then scan |
| Direct images | Propose and confirm page map first |
| Material ambiguity | Stop formal drafting and resolve it |
| Domain signal present | Load only matching conditional module |
| No domain signal | Keep that module inactive |
| User authorizes recommendations | Record each delegated decision |
| Later logic change | Update the same Markdown and decision record |
