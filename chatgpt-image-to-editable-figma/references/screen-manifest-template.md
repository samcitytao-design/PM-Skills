# Screen Manifest Template

## Summary

- Product:
- Platform:
- Target device class: Mobile portrait
- Fixed base dimensions: **720 × 1563 px**
- Screen count:
- Image count:
- Separate image rule: One screen or visually distinct state per image
- Size rule: Every generated image is exactly **720 × 1563 px**
- Approval rule: Images are generated only after the user approves the manifest, element inventory, and visual foundation

## Manifest

| ID | Screen name | Type | Source evidence | Entry trigger | User goal | Major regions | Primary action | Required state | Example data | Dimensions | Generate image | Filename | Element inventory status | Later editable-layer notes | Assumptions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 |  | Page |  |  |  |  |  | Default |  | 720 × 1563 px | Yes | `P01_<screen-name>_720x1563.png` | Needed / Drafted / Approved | Native editable / Image fill / Special handling notes |  |

## Flow Order

`P01 → P02 → P03`

## Long-Page Continuations

When one viewport cannot show all required content, create continuation rows such as `P01-A` and `P01-B`. Every continuation remains exactly **720 × 1563 px** and counts as a separate image.

## Optional States

List recommended but unapproved states separately. Do not add them to the generation count until approved.
