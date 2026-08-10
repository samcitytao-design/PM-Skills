# Reconstruction Contract

## Source Classification

| Source | Default treatment |
|---|---|
| Complete mobile app | Preserve the full pixel viewport, including system and bottom navigation regions. |
| Mobile web | Preserve browser-safe content bounds and distinguish page UI from browser chrome. |
| Tablet | Preserve orientation and source ratio; do not normalize to a phone canvas. |
| Desktop | Preserve source viewport and scrolling model; use responsive behavior only beyond it. |
| Partial UI | Use the crop's original pixel dimensions as the default web viewport and Figma frame; do not invent off-crop UI. Infer a full-device viewport only when the user requests a complete screen or surrounding context materially affects the deliverable. |
| Multi-screen image | Separate each complete screen/state, assign stable IDs, and implement their transitions. |

Do not normalize complete screenshots to a different standard width unless the user explicitly requests it.

## Element Inventory

Before coding, record:

- source dimensions and screen classification
- major layout regions and stacking order
- exact visible copy and typography hierarchy
- controls, selected/disabled/completed states, and destinations
- repeated patterns and proposed component names
- icons, logos, photos, illustrations, and other image regions
- overlays, sheets, dialogs, toasts, and navigation states

Flag uncertain OCR copy instead of silently substituting different text; keep confirmed copy as editable text nodes.

## Native DOM Mapping

| Visible element | Preferred implementation |
|---|---|
| Action | `<button type="button">` with a visible state change |
| Navigation | `<nav>` containing links or buttons with selected state |
| Progress | `<progress>` or an ARIA-labelled meter with a real fill element |
| Dialog/sheet | Accessible dialog markup, focus handling, close action, and backdrop |
| Repeated card/list row | Reusable React component rendered from structured data |
| Exact text | Editable text node; do not rasterize it |

Use CSS for layout, borders, shadows, radii, gradients, simple icons, and status shapes. Keep DOM nesting understandable because it becomes the basis of Figma layer structure.

## Asset Rules

Use image assets only for genuine photos, illustrations, brand marks, complex textures, or small details that cannot reasonably be reproduced as native DOM. Crop and size them as independent elements; do not combine nearby editable text or controls into the image.

Never use:

- the full source screenshot as a background
- sliced screenshot regions as fake cards or controls
- invisible hotspot overlays
- a canvas rendering that flattens editable interface structure

## Viewport and Responsiveness

Match the source pixel viewport for primary validation. For a partial crop, use the crop dimensions unless the user explicitly requests a complete device screen or the missing bounds materially change the output. Prevent browser default margins and accidental scale changes. Keep fixed mobile shells centered only when the surrounding desktop preview requires it; the captured root must retain the source dimensions. Add graceful behavior at nearby widths without changing the source-view composition.
