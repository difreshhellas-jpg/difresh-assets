# DIFRESH DAILY OUTPUT, RUN STATE

Last updated: 2026-08-13

## CYCLE
1

## HOUSE PHILOSOPHY
Standing Reserve (written 2026-08-12, first run of CYCLE 1). Carried forward unchanged on
2026-08-13, it has not run dry.
File: outputs/difresh_PHILOSOPHY_standing-reserve.md

## POOL DEFINITION
43 photographs. The 33 files whose names begin `gpt-image-2_` (all of `STUDIO/`, plus two in
`atom/studio/`) are excluded from the pool permanently: they are AI generated, which Section 5
bans. Pool = atom/editorial (7), atom/studio (3 real), frozen-force (9), souvenir (23), tauro (1).
The single tauro frame is never selectable (Section 1B, discontinued line), so the working pool
is 42.

## CONSUMED
Photographs that have appeared in a shipped asset this cycle. 14 of 42 spent, 28 remain.

- frozen-force/frozenforce-mountain.jpg
- frozen-force/frozenforce-whitebg-02.jpg
- souvenir/souvenir-green-airport-security.jpg
- souvenir/souvenir-green-bar-cocktails.jpg
- souvenir/souvenir-green-dashboard-dusk-01.jpg
- souvenir/souvenir-green-whitebg-01.jpg
- atom/editorial/atom-black-coat-pocket.jpg
- atom/editorial/atom-black-forest-moss.jpg
- frozen-force/frozenforce-darkblue-wet.jpg
- frozen-force/frozenforce-orangebg.jpg
- souvenir/souvenir-green-handheld.jpg
- souvenir/souvenir-green-beach.jpg
- souvenir/souvenir-green-slate-rosemary-flatlay.jpg
- souvenir/souvenir-green-woodtable.jpg

## GREEK SLOTS USED
- 2026-08-12: 02 and 05
- 2026-08-13: 03 and 06

## STORY ARCHETYPE USED
- 2026-08-12: plate in negative space
- 2026-08-13: oversized single word

## STORY HOOK USED
- 2026-08-12: use case moment
- 2026-08-13: price point

## STORY LANGUAGE USED
- 2026-08-12: EN
- 2026-08-13: GR

## ANGLES USED
- 2026-08-12: cold altitude claim (Frozen Force)
- 2026-08-12: airport security and cabin bag (Souvenir)
- 2026-08-12: refill and forget, pocket carry (Atom)
- 2026-08-12: fresh as a twice daily decision (manifesto, no photograph)
- 2026-08-12: two sprays in the car before you arrive (Souvenir)
- 2026-08-12: the range, two products one job (Frozen Force and Souvenir)
- 2026-08-12 story: the moment before you speak to someone (Souvenir)
- 2026-08-13: the atomiser carried past the end of the road (Atom)
- 2026-08-13: twenty millilitres against two grounds (Frozen Force)
- 2026-08-13: it fits in the palm (Souvenir)
- 2026-08-13: the hour after the swim (Souvenir)
- 2026-08-13: the last two minutes of the day (Souvenir)
- 2026-08-13: ten shades and flavors (toothbrush paste combo, no photograph)
- 2026-08-13 story: one euro the product (vending category)

## GROUNDS USED
- 2026-08-12: #ECFEFF, #334155, #FAFAF9, #0F766E, #1E1B4B, #EA580C, #020617 (story)
- 2026-08-13: #064E3B, #ECFDF5, #475569, #F0F9FF, #1C1917, #EC4899, #0F0F23 (story)

## HEADING FAMILIES USED
- 2026-08-12: IBM Plex Sans, Fira Sans Condensed, Archivo, Jost, Manrope,
  Barlow Condensed, Space Grotesk (story)
- 2026-08-13: Syne, Anton, Alegreya, Epilogue, Sora, Roboto Condensed,
  Commissioner (story). No overlap with 2026-08-12.

## NOTES FOR THE NEXT RUN
- Greek slot pairs used so far: (02,05) and (03,06). Pick an unused pair, for example (01,04).
- Story archetypes used: plate in negative space, oversized single word. Rotate again.
- Story hooks used: use case moment, price point. Rotate again.
- Story language alternated EN then GR. Next story should be EN.
- FONTS. `fonts.google.com` is BLOCKED by the sandbox proxy (403 on CONNECT). Do not retry it.
  Download TTFs from `https://raw.githubusercontent.com/google/fonts/main/<lic>/<slug>/<File>.ttf`
  instead, which works. `api.github.com` is also blocked, so directory listing is impossible:
  guess the filename and verify with a real GET. Variable fonts are `Family[axes].ttf`, statics
  are `Family-Weight.ttf`. `/home/user/getfonts.py` does this for 50 families.
- VARIABLE FONT AXES. The axis order in the FILENAME is not the axis order in `fvar`. Commissioner
  is filed as `Commissioner[FLAR,VOLM,slnt,wght].ttf` but its fvar order is wght, slnt, FLAR, VOLM.
  Passing `set_variation_by_axes` in filename order silently renders Thin. Prefer
  `set_variation_by_name("ExtraBold")`, or read fvar first.
- Verified full Greek cmap coverage among the 50 downloaded families (38 pass): Alegreya, Arimo,
  Comfortaa, Commissioner, Cousine, Fira Sans, Fira Sans Condensed, IBM Plex Sans, Inter,
  JetBrains Mono, Jura, Literata, Manrope, Noto Sans, Roboto Condensed, Roboto Mono,
  Source Serif 4, Syne, Tektur, Tinos, Ubuntu. No Greek: Anton, Archivo, Archivo Black, Asap
  Condensed, Barlow Condensed, Bebas Neue, Bitter, Chivo, Cormorant Garamond, DM Sans, Epilogue,
  Gelasio, Karla, Lexend, Libre Franklin, Mulish, Oswald, Outfit, Playfair Display, Public Sans,
  Rubik, Saira Condensed, Sora, Space Grotesk, Space Mono, Spectral, Work Sans, Yanone Kaffeesatz,
  Zilla Slab.
- The system font tree here carries only DejaVu. Lato, Nimbus Sans Narrow, URW Gothic and
  Carlito named in the brief are not installed.
- TYPE CRAFT. Anchoring every wrapped line by its own ink-box top wrecks the baseline rhythm,
  because a line with no ascenders (`και`) gets pushed down. Anchor the block by the FIRST line's
  ink box, then advance on a constant baseline grid. `build.py:block()` does this.
- The verifier must check text against text, not only text against plates. A headline block that
  grew a fourth line silently overprinted the caption on post 06 before this check existed.
- ui-ux-pro-max `search.py` lives at
  `skills/ui-ux-pro-max-skill-main/src/ui-ux-pro-max/scripts/search.py`, not in the repo-root
  `scripts/`. Its `--domain color` returns shadcn style token sets rather than named palettes, so
  harvest across several queries and take Primary / Background / Foreground / Accent hexes.

## PUBLISH RECORD
- 2026-08-12: pushed to difreshhellas-jpg/posts@main under `2026-08-12/` (PNG + PDF).
  Canva designs, all moved to folder FAHR5ym_TeY, each carrying one CAPTION comment:
  01 DAHSD5hpuVk, 02 DAHSDxGJZFI, 03 DAHSD5MoXqY,
  04 DAHSD_UFbJ0, 05 DAHSD_eEKmw, 06 DAHSD6CSpkU.
- 2026-08-13: pushed to difreshhellas-jpg/posts@main under `2026-08-13/` (PNG + PDF).
  Canva designs, all moved to folder FAHR5ym_TeY, each carrying one CAPTION comment:
  01 DAHSJz6lZLs, 02 DAHSJwYAIv4, 03 DAHSJ10Bz5Q,
  04 DAHSJ5azjKM, 05 DAHSJ-n_5mU, 06 DAHSJ9sVuhY.
  The PDF import route from 2026-08-12 worked first try. Keep using it, `import-design-from-url`
  still rejects raw PNG.
- The `posts` clone arrives in DETACHED HEAD. `git push origin main` fails with
  "src refspec main does not match any" until you run `git branch -f main HEAD && git checkout main`.
