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

Confirm one of these modes in the representative-table preview:

| Mode | Use when | Required shape |
|---|---|---|
| `row_complete` | Each prototype, page state, or design row will be reviewed, implemented, or accepted independently; also use whenever the user asks to keep all logic with the corresponding image | Each right cell is a complete requirement unit. Include every applicable condition, display rule, interaction outcome, business/lifecycle rule, fallback, exact UI string, and acceptance result. Repeat shared logic where necessary; never use “same as above” or require a table-external section to understand the row. |
| `shared_below` | The user explicitly approves a compact comparison centered on variant differences | Rows contain state-specific differences; genuinely common logic and test-point acceptance appear once below the table. |

When the user has not chosen a mode, recommend `row_complete` for page/state requirements and `shared_below` for compact experiment or style comparisons. The user's latest approved table structure always wins.

## Required Pre-Draft Preview

Before writing the final document, show:

1. the proposed document outline
2. the proposed test-point grouping
3. one representative table using actual evidence
4. selected logic-placement, image-reference, UI-copy-language, and acceptance-detail modes

Ask whether the user wants sections added, removed, renamed, reordered, or shortened. Formal drafting starts only after explicit approval.

## Table Pattern

```markdown
### T01 Test Point Name

| Prototype | Requirement summary |
|---|---|
| ![V01](assets/V01.png) | **适用条件**<br>1. Confirmed condition or state.<br><br>**页面规则**<br>1. Visible layout and behavior.<br><br>**交互流程**<br>1. Tap action → destination or result.<br>2. Close/back action → retained state.<br><br>**异常降级**<br>1. Confirmed unavailable or failure behavior.<br><br>**界面文案**<br>1. Element: `Exact approved copy`.<br><br>**本行验收标准**<br>1. Observable result for this state. |
| ![V02](assets/V02.png) | **适用条件**<br>1. Alternative condition or state.<br><br>**页面规则**<br>1. Visible layout and behavior for this state.<br><br>**交互流程**<br>1. Tap action → destination or result.<br><br>**异常降级**<br>1. Confirmed unavailable or failure behavior.<br><br>**界面文案**<br>1. Element: `Exact approved copy`.<br><br>**本行验收标准**<br>1. Observable result for this state. |
```

The example shows `row_complete`. For `shared_below`, remove repeated common logic from rows and add approved `#### 共用规则` and `#### 验收标准` blocks after the table.

## Stable Logic Slots

Use these slots in this order. Omit slots that are not applicable or not evidenced; do not manufacture content to fill the template.

| Slot | What it must answer |
|---|---|
| Applicability | Which condition, configuration value, state, or user group selects this variant? |
| Page/display rules | What appears, disappears, moves, stays fixed, or must not be obscured? |
| Interaction flow | What happens after every meaningful tap, close, back, swipe, or system action? Where does the user go and what state remains? |
| Business rules | Which eligibility, entitlement, consumption, state-transition, or cross-entry rules are needed to execute this row? |
| Configuration | Which exact parameter/value controls the behavior? Reference the central parameter table instead of repeating its full definition. |
| Lifecycle/frequency | When does it appear, how often, when is it consumed, and how can a new version show again? |
| Precedence/fallback | What wins when parameters conflict, and what happens for missing, invalid, or unavailable values? |
| UI copy | What exact approved string appears for each element and under which state or condition? Preserve its approved language even when the PRD narrative uses another language. |
| Measurement | Which exposure, action, success, failure, or guardrail matters when measurement is in scope? |
| Acceptance | What observable result proves this row is correct? Include it in-row for `row_complete`; keep it at test-point level for `shared_below`. |

Interaction flow is mandatory whenever an actionable control is shown. Do not stop at “clickable” or “enters the feature”; name the confirmed destination, outcome, close behavior, or unchanged state.

## Detail Rules

- Follow the confirmed logic-placement mode consistently. `row_complete` rows may repeat shared rules by design; `shared_below` rows contain differences and move only genuinely common logic below the table.
- In `row_complete`, use short ordered slot blocks inside the right cell. Do not create separate table-external sections for display rules, interactions, UI copy, exceptions, or acceptance that belong to the same prototype state.
- State exact configuration keys and exact values. Do not use `/`, combined values, or descriptive prose as an executable experiment value.
- Keep cloud-control definitions in one central parameter table: meaning, key, type, legal values, default, fallback, and precedence when applicable.
- Preserve the configuration granularity the user confirmed. If one switch controls the whole feature, do not invent additional switches; reference that single key from each affected row.
- Eligibility-gated content must define both qualified and unqualified visibility. When eligibility is mutable or externally resolved, also define loading/query-failure behavior and whether it is rechecked before an irreversible action. Incentive eligibility must not disable the underlying product capability unless the user explicitly confirms that dependency.
- Keep acceptance concise at the confirmed placement: per row for `row_complete`, or at test-point level for `shared_below`. Use Given/When/Then only when the user approves that style or precise transitions need it.
- Add experiment, events, push, permissions, data, or recovery sections only when requested or evidenced.
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
