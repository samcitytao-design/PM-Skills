# Validation, Synchronization, and Reporting

Run these checks after editing the Target Skill and before commit or synchronization.

## Behavioral Validation

| Check | Required question | Pass condition |
|---|---|---|
| Replay | If the updated Target Skill had existed at the start, would it have prevented or caught the important rework? | The new or strengthened rule directly addresses the root cause, not only the final symptom |
| Generalization | Does the lesson still work in a different domain or project with different values and presentation? | The trigger and behavior remain useful without source-project details |
| Counterexample | In what legitimate case should this rule not apply? | The rule has an observable condition or scope boundary and does not block valid alternatives |
| Regression | Which original Target Skill capabilities could this edit affect? | Existing validators/tests pass and preserved behavior remains reachable |
| Pollution | Did any current project detail enter the Skill? | No project name, transient value, amount, date, copy, page name, temporary design choice, or one-off rule is encoded as a default |
| Duplication | Does the Target Skill already express this lesson? | One authoritative rule remains; existing wording is modified, strengthened, generalized, merged, relocated, or removed before adding another |
| Conflict | Does the patch contradict another instruction? | Conflicts are resolved using the user's latest explicit direction and one coherent rule replaces competing versions |

When the Target Skill has tests, evals, fixtures, validators, or format checks, run them. For a new behavior supported by that test system, add a regression case. For judgment-heavy changes, run an isolated replay and at least one counterexample or different-domain scenario when agent evaluation is available.

Do not weaken a failed validation to make the patch pass. Refine the rule or the patch, then rerun the complete relevant suite.

## Runtime and Source-of-Truth Resolution

Confirm, do not assume:

| Item | Required evidence |
|---|---|
| Runtime Skill | Exact path currently loaded by Codex |
| Source of Truth | Exact maintained repository path |
| Relationship | Same path, symlink, identical copy, divergent copy, or unknown |
| Repository | Git root and expected remote URL |
| Revision context | Current branch, upstream, and latest remote state when network access is authorized |
| Worktree safety | `git status`, unrelated modifications, untracked files, and overlap with intended edits |

If Runtime and Source of Truth are separate, edit the maintained copy, validate it, synchronize only the Target Skill files to Runtime, and verify file equality. Never use a broad destructive sync to hide differences.

## Git Safety and Deployment

When the user requests repository synchronization:

1. Inspect Git root, remote, branch, status, and relevant diff before editing.
2. Preserve unrelated user changes. If they overlap the Target Skill and cannot be separated safely, stop and report the conflict.
3. Stage only files belonging to this Target Skill evolution.
4. Review staged diff and run the final validation suite again.
5. Use a commit message that describes the learned behavior, not `update skill`, `fix`, or `changes`.
6. Push without force. If the remote moved, fetch and reconcile safely; never overwrite it with a destructive reset.
7. Verify the remote branch or commit hash after push.

Authorization to evolve a Skill does not automatically authorize installation, commit, push, or changes to another repository. Perform only the synchronization actions the user requested.

## Final Report Contract

Keep the final report concise and evidence-based:

```markdown
## Skill Evolution Summary

Target Skill
<exact target name>

Learned
- <generalized behavior retained>

Updated
- <existing rule strengthened, merged, relocated, removed, or new gap filled>

Not Learned
- <project-specific value, preference, copy, or unproven inference intentionally excluded>

Validation
- Replay ✅/❌
- Generalization ✅/❌
- Counterexample ✅/❌
- Regression ✅/❌
- Pollution ✅/❌
- Duplication ✅/❌
- Conflict ✅/❌

Sync
- Local Skill ✅/❌
- GitHub ✅/❌

Commit
<verified hash or “not created”>
```

If any synchronization step fails, state what succeeded, what failed, why, current file/diff/commit state, and the exact next action. Never mark GitHub synchronized unless push and remote verification both succeeded.
