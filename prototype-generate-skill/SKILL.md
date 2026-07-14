---
name: prototype-generate-skill
description: Use when a user wants product requirements, PRDs, sketches, wireframes, screenshots, or written flows turned into a confirmed prototype screen plan, per-screen element inventory, and one separate 720×1563 prototype/reference image per approved page or state. This skill stops before editable Figma layer reconstruction.
---

# Prototype Generate Skill

## Purpose

Use this skill to turn product intent into a reviewable prototype image package:

1. Analyze the user's requirements and source prototypes.
2. Decompose the product flow into an explicit screen manifest.
3. List the required UI elements, content, states, and reusable patterns for every screen.
4. Present the manifest, element inventory, and visual foundation for user confirmation.
5. After explicit user approval, generate exactly one prototype/reference image for each approved screen or visual state.
6. Validate each generated image and package the outputs so another skill can convert them into editable Figma layers.

This skill is not for rebuilding images into editable Figma layers, creating Figma components, writing a full PRD, generating production code, or producing engineering handoff documentation unless the user separately asks for those deliverables.

## Capability Boundary

This skill owns:

- requirement analysis for prototype generation
- screen and state decomposition
- screen manifest creation
- per-screen UI element inventory
- shared visual foundation definition
- user confirmation before image generation
- separate image generation for approved screens
- visual QA for generated prototype/reference images
- handoff packaging for a later editable-layer skill

This skill does not own:

- converting raster images into editable Figma layers
- creating or modifying Figma files
- building Figma components, variables, styles, or prototypes
- claiming that generated raster images are editable source
- production UI implementation
- broad product strategy or full PRD writing

## Non-Negotiable Rules

### Fixed Canvas Size: 720 × 1563 px

**Every generated UI prototype/reference image must be exactly `720 × 1563 px` in portrait orientation.**

- This fixed size applies to every page, route, tab, overlay, modal state, empty state, success state, error state, loading state, and other manifest item marked for image generation.
- Do not generate mixed dimensions or mixed aspect ratios within the same task.
- Do not substitute common alternatives such as 720 × 1280, 1080 × 1920, 862 × 1822, 330 × 692, or device-mockup dimensions.
- Treat source screenshots and prototypes as structural or visual references. Recompose them into the fixed `720 × 1563 px` canvas rather than preserving a different source size.
- For long-scroll pages, represent one viewport per image. If more coverage is required, create continuation screens such as `P01-A`, `P01-B`, with every continuation still exactly `720 × 1563 px`.
- Do not use an extended scrolling canvas unless this skill is explicitly revised to allow another output standard.
- Any generated image that is not exactly `720 × 1563 px` fails validation and must be corrected before continuing.

### One Screen, One Image

**Every screen or visually distinct state must be generated as its own image.**

- Never place multiple app screens in one board, collage, contact sheet, presentation frame, or device lineup.
- Never combine separate routes, tabs, pages, modal states, empty states, success states, or error states into one reference image.
- A generated image must contain one full UI screen only, without surrounding moodboard content.
- If the user explicitly asks for a comparison board, storyboard, or multi-screen overview, treat it only as an additional presentation asset. Still generate and retain every approved screen separately at `720 × 1563 px`.

### Screen Count Must Be Traceable

Every image must map to one item in the approved screen manifest and use a stable screen ID, such as `P01`, `P02`, or `P03-SUCCESS`.

Do not silently add, remove, merge, or split screens after approval. If a new state is discovered during execution, add it to the manifest and clearly identify it as an inferred screen.

### Explicit Approval Before Image Generation

Do not generate any prototype/reference image until the user explicitly approves the screen manifest, element inventory, and visual foundation.

The approval request must state:

- total screen count
- total image count
- included pages and states
- canvas size: `720 × 1563 px`
- major assumptions
- anything inferred rather than user-provided

If approval is ambiguous, ask again. Do not treat silence as approval.

### Preserve Cross-Screen Consistency

Before asking for approval and before generating the first screen, establish a shared visual foundation covering:

- color roles
- typography hierarchy
- spacing rhythm
- corner radii
- elevation and shadows
- icon style
- navigation pattern
- image treatment
- button hierarchy
- form and feedback behavior

Every screen prompt and generated image must reuse this foundation unless the user requests a deliberate exception.

### Prototype Images Are Not Editable Source

A generated image is a visual target for review and later reconstruction. Do not claim that the prototype/reference image is editable source.

Instead, produce a clear element inventory that another skill can use to rebuild the image as editable layers. The inventory should identify:

- major layout regions
- text content and hierarchy
- controls and interaction states
- reusable components and repeated patterns
- icons and visual symbols
- data/content examples
- imagery or complex illustration regions
- regions likely to remain image fills
- regions expected to become native editable layers in a later skill

Never perform the editable-layer reconstruction inside this skill.

## Input Modes

Determine the input mode before planning:

| Input | Default treatment |
|---|---|
| Written requirement or PRD | Decompose into screens, then generate each screen |
| Low-fidelity wireframe | Preserve information architecture; redesign each screen at higher fidelity |
| Existing high-fidelity screenshot | Use as visual reference unless the user asks for redesign |
| Multi-screen prototype board | Detect and separate every screen before generation |
| Existing Figma file | Inspect only as source context if available; do not write to Figma in this skill |

## Required Workflow

### Step 1: Inspect All Source Material

Read the user's requirement, files, screenshots, prototypes, and existing Figma context before proposing screens.

Establish source priority:

1. the user's explicit latest instruction
2. the user's annotated prototype or screenshot
3. approved product flow or requirement document
4. existing design system or product conventions
5. clearly labeled inference

Do not redesign away explicit business logic or required modules.

### Step 2: Decompose The Requirement Into Product Structure

Extract:

- product type and scenario
- target platform; the output canvas remains fixed at `720 × 1563 px`
- primary user and user goal
- entry points and navigation model
- core task flow
- pages, routes, tabs, and overlays
- required states and transitions
- business-critical information and actions
- data examples and content density
- visual direction and brand constraints
- existing patterns that must be preserved

Then classify every candidate item as one of:

- **Page:** a route, tab, destination, or full-screen view
- **State:** a visually distinct condition of a page, such as loading, empty, error, success, disabled, bound, unbound, or modal-open
- **Component:** a reusable UI element that does not require its own full-screen image

### Step 3: Apply Screen Splitting Rules

Create a separate screen item when any of the following is true:

- the user navigates to a different route, tab, destination, or full-screen view
- a modal, sheet, drawer, permission prompt, or full-screen overlay is important to the requested flow
- loading, empty, error, success, disabled, bound, or unbound behavior is explicitly requested or business-critical
- the information hierarchy or primary action changes materially
- the source prototype already shows it as a separate screen

Do not create a separate screen merely because a page contains multiple cards or sections.

For a long scrollable page, design one `720 × 1563 px` viewport at a time. If more content must be shown, use continuation IDs such as `P01-A`, `P01-B`; every continuation must remain exactly `720 × 1563 px` and preserve visual continuity.

### Step 4: Build The Screen Manifest

Use [references/screen-manifest-template.md](references/screen-manifest-template.md).

The manifest must include for every screen:

- screen ID
- screen name
- type: page or state
- source or requirement evidence
- entry trigger
- user goal
- major visible regions
- primary and secondary actions
- example content or data
- dimensions and orientation, fixed as `720 × 1563 px`, portrait
- separate image filename
- element inventory status
- later editable-layer treatment notes
- assumptions or unresolved details

The final count of reference images must equal the final count of manifest rows marked `Generate image: Yes`.

### Step 5: Build The Page Element Inventory

For every manifest item, list the elements required to create the prototype image and to support a later editable-layer reconstruction.

Use [references/element-inventory-template.md](references/element-inventory-template.md).

The inventory must cover:

- screen ID and screen name
- top-to-bottom layout regions
- navigation, headers, footers, tabs, and bars
- cards, lists, forms, media regions, tables, overlays, and empty states
- visible text and example data
- primary, secondary, and destructive actions
- icons and image regions
- component reuse opportunities
- state-specific differences
- expected native editable regions for the later skill
- expected image-fill or difficult-to-reconstruct regions for the later skill
- unresolved content or interaction details

The element inventory is the bridge to the later editable-layer skill. Keep it specific enough that another skill can reconstruct the screens without re-interpreting the original requirements.

### Step 6: Define The Shared Visual Foundation

Before image generation, define a concise visual foundation:

- product personality and design direction
- background and surface system
- semantic color roles
- type scale and hierarchy
- spacing and grid
- component shape language
- iconography
- photography or illustration treatment
- interaction and state conventions
- accessibility constraints
- anti-patterns to avoid

Use [references/visual-foundation-template.md](references/visual-foundation-template.md).

If an existing design system is available, reuse it instead of inventing a new one.

### Step 7: Present The Prototype Generation Plan

Present the manifest, element inventory, and visual foundation for review before generating images.

The review must state clearly:

- total number of screens
- total number of images
- confirmation that each screen will be generated separately
- which states are included
- exact dimensions: `720 × 1563 px` for every screen
- which content is user-provided versus inferred
- which regions are expected to become native editable layers later
- which regions may remain image fills or require special treatment later
- assumptions and unresolved details

Stop and wait for explicit user approval. Do not generate images until the user confirms this plan.

### Step 8: Generate Each Screen Separately

Generate screens one by one in manifest order.

Every generation request must include:

1. the shared visual foundation
2. the exact screen ID and screen name
3. the screen-specific purpose and information hierarchy
4. all required visible regions and actions
5. realistic product copy and example data
6. the exact fixed canvas instruction: **720 × 1563 px, portrait**
7. the instruction: **one full UI screen only**
8. the instruction: **no collage, no multi-screen board, no moodboard, no surrounding presentation layout**
9. the instruction to avoid unreadable pseudo-text where possible
10. consistency anchors from previously approved screens

Use the prompt contract in [references/screen-generation-contract.md](references/screen-generation-contract.md).

File naming:

`<screen-id>_<screen-name>_720x1563.png`

Example:

`P03_withdrawal-details_720x1563.png`

### Step 9: Validate Each Generated Screen Before Continuing

After each image, run the checklist in [references/visual-qa-checklist.md](references/visual-qa-checklist.md).

At minimum verify:

- exactly one screen is present
- the image is exactly `720 × 1563 px` in portrait orientation
- required modules and actions are present
- no modules from another screen leaked into the image
- hierarchy matches the screen's user goal
- copy is readable and plausible
- global style matches approved screens
- bottom bars, safe areas, and scroll boundaries are correct
- state-specific UI is unmistakable
- the screen still matches the approved element inventory

If a screen fails, regenerate only that screen. Do not restart the entire set unless the shared visual foundation is wrong.

### Step 10: Run Cross-Screen Consistency QA

After all prototype/reference images are generated, verify the complete set:

- shared navigation dimensions and placement
- typography hierarchy
- color and surface roles
- spacing rhythm and grid
- component variants and states
- icon size and style
- button hierarchy
- form behavior and feedback
- image treatment
- safe-area handling within the fixed `720 × 1563 px` image canvas
- route and state naming

Fix local inconsistencies without changing already approved screen logic.

### Step 11: Package The Handoff For The Editable-Layer Skill

When image generation and QA are complete, package:

- approved screen manifest
- approved element inventory
- shared visual foundation
- generated image filenames
- per-screen QA notes
- known assumptions
- regions expected to become native editable layers later
- regions expected to remain image fills or need special treatment later
- any user-approved deviations from the plan

Do not create or modify a Figma file. Tell the user that the package is ready for the separate editable-layer skill.

## Change Requests And Iteration

When the user requests a change:

1. identify the affected screen IDs
2. preserve the shared visual foundation unless the request changes it
3. regenerate only affected reference images
4. update the manifest and element inventory for affected screens
5. re-run local QA and cross-screen regression checks

Do not regenerate unrelated screens.

## Assumption Policy

Ask only when a missing decision blocks the design.

Otherwise:

- make the smallest reasonable assumption
- label it in the manifest
- avoid inventing extra pages or business logic
- preserve the user's screen count when explicitly stated
- distinguish required states from optional recommendations

## Output Standard

When complete, report:

- approved screen manifest and final screen count
- generated image count and filenames
- element inventory status
- reusable patterns identified
- regions expected to become native editable layers in a later skill
- regions expected to remain image fills or need special treatment in a later skill
- assumptions made
- known fidelity gaps
- validation results, including confirmation that every image is exactly `720 × 1563 px`
- confirmation that no editable Figma reconstruction was performed by this skill

The final artifact must be a coherent product flow made of individually reviewable prototype/reference images plus a usable element inventory for the later editable-layer workflow, not a flat screenshot board.

## Failure Conditions

The task is not complete if any of the following is true:

- any generated image is not exactly `720 × 1563 px`
- mixed dimensions or aspect ratios appear within the screen set
- multiple screens were generated inside one image without explicit user instruction
- a manifest screen marked for generation has no matching image
- image count does not match the approved plan
- screens use inconsistent visual systems without justification
- the user was not asked to approve the manifest, element inventory, and visual foundation before image generation
- the element inventory is missing or too vague for a later editable-layer skill to use
- required states were silently omitted
- inferred screens were silently added
- raster images were misrepresented as editable source
- this skill created or modified Figma layers instead of handing off to the later editable-layer skill
