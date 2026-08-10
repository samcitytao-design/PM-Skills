# Interaction and QA Contract

## Interaction Inference

Choose behavior in this priority:

1. Explicit user instruction.
2. States or destinations visible in supplied images.
3. Established platform convention.
4. Reversible local-state simulation.

Ask only when competing choices materially change the deliverable. Otherwise state the assumption and implement it.

Cover every visible button, navigation item, tab, form control, task/claim action, modal trigger, and dismiss action. Suitable simulations include dialogs, sheets, toasts, selection, progress changes, completion/claimed states, tab switches, and internal route changes.

Do not perform real payments, authentication, account changes, external messages, deletion, or other live side effects without explicit authorization.

## Web Verification

Complete this evidence-backed checklist before deployment:

- [ ] Available lint, type, test, and production-build commands pass.
- [ ] Page renders at the source viewport without browser scaling.
- [ ] Rendered screenshot was compared with the source.
- [ ] Major region bounds, spacing, typography, colors, radii, borders, and shadows were checked.
- [ ] Exact visible copy was checked.
- [ ] Every visible interactive control was exercised.
- [ ] Dialogs, toasts, overlays, progress, and completion states close or reset predictably.
- [ ] Keyboard focus and accessible names work where practical.
- [ ] Browser console contains no unexplained errors.

After publication, open the public URL and verify the intended page, assets, and primary interactions again.

## Difference Reporting

Report concrete substitutions such as unavailable fonts, approximate icons, compressed imagery, or inferred off-screen behavior. A pixel-level first pass does not justify claiming exact identity when visible differences remain.
