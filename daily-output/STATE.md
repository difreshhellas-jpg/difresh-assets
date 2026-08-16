# DIFRESH DAILY OUTPUT, RUN STATE

Last updated: 2026-08-17

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

`leonardo-generated/` did not exist in the repo as of 2026-08-17, so the pool is unchanged from
2026-08-16. Treat that folder as a slow-growing pool, never as a same-day dependency.

## CYCLE
1

## HOUSE PHILOSOPHY
Standing Reserve (written 2026-08-12, first run of CYCLE 1). Carried forward unchanged on
2026-08-13, 2026-08-15 and 2026-08-16, it has not run dry. Under the new pipeline the "plate" is an AI
generated frame descended from a real reference photograph rather than the photograph itself; the
movement's refusal of the cut maps directly onto the new Section 1 rule 1.
File: outputs/difresh_PHILOSOPHY_standing-reserve.md

## POOL DEFINITION

**Revised 2026-08-15, re-confirmed 2026-08-17.** The prior definition excluded all 33
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
Photographs that have appeared in a shipped asset or brief this cycle. 33 of 67 spent, 34 remain.

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

## GREEK SLOTS USED
- 2026-08-12: 02 and 05
- 2026-08-13: 03 and 06
- 2026-08-15: 01 and 04
- 2026-08-16: 02 and 06
- 2026-08-17: 03 and 05

## STORY ARCHETYPE USED
- 2026-08-12: plate in negative space
- 2026-08-13: oversized single word
- 2026-08-15: split screen
- 2026-08-16: one line low
- 2026-08-17: price or number as hero

## STORY HOOK USED
- 2026-08-12: use case moment
- 2026-08-13: price point
- 2026-08-15: product spotlight
- 2026-08-16: location or partner
- 2026-08-17: single provocative line

## STORY LANGUAGE USED
- 2026-08-12: EN
- 2026-08-13: GR
- 2026-08-15: EN
- 2026-08-16: GR
- 2026-08-17: EN

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

## GROUNDS USED
- 2026-08-12: #ECFEFF, #334155, #FAFAF9, #0F766E, #1E1B4B, #EA580C, #020617 (story)
- 2026-08-13: #064E3B, #ECFDF5, #475569, #F0F9FF, #1C1917, #EC4899, #0F0F23 (story)
- 2026-08-15: #0F172A, #EEF2FF, #1F2937, #F8FAFC, #F0FDFA, #000000, #FDF2F8 (story)
- 2026-08-16: #000000, #0C4A6E, #7F1D1D, #FAFAFA, #F0FDF4, #EFF6FF, #1E293B (story)
- 2026-08-17: #18181B, #E8F2F8, #9A3412, #1E3A8A, #E4E4E7, #14532D, #BE185D (story)

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

## NOTES FOR THE NEXT RUN
- Greek slot pairs used: (02,05), (03,06), (01,04), (02,06), (03,05). Unused examples: (01,02),
  (01,03), (01,05), (01,06), (02,03), (02,04), (03,04), (04,05), (04,06), (05,06).
- Story archetypes used: plate in negative space, oversized single word, split screen, one line low,
  price or number as hero. Remaining: big centred statement on flat colour, text only manifesto.
  After those two the list is exhausted once, restart it with a different product and treatment.
- Story hooks: the list of five is now exhausted once (use case moment, price point, product
  spotlight, location or partner, single provocative line). Start the list again from the top with
  a different product and a different treatment.
- Story language ran EN, GR, EN, GR, EN. Next story should be GR.
- NEVER GUESS A STUDIO FILE FROM ITS NAME. One Tauro frame hides in `STUDIO/`; it is listed under
  POOL DEFINITION. Build the contact sheet and Read it every run.
- What is left after 2026-08-17 (34 frames). Strong environmental and editorial frames still
  unspent: atom/editorial linen-flatlay, travertine, window-burlap; atom/studio blackbg,
  whitebg-01, whitebg-02; frozen-force burlap-window, whitebg-01; souvenir bedsheets, books-candle,
  dashboard-dusk-02, herbs-aloe-flatlay, kraftpaper, smoke-slate, tropical, whitebg-02. That is 16.
  The other 18 are the small-product-on-near-black-with-reflection STUDIO look. The environmental
  frames will run out in roughly three more runs, after which the batch has to lean on the STUDIO
  reflection frames, which read better on light grounds where the black plate becomes a mass.
- Several remaining frames are warm cream and beige scenes (atom travertine, window-burlap,
  linen-flatlay, frozen-force burlap-window, souvenir kraftpaper, bedsheets, books-candle). The
  Section 5 palette ban governs the DESIGN palette, not the photograph. Pair those frames with a
  cold or saturated ground so the frame does not drift into the banned family. 2026-08-17 slot 03
  is the pattern: a warm desert photograph on a saturated terracotta ground reads as deliberate.
- SKILLS. `canvas-design` and `luxury-brand-post-library` invoke normally with the Skill tool.
  `taste-skill`, `brutalist-skill` and `minimalist-skill` are present in `skills/` but are NOT
  registered with the Skill tool in this sandbox, so they cannot be invoked; read
  `skills/taste-skill/SKILL.md` directly and run its Section 14 Pre-Flight Check by hand. Note the
  substitution in the final report every time.
- ui-ux-pro-max `search.py` lives at
  `skills/ui-ux-pro-max-skill-main/src/ui-ux-pro-max/scripts/search.py`. `--domain color` returns
  shadcn token sets. Harvest across several queries; skip palettes whose accent is brass or ochre
  (`#A16207`, `#D97706`, `#CA8A04`). The inversion trick still works: a palette's Foreground can
  serve as the ground and its Background as the text. Fresh grounds harvested but NOT yet spent:
  #E4E4E7 is now spent, but #64748B, #94A3B8, #BAE6FD, #E9EEF5, #37414F, #27273B, #0369A1,
  #0284C7, #15803D, #C2410C, #3F3F46, #27272A are all still available.
- Grounds spent across the cycle, do not repeat: #ECFEFF #334155 #FAFAF9 #0F766E #1E1B4B #EA580C
  #020617 #064E3B #ECFDF5 #475569 #F0F9FF #1C1917 #EC4899 #0F0F23 #0F172A #EEF2FF #1F2937 #F8FAFC
  #F0FDFA #000000 #FDF2F8 #0C4A6E #7F1D1D #FAFAFA #F0FDF4 #EFF6FF #1E293B #18181B #E8F2F8 #9A3412
  #1E3A8A #E4E4E7 #14532D #BE185D.
- FONTS. This sandbox has no font tree beyond DejaVu. Fetch TTFs from
  `raw.githubusercontent.com/google/fonts/main/<lic>/<slug>/<File>.ttf` and cmap check with
  fonttools. Verified FULL Greek on 2026-08-17: Fira Code, Fira Sans, Inter, JetBrains Mono,
  Open Sans, Source Sans 3, EB Garamond, Geologica, Vollkorn, Noto Serif.
  Verified NO Greek on 2026-08-17, do not use for a Greek slot: Cormorant, Playfair Display,
  Montserrat, Poppins, Public Sans, Nunito Sans, Russo One, Chakra Petch, Lora, Exo 2, Unbounded,
  Onest, Roboto Serif, Gantari. Note Cormorant specifically: it LOOKS like it should have Greek
  and does not, it nearly cost the 2026-08-17 Greek slot a font.
  Variable-font axis order matters for PIL `set_variation_by_axes`: Geologica is
  [CRSV, SHRP, slnt, wght], Nunito Sans is [YTLC, opsz, wdth, wght], Open Sans is [wdth, wght].
- Heading families spent across the cycle, do not reuse: IBM Plex Sans, Fira Sans Condensed,
  Archivo, Jost, Manrope, Barlow Condensed, Space Grotesk, Syne, Anton, Alegreya, Epilogue, Sora,
  Roboto Condensed, Commissioner, Jura, Rubik, Figtree, Tektur, Lexend, Outfit, Bebas Neue,
  Space Mono, Noto Sans, Bodoni Moda, Plus Jakarta Sans, Raleway, Comfortaa, Source Serif 4,
  Playfair Display, Fira Code, EB Garamond, Public Sans, Geologica, Poppins, Russo One.
- Pillow, numpy and fonttools are NOT preinstalled. `pip install --timeout 120 Pillow numpy
  fonttools` works.
- `fonts.google.com` is blocked by the sandbox proxy. `raw.githubusercontent.com` and
  `api.github.com` are reachable.

## PUBLISHING ROUTE, IMPORTANT, READ BEFORE SECTION 9

**The `difreshhellas-jpg/posts` repo cannot be written from this sandbox.** Confirmed 2026-08-17
on both available paths:
- `git push` to it returns `remote: access denied by the git proxy: difreshhellas-jpg/posts is not
  in this session's authorized repository set, so the proxy will not inject a credential for it`,
  then HTTP 403. An anonymous `git clone` of it still works, so it is readable but not writable.
- The GitHub MCP server returns `Access denied: repository "difreshhellas-jpg/posts" is not
  configured for this session. Allowed repositories: difreshhellas-jpg/difresh-assets`.
This is session configuration, not a transient failure, so retrying it is wasted effort. Fixing it
means adding `difreshhellas-jpg/posts` to the session's authorized sources.

**Working route used on 2026-08-17.** `difreshhellas-jpg/difresh-assets` is PUBLIC
(`api.github.com/repos/...` reports `"private": false`), so its raw URLs are fetchable by Canva.
Push the finished PNGs to `daily-output/<date>/` in difresh-assets and use
`https://raw.githubusercontent.com/difreshhellas-jpg/difresh-assets/main/daily-output/<date>/<file>.png`
as the public URL for the Canva step. Verified live with HTTP 200 before importing.

**Canva.** `import-design-from-url` STILL fails with `invalid_file` (the outage that began
2026-08-16 is not over). The Section 9 fallback works and is now the expected path:
1. `upload-asset-from-url` with the raw URL.
2. `copy-design` an existing 1080x1350 design from folder FAHR5ym_TeY. Copy the FIRST design you
   make today, not yesterday's, for slots 2 to 6; it is already the right shape.
3. `read-design` with `open_transaction: true` to get the transaction id and the RECT locator id.
4. `edit-design` with `update_fill` + `crop_media` + `update_title` in ONE call. **The
   `crop_media` is not optional.** `update_fill` alone leaves the image scaled up about 2.1 percent
   with an imageBox of roughly (-14.17, -11.34, 1102.68 x 1378.35), which is a real crop and
   violates Section 1 rule 1. Passing `crop_media` with left 0, top 0, width 1080, height 1350
   restores an exact 1:1 placement. Verify the returned document shows
   `imageBox=(0,0 1080x1350 rotation=0)` before committing.
5. `edit-design` with `finalize: commit`, operations omitted.
6. `move-item-to-folder` to FAHR5ym_TeY, then `comment-on-design` with the CAPTION line.
No `resize-design` was needed, because the copied base is already 1080x1350.

## PUBLISH RECORD
- 2026-08-12: pushed to difreshhellas-jpg/posts@main under `2026-08-12/` (PNG + PDF).
  Canva designs, all moved to folder FAHR5ym_TeY, each carrying one CAPTION comment:
  01 DAHSD5hpuVk, 02 DAHSDxGJZFI, 03 DAHSD5MoXqY,
  04 DAHSD_UFbJ0, 05 DAHSD_eEKmw, 06 DAHSD6CSpkU.
- 2026-08-13: pushed to difreshhellas-jpg/posts@main under `2026-08-13/` (PNG + PDF).
  Canva designs, all moved to folder FAHR5ym_TeY, each carrying one CAPTION comment:
  01 DAHSJz6lZLs, 02 DAHSJwYAIv4, 03 DAHSJ10Bz5Q,
  04 DAHSJ5azjKM, 05 DAHSJ-n_5mU, 06 DAHSJ9sVuhY.
- 2026-08-15: brief only, per the then-current restructured pipeline. No PNG, no Canva design.
- 2026-08-16: brief only. The local automation that was supposed to finish the job produced exactly
  one Canva design, `DIFRESH 2026-08-16 01` (DAHScUDdPNA). The other five never appeared.
- 2026-08-17: FULL PRODUCTION restored in this routine. Seven PNGs rendered with Pillow and pushed
  to difreshhellas-jpg/difresh-assets@main under `daily-output/2026-08-17/` (the posts repo was not
  writable, see PUBLISHING ROUTE above). Six posts imported to Canva via the fallback path, all
  moved to folder FAHR5ym_TeY, each carrying one CAPTION comment:
  01 DAHSfTEwIjY, 02 DAHSffjJBhM, 03 DAHSfTCG3Ms,
  04 DAHSfdr08Ds, 05 DAHSfUqXsqc, 06 DAHSfedDEb4.
  The story `difresh_2026-08-17_story.png` was rendered and pushed but, per Section 9c, never sent
  to Canva. Contact sheets at `outputs/contact-sheet-2026-08-17-A.png` and `-B.png`.
