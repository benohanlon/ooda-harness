# Editable OODA artwork

Kit 2.1 uses live SVG type and separate generated photographic layers. This makes copy, font weights, colours and spacing reproducible across the collection.

| Layout | Canvas | Source |
| --- | --- | --- |
| Full cover | 1280 ×640 | [SVG](cover-editable.svg) |
| Compact landscape | 960 ×720 | [SVG](compact-landscape.svg) |
| Square | 1080 ×1080 | [SVG](square.svg) |
| Portrait | 1080 ×1350 | [SVG](portrait.svg) |
| Five character cards | 1536 ×1024 each | [Data](../profile-cards.json) and profile-pack SVGs |
| Cognitive dipole | 1254 ×1254 | [SVG](cognitive-dipole.svg) |
| Ecology overview | 1024 ×1536 | [SVG](ecology-stack.svg) |

[Shared tokens](../tokens.json) own colour and type choices. The [source builder](build-source.py) emits character cards, diagrams and specimens and applies the new palette to the existing cover layouts. The role/architecture content is native SVG, not generated lettering. The image layers retain their own provenance.

## Edit and render

Extract [kit 2.1](../downloads/sovereign-ooda-brand-kit-v2.1.zip), keeping the brand and assets directories together. Install bundled TTFs when editing in a desktop vector editor. The renderer embeds the fonts automatically and makes no remote font or image requests.

Requirements: Python 3 (standard library only), Node.js and the pinned Playwright package. From this directory:

```sh
npm install
npx playwright install chromium
python build-source.py
npm run render
python package-kit.py
```

On Windows, use the available Python 3 command or its absolute executable path. An existing browser can be selected with PLAYWRIGHT_CHROMIUM_EXECUTABLE. PLAYWRIGHT_MODULE can select an installed Playwright module. OODA_RENDER_REPORT optionally writes the actual font, text-boundary and type-slot check results.

The renderer checks font loading, canvas boundaries, card-column overflow and the exact complete cover copy. It exports the eleven layouts, lossless master, specimens and galleries. Review the resulting images visually: those checks do not establish composition quality or diagram correctness.

The canonical role PNGs remain under assets/roles; diagram PNGs remain under brand/assets. Profile-pack numbers are artwork identifiers only. Research and Engineering deliberately use role labels until numbers are chosen. Harry's regular setup and bold second line share one font family and size.

## Sources and review

The full-card source images for Baldwin, Blake and Harry are clipped to their photographic band; old generated headers/footers in those source files are not rendered. Baldwin's flattened quotation was removed with the image tool before live re-typesetting. Bateson's old central banner was removed and its woodland restored. The ship retains its red cheek, Ithaca and hearth smoke.

Keep candidate assets separate from source text and preserve Git history. Check image identity, each word, attribution, intended relationships and the whole collection at matching size before publication. Changes to a role image do not install or appoint its role.
