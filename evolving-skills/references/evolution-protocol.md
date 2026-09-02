# Skill Evolution Protocol

Use this protocol after the Target Skill is explicit and readable.

## 1. Evidence Reconstruction

Read the current conversation as an ordered usage trace, not a collection of isolated user statements. Capture:

| Stage | Evidence to recover |
|---|---|
| Initial task | What the Target Skill was asked to produce or change |
| Initial constraints | Scope, format, quality, style, safety, and synchronization requirements already stated |
| Initial output | What the first Target Skill result actually did |
| Feedback loop | Each addition, rejection, correction, rework request, and change of scope or preference |
| Intermediate revisions | What changed after each feedback item and whether the same issue recurred |
| Final state | The accepted result, retained changes, abandoned approaches, and unresolved items |

Evidence priority:

1. user's latest explicit decision
2. explicit long-term preference
3. repeated correction or explicit Agent error
4. accepted final behavior supported by the revision history
5. Agent inference, clearly labeled

Acceptance is a strong signal, not proof that every final detail is reusable. If only the final artifact is available, do not invent the missing delta or causal explanation.

## 2. Delta Ledger

For every meaningful change, reason internally with this record:

| Field | Question |
|---|---|
| Before | What did the initial or intermediate output do? |
| Feedback | What exactly did the user reject, correct, add, or constrain? |
| After | What changed in the next accepted direction? |
| Why better | Which observable problem did the change remove? |
| Root cause | What Target Skill gap, weakness, conflict, or missing validation allowed the problem? |
| Candidate lesson | What conditional, reusable behavior might prevent recurrence? |
| Evidence strength | Explicit long-term request, repeated feedback, explicit correction, accepted pattern, or inference |

Repeated correction of the same issue is a high-priority signal: inspect for a weak rule, conflicting rule, missing execution order, missing validation, or an overly permissive inference boundary.

## 3. Classify the Change

Classify each delta before proposing a Skill edit:

| Class | Default decision |
|---|---|
| Task content: value, copy, date, threshold, or other current deliverable input | Do not learn |
| User changed their mind without exposing a process failure | Do not learn |
| Current-project exception | Do not learn unless it can be safely generalized |
| Agent correction exposing failure to respect an existing boundary | Candidate lesson |
| Missing capability or repeatedly omitted completeness check | Candidate lesson |
| Explicit long-term preference using terms such as “以后”, “统一”, “默认”, or “每次都” | Strong candidate within the Target Skill's scope |
| Better decision pattern visible across the revision path | Candidate only after extracting the decision principle from the chosen UI/content outcome |

## 4. Candidate Lesson Filter

Accept a lesson only when all required questions have defensible answers:

| Dimension | Acceptance test |
|---|---|
| Reusability | Would the behavior help another task of the same class? |
| Stability | Is it likely to remain valid beyond the current project? |
| Scope | Does it belong to this Target Skill or a clearly defined task class it owns? |
| Evidence | Is it supported by an explicit preference, correction, recurrence, or stable accepted delta? |
| Value | Will it reduce rework, improve accuracy/completeness, or prevent the same error? |
| Overfitting risk | Can it be stated without current names, values, copy, visual choices, or business rules? |

If the lesson fails overfitting, generalize again or reject it. If it cannot be written as an observable condition and behavior, keep it out of the Skill.

## 5. Root-Cause Mapping

Map surface symptoms to the smallest durable correction:

| Root cause | Preferred Skill operation |
|---|---|
| Rule exists but was too soft | Strengthen the existing rule with a clear trigger and MUST/MUST NOT outcome |
| Rule exists but is vague | Modify it to define the observable condition, action, and boundary |
| Two rules conflict | Replace or merge them into one authoritative rule using the evidence priority |
| Required output element is repeatedly omitted | Add or strengthen a structural slot/checklist item |
| Agent over-infers | Tighten the evidence boundary and define when clarification is blocking |
| Shared change leaves stale dependent content | Add dependency enumeration and a stale-reference validation step |
| Output shape causes repeated misunderstanding | Define the positive output contract and confirm it before production |
| Completion check missed the error | Add the smallest validation that would have caught the actual failure |

Do not add a second rule beside a weak original. Edit the original unless the new behavior belongs to a distinct existing section.

## 6. Scope of the Edit

Before editing, map every accepted lesson to:

- the existing rule it modifies, or the precise gap it fills
- the file and section that own the behavior
- the validation that proves the change works
- the existing behavior that must continue to work

The evolution is incomplete if the patch fixes the source example but cannot explain the generalized trigger, if the same rule is repeated in multiple authoritative locations, or if unrelated Target Skill behavior changes without evidence.
