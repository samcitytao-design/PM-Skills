# PRD Content Schema

Use this logical model whether the document is written directly or generated from JSON.

## Top-Level Fields

| Field | Required | Content |
|---|---|---|
| `document_profile` | Yes | `full_spec` or `review_table`, confirmed before drafting |
| `delivery` | Yes | `language`, `image_mode`, `acceptance_detail`, `output_target`, and `update_mode` |
| `meta` | Yes | title, version, date, status, source mode |
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
- `shared_rules`: logic common to every variant, written once
- `acceptance`: concise test-point acceptance only when included by the approved template

Each variant contains:

- `id`, `name`, and `images`
- `applicability`: selecting condition or exact configuration value
- `display`: visible behavior and layout differences
- `interactions`: actions with destination, result, close behavior, or retained state
- `configuration`: parameter references needed in this row
- `lifecycle`, `fallback`, and `measurement` only when applicable

The renderer must preserve test-point grouping. It must not turn each variant image into an independent page section.

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
    "image_mode": "relative",
    "acceptance_detail": "concise",
    "output_target": "Example-PRD.md",
    "update_mode": "new_file"
  },
  "meta": {
    "title": "Example PRD",
    "version": "1.0",
    "date": "2026-01-01"
  },
  "overview": {
    "goal": "Help a user complete a defined task.",
    "scope": ["Included behavior"]
  },
  "sources": ["Confirmed prototype package"],
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
          "interactions": ["Select the primary control → confirmed destination or result."]
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

- `blocking_decisions` must be present as an empty list.
- `document_profile` and non-empty `delivery` must be present.
- `full_spec` requires non-empty `pages`.
- `review_table` requires non-empty `test_points`, and every test point requires at least one variant.
- `delivery.image_mode` is `relative`, `external`, or `mixed`.
- `delivery.update_mode` is `new_file` or `update_existing`.
- Absolute local image paths are never valid.
