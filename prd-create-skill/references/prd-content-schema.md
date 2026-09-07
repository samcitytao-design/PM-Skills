# PRD Content Schema

Use this logical model whether the document is written directly or generated from JSON.

## Top-Level Fields

| Field | Required | Content |
|---|---|---|
| `document_profile` | Yes | `full_spec` or `review_table`, confirmed before drafting |
| `delivery` | Yes | `language`, optional distinct `ui_copy_language`, `image_mode`, `acceptance_detail`, `output_target`, `update_mode`, and confirmed review-table `logic_placement` |
| `meta` | Yes | title; other metadata is internal or rendered only if the output contract includes it |
| `overview` | Yes | background, goal, users, scenarios, success, scope, non-goals as applicable |
| `sources` | Yes | prototype files, manifest source, evidence notes |
| `pages` | For `full_spec` | stable page/state records |
| `test_points` | For `review_table` | one requirement/test variable with one or more variant rows |
| `actors` | When evidenced | role, authority, ownership, entry |
| `flows` | When multiple steps exist | starts, nodes, decisions, ends, recovery |
| `states` | When state changes exist | state, entry event, exit event, persistence |
| `rules` | When evidenced | behavior and configurable/fixed ownership |
| `data` | When evidenced | meaning, source, format, validation, freshness |
| `dependencies` | When evidenced | external capability and unavailable behavior |
| `risks` | When evidenced | error, privacy, constraints, recovery |
| `measurement` | When required | success metric, event, result, failure reason |
| `decisions` | Yes | confirmed and delegated decisions only |
| `future` | Optional | non-blocking improvements outside acceptance |

## Full-Spec Page Record

Every page or state contains:

- `id`, `name`, `type`, `image`
- purpose
- actor and entry/preconditions when evidenced
- visible regions and content
- primary, secondary, cancel, close, back, and destructive actions when present
- local states and cross-page effects
- loading, empty, failure, timeout, repeated-action behavior as applicable
- dependencies and permissions only when evidenced
- acceptance criteria at the approved detail level
- evidence notes and confirmed inference decisions

## Review-Table Test-Point Record

Every test point contains:

- `id`, `name`, and optional purpose
- `variants`: one row per confirmed style, state, position, or value
- `shared_rules`: logic common to every variant; rendered in every row for `row_complete` or once below for `shared_below`
- `acceptance`: concise test-point acceptance; rendered in every row for `row_complete` or once below for `shared_below`

Each variant contains:

- `id`, `name`, and `images`
- `applicability`: selecting condition or exact configuration value
- `display`: visible behavior and layout differences
- `interactions`: actions with destination, result, close behavior, or retained state
- `configuration`: parameter references needed in this row
- `rules`, `lifecycle`, `fallback`, `copy`, `measurement`, and row-specific `acceptance` only when applicable

`delivery.logic_placement` accepts `row_complete` or `shared_below`. New review-table documents must set it explicitly after resolving the output contract through explicit instructions, an approved reference, or standing defaults. The renderer defaults to `shared_below` only for backward compatibility with existing models.

The renderer must preserve test-point grouping. It must not turn each variant image into an independent page section.

## Five-Module Rendering

Set `delivery.outline_profile` to `five_section` for the standing format. It requires `review_table` and `row_complete`. Supply `overview.background` and `overview.goals` as concise text/list values, `configuration_summary` as concise responsibility statements, and `tracking` as a list of `{event, trigger, parameters}` objects. Each must be explicit; use a truthful no-new-controls/no-new-tracking statement for an inapplicable module rather than inventing capabilities.

Sources and decisions are retained internally, not rendered as extra sections. Put rules, data, state, recovery and dependencies in applicable variant rows; non-empty detached top-level rule collections are rejected rather than silently dropped. The five-module renderer never adds future/decision/acceptance chapters. Omitted `outline_profile` retains legacy output for backward compatibility only; new work follows the resolved contract.

## Decision Record

Only resolved decisions enter the formal model:

- `id`
- question or decision title
- resolution
- source: explicit user choice or delegated recommendation
- impact

An unresolved blocking decision makes the model invalid.

## Review-Table JSON Example

```json
{
  "document_profile": "review_table",
  "delivery": {
    "language": "zh-CN",
    "outline_profile": "five_section",
    "ui_copy_language": "en",
    "image_mode": "relative",
    "acceptance_detail": "none",
    "logic_placement": "row_complete",
    "output_target": "Example-PRD.md",
    "update_mode": "new_file"
  },
  "meta": {
    "title": "Example PRD",
    "version": "1.0",
    "date": "2026-01-01"
  },
  "overview": {
    "background": ["Describe the confirmed problem."],
    "goals": ["Help a user complete the defined task."]
  },
  "sources": ["Confirmed prototype package"],
  "configuration_summary": ["No remote controls are included in this example."],
  "tracking": ["No new tracking is included in this example."],
  "test_points": [
    {
      "id": "T01",
      "name": "Example test point",
      "variants": [
        {
          "id": "V01",
          "name": "Variant A",
          "images": ["assets/V01.png"],
          "applicability": ["parameter=value_a"],
          "display": ["Confirmed visible behavior."],
          "interactions": ["Select the primary control → confirmed destination or result."],
          "copy": ["Primary action: Exact approved copy"],
          "acceptance": ["The matching state shows the approved action and reaches the confirmed result."]
        }
      ],
      "shared_rules": [],
      "acceptance": ["The selected configuration renders the matching variant."]
    }
  ],
  "decisions": [],
  "blocking_decisions": []
}
```

## Renderer Contract

- `delivery.outline_profile` is `five_section` or `legacy` (omission is backward-compatible legacy).
- The output contract, not the existence of an internal field, decides which modules render.

- `blocking_decisions` must be present as an empty list.
- `document_profile` and non-empty `delivery` must be present.
- `full_spec` requires non-empty `pages`.
- `review_table` requires non-empty `test_points`, and every test point requires at least one variant.
- `delivery.image_mode` is `relative`, `external`, or `mixed`.
- `delivery.update_mode` is `new_file` or `update_existing`.
- `delivery.logic_placement`, when present, is `row_complete` or `shared_below`; omission retains legacy `shared_below` rendering.
- Absolute local image paths are never valid.
