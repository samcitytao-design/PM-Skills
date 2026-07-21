# Portable Markdown Profiles

Select and preview one profile before formal drafting. Do not silently choose a document structure.

## Profile Selection

| Profile | Use when | Primary unit |
|---|---|---|
| Review table | Test points, AB experiments, positions, styles, or several variants of one requirement | One table per test point, one row per variant |
| Full spec | Independent pages, multi-step flows, states, data, dependencies, or recovery dominate | One section per page/state plus flow detail |

Use the review-table profile by default when both profiles are plausible and the user is preparing a UI/product review. Read [review-table-template.md](review-table-template.md) for its grouping and logic rules.

## Review-Table Document Order

Preview this outline and let the user add, remove, rename, reorder, or shorten sections:

1. title and confirmed metadata
2. background and goal
3. scope and non-goals as applicable
4. input evidence/page map when useful to reviewers
5. page requirements organized by test point
6. central configuration parameter table when configuration exists
7. experiment plan when testing exists
8. events and success/guardrail measurement when requested
9. conditional modules such as push, permissions, data, dependencies, or recovery only when evidenced
10. confirmed decision record when useful for maintenance

## Full-Spec Document Order

1. title and metadata
2. background, goal, users, scope, non-goals, success
3. source and page map
4. information architecture, flows, and states
5. page requirements
6. rules, data, dependencies, and recovery as applicable
7. measurement as applicable
8. acceptance summary
9. confirmed decision record
10. future optimization when explicitly retained

Omit inapplicable sections instead of filling them with invented content.

## Full-Spec Page Layout

```markdown
## 页面需求

### P01 Page Name

> Type: Page | Source: `assets/P01.png`

| Prototype | Requirement summary |
|---|---|
| ![P01 prototype](assets/P01.png) | **Purpose**<br>Confirmed purpose.<br><br>**Key elements**<br>1. Element A<br><br>**Interactions**<br>1. Action → confirmed result. |

#### States And Recovery

| State | Trigger | Visible behavior | Exit or recovery |
|---|---|---|---|
| Default | Page entry | Confirmed display | Confirmed action |

#### Acceptance Criteria

- Concise acceptance in the approved style.
```

## Flow Layout

Use Mermaid only for meaningful multi-step or branching flows and follow it with concise text steps. Do not invent a branch to make a diagram look complete.

## Portability

- use the confirmed image mode: copied relative assets for a portable package, or stable HTTPS images for an online-review document
- never use absolute local filesystem paths
- use standard headings, lists, blockquotes, tables, images, and fenced Mermaid
- avoid external CSS, scripts, editor directives, or style-dependent meaning
- avoid nested tables and long prose inside table cells
- use `<br>` only inside compact summary tables
- include text steps when Mermaid support is uncertain

## Final Sections

Use `已确认决策记录`, never `待确认问题`. Use `后续优化` only for explicitly accepted non-blocking ideas outside current acceptance.
