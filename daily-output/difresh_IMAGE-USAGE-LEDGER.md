# DIFRESH IMAGE USAGE LEDGER

Cycle 1. Updated 2026-08-15.

The rule: no reference image is reused until every eligible image in the pool has been used once.

**Pool revised 2026-08-15.** The prior definition excluded all 33 `gpt-image-2_*` files as AI
generated. That exclusion is withdrawn per the 2026-08-14 brief revision, which confirms the STUDIO
renders are valid reference material for the local AI generation step.

Of the 69 files in the repo, two are permanently excluded:

- `tauro/tauro-product.jpeg`, discontinued line
- `STUDIO/gpt-image-2_professional_photo_of_just_make_it_for_16_9_dont_change_anythingjust_make_it_for-0 (3).jpg`,
  which is a **Tauro product filed under `STUDIO/`**. Confirmed by eye on 2026-08-15. The filename
  gives no clue.

**Working pool: 67. Spent: 20. Remaining in cycle 1: 47.**

## Spent

| # | Reference image | Run | Asset |
|---|---|---|---|
| 1 | frozen-force/frozenforce-mountain.jpg | 2026-08-12 | 01 |
| 2 | souvenir/souvenir-green-airport-security.jpg | 2026-08-12 | 02 |
| 3 | atom/editorial/atom-black-coat-pocket.jpg | 2026-08-12 | 03 |
| 4 | souvenir/souvenir-green-dashboard-dusk-01.jpg | 2026-08-12 | 05 |
| 5 | frozen-force/frozenforce-whitebg-02.jpg | 2026-08-12 | 06 |
| 6 | souvenir/souvenir-green-whitebg-01.jpg | 2026-08-12 | 06 |
| 7 | souvenir/souvenir-green-bar-cocktails.jpg | 2026-08-12 | story |
| 8 | atom/editorial/atom-black-forest-moss.jpg | 2026-08-13 | 01 |
| 9 | frozen-force/frozenforce-darkblue-wet.jpg | 2026-08-13 | 02 left |
| 10 | frozen-force/frozenforce-orangebg.jpg | 2026-08-13 | 02 right |
| 11 | souvenir/souvenir-green-handheld.jpg | 2026-08-13 | 03 |
| 12 | souvenir/souvenir-green-beach.jpg | 2026-08-13 | 04 |
| 13 | souvenir/souvenir-green-slate-rosemary-flatlay.jpg | 2026-08-13 | 05 |
| 14 | souvenir/souvenir-green-woodtable.jpg | 2026-08-13 | story |
| 15 | atom/studio/gpt-image-2_can_you_make_a_cinematic_shot_of_this_atomizer_floating_diagonal_alignment_while-0.jpg | 2026-08-15 | 01 |
| 16 | STUDIO/gpt-image-2_professional_photo_of_just_make_it_for_16_9_dont_change_anythingjust_make_it_for-0 (10).jpg | 2026-08-15 | 02 |
| 17 | STUDIO/gpt-image-2_professional_photo_of_just_make_it_for_16_9_dont_change_anything_photography-0 (2).jpg | 2026-08-15 | 03 |
| 18 | frozen-force/frozenforce-snow.jpg | 2026-08-15 | 04 |
| 19 | souvenir/souvenir-green-marble-bathroom.jpg | 2026-08-15 | 05 |
| 20 | souvenir/souvenir-green-teal-coral-cube.jpg | 2026-08-15 | story |

## Remaining in cycle 1 (47)

**atom/editorial (5):** atom-black-botanicals-flatlay, atom-black-linen-flatlay, atom-black-smoke,
atom-black-travertine, atom-black-window-burlap.

**atom/studio (4):** atom-black-blackbg, atom-black-whitebg-01, atom-black-whitebg-02,
`gpt-image-2_can_you_make_a_cinematic_shot_of_this_atomizer_floating_diagonal_alignment_while-0 (2).jpg`.

**frozen-force (4):** frozenforce-burlap-window, frozenforce-smoke, frozenforce-tropical-fruit,
frozenforce-whitebg-01.

**souvenir (13):** souvenir-green-bedsheets, souvenir-green-books-candle,
souvenir-green-crackedearth, souvenir-green-dashboard-dusk-02, souvenir-green-gym,
souvenir-green-herbs-aloe-flatlay, souvenir-green-kraftpaper, souvenir-green-rocks-water,
souvenir-green-smoke-slate, souvenir-green-tropical, souvenir-green-wetsurface,
souvenir-green-whitebg-02, souvenir-green-yellowbg.

**STUDIO (21):** all remaining `gpt-image-2_*` frames except the two spent on 2026-08-15 and the
one permanently excluded Tauro frame. Contents by eye, from the 2026-08-15 contact sheet:
one Durex Sensitive carton on red, one Durex Classic carton (spent), one Frozen Force bottle on
black, and eighteen renders of the toothbrush paste combo tube in individual shades, most on a
near black ground with a mirror reflection.

## Standing note on the pool

Verdicts belong to an image on a date, never carried over.

**Never guess a file from its name.** Every STUDIO filename is the same truncated prompt fragment,
so the names carry no information at all. The 2026-08-15 run nearly shipped a Tauro product because
of this. Two older traps still hold: `frozenforce-whitebg-01` and `souvenir-green-whitebg-02` are
both shot on a near black ground, not white.

Roughly half the remaining pool is a small product lit on a near black ground with a mirror
reflection. Those are weak references for the AI generation step, because the product occupies too
little of the frame for the generator to lock onto its details. Prefer the environmental and
editorial frames when there is a choice.

Several of the strongest remaining environmental frames are lit warm, on cream linen, kraft paper
or travertine. Section 5 bans that palette in the generated imagery as well as in the graphic
layer, so the image prompt has to actively regrade them cold. Slot 05 on 2026-08-15 is the worked
example: the reference is a warm bathroom with a brass tap, and the prompt specifies cool north
light, grey white marble and brushed steel instead.
