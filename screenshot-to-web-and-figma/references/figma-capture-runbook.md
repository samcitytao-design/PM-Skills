# Editable Figma Capture Runbook

## Prerequisites

- Finish local visual and interaction verification first.
- Identify the smallest root selector containing the reconstructed screen.
- Record source viewport dimensions.
- Load `figma:figma-create-new-file`, `figma:figma-generate-design`, and `figma:figma-use` before corresponding write calls.

## Capture

1. Create a new Figma Design file unless the user explicitly supplies a destination.
2. Start the verified page locally.
3. Temporarily add the official HTML-to-design capture script supplied by the active Figma provider. Do not add it to the deployed production page.
4. Set the browser viewport to the source dimensions.
5. Open the provider-generated capture URL with the selected root selector and single-use capture ID.
6. Poll the capture job until success or terminal failure. Never reuse a consumed capture ID.
7. Save the returned Figma file URL and captured node ID.

## Editable-Layer Verification

Inspect captured metadata and a Figma screenshot. Require:

- multiple nested `FRAME` nodes matching expected screen sections
- editable `TEXT` nodes containing visible source copy
- independent buttons, cards, navigation items, and repeated rows
- frame dimensions matching the intended source viewport
- a rendered result visually consistent with the verified webpage

A single image node, missing editable text, or absent expected sections fails verification. Correct the semantic DOM or root selector and capture again.

## Cleanup

1. Remove the temporary capture script from source.
2. Stop the local server or tunnel started for capture.
3. Close capture-only browser tabs.
4. Reset any viewport override.
5. Run `git diff --check` and inspect `git status --short`.
6. Preserve user changes and confirm no capture-only source change remains.

Do not claim that DOM event handlers became Figma prototype links. The raw capture creates editable visual layers; componentization, variants, and prototype wiring are a separate follow-up.

## Desktop Fallback

Use `@web-to-figma/desktop` only when the active Figma provider cannot capture HTML directly. Check the current official documentation or CLI `--help` before use; do not rely on memorized flags. Apply the same editable-layer verification and cleanup requirements.
