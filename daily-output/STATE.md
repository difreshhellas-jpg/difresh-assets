# DIFRESH DAILY OUTPUT, RUN STATE

Last updated: 2026-08-18 (full production run)

## SCHEDULING NOTE, READ FIRST

2026-08-17 fired TWICE for the same calendar date. The second firing correctly did NOT regenerate:
it checked the Canva folder, found `DIFRESH 2026-08-17 01` through `06` already filed and
captioned, and left them alone. Keep doing that. Before generating, check the posts repo for a
folder named for today's date AND the Canva folder for a design titled `DIFRESH <date> 01`. If a
complete batch is already there, verify it, close any real gap, update this file, and stop.
Producing a second batch hands the local publisher twelve posts to push in one day.

2026-08-18 checked both and found neither, so it produced a full fresh batch.

## PIPELINE

**Restructured again 2026-08-17, reverting the 2026-08-14 brief-only split.** This routine is the
whole production pipeline once more: it art directs, renders the final PNGs with Pillow, publishes
them, and imports the six posts into Canva itself. Nothing local needs to run for a post to reach
Canva. The only remaining local jobs are (a) `difresh-image-generation`, a fully decoupled daily
Leonardo AI job that drops raw renders into `leonardo-generated/<date>/` and reads nothing this
routine writes, and (b) the publisher that reads captioned designs out of the Canva folder and
posts to Instagram and Facebook.

The 2026-08-14 split cost several days of zero posts because it depended on a Windows Scheduled
Task and a live Leonardo browser session, both of which failed silently. Evidence in Canva: the
2026-08-16 local run produced exactly one design (`DIFRESH 2026-08-16 01`) out of six.

`leonardo-generated/` STILL did not exist in the repo as of 2026-08-18, three days after the
decoupled `difresh-image-generation` job was meant to start filling it. That job has produced zero
frames so far. It is fully decoupled, so this routine is not blocked by it and must never wait on
it, but somebody should check whether that local job is actually running. The pool is unchanged
from 2026-08-16.

## CYCLE
1

## HOUSE PHILOSOPHY
Standing Reserve (written 2026-08-12, first run of CYCLE 1). Carried forward unchanged on
2026-08-13, 2026-08-15, 2026-08-16, 2026-08-17 and 2026-08-18, it has not run dry. Under the new pipeline the "plate" is an AI
generated frame descended from a real reference photograph rather than the photograph itself; the
movement's refusal of the cut maps directly onto the new Section 1 rule 1.
File: outputs/difresh_PHILOSOPHY_standing-reserve.md

## POOL DEFINITION

**Revised 2026-08-15, re-confirmed 2026-08-18.** The prior definition excluded all 33
`gpt-image-2_` files as AI generated. That exclusion is withdrawn: STUDIO renders and Leonardo
renders are valid finished hero imagery, placed directly, not used as generation references.

Full pool = atom/editorial (7), atom/studio (5), frozen-force (9), souvenir (23), STUDIO (24),
tauro (1). Total 69. `leonardo-generated/` is still absent, contributing 0.

Permanently excluded, never selectable:
- `tauro/tauro-product.jpeg` (discontinued line, Section 1B)
- `STUDIO/gpt-image-2_professional_photo_of_just_make_it_for_16_9_dont_change_anythingjust_make_it_for-0 (3).jpg`
  **This is a TAURO product filed under `STUDIO/`, not under `tauro/`.** Opened and confirmed by
  eye on 2026-08-15. The filename gives no clue. Never select it.

Working pool is therefore **67**.

## CONSUMED
Photographs that have appeared in a shipped asset or brief this cycle. 41 of 67 spent, 26 remain.

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
- atom/studio/gpt-image-2_can_you_make_a_cinematic_shot_of_this_atomizer_floating_diagonal_alignment_while-0.jpg
- STUDIO/gpt-image-2_professional_photo_of_just_make_it_for_16_9_dont_change_anythingjust_make_it_for-0 (10).jpg
- STUDIO/gpt-image-2_professional_photo_of_just_make_it_for_16_9_dont_change_anything_photography-0 (2).jpg
- frozen-force/frozenforce-snow.jpg
- souvenir/souvenir-green-marble-bathroom.jpg
- souvenir/souvenir-green-teal-coral-cube.jpg
- atom/studio/gpt-image-2_can_you_make_a_cinematic_shot_of_this_atomizer_floating_diagonal_alignment_while-0 (2).jpg
- frozen-force/frozenforce-smoke.jpg
- STUDIO/gpt-image-2_professional_photo_of_just_make_it_for_16_9_dont_change_anything_photography-0 (1).jpg
- STUDIO/gpt-image-2_professional_photo_of_ΜΑΚΕ_ΤΗΕ_ΣΕΨΟΝΔ_ΙΜΑΓΕ_ΠΗΟΤΟΓΡΑΠ-0 (2).jpg
- STUDIO/gpt-image-2_professional_photo_of_COPY_THE_FIRSAT_IAMGE_JUST_CHANGE_THE_PRODUCT_COLOR_TO_THE-0 (15).jpg
- souvenir/souvenir-green-yellowbg.jpg
- souvenir/souvenir-green-rocks-water.jpg
- atom/editorial/atom-black-smoke.jpg
- souvenir/souvenir-green-wetsurface.jpg
- souvenir/souvenir-green-crackedearth.jpg
- frozen-force/frozenforce-tropical-fruit.jpg
- souvenir/souvenir-green-gym.jpg
- atom/editorial/atom-black-botanicals-flatlay.jpg

- souvenir/souvenir-green-bedsheets.jpg
- frozen-force/frozenforce-burlap-window.jpg
- atom/editorial/atom-black-window-burlap.jpg
- STUDIO/gpt-image-2_professional_photo_of_COPY_THE_FIRSAT_IAMGE_JUST_CHANGE_THE_PRODUCT_COLOR_TO_THE-0 (11).jpg
- STUDIO/gpt-image-2_professional_photo_of_COPY_THE_FIRSAT_IAMGE_JUST_CHANGE_THE_PRODUCT_COLOR_TO_THE-0 (13).jpg
- STUDIO/gpt-image-2_professional_photo_of_COPY_THE_FIRSAT_IAMGE_JUST_CHANGE_THE_PRODUCT_COLOR_TO_THE-0 (9).jpg
- souvenir/souvenir-green-books-candle.jpg
- frozen-force/frozenforce-whitebg-01.png

## GREEK SLOTS USED
- 2026-08-12: 02 and 05
- 2026-08-13: 03 and 06
- 2026-08-15: 01 and 04
- 2026-08-16: 02 and 06
- 2026-08-17: 03 and 05
- 2026-08-18: 01 and 06

## STORY ARCHETYPE USED
- 2026-08-12: plate in negative space
- 2026-08-13: oversized single word
- 2026-08-15: split screen
- 2026-08-16: one line low
- 2026-08-17: price or number as hero
- 2026-08-18: big centred statement on flat colour

## STORY HOOK USED
- 2026-08-12: use case moment
- 2026-08-13: price point
- 2026-08-15: product spotlight
- 2026-08-16: location or partner
- 2026-08-17: single provocative line
- 2026-08-18: product spotlight (list restarted, Frozen Force, different product and treatment
  from 2026-08-15's Souvenir spotlight)

## STORY LANGUAGE USED
- 2026-08-12: EN
- 2026-08-13: GR
- 2026-08-15: EN
- 2026-08-16: GR
- 2026-08-17: EN
- 2026-08-18: GR

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
- 2026-08-15: the atomiser costs one euro, the scent stays yours (Atom)
- 2026-08-15: the shade you pick is how you find it again (toothbrush paste combo)
- 2026-08-15: bought without a conversation (Durex)
- 2026-08-15: cold you can carry (Frozen Force)
- 2026-08-15: your name on the tube (Souvenir custom branded line)
- 2026-08-15: travel size is not a sample (vending category, no photograph)
- 2026-08-15 story: the green tube, on its own (Souvenir)
- 2026-08-16: the mist is the product, the bottle stays home (Atom)
- 2026-08-16: the shift ends, the night does not (Frozen Force)
- 2026-08-16: the hour you did not plan (Durex)
- 2026-08-16: brush and paste in one tube, one thing to pack (toothbrush paste combo)
- 2026-08-16: the machine is for the thing you forgot (vending category, no photograph)
- 2026-08-16: the second time you leave the house (Souvenir)
- 2026-08-16 story: on the crossing (Souvenir)
- 2026-08-17: discretion, the atomiser gives nothing away (Atom)
- 2026-08-17: the tube that lives where the water is (Souvenir toothbrush paste combo)
- 2026-08-17: micro kai antechei, small and it holds up (Souvenir, Greek)
- 2026-08-17: the drink was worth it, the aftermath is not (Frozen Force)
- 2026-08-17: the gym bag is not a bathroom cabinet (Souvenir, Greek)
- 2026-08-17: open when nothing else is (vending category, no photograph)
- 2026-08-17 story: not a sample price, the price (Atom, price as hero)
- 2026-08-18: beside the pillow, not in the bathroom (Souvenir combo tube, Greek)
- 2026-08-18: it fits where a bottle will not (Frozen Force)
- 2026-08-18: carried all season, refilled once (Atom)
- 2026-08-18: the range reads as a colour system (toothbrush paste combo tubes, triptych)
- 2026-08-18: the decision takes ten seconds (vending category, no photograph)
- 2026-08-18: the souvenir that gets used up (Souvenir custom branded line, Greek)
- 2026-08-18 story: it fits everywhere (Frozen Force, product spotlight)

## GROUNDS USED
- 2026-08-12: #ECFEFF, #334155, #FAFAF9, #0F766E, #1E1B4B, #EA580C, #020617 (story)
- 2026-08-13: #064E3B, #ECFDF5, #475569, #F0F9FF, #1C1917, #EC4899, #0F0F23 (story)
- 2026-08-15: #0F172A, #EEF2FF, #1F2937, #F8FAFC, #F0FDFA, #000000, #FDF2F8 (story)
- 2026-08-16: #000000, #0C4A6E, #7F1D1D, #FAFAFA, #F0FDF4, #EFF6FF, #1E293B (story)
- 2026-08-17: #18181B, #E8F2F8, #9A3412, #1E3A8A, #E4E4E7, #14532D, #BE185D (story)
- 2026-08-18: #BAE6FD, #C2410C, #164E63, #F2F3F4, #0B0B10, #3F3F46, #4338CA (story)

## HEADING FAMILIES USED
- 2026-08-12: IBM Plex Sans, Fira Sans Condensed, Archivo, Jost, Manrope,
  Barlow Condensed, Space Grotesk (story)
- 2026-08-13: Syne, Anton, Alegreya, Epilogue, Sora, Roboto Condensed,
  Commissioner (story). No overlap with 2026-08-12.
- 2026-08-15: Jura, Rubik, Figtree, Tektur, Lexend, Outfit, Bebas Neue (story).
  No overlap with either prior day.
- 2026-08-16: Space Mono, Noto Sans, Bodoni Moda, Plus Jakarta Sans, Raleway, Comfortaa,
  Source Serif 4 (story). No overlap with any prior day.
- 2026-08-17: Playfair Display, Fira Code, EB Garamond, Public Sans, Geologica, Poppins,
  Russo One (story). No overlap with any prior day.
- 2026-08-18: Sofia Sans, Antonio, Bricolage Grotesque, Wix Madefor Display, Gabarito, Vollkorn,
  Literata (story). No overlap with any prior day.

## NOTES FOR THE NEXT RUN

- Greek slot pairs used: (02,05), (03,06), (01,04), (02,06), (03,05), (01,06). Unused: (01,02),
  (01,03), (01,05), (02,03), (02,04), (03,04), (04,05), (04,06), (05,06).
- Story archetypes: all seven are now used once (plate in negative space, oversized single word,
  split screen, one line low, price or number as hero, big centred statement on flat colour, text
  only manifesto is the ONLY one still unused). Use text only manifesto next, then restart the
  list with a different product and treatment.
- Story hooks: list restarted 2026-08-18 with product spotlight on Frozen Force. Next: use case
  moment, location or partner, price point, single provocative line, each with a product it has
  not carried before.
- Story language ran EN, GR, EN, GR, EN, GR. Next story should be EN.
- NEVER GUESS A STUDIO FILE FROM ITS NAME. One Tauro frame hides in `STUDIO/`; it is listed under
  POOL DEFINITION. Build the contact sheet and Read it every run.
- **What is left after 2026-08-18: 26 frames.** The environmental and editorial frames are nearly
  gone. Still unspent: atom/editorial linen-flatlay, travertine; atom/studio blackbg, whitebg-01,
  whitebg-02; souvenir dashboard-dusk-02, herbs-aloe-flatlay, kraftpaper, smoke-slate, tropical,
  whitebg-02. That is 11. The other 15 are the small-product-on-near-black-with-reflection STUDIO
  look. Frozen Force is now FULLY SPENT for this cycle, both remaining frames went 2026-08-18.
  Expect the next two runs to lean heavily on the STUDIO reflection frames, which read best on
  light grounds where the black plate becomes a deliberate mass, and which work well ganged as a
  triptych (see 2026-08-18 slot 04).
- `atom/studio/atom-black-whitebg-01` is an atomiser on a BLACK ground and
  `atom-black-whitebg-02` is on a PURE WHITE ground, despite both filenames saying whitebg.
  `atom-black-blackbg` is black on black and is nearly unusable, the product barely reads.
  Confirmed by eye on the 2026-08-18 contact sheet.
- Warm cream and beige photographic scenes still in the pool (atom travertine, linen-flatlay,
  souvenir kraftpaper). The Section 5 palette ban governs the DESIGN palette, not the photograph.
  Pair those frames with a cold or saturated ground. 2026-08-18 slot 02 is the pattern: a warm
  burlap and window-light photograph on a burnt orange ground, and slot 03, the same warm burlap
  on deep teal. Both read as deliberate.
- SKILLS. `canvas-design` and `luxury-brand-post-library` invoke normally with the Skill tool.
  `taste-skill`, `brutalist-skill` and `minimalist-skill` are present in `skills/` but are still
  NOT registered with the Skill tool in this sandbox (confirmed again 2026-08-18, `Skill` returns
  `Unknown skill: taste-skill`). Read `skills/taste-skill/SKILL.md` directly and run its Section 14
  Pre-Flight Check by hand. Note the substitution in the final report every time.
- ui-ux-pro-max `search.py` lives at
  `skills/ui-ux-pro-max-skill-main/src/ui-ux-pro-max/scripts/search.py`. `--domain color` returns
  shadcn token sets; harvest across several queries and skip palettes whose accent is brass or
  ochre. The inversion trick still works: a palette's Foreground can serve as the ground and its
  Background as the text (2026-08-18 slot 03 used it). **`--domain typography` is now effectively
  exhausted**: every pairing it returns names families already spent (Playfair Display, Bebas Neue,
  Russo One, Rubik, Barlow Condensed, Outfit, Public Sans, Source Serif 4, Inter, Cormorant). Take
  the STRUCTURE it recommends (display or condensed grotesque heading plus neutral sans body, a
  5:1 headline to body ratio, mono only for meta) and apply it to unspent families. Say so in the
  report rather than pretending the pairing came back fresh.
- Fresh grounds harvested but NOT yet spent: #64748B, #94A3B8, #E9EEF5, #37414F, #27273B, #0369A1,
  #0284C7, #15803D, #E8ECF0, #E6E8EA, #312E81, #6B7280, #09090B, #0891B2, #22D3EE, #7C3AED.
  CAUTION on the light neutrals: white text fails 4.5:1 on #6B7280 (4.48) and #64748B (4.36), so
  those only work as grounds with DARK text.
  AVOID as grounds even though the palettes return them: #F5F5F0, #FFFBEB, #FFF7ED. They sit in
  the banned cream family from Section 5.
- Grounds spent across the cycle, do not repeat: #ECFEFF #334155 #FAFAF9 #0F766E #1E1B4B #EA580C
  #020617 #064E3B #ECFDF5 #475569 #F0F9FF #1C1917 #EC4899 #0F0F23 #0F172A #EEF2FF #1F2937 #F8FAFC
  #F0FDFA #000000 #FDF2F8 #0C4A6E #7F1D1D #FAFAFA #F0FDF4 #EFF6FF #1E293B #18181B #E8F2F8 #9A3412
  #1E3A8A #E4E4E7 #14532D #BE185D #BAE6FD #C2410C #164E63 #F2F3F4 #0B0B10 #3F3F46 #4338CA.
- FONTS. This sandbox has no font tree beyond DejaVu. Fetch TTFs from
  `raw.githubusercontent.com/google/fonts/main/<lic>/<slug>/<File>.ttf` and cmap check with
  fonttools. Note `apache/arimo`, `apache/opensans` and `apache/tinos` 404 at those paths.
  Verified FULL Greek (cumulative): Advent Pro, Alegreya Sans, Anonymous Pro, Cousine, Fira Code,
  Fira Sans, Inter, JetBrains Mono, Literata, Noto Serif, Open Sans, Piazzolla, Sofia Sans,
  Source Sans 3, Ubuntu, Vollkorn, EB Garamond, Geologica.
  Verified NO Greek, do not use for a Greek slot: Alumni Sans, Antonio, Archivo Narrow, Asap,
  Bricolage Grotesque, Chakra Petch, Cormorant, Encode Sans, Exo 2, Familjen Grotesk,
  Frank Ruhl Libre, Gabarito, Gantari, Golos Text, Heebo, Instrument Sans, Karla, Lora, Manuale,
  Montserrat, Mulish, Newsreader, Nunito, Nunito Sans, Onest, Oswald, Petrona, Playfair Display,
  Poppins, PT Sans (web subset), PT Serif (web subset), Public Sans, Red Hat Display, Roboto Serif,
  Russo One, Schibsted Grotesk, Signika, Space Grotesk, Unbounded, Wix Madefor Display.
  Note Cormorant and Bricolage Grotesque specifically: both LOOK like they should carry Greek and
  do not.
  Variable-font axis order matters for PIL. Do NOT hardcode it, read `font.get_variation_axes()`
  and match axes by tag, which is what `build.py` does now.
- **Serif caps run small.** Vollkorn at size 59 produced a 43px cap height, which lands squarely in
  the comfortable middle Section 6 bans. Fitting a long Greek headline to a narrow measure is what
  causes this. Fix by breaking into MORE, SHORTER lines rather than accepting a small size:
  4 lines at a 540px measure gave size 102 and a 74px cap. Always eyeball the rendered headline,
  the mechanical checks pass a too-small headline happily.
- Heading families spent across the cycle, do not reuse: IBM Plex Sans, Fira Sans Condensed,
  Archivo, Jost, Manrope, Barlow Condensed, Space Grotesk, Syne, Anton, Alegreya, Epilogue, Sora,
  Roboto Condensed, Commissioner, Jura, Rubik, Figtree, Tektur, Lexend, Outfit, Bebas Neue,
  Space Mono, Noto Sans, Bodoni Moda, Plus Jakarta Sans, Raleway, Comfortaa, Source Serif 4,
  Playfair Display, Fira Code, EB Garamond, Public Sans, Geologica, Poppins, Russo One,
  Sofia Sans, Antonio, Bricolage Grotesque, Wix Madefor Display, Gabarito, Vollkorn, Literata.
- Pillow, numpy and fonttools are NOT preinstalled. `pip install --timeout 120 Pillow numpy
  fonttools` works.
- `fonts.google.com` is blocked by the sandbox proxy. `raw.githubusercontent.com` and
  `api.github.com` are reachable.
- **Accent contrast is not the same as accent visibility.** A #7C3AED bar on a #4338CA ground is
  1.39:1 and simply disappears; it passed every mechanical check because an accent used as a
  graphic element has no contrast requirement. The 2026-08-18 story fixed it by making the accent
  a large offset plane set BEHIND the plate instead of a thin rule. If ground and accent are the
  same hue family, make the accent BIG or pick a different one.

## PUBLISHING ROUTE, IMPORTANT, READ BEFORE SECTION 9

**`difreshhellas-jpg/posts` is writable. Re-confirmed 2026-08-18 with a real push.** Section 9b's
route is live: push finished PNGs to `posts` under `<date>/` and serve them from
`https://raw.githubusercontent.com/difreshhellas-jpg/posts/main/<date>/<file>.png`. All seven
2026-08-18 URLs returned HTTP 200 at full byte length before any Canva call.

Sandbox quirk: the pre-cloned `posts` checkout can arrive on a DETACHED HEAD, so a bare
`git push -u origin main` fails with `src refspec main does not match any`. That is not an access
failure. Run `git checkout -B main origin/main` first. Also set `git config user.email` and
`user.name`, they are not preset.

*Fallback if `posts` ever goes unwritable again.* `difresh-assets` is PUBLIC, so push the PNGs to
`daily-output/<date>/` there and serve from
`https://raw.githubusercontent.com/difreshhellas-jpg/difresh-assets/main/daily-output/<date>/<file>.png`.

**Canva.** `import-design-from-url` STILL fails with `invalid_file`. The outage that began
2026-08-16 has now run three days. The Section 9 fallback works and is the expected path:
1. `upload-asset-from-url` with the raw URL. Confirm the returned `metadata` reads 1080x1350.
2. `copy-design` an existing 1080x1350 design from folder FAHR5ym_TeY. Copy the FIRST design you
   make today for slots 2 to 6; it is already the right shape and its element locator is identical
   across copies, so you can batch the reads and edits.
3. `read-design` with `open_transaction: true` for the transaction id and the RECT locator id.
   Filter to `fields: ["design_content"]` to keep the response small.
4. `edit-design` with `update_fill` + `crop_media` + `update_title` in ONE call. **The `crop_media`
   is not optional.** `update_fill` alone leaves the image scaled up about 2.1 percent, a real crop
   that violates Section 1 rule 1. Pass left 0, top 0, width 1080, height 1350 and confirm the
   returned document shows `imageBox=(0,0 1080x1350 rotation=0)` before committing.
5. `edit-design` with `finalize: commit`, operations omitted.
6. `move-item-to-folder` to FAHR5ym_TeY, then `comment-on-design` with the CAPTION line.
No `resize-design` needed, the copied base is already 1080x1350. Steps 1 to 6 batch cleanly five
slots at a time.

## PUBLISH RECORD
- 2026-08-12: pushed to difreshhellas-jpg/posts@main under `2026-08-12/` (PNG + PDF).
  Canva designs, all in folder FAHR5ym_TeY, each carrying one CAPTION comment:
  01 DAHSD5hpuVk, 02 DAHSDxGJZFI, 03 DAHSD5MoXqY,
  04 DAHSD_UFbJ0, 05 DAHSD_eEKmw, 06 DAHSD6CSpkU.
- 2026-08-13: pushed to difreshhellas-jpg/posts@main under `2026-08-13/` (PNG + PDF).
  01 DAHSJz6lZLs, 02 DAHSJwYAIv4, 03 DAHSJ10Bz5Q,
  04 DAHSJ5azjKM, 05 DAHSJ-n_5mU, 06 DAHSJ9sVuhY.
- 2026-08-15: brief only, per the then-current restructured pipeline. No PNG, no Canva design.
- 2026-08-16: brief only. The local automation that was supposed to finish the job produced exactly
  one Canva design, `DIFRESH 2026-08-16 01` (DAHScUDdPNA). The other five never appeared.
- 2026-08-17: FULL PRODUCTION restored in this routine. Seven PNGs pushed to difresh-assets under
  `daily-output/2026-08-17/` (posts was not writable at first firing), then to
  posts@main under `2026-08-17/` at the second firing. Six posts imported via the fallback path:
  01 DAHSfTEwIjY, 02 DAHSffjJBhM, 03 DAHSfTCG3Ms,
  04 DAHSfdr08Ds, 05 DAHSfUqXsqc, 06 DAHSfedDEb4.
  Story rendered and pushed but, per Section 9c, never sent to Canva.
- 2026-08-18: FULL PRODUCTION. Seven PNGs pushed to difreshhellas-jpg/posts@main under
  `2026-08-18/`, all seven raw URLs verified HTTP 200 at full byte length. Six posts reached Canva
  via the fallback path (import-design-from-url failed `invalid_file` again), all moved to folder
  FAHR5ym_TeY, each carrying exactly one CAPTION comment:
  01 DAHSn-uiIfY, 02 DAHSn4Mla70, 03 DAHSn3IqQCM,
  04 DAHSnw_Xu5s, 05 DAHSn846-_o, 06 DAHSn3rQKJU.
  Greek on slots 01 and 06, English on 02, 03, 04, 05. Story `difresh_2026-08-18_story.png`
  (Greek) rendered and pushed but, per Section 9c, never sent to Canva.
  Contact sheets at `outputs/contact-sheet-2026-08-18-A.png` and `-B.png`.
  Eight images consumed, taking CONSUMED to 41 of 67.
