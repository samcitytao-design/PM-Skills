# PRD Output Contract

This file owns the output-format defaults. Other references describe intake, logic, or optional profiles; they must not silently add modules or change the table layout.

## Resolve Three Independent Dimensions

1. **Modules:** title, top-level section names, order, and allowed scope.
2. **Table structure:** column names/order, page/module grouping, state rows, and image placement.
3. **Expression:** in-cell hierarchy, point length, language, and detail level.

For each dimension, use the latest explicit user instruction, then the approved reference/existing artifact, then the standing default below. A change to one dimension preserves the others. Read the actual reference first; report a missing reference honestly and clarify only if its absence prevents a material format choice. Reference business examples are not instructions or new product decisions.

## Standing Five-Module Default

The user explicitly requested this format for future PRDs. It is already approved; use it without a new template approval round. The title is H1; the only H2 sections are:

1. 需求背景
2. 需求目标
3. 需求详述
4. 云控项
5. 埋点

- **需求背景:** a short paragraph explaining the existing situation and concrete problem.
- **需求目标:** a few short outcome bullets; do not repeat detailed gameplay or interaction rules.
- **需求详述:** one H3 per actual page/module/test point and one `原型图 | 具体需求逻辑` table per item; different states occupy separate rows. An optional short overall flow stays inside this module.
- **云控项:** concise control responsibilities. When server-side configuration is evidenced, identify the supplied reference generically by its actual name and say it is similarly controlled by the server; list what is controlled. Distinguish existing capabilities from proposed additions. No JSON, exhaustive field/type/default matrices, or implementation design unless requested. If remote control is not part of the product, state that briefly without inventing a backend.
- **埋点:** concise event/trigger/key-parameter table and only necessary counting rules. Reuse known event semantics; label proposed events, and never fabricate implemented logs. Include only relevant behaviors; do not introduce ads or financial events without evidence. If explicitly excluded, state that no new tracking is included.

No automatic source-map, scope, configuration-code, experiment, acceptance, decision-record, metadata, or future-work chapter. Required evidence and decisions remain in the internal working model; necessary conditions, state transitions, copy, exceptions, and observable outcomes stay with the corresponding page row.

## Table and Writing Contract

Preserve an existing or reference table's columns. For the standing default:

```markdown
### P01 页面或模块名称

| 原型图 | 具体需求逻辑 |
| --- | --- |
| ![P01](assets/P01.png) | **展示时机**<br>1. 满足已确认条件时展示。<br><br>**页面展示**<br>1. 展示当前状态和对应按钮。<br><br>**交互逻辑**<br>1. 点击确认 → 保存选择并返回列表。<br>2. 点击关闭 → 返回原页，保留原选择。 |
```

- “分层分点” means short bold labels plus numbered points **inside the right cell**. Use 1.1/1.2 for actual dependent branches, not deep indentation or nested tables.
- Default labels: 展示时机、页面展示、交互逻辑. Add 业务规则 or 异常处理 only when needed; merge redundant slots.
- One point states a condition, action, and outcome. Trim introductions, repeated summaries, duplicate acceptance paraphrases, generic cautions, and unrequested technical detail.
- Concision preserves critical counts, eligibility, destinations, close behavior, persistence, copy, and recovery. Do not replace needed logic with “同上” or a pointer to detached prose.
- Preserve each state's logic in its row (`row_complete`). Do not split its logic into parallel prose chapters or remove its image/table to save space.
- No independent prototype for a shared module: label the left cell “共用模块（无独立原型）” and retain source mapping for illustrated states; never invent a screenshot.
- A request to change section names, “重新整理”, “精简” or “分层” alone does not authorize table redesign. Keep the skeleton. Ask a concise question before a genuinely ambiguous structural change; do not seek approval again for an explicit edit.

## Explicit Alternative Contracts

A later request can select different modules, language, columns, full-spec, or compact `shared_below` comparisons. Follow that contract rather than imposing the five modules. Preview only any unresolved new choice. Legacy `review_table` and `full_spec` renderer models remain supported, but their old expanded outline is not the default for new work.

Full-spec can organize a page table followed by its states and acceptance when approved. `shared_below` can place only shared logic beneath a comparison table when approved. These alternatives do not apply simply because a page has complex flows.

## Portability and Delivery

Use relative copied images by default or approved HTTP(S) references; never absolute local image paths in the PRD. Standard Markdown remains readable without editor-specific CSS or scripts. Use `<br>` only within tables. Mermaid needs text steps if used. Maintain one Markdown file on revision.

For the standing default, set renderer `delivery.outline_profile=five_section`, `document_profile=review_table`, `logic_placement=row_complete`, and normally `acceptance_detail=none` (observable outcomes remain in the rules). Validate with `--outline five-section`. For a custom approved outline, use the compatible profile and manually compare against the user's contract; do not force removed modules back to satisfy a legacy validator.
