# Visual QA Checklist

## Canvas Compliance

- [ ] Image dimensions are exactly **720 × 1563 px**
- [ ] Orientation is portrait
- [ ] The interface fills the canvas without a decorative device wrapper
- [ ] No mixed size or alternate aspect ratio is used
- [ ] Long-page continuation screens are also exactly **720 × 1563 px**

## Screen Isolation

- [ ] Exactly one screen or approved state is present
- [ ] No collage, board, device lineup, or adjacent screen appears
- [ ] Screen ID matches the manifest

## Structure

- [ ] All required regions are present
- [ ] Primary action is visually clear
- [ ] Information hierarchy matches the user goal
- [ ] Safe areas and system chrome are plausible within the fixed canvas

## State Accuracy

- [ ] Selected, disabled, loading, empty, error, success, bound, or unbound state is unmistakable
- [ ] No state from another manifest item leaked into this screen

## Content

- [ ] Product copy is readable
- [ ] Example data is plausible and internally consistent
- [ ] No critical text is cropped or garbled

## Visual Consistency

- [ ] Colors follow the shared semantic roles
- [ ] Typography follows the shared hierarchy
- [ ] Spacing, radii, shadows, icons, and buttons match approved screens
- [ ] Navigation and repeated components remain consistent

## Handoff Readiness

- [ ] Native-layer regions are identifiable
- [ ] Image-fill regions are identified
- [ ] Repeated components are recognizable
- [ ] Screen matches the approved element inventory
- [ ] Handoff notes are specific enough for a separate editable-layer skill
- [ ] No visual detail requires falsely claiming perfect raster decomposition

## Result

- PASS: Continue to next screen
- FAIL: Regenerate or repair this screen only, record the failure reason
- Automatic FAIL: Image is not exactly **720 × 1563 px**
