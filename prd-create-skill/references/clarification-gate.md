# Clarification Gate

## Scan Report Shape

1. input mode and evidence summary
2. confirmed page coverage
3. confirmed product logic
4. conflicts, missing logic, and labeled inference
5. activated conditional modules with signals
6. proposed page/test-point/variant grouping
7. decision table
8. document-format decision table
9. proposed outline and representative table preview
10. expected formal PRD coverage

## Decision Record

| Field | Required content |
|---|---|
| Decision ID | Stable ID such as `D-001` |
| Question | One decision in neutral language |
| Evidence | Why the issue exists |
| Impact | Pages, states, actors, workflow, data, dependency, acceptance, or artifact format |
| Options | 2-3 mutually exclusive choices |
| Recommendation | One choice and concrete rationale |
| Priority | Blocking, important, or optimization |
| Resolution | User choice or explicit delegation |

## Priority Test

`Blocking` means different answers change at least one of:

- product scope or user outcome
- page, state, or workflow behavior
- authority, ownership, or visibility
- key data meaning or calculation
- dependency behavior or recovery
- acceptance result
- final artifact structure, portability, or review usability

`Important` improves completeness or reduces risk but can be specified later without changing current acceptance. `Optimization` is outside the current requirement.

## Consolidated Confirmation Pack

Batch all currently discoverable decisions by default. Cover only applicable topics, but always include document format.

| Block | Confirm when applicable |
|---|---|
| Scope | objective, in-scope/out-of-scope behavior, success, release or experiment boundary |
| Evidence map | pages, states, overlays, fragments, test points, variants, duplicate or supporting images |
| Interaction | entry, meaningful actions, destination/result, close/back behavior, completion, recovery |
| Configuration | independent parameters, exact values, defaults, precedence, invalid/missing-value fallback, effective timing |
| Lifecycle | first use, frequency, consumed timing, version reset, persistence |
| Measurement | exposure, click, funnel success, failure reason, guardrails |
| Document format | language, full-spec/review-table profile, outline, table columns, image mode, acceptance detail, output path/name, update-existing/new-file |

For each unresolved blocking row, provide 2-3 mutually exclusive options, concrete impact, and one recommendation. The user may approve all recommendations in one reply.

After the decision table, show the proposed final outline and one representative table populated with actual evidence. Ask whether any section, column, detail level, or wording style should change.

## Conversation Rules

- Ask all currently known blocking decisions in one structured batch by default.
- Ask one at a time only when the user requests an interview-style process.
- Lead with the recommendation, then explain trade-offs.
- When the user says “use your recommendations,” record each decision as delegated.
- Do not infer approval from silence, urgency, or a request to “just draft it.”
- Do not treat product-logic approval as format approval unless the reply clearly covers both.
- If new evidence reveals a genuinely new blocker after confirmation, ask only the supplemental question and reconfirm the affected template portion.
- Do not publish a formal PRD with temporary decisions or a pending-questions section.

## Ready-To-Draft Gate

Formal drafting can start only when:

- page/test-point mapping is confirmed
- all blocking decisions have resolutions
- evidence and inference are separated
- activated modules are recorded
- expected PRD coverage is agreed
- document profile, outline, table structure, image mode, acceptance detail, and output target are confirmed
- the representative template preview is explicitly approved
