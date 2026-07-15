# Direct Prototype Intake

This intake organizes existing images only. It never generates replacement screens, enforces a canvas size, or invokes an upstream prototype-generation skill.

## Required Inventory

For every source image record:

| Field | Meaning |
|---|---|
| Source file | Original filename or attachment label |
| Proposed ID | Stable ID such as `P01` or `P03-ERROR` |
| Proposed name | Neutral name based on visible purpose |
| Classification | Page, state, overlay, fragment, or continuation |
| Visible evidence | Text, controls, navigation, data, and state indicators actually visible |
| Inference | Possible entry, action, relationship, or purpose not directly visible |
| Confidence | High, medium, or low |
| Generate PRD section | Yes/No and reason |

## Splitting Rules

Use separate IDs when the image shows a different route, tab, full-screen view, meaningful overlay, or state whose actions or outcomes materially differ.

Do not split merely because one page contains multiple cards or sections. Treat a cropped image as a fragment until its parent page is known. Treat visually identical images with different data as one page unless the data represents a distinct business state.

## Evidence Rules

- OCR text is evidence of visible copy, not proof of business rules behind it.
- A disabled control proves the visual state exists; it does not prove why it is disabled.
- A number proves an example display value; it does not prove calculation, currency, precision, or ownership.
- A button label suggests an action; its destination and side effects remain inference until evidenced.
- Similar visual patterns suggest reuse; they do not prove shared implementation.

## Approval Request

Present the total image count, proposed page/state count, mapping table, inferred relationships, duplicates/fragments, and missing evidence. Ask for explicit approval.

Do not interpret “continue,” silence, or approval of one row as approval of the complete map unless the user's wording clearly covers the whole set.
