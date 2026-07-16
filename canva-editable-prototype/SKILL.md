---
name: canva-editable-prototype
description: Use when converting UI screenshots, prototype PNGs, wireframes, or generated app screens into Canva designs where text, controls, cards, icons, and image regions must remain separately editable.
---

# Canva Editable Prototype

## Principle

Treat editability as a verified requirement, not a claim. A visually correct Canva page fails when visible text is baked into an image.

## Workflow

1. Inspect every source image and record its dimensions.
2. Create a per-screen element inventory before calling Canva. Capture exact visible copy, hierarchy, controls, repeated components, icons, and image-fill regions. Read [references/editability-qa.md](references/editability-qa.md).
3. Check whether Canva tools are callable.
   - If callable, continue.
   - If the user explicitly requested Canva and tools are absent, use plugin discovery and request installation. Never claim installation without a successful result.
4. Choose the conversion path:
   - Use `canva_image_to_design` for flat references when retaining geometry is the first priority.
   - Use `canva_generate_design` with a complete screen brief when native text editability is the first priority or a previous Magic Layers conversion flattened text. Use a phone-wallpaper/custom mobile design type and include every string verbatim.
5. Create one Canva design per screen unless the user requests a combined design.
6. Audit the result before handoff:
   - Verify title and page count with `canva_get_design`.
   - Start an editing transaction to inspect returned rich-text and fill elements when available.
   - Compare detected text elements against the inventory.
   - Cancel the inspection transaction when no edits are required.
7. If any required string is missing from editable text:
   - Do not report the design as fully editable.
   - Retry once using the native-generation path with exact copy and simplified layout instructions.
   - If Canva still flattens or omits required text, report the limitation and identify the affected strings. Do not silently accept the raster result.
8. Present direct Canva edit links and a short QA table listing native text, native UI elements, image fills, and known gaps.

## Fidelity Rules

- Preserve the source canvas ratio and one-screen-per-page mapping.
- Quote every visible string verbatim in Canva generation prompts.
- Keep photos, complex illustrations, gradients, and cinematic thumbnails as image fills.
- Require headings, body copy, labels, buttons, navigation, tags, timestamps, and metadata to be native text.
- Require simple cards, dividers, pills, buttons, and backgrounds to be native shapes when Canva exposes them.
- Prefer fewer accurate layers over many mislabeled or duplicated layers.
- Never describe a whole-image fill as editable layers.

## Canva Transaction Safety

- Use `start_editing_transaction` before inspecting or changing an existing design.
- Show returned previews when the tool provides them.
- Ask for explicit approval before committing draft edits.
- Cancel abandoned transactions so draft state is not left unresolved.

## Output

Report for each screen:

- source filename
- Canva design ID and edit link
- page count
- editable text coverage
- editable UI coverage
- image-fill regions
- unresolved fidelity gaps
