# Element Inventory Template

Use this template after the screen manifest and before image generation. The goal is to make every page explicit enough for image generation now and editable-layer reconstruction later.

## Summary

- Product:
- Inventory version:
- Source requirement:
- Approved screen manifest:
- Fixed image dimensions: **720 × 1563 px**, portrait
- Handoff target: separate editable-layer skill

## Per-Screen Inventory

### `<screen-id>` — `<screen name>`

- Type: Page / State
- User goal:
- Entry trigger:
- Required state:
- Primary action:
- Secondary actions:

#### Layout Regions

List regions from top to bottom.

| Region | Purpose | Required elements | Content/data | State notes |
|---|---|---|---|---|
| Status / safe area |  |  |  |  |
| Header / app bar |  |  |  |  |
| Main content |  |  |  |  |
| Footer / bottom nav |  |  |  |  |

#### UI Elements

| Element | Role | Copy/data | Visual priority | Reuse/component candidate | Later editable-layer expectation |
|---|---|---|---|---|---|
|  |  |  | Primary / Secondary / Tertiary | Yes / No | Native editable / Image fill / Special handling |

#### Media And Complex Visuals

| Region | Source or prompt direction | Later treatment expectation | Notes |
|---|---|---|---|
|  |  | Image fill / Editable approximation / Special handling |  |

#### Interaction And State Details

- Active tab or selection:
- Loading/empty/error/success behavior:
- Disabled or unavailable actions:
- Overlay/modal/sheet behavior:
- Microcopy and feedback:

#### Assumptions And Open Questions

- Assumptions:
- Unresolved details:

## Reusable Patterns Across Screens

| Pattern | Appears in screens | Expected variants | Notes for later editable-layer skill |
|---|---|---|---|
|  |  |  |  |

## Handoff Notes For Editable-Layer Skill

- Regions expected to become native editable layers:
- Regions expected to remain image fills:
- Regions needing special reconstruction judgment:
- Shared components likely needed:
- Text styles likely needed:
- Color/style tokens likely needed:
