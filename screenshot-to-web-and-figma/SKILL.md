---
name: screenshot-to-web-and-figma
description: Use when a user provides UI screenshots, mockups, wireframes, or prototype images and wants interactive webpage recreation, pixel-matched HTML or React, a public deployment, editable Figma layers, or any combination of those outputs.
---

# Screenshot to Web and Figma

## Overview

Reconstruct supplied UI images as real interactive DOM, publish the verified page, and capture that DOM into a new editable Figma Design file. Treat the image as evidence to inspect, never as the implementation.

## Required Capability Routing

- **REQUIRED SUB-SKILL:** Use `sites:sites-building` for the web project and `sites:sites-hosting` for default publication.
- **REQUIRED SUB-SKILL:** Use `figma:figma-create-new-file` before creating a Figma file.
- **REQUIRED SUB-SKILL:** Use `figma:figma-generate-design` with `figma:figma-use` for webpage-to-Figma translation; load `figma:figma-use` before any `use_figma` call.
- Use an available browser-control capability for viewport rendering, interaction checks, capture navigation, and screenshots.
- Use the active image-inspection capability to inspect every supplied image at original resolution before planning.

If a required capability is unavailable, finish all independent stages, preserve their artifacts, and report the exact capability or authorization needed to resume.

Treat source inspection as read-only intake, not as a project mutation. If a new Sites project is required, make initialization the first project-changing action after intake. Treat an explicit request for a public link as deployment approval; ask again only when the hosting tool enforces a separate confirmation.

## Non-Negotiable Contract

- Never use the source screenshot as a page background.
- Never substitute full-page image slices, invisible hotspots, or a flattened screenshot for native structure.
- Use React and semantic HTML/CSS by default. Build text, cards, buttons, navigation, inputs, progress, status, and dialogs as real elements.
- Make repeated patterns reusable components with stable, descriptive names.
- Preserve exact visible copy and the complete-screen source viewport unless the user explicitly requests responsive redesign.
- Implement every visible control with a reversible interaction or a clear internal destination.
- Publish with Sites by default after local verification.
- Create a new Figma Design file unless the user explicitly supplies a destination.
- Verify nested editable `FRAME` and `TEXT` nodes before calling the Figma result editable.
- Remove the temporary capture script, stop local servers, close capture tabs, reset altered viewports, and verify source cleanliness before handoff.

## Workflow

### 1. Inspect and classify the input

1. Confirm every referenced image is readable.
2. Inspect each image at original resolution and record its pixel dimensions.
3. Classify each source as complete mobile app, mobile web, tablet, desktop, partial UI, or multi-screen.
4. Read [references/reconstruction-contract.md](references/reconstruction-contract.md) completely.
5. Ask one concise question only when a missing choice materially changes screen count, viewport, or behavior. Otherwise state the assumption and continue.

### 2. Inventory the screen

List the major regions, exact text, controls, repeated patterns, imagery, and visible states. Identify likely component boundaries and interactions before coding. For multiple screens, assign stable screen IDs and preserve their relationships.

### 3. Build semantic interactive DOM

1. Create or reuse a React project that supports public Sites hosting.
2. Reconstruct the screen with semantic HTML/CSS and reusable components.
3. Use native elements and CSS shapes/icons where practical. Use raster assets only for genuine image content or visual details that cannot reasonably be native DOM.
4. Read [references/interaction-and-qa.md](references/interaction-and-qa.md) completely.
5. Implement explicit behavior first; infer missing behavior with reversible local state such as dialogs, toasts, progress, claim/completion, tabs, and internal navigation.

### 4. Verify and iterate locally

1. Run the available lint, type, test, and production-build commands.
2. Open the page at the source viewport and capture a rendered screenshot.
3. Compare structure, bounds, spacing, typography, color, radii, shadows, icons, and content density.
4. Exercise every visible control and inspect each resulting state.
5. Iterate until the page is a credible pixel-level first pass. Record remaining differences instead of hiding them.

### 5. Publish publicly

1. Use `sites:sites-hosting` after the Sites build workflow.
2. Publish the locally verified page by default.
3. Open the returned public URL in a clean view and verify that the intended screen renders.
4. Preserve the URL for final handoff. If authorization blocks publication, preserve the verified source and state the exact resume step.

### 6. Capture editable Figma layers

1. Read [references/figma-capture-runbook.md](references/figma-capture-runbook.md) completely.
2. Load the mandatory Figma Skills before their corresponding write calls.
3. Create a new Figma Design file unless the user supplied a destination.
4. Capture the verified DOM using the active provider's supported HTML-to-design flow.
5. Inspect metadata and a rendered Figma screenshot. Require independent expected sections plus nested `FRAME` and editable `TEXT` nodes.
6. Treat a single flattened image or missing editable text as failed verification and recapture from semantic DOM.
7. Follow the active Figma workflow's distinction between a raw capture reference and a production design. If it requires deletion of the raw capture, first create and verify the final editable screen; the file must retain at least one complete editable design frame.
8. Complete every cleanup step in the runbook.

### 7. Hand off

Return, in this order:

1. Source directory or repository path.
2. Public webpage URL.
3. Figma file URL and captured node.
4. Interaction summary.
5. Verification commands and evidence.
6. Known differences, substitutions, or recoverable partial failures.

State that HTML interactions do not automatically become Figma prototype connections. Offer component/variant/prototype wiring as a separate follow-up.

## Failure Recovery

| Failure | Required response |
|---|---|
| Missing image | Ask the user to attach it again; do not invent the UI. |
| Ambiguous partial crop | Infer a viewport when safe; ask only if the viewport changes the intended deliverable. |
| Missing font or icon | Use the closest available substitute and disclose it. |
| Build or interaction failure | Diagnose and repair before deployment. |
| Sites authorization failure | Preserve verified source and local evidence; report the resume step. |
| Figma authorization failure | Preserve source and public URL; resume at file creation after login. |
| Capture failure | Check capture script, URL reachability, root selector, viewport, and terminal capture status. |
| Flattened Figma result | Fail verification and recapture; never report editable success. |

## Red Flags

- Coding before inspecting the source at original resolution.
- Styling a single full-screen `<img>` or background image.
- Adding transparent click regions over screenshot pixels.
- Claiming pixel accuracy without a target-viewport render comparison.
- Publishing before build and interaction checks pass.
- Calling Figma output editable without metadata evidence.
- Leaving capture instrumentation, servers, tabs, or source diffs behind.
- Claiming webpage behavior became Figma prototype wiring automatically.

If any red flag appears, stop that stage, correct it, and repeat its verification.
