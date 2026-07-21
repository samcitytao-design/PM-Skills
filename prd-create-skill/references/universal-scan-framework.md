# Universal PRD Scan Framework

Use every section as a lens, not as a demand to invent content. Mark a dimension `Not applicable` only when evidence supports that conclusion; otherwise distinguish `No issue found in available evidence` from `Confirmed complete`.

If source files have not actually been inspected, do not publish project-specific findings. State which evidence is required and describe only the generic procedure.

## 1. Goal And Scope

- problem, target outcome, users, context, success criteria
- included scope, excluded scope, and prototype features outside stated scope

## 2. Actors, Entry, And Authority

- who can enter, view, act, manage, or own data
- entry points, prerequisites, exit paths, and role differences

## 3. Pages And Navigation

- page/state/overlay identity
- enter, back, close, switch, deep-link, and cross-entry behavior
- navigation hierarchy and selected state

## 4. Actions And Feedback

- trigger, precondition, immediate feedback, final result
- primary, secondary, cancel, undo, destructive, and repeated actions

## 5. State And Lifecycle

- initial, loading, empty, normal, partial, success, failure, disabled, expired
- events that change state; persistence across refresh, re-entry, session change, or concurrent update

## 6. Workflow And Decisions

- primary path, branch conditions, interruptions, recovery, and completion definition
- explicit start and end for every material path

## 7. Data And Content

- source, format, validation, default, empty value, display, calculation, sorting, filtering, paging, search, refresh
- ownership, freshness, consistency, edit conflicts, dynamic copy, localization

## 8. Dependencies And Configuration

- external systems, runtime capabilities, permissions, network, environment
- fixed versus configurable behavior; missing configuration and incompatible versions

## 9. Errors, Recovery, And Reliability

- failure, timeout, interruption, duplicate request, partial success
- retry, cancel, rollback, idempotency, recovery, offline, degraded operation, terminal failure

## 10. Security, Privacy, And Applicable Constraints

- identity, authorization, sensitive data, audit, least privilege
- collection, storage, display, export, retention, deletion
- region, age, organization, or industry constraints only when applicable

## 11. Usability And Accessibility

- discoverability, hierarchy, feedback, input method, keyboard/focus, contrast, alternatives, assistive technology
- screen size, language length, zoom, dynamic text, reduced motion when relevant

## 12. Measurement, Operations, And Acceptance

- success measurement and key failure reasons
- configuration, moderation, review, audit, or manual operations when evidenced
- acceptance coverage at the user-approved detail level; use Given/When/Then only when approved or when precise transitions require it

## Output Classification

Classify every scan result as one of:

- `Confirmed`: directly supported by a higher-priority source
- `Conflict`: two sources disagree
- `Missing`: required to close a visible path but absent
- `Inference`: plausible but not confirmed
- `Optional`: improvement outside current acceptance

Before emitting an item, cite the source image, manifest row, user statement, or confirmed decision that made it relevant. If no citation exists, omit the item or phrase it as a question without asserting the underlying capability exists.
