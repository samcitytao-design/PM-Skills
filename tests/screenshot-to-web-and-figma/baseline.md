# Baseline Evaluation

## Scenario

```text
Recreate /Users/shareit/Downloads/Frame 43.png as a pixel-matched interactive React/HTML page. Publish it publicly and create a new editable Figma file from the implementation. Do not ask questions unless a missing answer materially changes the result.
```

The evaluator received no custom Skill and performed no writes, deployment, or Figma mutation.

## Observed Result

- Completed in the proposed workflow: original-resolution inspection, UI inventory, semantic React/HTML reconstruction, real elements instead of an embedded screenshot, inferred interactions, target-viewport comparison, production verification, public deployment, new Figma file creation, editable-layer intent, visual comparison, and a multi-artifact final handoff.
- Omitted: explicit routing through Sites for default hosting; mandatory prerequisite Skill loading before Figma write calls; explicit metadata inspection for nested `FRAME` and editable `TEXT` nodes; temporary capture-script removal; local server shutdown; capture-tab closure; viewport reset; and final source-worktree cleanliness verification.
- Unsafe shortcut or ambiguity: the phrase “rebuilding/importing” did not specify a deterministic DOM-to-Figma capture path and could permit inconsistent reconstruction methods.

## Guidance Required

- State Sites as the default publishing capability and require verification of the public URL.
- State the prerequisite Figma Skills that must be loaded before corresponding tools.
- Provide one ordered HTML-to-design capture runbook with observable editable-layer checks.
- Make removal of capture instrumentation, process/tab cleanup, viewport reset, and clean-worktree verification required completion steps.
