# OODA design guidelines

Kit 2.1 · 10 November 2026. This refresh applies Ben's selected character-card direction across the OODA kit. It supersedes the old green/gold/bone palette for current production; prior work remains in Git history and the v1.3 archive.

## Purpose and visual identity

Use the [current cover](../assets/sovereign-ooda-cover.jpg) and [character collection](previews/profile-cards.png) together as references. The family combines dark petrol teal, luminous mint, restrained orange, tactile print detail and disciplined typography. Nous Research / Hermes is an influence, not a licence to add third-party marks or claim official brand specifications.

Preserve each image's job and meaning. The eye carries human agency and the surrounding world. Baldwin counsels personal responsibility. Blake brings commercial accountability. Harry represents the sovereign's candidate interests. Bateson's woodland expresses ecology and relationships. Odysseus's ship, red cheek, distant Ithaca and hearth smoke express resourcefulness and homecoming. Architecture illustrations explain relationships governed by the written contracts.

## Colour

| Production value | Hex | Purpose |
| --- | --- | --- |
| Petrol dark | #031C1D | Flat background and negative space |
| Mint | #B8F4DC | Primary type, rules and photographic highlights |
| Muted teal | #5F8D85 | Supporting boundaries and photographic midtones |
| Signal orange | #F17435 | Selected emphasis, action and restrained accents |

These values are authoritative for flat native text and geometry. Photographs retain tonal variation; different source lighting is not permission to change the ink palette. Do not reintroduce bone, antique gold, emerald or unrelated white into current labels. Keep sufficient contrast and use wording/geometry as well as colour to explain diagram relationships. Avoid glows and decorative gradients in the information layers.

## Typography

| Function | Family | Weight |
| --- | --- | --- |
| Headers and metadata | IBM Plex Mono | Regular 400 / Medium 500 |
| Character names | Barlow Condensed | Black 900 |
| Role titles | Barlow Condensed | Bold 700 |
| Quotes | Barlow Condensed | Regular 400 and Bold 700 |
| Human message and diagram hierarchy | Inter | Bold 700 |

Use actual bundled fonts with live SVG type. Generated artwork's apparent letterforms are references, not reproducible font definitions. Keep text separate from the photographic layer. A copy edit must not regenerate faces or reinterpret the entire layout.

Harry's two quote lines use the same family and size: setup regular, challenge bold. Preserve Ben's exact wording: “Right now I'm in first gear. Would you like to see me shift to six?” Do not silently substitute “sixth”. Role copy written for Bateson and Odysseus is not a source quotation.

## Character-card geometry

The canvas is **1536 × 1024**, ratio 3:2. All dimensions are explicit in [tokens](tokens.json) and the [source builder](templates/build-source.py).

- Header bottom rule: y58. Picture bounds: x24, y60, width1488, height744.
- Information band starts at y804. Orange divider: x500. Title/quote column: x530.
- Name type: 116px at weight900; title: 41px; quote: 29px, line height32px. These sizes are common to the set. Name length does not move the divider.
- Destination URL: bottom right, mint IBM Plex Mono 22px. Keep a minimum 24px gap from source credits.
- Attribution rule: y970. Metadata stays within the frame. Long character surnames can use the designated secondary line; long quotations wrap within the common quote area.
- Keep the header, frame, rules, margins, metadata spacing and semantic colours constant. Essential text must remain legible at actual display size. Full attribution and a long source quotation may need full-size viewing.

001 is Baldwin, 002 Blake and 003 Harry. Further numbering remains unassigned until selected. The card number identifies artwork in this collection; it is not a deployment identity or installer selection.

## Cover composition and exact copy

Keep the 2:1 cover's oblique eye, large iris, dark pupil and reflected-world detail. The iris remains the intimate fragment of a person in a moment of noticing. Avoid a frontal whole-eye substitute or arbitrary pupil movement. The mint/teal source is a new image-tool derivative, not a pixel-identical restoration.

The title sits above a thin orange rule. The eye is dominant, with the complete upright personal message inside the pupil. Strategic labels and the two-line cognitive footer remain subordinate. The current native cover export is 1280 ×640; the new photographic source is 1774 ×887. Do not imply an upscale creates new detail.

Exact chosen copy:

- SOVEREIGN OODA HARNESS
- THERE'S / SOMETHING / IN YOU / THAT THE WORLD / NEEDS
- COUNTER-REVOLUTIONARY / MANOEUVRE WARFARE
- COGNITIVE SUPERIORITY / WITHIN THE DISTRIBUTED MIND

Keep the British spelling MANOEUVRE, the hyphen and NEEDS without a full stop. Add **sovereignharness.io** as a visible destination footer, following Ben's 10 November correction. Use mint IBM Plex Mono at full opacity on dark negative space. Preserve the selected cover copy, composition and source credits. Do not add an author name or signature to the cover; keep creator attribution in accompanying text and metadata.

Alternative cover layouts recompose the image and retain the entire wording. Do not stretch anatomy, crop text away or change the message for a different ratio.

## Illustration and diagram integrity

Use image generation for photographic or poetic artwork changes. Preserve recognisable character and source-specific meaning. Keep credits and the difference between a source quote and role copy explicit. Do not invent a photographer or imply documentary accuracy for the generated ship illustration.

Use native SVG for diagram text, nodes and connectors. Labels must describe the written system faithfully: one accountable agent can handle ordinary work; paired mode is selectively commissioned, with two complete OODAs and complementary, reversible positions. A diagram does not instantiate that mode. Arrowheads and boundaries carry meaning, so inspect them visually as well as checking label fit. Keep an illustrative, non-canonical status.

## Production and review

1. Recover the current brief, exact copy and relevant source image.
2. Reuse the palette, fonts, fixed layout and existing renderer.
3. Save photographic edits as distinct sources; keep their prompts and provenance.
4. Edit native type and data, build and render the affected exports.
5. Compare at common size and at intended viewing size. Check text, credits, geometry, meaningful details and collection coherence.
6. Repair the actual defect. A successful render or font-load check alone is not visual acceptance.
7. Update the manifest and downloadable kit with the final assets and verify links. Retain previous accepted versions in Git history.

Publication, deployment and GitHub's social-preview setting remain separate effects. New artwork does not appoint roles or change profile IDs. The brand kit creates no permission for personal data disclosure or unrelated repository changes.
