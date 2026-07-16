# Editability QA

## Inventory

For each screen, list:

| Element | Exact content | Expected Canva type | Required |
|---|---|---|---|
| Heading | Verbatim text | Text | Yes |
| Body copy | Verbatim text | Text | Yes |
| Button label | Verbatim text | Text inside shape | Yes |
| Card | Purpose/name | Shape/group | Yes |
| Icon | Semantic name | Vector/graphic | Preferred |
| Photo/hero | Visual description | Image fill | Yes |

## Audit Gate

A design passes only when:

- every required visible string exists as a native rich-text element;
- text is not duplicated inside an underlying raster layer;
- photos and complex artwork remain separate from editable text;
- simple UI surfaces are independent shapes or groups where supported;
- the page count and aspect ratio match the source set;
- no screen is represented only by one full-page image.

## Failure Report

When a design fails, report:

- missing native text strings;
- regions still flattened into images;
- visual differences introduced by regeneration;
- whether another Canva pass is likely to help;
- whether manual Canva reconstruction is required.
