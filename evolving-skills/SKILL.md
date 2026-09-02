---
name: evolving-skills
description: Use when a user explicitly names an existing Target Skill and asks to improve it from a completed or substantially completed real usage history containing feedback, corrections, revisions, or accepted outcomes.
---

# Evolving Skills

## Purpose

Improve one user-specified Target Skill from evidence produced by its real use. Reconstruct the path from initial request to accepted result, identify why corrections were needed, retain reusable behavior, and make the smallest validated change that reduces future correction cost.

Core principles:

- The user specifies the Skill to evolve.
- Real usage supplies evidence; conversation history supplies learning signals.
- Accepted revisions reveal useful deltas, but corrections are evidence rather than rules.
- Learn the reason behind a correction, not its project-specific outcome.
- Prefer improving existing rules over accumulating new ones.

This Skill is domain-neutral. It must not encode business knowledge, design taste, numerical values, copy, page details, or workflow parameters from one project.

## Non-Negotiable Gates

1. Require one explicit Target Skill. Never infer it from recency, file names, or the last tool used. If absent or ambiguous, ask the user to name it and stop before mutation.
2. Read the complete Target Skill and every supporting resource relevant to a candidate change before editing.
3. Review the fullest available usage history: initial task and constraints, initial output, each correction and revision, abandoned options, and the final accepted state. Do not treat the latest message or final artifact as the complete history.
4. If missing history prevents reliable Initial → Final attribution, state the evidence gap and do not manufacture a lesson. Continue only with conclusions supported by available evidence.
5. Modify only the named Target Skill. A correction may expose another Skill's issue, but that does not authorize changing it.

## Required Workflow

1. **Resolve the Target.** Locate the Runtime Skill currently loaded and the Source of Truth that should be maintained. Determine whether they are the same path, copies, or divergent versions. When Git is involved, inspect root, remote, branch, status, and relevant history before editing.
2. **Reconstruct the evolution.** Follow [references/evolution-protocol.md](references/evolution-protocol.md) and build an internal Delta Ledger from initial output through accepted result.
3. **Find root causes.** For every meaningful rework, distinguish the surface correction from the missing, weak, conflicting, or unenforced Target Skill behavior that allowed it.
4. **Filter candidate lessons.** Evaluate reusability, stability, scope, evidence strength, future value, and overfitting risk. Record both `Learned` and `Not Learned` decisions.
5. **Plan the minimal edit.** For each accepted lesson, search the Target Skill first. Prefer `MODIFY → STRENGTHEN → GENERALIZE → MERGE → RELOCATE → ADD`; use `REMOVE` when an obsolete or conflicting rule must be replaced. Add a section only when no existing location fits.
6. **Edit safely.** Preserve unrelated behavior and user changes. Use conditional `WHEN → MUST/SHOULD` rules when the lesson is context-dependent. Do not copy the source project's example into the Target Skill.
7. **Validate before deployment.** Follow [references/validation-and-sync.md](references/validation-and-sync.md). Run Replay, Generalization, Counterexample, Regression, Pollution, Duplication, and Conflict checks plus any existing Skill tests or validators.
8. **Synchronize only when requested.** Make Runtime and Source-of-Truth copies identical without overwriting unknown changes. Review the exact diff, commit only Target Skill evolution files, use a message describing what the Skill learned, push without force, and verify the remote revision.
9. **Report concisely.** Name the Target Skill, Learned, Updated, Not Learned, validation results, synchronization state, and commit hash. Never claim local or GitHub synchronization without verifying it.

## Stop Conditions

Stop without modifying or pushing when the Target Skill is unspecified, the Target Skill cannot be read, evidence cannot support a reusable lesson, Runtime/Source-of-Truth identity is unresolved, relevant files contain unsafe unknown changes, or remote authorization fails. Preserve safe work and report the exact completed and blocked steps.
