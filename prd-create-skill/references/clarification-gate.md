# Clarification Gate

## Scan Report Shape

1. input mode and evidence summary
2. confirmed page coverage
3. confirmed product logic
4. conflicts, missing logic, and labeled inference
5. activated conditional modules with signals
6. decision table
7. expected formal PRD coverage

## Decision Record

| Field | Required content |
|---|---|
| Decision ID | Stable ID such as `D-001` |
| Question | One decision in neutral language |
| Evidence | Why the issue exists |
| Impact | Pages, states, actors, workflow, data, dependency, acceptance |
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

`Important` improves completeness or reduces risk but can be specified later without changing current acceptance. `Optimization` is outside the current requirement.

## Conversation Rules

- Ask one blocking decision at a time by default.
- Lead with the recommendation, then explain trade-offs.
- Accept a batch only when the user asks for it.
- When the user says “use your recommendations,” record each decision as delegated.
- Do not infer approval from silence, urgency, or a request to “just draft it.”
- Do not publish a formal PRD with a temporary decision or a final pending-questions section.

## Ready-To-Draft Gate

Formal drafting can start only when:

- page mapping is confirmed
- all blocking decisions have resolutions
- evidence and inference are separated
- activated modules are recorded
- expected PRD coverage is agreed or follows directly from confirmed scope
