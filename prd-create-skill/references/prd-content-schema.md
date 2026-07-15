# PRD Content Schema

Use this logical model whether the document is written directly or generated from JSON.

## Top-Level Fields

| Field | Required | Content |
|---|---|---|
| `meta` | Yes | title, version, date, status, source mode |
| `overview` | Yes | background, goal, users, scenarios, success, scope, non-goals |
| `sources` | Yes | prototype files, manifest source, evidence notes |
| `actors` | When evidenced | role, authority, ownership, entry |
| `pages` | Yes | stable page/state records |
| `flows` | When multiple steps exist | starts, nodes, decisions, ends, recovery |
| `states` | When state changes exist | state, entry event, exit event, persistence |
| `rules` | When evidenced | behavior and configurable/fixed ownership |
| `data` | When evidenced | meaning, source, format, validation, freshness |
| `dependencies` | When evidenced | external capability and unavailable behavior |
| `risks` | When evidenced | error, security, privacy, constraints, recovery |
| `measurement` | When required | success metric, event, result, failure reason |
| `decisions` | Yes | confirmed and delegated decisions only |
| `future` | Optional | non-blocking improvements outside acceptance |

## Page Record

Every page or state contains:

- `id`, `name`, `type`, `image`
- purpose
- actor and entry/preconditions when evidenced
- visible regions and content
- primary, secondary, cancel, close, back, and destructive actions when present
- local states and cross-page effects
- loading, empty, failure, timeout, repeated-action behavior as applicable
- dependencies and permissions only when evidenced
- acceptance criteria in Given/When/Then form
- evidence notes and confirmed inference decisions

## Decision Record

Only resolved decisions enter the formal model:

- `id`
- question or decision title
- resolution
- source: explicit user choice or delegated recommendation
- impact

An unresolved blocking decision makes the model invalid.

## JSON Contract For Bundled Renderer

The renderer accepts UTF-8 JSON with this minimal shape:

```json
{
  "meta": {"title": "Example PRD", "version": "1.0", "date": "2026-01-01"},
  "overview": {"goal": "Help a user complete a defined task.", "scope": ["Included behavior"], "non_goals": []},
  "sources": ["Confirmed prototype package"],
  "pages": [
    {
      "id": "P01",
      "name": "Example page",
      "type": "Page",
      "image": "assets/P01.png",
      "purpose": "Complete the primary task.",
      "elements": ["Primary control"],
      "interactions": ["Selecting the control produces the confirmed result."],
      "states": ["Default"],
      "exceptions": [],
      "acceptance": ["Given the page is available, when the user selects the primary control, then the confirmed result is shown."]
    }
  ],
  "decisions": [{"id": "D-001", "title": "Primary result", "resolution": "Use the confirmed result.", "source": "User choice", "impact": ["P01"]}],
  "blocking_decisions": []
}
```

Additional fields may be rendered as normal Markdown sections when present. `blocking_decisions` must be an empty list.

The `blocking_decisions` field is mandatory. A missing, null, non-list, or non-empty value makes the model invalid and must stop formal rendering.
