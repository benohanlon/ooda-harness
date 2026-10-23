# Editable layout prototypes

Template revision 0.1, included in kit v1.3. **These are studies, not approved replacements for cover v1.2.**

Each SVG has editable text, explicit coordinates and a separate linked photographic layer. All four retain the full chosen wording, including NEEDS without a full stop. The clean eye was prepared by removing the flattened letters and rules from the approved image with the built-in image tool. Some photographic detail may differ. Preserve the approved cover as the benchmark.

| Layout | Dimensions | Source | Preview |
| --- | --- | --- | --- |
| Full cover | 1280 × 640 | [SVG](cover-editable.svg) | [JPEG](../previews/cover-editable.jpg) |
| Compact landscape | 960 × 720 | [SVG](compact-landscape.svg) | [JPEG](../previews/compact-landscape.jpg) |
| Square | 1080 × 1080 | [SVG](square.svg) | [JPEG](../previews/square.jpg) |
| Portrait | 1080 × 1350 | [SVG](portrait.svg) | [JPEG](../previews/portrait.jpg) |

## Edit

Download and extract the [complete kit](../downloads/sovereign-ooda-brand-kit-v1.3.zip). Keep the folders together. Install the TTF files in [fonts/](../fonts/README.md) for desktop editing. Open an SVG in a vector editor, or edit its text nodes and coordinates in a text editor. Keep the image's proportions and the complete chosen copy.

The SVGs reference the eye and fonts using relative paths. Their JPEG previews are the portable display exports for GitHub. An isolated SVG copied out of the kit will lose those dependencies.

## Render

The included Node renderer uses Playwright and Chromium. It reads the linked local image and fonts, embeds them into a temporary browser document, waits for the fonts to load and exports a JPEG or PNG at the SVG's declared size. It does not request remote images or fonts.

From this `brand/templates` directory:

```sh
npm install
npx playwright install chromium
npm run render
```

To use an existing Chromium or Chrome executable, set `PLAYWRIGHT_CHROMIUM_EXECUTABLE` to its path before running. Playwright is pinned in [package.json](package.json). The [renderer](render.mjs) also rebuilds the colour and typography specimens and the template gallery.

## Select a revision

Compare exports beside the approved cover at full size and at their intended display width. Check every word, natural anatomy, pupil contrast, margins and the eye's diagonal geometry. The compact layout enlarges the central message through recomposition; it does not create more detail by enlarging the source image.

Keep these previews under `previews/`. A template becomes a new approved artwork only when the sovereign selects it and the guide, manifest and project's chosen approval record are updated together.
