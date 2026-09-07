# Review-Table PRD Profile

Use this profile when prototypes represent test points, experiments, placement options, visual treatments, or multiple styles of the same page behavior. The unit of organization is the **test point**, not the image.

## Grouping Model

```text
Test point
├── Variant A: one prototype row
├── Variant B: one prototype row
└── Logic placement: row-complete or shared-below, confirmed before drafting
```

- Create one `###` section and one prototype/requirement table per test point or page requirement.
- Put every confirmed style or state belonging to that test point in the same table as a separate body row.
- Put multiple images in one left cell only when they demonstrate the same logic, such as one guide adapted to two already-defined entry positions.
- Split test points when variants test different variables, have different success metrics, or can be enabled independently.
- Keep source-image IDs for traceability even when several images are grouped under one test point.

## Logic Placement Contract

Use the resolved mode from markdown-template.md. Only a genuinely new proposed mode needs a preview:

| Mode | Use when | Required shape |
|---|---|---|
| `row_complete` | Each prototype, page state, or design row will be reviewed, implemented, or accepted independently; also use whenever the user asks to keep all logic with the corresponding image | Each right cell is a complete requirement unit. Include every applicable condition, display rule, interaction outcome, business/lifecycle rule, fallback, exact UI string, and acceptance result. Repeat shared logic where necessary; never use “same as above” or require a table-external section to understand the row. |
| `shared_below` | The user explicitly approves a compact comparison centered on variant differences | Rows contain state-specific differences; genuinely common logic and test-point acceptance appear once below the table. |

The standing contract resolves the default to `row_complete`. Use `shared_below` only when explicitly selected by the user or an approved reference. Do not infer a format change from the subject of the work.

## Required Pre-Draft Preview

Use the output contract in markdown-template.md. Keep an approved table's columns and grouping. Preview the outline and a real row only when proposing an unresolved new format; an explicit revision or standing preference already resolves it.

## Table Pattern

```markdown
### T01 Page or test-point name

| 原型图 | 具体需求逻辑 |
|---|---|
| ![V01](assets/V01.png) | **展示时机**<br>1. Confirmed condition A.<br><br>**页面展示**<br>1. Display the current state and exact approved button text.<br><br>**交互逻辑**<br>1. Confirm → save the selection and return to the list.<br>2. Close → return to the original page without changing the selection. |
| ![V02](assets/V02.png) | **展示时机**<br>1. Confirmed condition B.<br><br>**页面展示**<br>1. Display the unavailable state.<br><br>**交互逻辑**<br>1. Retry → recheck availability and update this state.<br>2. Close → return to the original page. |
```

The example shows `row_complete`. For `shared_below`, remove repeated common logic from rows and add `#### 共用规则` after the table; add `#### 验收标准` only if the user selected that acceptance detail.

## Stable Logic Slots

These slots are a coverage checklist, not mandatory visible subheadings. Use the concise labels and numbered in-cell recipe in markdown-template.md; merge related slots and omit irrelevant ones.

| Slot | What it must answer |
|---|---|
| Applicability | Which condition, configuration value, state, or user group selects this variant? |
| Page/display rules | What appears, disappears, moves, stays fixed, or must not be obscured? |
| Interaction flow | What happens after every meaningful tap, close, back, swipe, or system action? Where does the user go and what state remains? |
| Business rules | Which eligibility, entitlement, consumption, state-transition, or cross-entry rules are needed to execute this row? |
| Configuration | Which approved control affects this behavior? Give product meaning; exact keys only when requested. |
| Lifecycle/frequency | When does it appear, how often, when is it consumed, and how can a new version show again? |
| Precedence/fallback | What wins when parameters conflict, and what happens for missing, invalid, or unavailable values? |
| UI copy | What exact approved string appears for each element and under which state or condition? Preserve its approved language even when the PRD narrative uses another language. |
| Measurement | Which exposure, action, success, failure, or guardrail matters when measurement is in scope? |
| Acceptance | What observable result proves this row is correct? Include it in-row for `row_complete`; keep it at test-point level for `shared_below`. |

Interaction flow is mandatory whenever an actionable control is shown. Do not stop at “clickable” or “enters the feature”; name the confirmed destination, outcome, close behavior, or unchanged state.

## Detail Rules

- Follow the confirmed logic-placement mode consistently. `row_complete` rows may repeat shared rules by design; `shared_below` rows contain differences and move only genuinely common logic below the table.
- In `row_complete`, use short ordered slot blocks inside the right cell. Do not create separate table-external sections for display rules, interactions, UI copy, exceptions, or acceptance that belong to the same prototype state.
- When an implementation or experiment configuration is explicitly requested, give exact keys and values. Otherwise describe what is controlled at the approved product level.
- Follow the 云控项 depth defined by the output contract. A server configuration reference does not by itself authorize a field/type/default matrix or JSON output.
- Preserve the configuration granularity the user confirmed. If one switch controls the whole feature, do not invent additional switches; reference that single key from each affected row.
- Eligibility-gated content must define both qualified and unqualified visibility. When eligibility is mutable or externally resolved, also define loading/query-failure behavior and whether it is rechecked before an irreversible action. Incentive eligibility must not disable the underlying product capability unless the user explicitly confirms that dependency.
- Observable outcomes must be clear; do not restate every rule as a second acceptance block. Render a dedicated acceptance block only at the approved detail level and placement: per row for `row_complete`, or at test-point level for `shared_below`. Use Given/When/Then only when the user approves that style or precise transitions need it.
- Place evidenced experiment, tracking, permission, data, and recovery logic inside the approved modules. Add a new section only when the user explicitly authorizes changing the outline.
- Preserve advertisement, navigation, or other guardrails only when they are part of the confirmed requirement.

## Anti-Patterns

- one page section per screenshot when screenshots are variants of one test point
- one giant table containing unrelated test points
- using `shared_below` after the user asks for self-contained rows
- using “same as above,” “see shared rules,” or another cross-reference inside a `row_complete` requirement cell
- splitting one prototype state's display, interaction, fallback, copy, and acceptance across parallel sections
- repeating identical shared rules in every row when `shared_below` was approved
- listing a button without its destination or result
- burying unresolved decisions in the final PRD
- copying project-specific parameters, copy, frequency, or metrics into a reusable template
