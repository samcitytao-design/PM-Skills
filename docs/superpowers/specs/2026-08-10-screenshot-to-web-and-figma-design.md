# Screenshot to Web and Figma Skill Design

## Objective

Create a reusable Codex skill named `screenshot-to-web-and-figma` that accepts one or more UI screenshots and produces three required deliverables:

1. A React/semantic HTML implementation with simulated interactions.
2. A publicly deployed webpage URL.
3. A newly created Figma Design file containing editable layers captured from the real DOM.

The implementation must reconstruct the interface. It must never place the source screenshot behind the page or use it as a full-page image substitute.

## Trigger and Invocation

The skill should trigger when a user asks to convert, recreate, rebuild, or pixel-match a UI screenshot, mockup, wireframe, or prototype image into an interactive webpage and editable Figma design.

Example invocation:

```text
$screenshot-to-web-and-figma Recreate this UI screenshot as an interactive webpage and editable Figma file.
```

## Scope

### Included

- Inspect one or more supplied UI images.
- Classify the source as mobile app, mobile web, desktop, tablet, partial UI, or multi-screen input.
- Extract visible text, structure, spacing, colors, typography, controls, icons, and repeated patterns.
- Build the page with React and semantic HTML/CSS components.
- Simulate plausible interactions through dialogs, toasts, tabs, progress, claimed states, and navigation.
- Render and visually compare the implementation against the source.
- Publish the webpage by default with Sites.
- Create a new Figma Design file and capture the rendered DOM into it.
- Verify that the Figma result contains nested editable frames and text rather than one flattened bitmap.
- Return source location, public URL, Figma URL, interaction notes, verification results, and known differences.

### Excluded by Default

- Production backend integration.
- Real payments, authentication, analytics, or destructive actions.
- Production-ready accessibility certification.
- Converting complex illustrations or photographs into native vectors.
- Building a full Figma component library unless explicitly requested.

## Architecture

Use a compact orchestration skill with progressive disclosure:

```text
screenshot-to-web-and-figma/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── reconstruction-contract.md
    ├── interaction-and-qa.md
    └── figma-capture-runbook.md
```

- `SKILL.md` owns the ordered workflow, hard gates, required deliverables, failure recovery, and capability routing.
- `reconstruction-contract.md` defines screenshot classification, DOM/component reconstruction rules, responsive sizing, and prohibited shortcuts.
- `interaction-and-qa.md` defines interaction inference, visual comparison, functional checks, and acceptance criteria.
- `figma-capture-runbook.md` defines temporary capture-script injection, Figma file creation, DOM capture, editable-layer inspection, and cleanup.

Do not add a generic React starter asset in the first version. The surrounding Sites workflow already owns project scaffolding, and a bundled starter would become stale and constrain framework-specific choices.

## Workflow

### 1. Intake and Source Inspection

- Confirm that every referenced image is readable.
- Inspect the image at original resolution.
- Record source dimensions and classify the UI form factor.
- Detect whether multiple screens or distinct states are present.
- Ask only for missing information that would materially change the output; otherwise infer sensible behavior and proceed.

### 2. Reconstruction Plan

- Create a concise element inventory covering layout regions, text, controls, repeated components, imagery, and expected interactions.
- Preserve the source viewport and major information hierarchy.
- Choose React with semantic HTML/CSS as the default implementation.
- Use real DOM elements for cards, text, buttons, navigation, progress, status indicators, and dialogs.
- Use image assets only for genuine image content or visual details that cannot reasonably be represented as native layers.

### 3. Interactive Web Implementation

- Build each repeated pattern as a reusable component.
- Keep controls keyboard-operable where practical.
- Implement inferred interactions with local state, dialogs, toasts, progress changes, claim/completion states, and internal navigation.
- Avoid live external side effects unless the user explicitly authorizes them.
- Keep the screenshot available only as a visual reference, never as a page background.

### 4. Web Verification

- Run the relevant lint, type, test, and build commands available in the generated project.
- Open the local page at the target viewport.
- Capture a rendered screenshot and compare structure, alignment, spacing, text, colors, radii, shadows, and component states.
- Exercise every visible interactive control and confirm its state change or destination.
- Iterate until the result is a credible pixel-level first pass or clearly disclose remaining differences.

### 5. Default Public Deployment

- Invoke the Sites build and hosting capabilities.
- Publish the verified page by default.
- Confirm that the public URL loads and renders the intended page.
- Treat an unavailable hosting capability or missing authorization as a recoverable partial failure: preserve the working source and local verification, then state the exact resume step.

### 6. Editable Figma Capture

- Load the mandatory Figma file-creation, design-generation, and Figma-use skills before their corresponding tools.
- Create a new Figma Design file unless the user explicitly supplies a destination file.
- Temporarily add the official HTML-to-design capture script only to the local capture target.
- Capture the smallest root selector that contains the reconstructed screen.
- Poll the capture job until it succeeds or returns a terminal failure.
- Inspect Figma metadata to verify nested `FRAME` and `TEXT` nodes, independently selectable controls, and expected sections.
- Obtain a Figma screenshot for visual verification.
- Remove the temporary capture script, stop local servers, close capture tabs, and confirm the source worktree is clean.

### 7. Final Handoff

Return:

- source directory or repository path
- public webpage URL
- Figma Design URL and captured node
- interaction summary
- verification commands and results
- known differences or partial failures

Do not claim that HTML interactions automatically become Figma prototype connections. Describe the captured result as editable layers; offer component/variant/prototype wiring as a separate follow-up.

## Failure Recovery

- Missing image: ask the user to attach it again and stop before implementation.
- Ambiguous multi-screen source: identify the detected screens and request only the choice that changes scope.
- Missing font or icon: use the closest available substitute and disclose it.
- Build failure: diagnose and repair before publishing.
- Sites authorization or deployment failure: preserve the verified local project and provide a resume command or authorization step.
- Figma authorization failure: preserve the deployed webpage URL and resume from Figma file creation after login.
- Capture failure: verify the capture script, URL reachability, root selector, and viewport before retrying.
- Flattened Figma result: fail verification and recapture from semantic DOM; never report it as editable success.

## Validation Strategy

Treat this as a technique skill and test it on realistic variation:

1. Baseline a screenshot-to-web request without the new skill and record omissions such as missing deployment, flattened capture, weak interaction coverage, or leaked temporary scripts.
2. Run the same scenario with the skill and verify the ordered three-part delivery.
3. Run a variation with a partial screenshot or multiple states to check classification and clarification behavior.
4. Validate the skill folder with Skill Creator's `quick_validate.py`.
5. Check `agents/openai.yaml` against the final `SKILL.md`.
6. Confirm the local installed copy matches the committed repository copy.

## Acceptance Criteria

The skill is complete when:

- Its name and frontmatter pass validation.
- Its description reliably triggers for screenshot/image-to-web-and-Figma requests.
- The workflow explicitly prohibits screenshot-as-background reconstruction.
- It requires semantic React/HTML components and interaction simulation.
- It publishes a public webpage by default.
- It creates a new editable Figma Design file by default.
- It verifies nested editable Figma nodes and visual similarity.
- It cleans temporary capture instrumentation and local processes.
- It has been installed under `~/.codex/skills/screenshot-to-web-and-figma`.
- Repository and installed copies are identical.
- The GitHub branch contains only files related to this skill and its design/plan documentation.

## Repository and Delivery

- Repository: `samcitytao-design/PM-Skills`
- Branch: `agent/add-screenshot-to-web-and-figma-skill`
- Local skill destination: `~/.codex/skills/screenshot-to-web-and-figma`
- Publish flow: commit the finished skill, push the branch, and open a draft pull request against the repository's default branch.

GitHub authentication is a prerequisite for the final push. If the local `gh` token is invalid, request re-authentication with `gh auth login` before the publishing step.
