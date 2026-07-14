# Screen Generation Contract

Use one generation request per manifest screen.

## Global Foundation

Repeat the approved visual foundation without changing its semantic roles.

## Fixed Canvas Standard

- Exact output dimensions: **720 × 1563 px**
- Orientation: portrait
- One screen or approved state per image
- The interface must fill the canvas; do not place it inside a decorative device frame
- Do not use another size or aspect ratio
- Long flows must use separate continuation screens, each exactly **720 × 1563 px**

## Screen Identity

- Screen ID:
- Screen name:
- Product and platform:
- Exact dimensions: **720 × 1563 px**
- Orientation: portrait
- Output filename: `<screen-id>_<screen-name>_720x1563.png`

## Screen Purpose

- Entry trigger:
- User goal:
- Primary action:
- Secondary actions:

## Required Visible Regions

List every required region from top to bottom.

## Required Content

Use realistic, readable product copy and plausible example data.

## State Definition

State exactly what is active, selected, loading, empty, disabled, successful, failed, bound, or unbound.

## Hard Output Constraints

- Generate one full UI screen only.
- Generate the image at exactly **720 × 1563 px** in portrait orientation.
- Do not include another screen, alternate state, comparison view, device lineup, collage, contact sheet, moodboard, annotation board, or presentation frame.
- Do not place the UI inside a decorative phone mockup unless the user explicitly requests a separate presentation asset; the actual screen reference must still be delivered separately at **720 × 1563 px**.
- Fill the full canvas with the interface.
- Preserve the approved global visual foundation.
- Keep text readable and avoid pseudo-text where possible.
- Reject and regenerate any result whose canvas is not exactly **720 × 1563 px**.
