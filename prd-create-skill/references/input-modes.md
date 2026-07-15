# Input Modes

## Mode A: Standard Prototype Package

Expected evidence may include:

- approved screen/state manifest
- per-screen element inventory
- visual foundation
- one image per approved screen or state
- QA notes, assumptions, and special-treatment notes

Verify rather than assume completeness:

| Check | Pass condition |
|---|---|
| Stable IDs | Every manifest item has a unique ID |
| Image mapping | Each generated item maps to an existing image |
| Count | Manifest and image counts agree, except documented shared images |
| State coverage | Explicit business-critical states are present |
| Source clarity | User-provided facts and inferred content are distinguishable |

The upstream manifest is an approved visual plan, not proof that all product rules are complete.

## Mode B: Direct Prototype Images

Accept images from any source: design exports, screenshots, wireframes, hand sketches, generated images, presentation crops, or mixed sets.

Before scanning product logic:

1. inventory files
2. identify duplicates, variants, fragments, overlays, and unreadable assets
3. propose stable IDs and names
4. create an evidence/inference split
5. obtain explicit page-map approval

Read [prototype-intake.md](prototype-intake.md) for the required table and confirmation gate.

## Mixed Inputs

When a package and additional images coexist:

- treat user-labeled additions as candidate new states or replacements
- do not silently overwrite package images
- identify conflicts by ID, filename, visible state, and timestamp when available
- ask which source governs only when the conflict changes requirements

## Unsupported Or Incomplete Files

Report unreadable files and continue with readable evidence when that does not change the page map. If missing files prevent identifying pages or critical states, stop at the intake report and request the missing evidence.
