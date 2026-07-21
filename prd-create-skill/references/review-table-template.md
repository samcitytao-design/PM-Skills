# Review-Table PRD Profile

Use this profile when prototypes represent test points, experiments, placement options, visual treatments, or multiple styles of the same page behavior. The unit of organization is the **test point**, not the image.

## Grouping Model

```text
Test point
├── Variant A: one prototype row
├── Variant B: one prototype row
└── Shared rules: written once below the table
```

- Create one `###` section and one prototype/requirement table per test point or page requirement.
- Put every confirmed style or state belonging to that test point in the same table as a separate body row.
- Put multiple images in one left cell only when they demonstrate the same logic, such as one guide adapted to two already-defined entry positions.
- Split test points when variants test different variables, have different success metrics, or can be enabled independently.
- Keep source-image IDs for traceability even when several images are grouped under one test point.

## Required Pre-Draft Preview

Before writing the final document, show:

1. the proposed document outline
2. the proposed test-point grouping
3. one representative table using actual evidence
4. selected image-reference and acceptance-detail modes

Ask whether the user wants sections added, removed, renamed, reordered, or shortened. Formal drafting starts only after explicit approval.

## Table Pattern

```markdown
### T01 Test Point Name

| Prototype | Requirement summary |
|---|---|
| ![V01](assets/V01.png) | **适用条件**<br>- Confirmed condition or configuration value.<br><br>**页面规则**<br>- Visible layout and behavior.<br><br>**交互流程**<br>- Tap action → destination or result.<br>- Close/back action → retained state. |
| ![V02](assets/V02.png) | **适用条件**<br>- Alternative value.<br><br>**页面规则**<br>- Only the differences for this variant.<br><br>**交互流程**<br>- Tap action → destination or result. |

#### 共用规则

- Rules that apply to every row.

#### 验收标准

- Concise test-point acceptance when the approved template includes acceptance criteria.
```

## Stable Logic Slots

Use these slots in this order. Omit slots that are not applicable or not evidenced; do not manufacture content to fill the template.

| Slot | What it must answer |
|---|---|
| Applicability | Which condition, configuration value, state, or user group selects this variant? |
| Page/display rules | What appears, disappears, moves, stays fixed, or must not be obscured? |
| Interaction flow | What happens after every meaningful tap, close, back, swipe, or system action? Where does the user go and what state remains? |
| Configuration | Which exact parameter/value controls the behavior? Reference the central parameter table instead of repeating its full definition. |
| Lifecycle/frequency | When does it appear, how often, when is it consumed, and how can a new version show again? |
| Precedence/fallback | What wins when parameters conflict, and what happens for missing, invalid, or unavailable values? |
| Measurement | Which exposure, action, success, failure, or guardrail matters when measurement is in scope? |

Interaction flow is mandatory whenever an actionable control is shown. Do not stop at “clickable” or “enters the feature”; name the confirmed destination, outcome, close behavior, or unchanged state.

## Detail Rules

- Describe variant differences in the row; move shared logic below the table.
- State exact configuration keys and exact values. Do not use `/`, combined values, or descriptive prose as an executable experiment value.
- Keep cloud-control definitions in one central parameter table: meaning, key, type, legal values, default, fallback, and precedence when applicable.
- Keep acceptance concise at test-point level. Use Given/When/Then only when the user approves that style or precise transitions need it.
- Add experiment, events, push, permissions, data, or recovery sections only when requested or evidenced.
- Preserve advertisement, navigation, or other guardrails only when they are part of the confirmed requirement.

## Anti-Patterns

- one page section per screenshot when screenshots are variants of one test point
- one giant table containing unrelated test points
- repeating identical shared rules in every row
- listing a button without its destination or result
- burying unresolved decisions in the final PRD
- copying project-specific parameters, copy, frequency, or metrics into a reusable template
