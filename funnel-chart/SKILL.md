---
name: funnel-chart
description: Use when a user provides funnel steps (nodes) with numbers and wants a conversion funnel chart image, or asks to turn a metric chain (DAU → withdrawal page → bubble → click → submit → withdrawal success) into a funnel/漏斗图/转化图. Also use for penetration funnels, stage drop-off charts, and multi-period funnel comparisons.
---

# Funnel Chart

## Purpose

Turn a list of funnel stages and their user counts into one clean, presentation-ready funnel PNG. Every percentage is computed by the bundled renderer from the counts — the config never stores a hardcoded percentage, so numbers and ratios can never drift apart.

## Principle

- **Counts are the source of truth.** The user supplies stage names and counts; per-stage penetration, cumulative penetration against the first stage, drop-off users and drop-off rate, and end-to-end penetration are all derived by `scripts/render_funnel.py`.
- **One screen, one kind of information.** Counts live inside the funnel blocks; percentages appear exactly once, in the right-hand data column. Repeated figures caused two rejected drafts (see `references/origin-case.md`).
- **Never invent numbers.** If counts are missing, ask for them. If the user explicitly asks for an illustrative draft, every illustrative value must be labeled as such in both the image and the reply.
- **Always date the data.** Multi-period data gets one image per period, each with its own date badge — never mixed into one chart.

## Required Input

Stages in chronological order with their user counts (the first stage is the base and counts must decrease monotonically).

| Situation | Action |
| --- | --- |
| All counts provided | Render immediately, and attach the computed ratios in the reply |
| Partially provided, or percentages instead of counts | Ask once for everything: ① stage names ② counts per stage (percentages are acceptable if the denominator is named) ③ data date ④ penetration basis (stage-over-stage vs. all-against-base) |
| Narrative only, no numbers | Ask for the numbers; only proceed as a clearly labeled illustrative draft if the user asks for one |

Optional: title, data date badge, stage-level notes such as the dominant reason for loss at the final stage, 16:9 output, custom colors.

## Workflow

1. **Validate.** Counts must decrease stage by stage. If a stage is larger than the previous one, ask whether the basis differs instead of rendering silently.
2. **Write a config JSON** (schema: `references/config-schema.md`). Only `name` and `count` are required; the final stage may carry a `note`.
3. **Render.**
   ```bash
   python3 scripts/render_funnel.py --config <config>.json
   ```
   The renderer prints each stage's count and penetration rate plus the end-to-end rate — use those printed values in the reply instead of doing arithmetic by hand. Keep the config and the PNG in the project folder, not in the skill folder; a config copied out of the skill needs its `out` path adjusted (see `references/config-schema.md`).
4. **Inspect the rendered PNG before delivering.** Check that the title and date badge are not clipped, the right-hand column has no line collisions, the final-stage `note` does not overlap a funnel block, and the footer is complete.
5. **Deliver** the PNG plus a Markdown table of stage / count / stage penetration / cumulative / drop-off, and name the largest drop-off stage. When the user changes numbers, edit the config and re-render.

## Output Contract

- Layout: title and date badge top-left, four KPI cards (end-to-end penetration, base count, final-stage count, largest single-stage drop-off), a funnel whose width is the square-root-compressed count with translucent connectors between stages, a right-hand column holding stage penetration / cumulative / drop-off, and a two-part footer stating data source and basis.
- Color: one warm-to-cool ramp (orange → red → magenta → purple → blue); the final stage reads cooler to signal closure. Do not use five saturated competing hues.
- Funnel blocks show counts only; each percentage appears once, in the right-hand column.
- Mark the largest drop-off stage with a red "最大漏损" chip beside its name. Put the dominant reason for final-stage loss in red on the last line of the right-hand column, never inside a funnel block.
- Do not stack a drop-off ranking panel plus a wide data table on top of the funnel — that duplication is what made earlier drafts feel dense and unclear.
- Support 3–8 stages; the canvas height adapts to the stage count.

## References

- `references/config-schema.md` — JSON field reference and minimal example.
- `references/example_spp_funnel.json` — real case (SSP withdrawal subsidy funnel, 2026-09-22).
- `references/origin-case.md` — how the layout was settled and which drafts were rejected, to be read before restyling.

## Invocation Example

`Use $funnel-chart. Data date 2026-09-22: 7,848 → 5,700 → 5,411 → 1,052 → 509 → 314; final-stage loss reason: 74.2% rejected for insufficient balance.`

When the user only says "draw me a funnel", collect the four required inputs in one question first, then render.
