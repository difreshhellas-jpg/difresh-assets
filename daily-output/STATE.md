# DIFRESH DAILY OUTPUT, RUN STATE

Last updated: 2026-08-19 (full production run)

## SCHEDULING NOTE, READ FIRST

2026-08-17 fired TWICE for the same calendar date. The second firing correctly did NOT regenerate:
it checked the Canva folder, found `DIFRESH 2026-08-17 01` through `06` already filed and
captioned, and left them alone. Keep doing that. Before generating, check the posts repo for a
folder named for today's date AND the Canva folder for a design titled `DIFRESH <date> 01`. If a
complete batch is already there, verify it, close any real gap, update this file, and stop.
Producing a second batch hands the local publisher twelve posts to push in one day.

2026-08-18, 2026-08-19 and 2026-08-20 all checked and found neither, so each produced a full fresh
batch.

## PIPELINE

**Restructured again 2026-08-17, reverting the 2026-08-14 brief-only split.** This routine is the
whole production pipeline once more: it art directs, renders the final PNGs with Pillow, publishes
them, and imports the six posts into Canva itself. Nothing local needs to run for a post to reach
Canva. The only remaining local jobs are (a) `difresh-image-generation`, a fully decoupled daily
Leonardo AI job that drops raw renders into `leonardo-generated/<date>/` and reads nothing this
routine writes, and (b) the publisher that reads captioned designs out of the Canva folder and
posts to Instagram and Facebook.

**`leonardo-generated/` IS ALIVE AND ON SCHEDULE.** `2026-08-18/` and `2026-08-19/` each landed five
frames (atom, durex, frozen-force, souvenir, toothbrush-combo). They are strong, genuinely
cinematic, and clearly the best material in the pool. 2026-08-19 spent three of the 08-18 batch;
2026-08-20 spent four of the 08-19 batch. Two consecutive on-time days now, so the local job looks
healthy. Expect roughly five more per day; if a day is missing, that job stopped again, but this
routine is never blocked by it. NOTE: the five frames repeat the same five product setups each day,
so an `08-20/atom.jpg` will be a different take on the same idea as `08-19/atom.jpg`, not a new
product. Judge each from the contact sheet as always.

## CYCLE
1

## HOUSE PHILOSOPHY
Standing Reserve (written 2026-08-12, first run of CYCLE 1). Carried forward unchanged on
2026-08-13, 2026-08-15, 2026-08-16, 2026-08-17, 2026-08-18, 2026-08-19 and 2026-08-20; it has not
run dry. Under the
new pipeline the "plate" is an AI generated frame descended from a real reference photograph rather
than the photograph itself; the movement's refusal of the cut maps directly onto Section 1 rule 1.
File: daily-output/difresh_PHILOSOPHY_standing-reserve.md (the path was misrecorded as
outputs/ until 2026-08-20; it has always lived under daily-output/).

## POOL DEFINITION

**Revised 2026-08-15, re-confirmed 2026-08-20.** The prior definition excluded all 33
`gpt-image-2_` files as AI generated. That exclusion is withdrawn: STUDIO renders and Leonardo
renders are valid finished hero imagery, placed directly, not used as generation references.

Full pool = atom/editorial (7), atom/studio (5), frozen-force (9), souvenir (23), STUDIO (24),
tauro (1), leonardo-generated (10, five per day for 2026-08-18 and 2026-08-19). Total 79.
The pool GROWS by about five a day, so recount it at the start of every run rather than trusting
this number.

Permanently excluded, never selectable:
- `tauro/tauro-product.jpeg` (discontinued line, Section 1B)
- `STUDIO/gpt-image-2_professional_photo_of_just_make_it_for_16_9_dont_change_anythingjust_make_it_for-0 (3).jpg`
  **This is a TAURO product filed under `STUDIO/`, not under `tauro/`.** Opened and confirmed by
  eye on 2026-08-15. The filename gives no clue. Never select it.

Working pool is therefore **77** as of 2026-08-20.

## CONSUMED
Photographs that have appeared in a shipped asset or brief this cycle. 52 of 77 spent, 25 remain.

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

- leonardo-generated/2026-08-18/frozen-force.jpg
- leonardo-generated/2026-08-18/toothbrush-combo.jpg
- leonardo-generated/2026-08-18/atom.jpg
- souvenir/souvenir-green-kraftpaper.jpg
- souvenir/souvenir-green-tropical.jpg

- leonardo-generated/2026-08-19/durex.jpg
- leonardo-generated/2026-08-19/toothbrush-combo.jpg
- leonardo-generated/2026-08-19/atom.jpg
- leonardo-generated/2026-08-19/frozen-force.jpg
- souvenir/souvenir-green-dashboard-dusk-02.jpg
- atom/editorial/atom-black-travertine.jpg

## GREEK SLOTS USED
- 2026-08-12: 02 and 05
- 2026-08-13: 03 and 06
- 2026-08-15: 01 and 04
- 2026-08-16: 02 and 06
- 2026-08-17: 03 and 05
- 2026-08-18: 01 and 06
- 2026-08-19: 02 and 04
- 2026-08-20: 01 and 05

## STORY ARCHETYPE USED
- 2026-08-12: plate in negative space
- 2026-08-13: oversized single word
- 2026-08-15: split screen
- 2026-08-16: one line low
- 2026-08-17: price or number as hero
- 2026-08-18: big centred statement on flat colour
- 2026-08-19: text only manifesto
- 2026-08-20: plate in negative space (list restarted, Atom on travertine, deep slate void)

## STORY HOOK USED
- 2026-08-12: use case moment
- 2026-08-13: price point
- 2026-08-15: product spotlight
- 2026-08-16: location or partner
- 2026-08-17: single provocative line
- 2026-08-18: product spotlight (list restarted, Frozen Force)
- 2026-08-19: use case moment (vending category, no product named, dawn ferry deck)
- 2026-08-20: location or partner (Athens to the island, no partner named, Atom)

## STORY LANGUAGE USED
- 2026-08-12: EN
- 2026-08-13: GR
- 2026-08-15: EN
- 2026-08-16: GR
- 2026-08-17: EN
- 2026-08-18: GR
- 2026-08-19: EN
- 2026-08-20: GR

## ANGLES USED
(2026-08-12 through 2026-08-18 unchanged, see git history for the full earlier list)
- 2026-08-12: cold altitude claim (Frozen Force); airport security and cabin bag (Souvenir);
  refill and forget, pocket carry (Atom); fresh as a twice daily decision (manifesto, no
  photograph); two sprays in the car before you arrive (Souvenir); the range, two products one job;
  story: the moment before you speak to someone (Souvenir)
- 2026-08-13: the atomiser carried past the end of the road (Atom); twenty millilitres against two
  grounds (Frozen Force); it fits in the palm (Souvenir); the hour after the swim (Souvenir); the
  last two minutes of the day (Souvenir); ten shades and flavors (combo, no photograph);
  story: one euro the product (vending category)
- 2026-08-15: the atomiser costs one euro, the scent stays yours (Atom); the shade you pick is how
  you find it again (combo); bought without a conversation (Durex); cold you can carry (Frozen
  Force); your name on the tube (Souvenir custom branded); travel size is not a sample (vending,
  no photograph); story: the green tube, on its own (Souvenir)
- 2026-08-16: the mist is the product, the bottle stays home (Atom); the shift ends, the night does
  not (Frozen Force); the hour you did not plan (Durex); brush and paste in one tube, one thing to
  pack (combo); the machine is for the thing you forgot (vending, no photograph); the second time
  you leave the house (Souvenir); story: on the crossing (Souvenir)
- 2026-08-17: discretion, the atomiser gives nothing away (Atom); the tube that lives where the
  water is (Souvenir combo); micro kai antechei, small and it holds up (Souvenir, Greek); the drink
  was worth it, the aftermath is not (Frozen Force); the gym bag is not a bathroom cabinet
  (Souvenir, Greek); open when nothing else is (vending, no photograph); story: not a sample price,
  the price (Atom)
- 2026-08-18: beside the pillow, not in the bathroom (combo, Greek); it fits where a bottle will not
  (Frozen Force); carried all season, refilled once (Atom); the range reads as a colour system
  (combo tubes, triptych); the decision takes ten seconds (vending, no photograph); the souvenir
  that gets used up (Souvenir custom branded, Greek); story: it fits everywhere (Frozen Force)
- 2026-08-19: cold enough to notice, the bottle you carry on not the shelf you leave behind
  (Frozen Force)
- 2026-08-19: nobody asks for a toothbrush, the guest who will not ask (toothbrush paste combo, Greek)
- 2026-08-19: used, not saved, against hoarding a travel size thing (Atom)
- 2026-08-19: you do not buy it for yourself (Souvenir custom branded line, Greek)
- 2026-08-19: the heat outlasts the shower (Souvenir, tropical)
- 2026-08-19: five things, five prices, the whole line as a priced collection (type only, no photograph)
- 2026-08-19 story: six in the morning on the deck (use case moment, no product named)
- 2026-08-20: in the bag, not in the drawer (Durex, Greek)
- 2026-08-20: brush somewhere that isn't home (toothbrush paste combo)
- 2026-08-20: no mirror required, built for the part of the trip without one (Atom)
- 2026-08-20: most souvenirs sit on a shelf, this one starts working the same evening
  (Souvenir custom branded line)
- 2026-08-20: two lines of overheard speech, "did you forget anything" and "no, I got it
  downstairs" (type only, no photograph, Greek)
- 2026-08-20: 20ml is not a trial size of something bigger, there is no bigger (Frozen Force)
- 2026-08-20 story: from Athens to the island (location, no partner named, Atom)

## GROUNDS USED
- 2026-08-12: #ECFEFF, #334155, #FAFAF9, #0F766E, #1E1B4B, #EA580C, #020617 (story)
- 2026-08-13: #064E3B, #ECFDF5, #475569, #F0F9FF, #1C1917, #EC4899, #0F0F23 (story)
- 2026-08-15: #0F172A, #EEF2FF, #1F2937, #F8FAFC, #F0FDFA, #000000, #FDF2F8 (story)
- 2026-08-16: #000000, #0C4A6E, #7F1D1D, #FAFAFA, #F0FDF4, #EFF6FF, #1E293B (story)
- 2026-08-17: #18181B, #E8F2F8, #9A3412, #1E3A8A, #E4E4E7, #14532D, #BE185D (story)
- 2026-08-18: #BAE6FD, #C2410C, #164E63, #F2F3F4, #0B0B10, #3F3F46, #4338CA (story)
- 2026-08-19: #E2E8F0, #312E81, #37414F, #831843, #09090B, #F0F8F6, #FAF5FF (story)
- 2026-08-20: #F97316, #171939, #E9EEF5, #94A3B8, #22D3EE, #E1F2ED, #272F42 (story)

## HEADING FAMILIES USED
- 2026-08-12: IBM Plex Sans, Fira Sans Condensed, Archivo, Jost, Manrope, Barlow Condensed, Space Grotesk
- 2026-08-13: Syne, Anton, Alegreya, Epilogue, Sora, Roboto Condensed, Commissioner
- 2026-08-15: Jura, Rubik, Figtree, Tektur, Lexend, Outfit, Bebas Neue
- 2026-08-16: Space Mono, Noto Sans, Bodoni Moda, Plus Jakarta Sans, Raleway, Comfortaa, Source Serif 4
- 2026-08-17: Playfair Display, Fira Code, EB Garamond, Public Sans, Geologica, Poppins, Russo One
- 2026-08-18: Sofia Sans, Antonio, Bricolage Grotesque, Wix Madefor Display, Gabarito, Vollkorn, Literata
- 2026-08-19: Questrial, Piazzolla, Archivo Black, Advent Pro, DM Serif Display, League Spartan,
  Marcellus (story). No overlap with any prior day.
  Bodies: Chivo, Source Sans 3, Red Hat Text, Ubuntu, Albert Sans, Urbanist, Karla.
- 2026-08-20: GFS Didot, Big Shoulders Display, Newsreader, Anybody, Roboto Slab, Zilla Slab,
  GFS Neohellenic (story). No overlap with any prior day.
  Bodies: Lato, Hanken Grotesk, Familjen Grotesk, Asap, Cousine, Mulish, Noto Sans Display.

## NOTES FOR THE NEXT RUN

- Greek slot pairs used: (02,05), (03,06), (01,04), (02,06), (03,05), (01,06), (02,04), (01,05).
  Unused: (01,02), (01,03), (02,03), (03,04), (04,05), (04,06), (05,06).
- Story archetypes: the list restarted 2026-08-20 with plate in negative space (Atom on travertine,
  deep slate). Next unused in the restarted list: one line low, big centred statement on flat
  colour, split screen, oversized single word, price or number as hero, text only manifesto.
- Story hooks: 2026-08-20 took location or partner. Next should be price point, then single
  provocative line, then product spotlight.
- Story language ran EN, GR, EN, GR, EN, GR, EN, GR. **Next story should be EN.**
- **The type only post must stop being a vending manifesto.** 2026-08-15, 16, 17 and 18 all made the
  no-photograph slot a vending category manifesto; that is a template, not a decision. 2026-08-19
  broke it by making the type only post a priced list of the whole line (Louis Vuitton collection
  voice). 2026-08-20 broke it again with two lines of overheard DIALOGUE split across a cyan field
  and a white plane, a scene rather than a statement. Keep finding a genuinely different KIND of
  type only post. Kinds now spent: manifesto, priced list, dialogue. Untried: a single question with
  no answer, a date and time, a set of instructions, one word repeated.
- **What is left after 2026-08-20: 25 frames**, plus whatever the Leonardo job has dropped since.
  Still unspent and genuinely usable: atom/editorial linen-flatlay; atom/studio whitebg-01,
  whitebg-02; souvenir herbs-aloe-flatlay, smoke-slate, whitebg-02; leonardo-generated/2026-08-18
  durex and souvenir; leonardo-generated/2026-08-19 souvenir. That is 9. Add atom/studio blackbg
  (black on black, nearly unusable) and the 15 small-product-on-near-black-with-reflection STUDIO
  frames to reach 25.
  **The strong material is thinning.** Only two environmental/editorial real photographs remain
  (linen-flatlay, herbs-aloe-flatlay) and both are warm cream/sand grounds, which is awkward next
  to the SECTION 5 cream ban and needs a cold ground to work against. From roughly 2026-08-22 the
  batch will lean almost entirely on `leonardo-generated/`, so a missed day from that local job
  starts to bite. If it stalls for two days running, expect to ship STUDIO near-black frames and
  plan compositions that suit a small product in a large void.
  NOTE: `leonardo-generated/2026-08-18/souvenir.jpg` is a near duplicate of
  `souvenir/souvenir-green-smoke-slate.jpg`, and `leonardo-generated/2026-08-19/souvenir.jpg` (green
  tube on a pebble in pale mist) is close to neither. Do not ship the first two in one batch.
- `atom/studio/atom-black-whitebg-01` is an atomiser on a BLACK ground and `atom-black-whitebg-02`
  is on a PURE WHITE ground, despite both filenames saying whitebg. `atom-black-blackbg` is black
  on black and is nearly unusable. Confirmed by eye again on the 2026-08-19 contact sheet.
- One STUDIO frame, `..._just_make_it_for_16_9_dont_change_anything_photography-0.jpg`, is a
  FROZEN FORCE bottle, not a combo tube. It is still unspent and is the only Frozen Force frame
  left in the pool.
- SKILLS. `canvas-design` and `luxury-brand-post-library` invoke normally with the Skill tool.
  `taste-skill`, `brutalist-skill` and `minimalist-skill` are present in `skills/` but are still
  NOT registered with the Skill tool in this sandbox (confirmed again 2026-08-20, `Skill` returns
  `Unknown skill: taste-skill`). Read `skills/taste-skill/SKILL.md` directly and run its Section 14
  Pre-Flight Check by hand. Note the substitution in the final report every time.
- ui-ux-pro-max `search.py` lives at
  `skills/ui-ux-pro-max-skill-main/src/ui-ux-pro-max/scripts/search.py`. Many natural-language
  queries return 0 results; it matches product-category words, so query "fitness training energy",
  "travel booking summer", "meditation mindfulness calm", "developer tools terminal",
  "luxury fashion boutique" rather than mood words like "tropical heat saturated island".
  **`--domain typography` is exhausted**: every pairing it returns names families already spent
  (Playfair Display, Inter, Source Serif 4, Cormorant, Montserrat, JetBrains Mono). Take the
  STRUCTURE it recommends (display or condensed heading plus neutral sans body, 5:1 headline to
  body ratio, mono only for meta) and apply it to unspent families. Say so in the report.
- **Mid-tone grounds usually fail BOTH white and near-black text.** 2026-08-19 lost three grounds
  this way before rendering: #0891B2, #16A34A and #3B82F6 all sit near 4:1 either direction. Check
  the pair numerically BEFORE committing to a ground, and leave real headroom, because grain
  costs about 0.5 to 1.3 points of measured contrast. #E11D48 computed 4.73 flat and measured 3.80
  after grain; #7C3AED computed 5.71 and measured 4.45. Aim for a flat-computed 6:1 or better.
- **Compute the ground/text pair BEFORE committing, and demand 6:1 flat.** 2026-08-20 built a
  candidate table of 31 harvested hexes against ten text values first and picked only from rows
  clearing 7:1, which is why all seven measured 6.06 or better after grain with zero re-renders.
  That table takes one short script and saves an hour. Do it every run.
- Grain: sigma 1.8, amplitude 3.6 is a good setting. Amplitude 5.0 was heavy enough to break
  otherwise-passing contrast pairs.
- **The ground bleed is easy to overdo.** At 6 percent with a soft falloff it reads as a blurry
  vignette, which looks like a mistake, not like one manufactured surface. 4 percent with a sharp
  falloff (exponent 2.6, blur only 0.12 of the band) is right.
- **Accent planes must be anchored to an edge.** A rectangle floating in the middle of the field
  reads as a stray swatch. 2026-08-19 fixed this by bleeding every accent off a frame edge, with a
  different geometry per frame (right edge band, bottom right corner, top left corner, full width
  foot). Keep varying the geometry so the accent device itself is not a template.
- Fresh grounds harvested but NOT yet spent: #64748B, #27273B, #0369A1, #0284C7, #15803D, #E8ECF0,
  #E6E8EA, #6B7280, #0891B2, #7C3AED, #27272A, #0C0C0C, #181818, #E8ECF1, #059669, #10B981,
  #16A34A, #3B82F6, #BFDBFE, #1B1B30, #1A1E2F, #F1EEF5, #8B5CF6, #E8F1F3, #E7EFF5, #F6F6F7,
  #EDEEEF, #EFF7FB, #171717, #1F2937, #EBF0F5, #E8F0F3, #134E4A, #E0F0F8, #0E1223, #1B2336,
  #2563EB, #FDE68A, #F1F2EF, #F9A8D4, #FBCFE8, #22C55E, #F97316(now spent), #DC2626, #D97706.
  CAUTION on the last three: #D97706 computes only 6.24 against near-black and 3.19 against white,
  and #DC2626 and #6B7280 both sit at 4.83/4.12, so none of them clears the 6:1 headroom rule as a
  GROUND. Use them as accents. #FDE68A and #F1F2EF sit close to the banned cream family, skip them.
  CAUTION: white text fails 4.5:1 on #6B7280 (4.48), #64748B (4.36) and #78716C (4.66 flat, fails
  after grain). Those work only as grounds with DARK text.
  AVOID as grounds: #F5F5F0, #FFFBEB, #FFF7ED, they sit in the banned cream family.
- Grounds spent across the cycle, do not repeat: #ECFEFF #334155 #FAFAF9 #0F766E #1E1B4B #EA580C
  #020617 #064E3B #ECFDF5 #475569 #F0F9FF #1C1917 #EC4899 #0F0F23 #0F172A #EEF2FF #1F2937 #F8FAFC
  #F0FDFA #000000 #FDF2F8 #0C4A6E #7F1D1D #FAFAFA #F0FDF4 #EFF6FF #1E293B #18181B #E8F2F8 #9A3412
  #1E3A8A #E4E4E7 #14532D #BE185D #BAE6FD #C2410C #164E63 #F2F3F4 #0B0B10 #3F3F46 #4338CA #E2E8F0
  #312E81 #37414F #831843 #09090B #F0F8F6 #FAF5FF #F97316 #171939 #E9EEF5 #94A3B8 #22D3EE #E1F2ED
  #272F42.
- FONTS. This sandbox has no font tree beyond DejaVu. Fetch TTFs from
  `raw.githubusercontent.com/google/fonts/main/<lic>/<slug>/<File>.ttf`. Try `ofl`, then `apache`,
  then `ufl` (Ubuntu lives under `ufl`). Note `apache/arimo`, `apache/opensans` and `apache/tinos`
  404 at those paths. Bracketed variable filenames must be URL encoded (`%5Bwght%5D`).
  Verified FULL Greek (cumulative): Advent Pro, Alegreya Sans, Anonymous Pro, Cousine, Fira Code,
  Fira Sans, Inter, JetBrains Mono, Literata, Noto Serif, Open Sans, Piazzolla, Sofia Sans,
  Source Sans 3, Ubuntu, Vollkorn, EB Garamond, Geologica, GFS Didot, GFS Neohellenic, Lato,
  Noto Sans Display, Roboto Slab.
  **The two GFS faces are authentically Greek designs and are the best Greek display material found
  so far.** Paths: `ofl/gfsdidot/GFSDidot-Regular.ttf` and, note the missing hyphen,
  `ofl/gfsneohellenic/GFSNeohellenic.ttf` plus `GFSNeohellenicBold.ttf`. Both are Regular/Bold
  statics, no variable axes. `ofl/anekgreek/AnekGreek[wdth,wght].ttf` 404s under every encoding
  tried, do not waste time on it.
  Verified NO Greek: Alumni Sans, Antonio, Anybody, Archivo Narrow, Asap, Big Shoulders Display,
  Bricolage Grotesque, Cabin, Chakra Petch, Darker Grotesque, Familjen Grotesk, Hanken Grotesk,
  Mulish, Newsreader, Titillium Web, Zilla Slab, Arsenal,
  Cormorant, Encode Sans, Exo 2, Familjen Grotesk, Frank Ruhl Libre, Gabarito, Gantari, Golos Text,
  Heebo, Instrument Sans, Karla, Lora, Manuale, Montserrat, Mulish, Newsreader, Nunito, Nunito Sans,
  Onest, Oswald, Petrona, Playfair Display, Poppins, PT Sans, PT Serif, Public Sans, Red Hat Display,
  Roboto Serif, Russo One, Schibsted Grotesk, Signika, Space Grotesk, Unbounded, Wix Madefor Display.
  Variable-font axis ORDER differs per file (Piazzolla is wght,opsz but Advent Pro is wdth,wght).
  Read `fvar` with fontTools and match axes by TAG. Never hardcode the order.
- **Serif caps run small.** Fitting a long headline to a narrow measure is what causes it. Fix by
  breaking into MORE, SHORTER lines rather than accepting a small size. The 2026-08-19 story went
  from two lines at cap 132 (limp on a 1920 tall canvas) to three shorter lines at cap 180.
- Heading families spent across the cycle, do not reuse: IBM Plex Sans, Fira Sans Condensed,
  Archivo, Jost, Manrope, Barlow Condensed, Space Grotesk, Syne, Anton, Alegreya, Epilogue, Sora,
  Roboto Condensed, Commissioner, Jura, Rubik, Figtree, Tektur, Lexend, Outfit, Bebas Neue,
  Space Mono, Noto Sans, Bodoni Moda, Plus Jakarta Sans, Raleway, Comfortaa, Source Serif 4,
  Playfair Display, Fira Code, EB Garamond, Public Sans, Geologica, Poppins, Russo One,
  Sofia Sans, Antonio, Bricolage Grotesque, Wix Madefor Display, Gabarito, Vollkorn, Literata,
  Questrial, Piazzolla, Archivo Black, Advent Pro, DM Serif Display, League Spartan, Marcellus.
- Pillow, numpy and fonttools are NOT preinstalled. `pip install --timeout 120 Pillow numpy
  fonttools` works.
- `fonts.google.com` is blocked by the sandbox proxy. `raw.githubusercontent.com` and
  `api.github.com` are reachable.
- The build script is committed each run as `outputs/build-<date>.py`. Starting from the previous
  day's script saves a lot of time; 2026-08-19's has the ink-bbox typesetter, the contain-fit
  placer, the plate/type intersection assert and the pixel-sampled contrast check already working.

## PUBLISHING ROUTE, IMPORTANT, READ BEFORE SECTION 9

**`difreshhellas-jpg/posts` is writable. Re-confirmed 2026-08-19 with a real push.** Section 9b's
route is live: push finished PNGs to `posts` under `<date>/` and serve them from
`https://raw.githubusercontent.com/difreshhellas-jpg/posts/main/<date>/<file>.png`. All seven
2026-08-19 URLs returned HTTP 200 at exact local byte length before any Canva call.

Sandbox quirk: the pre-cloned `posts` checkout arrives on the session's feature branch, so a bare
`git push -u origin main` can fail. Run `git checkout -B main origin/main` first. Also set
`git config user.email` and `user.name`, they are not preset. The `difresh-assets` checkout arrives
on its own feature branch too, but at the same commit as `origin/main`.

*Fallback if `posts` ever goes unwritable again.* `difresh-assets` is PUBLIC, so push the PNGs to
`daily-output/<date>/` there and serve from
`https://raw.githubusercontent.com/difreshhellas-jpg/difresh-assets/main/daily-output/<date>/<file>.png`.

**Canva.** `import-design-from-url` STILL fails with `invalid_file`. The outage that began
2026-08-16 has now run FIVE days (re-tested 2026-08-20 on a known-good freshly pushed PNG).
Treat the fallback as the normal route and spend one call proving the outage, not more. The Section 9 fallback works and is the expected path:
1. `upload-asset-from-url` with the raw URL. Confirm the returned `metadata` reads 1080x1350.
2. `copy-design` an existing 1080x1350 design from folder FAHR5ym_TeY. All six copies share the
   same page id and element locator, so you can batch every step five or six at a time.
3. `read-design` with `open_transaction: true`, `filter.fields: ["design_content"]`. The locator has
   now been stable for FOUR runs: page `PBKpkQVGS8vWFp2L`, element
   `PBKpkQVGS8vWFp2L-LBwrx04FDg4WbCVH`. Verify it rather than assuming it.
   The whole fallback batches cleanly: upload all six assets in one message, copy the base design
   six times in one message, open all six transactions in one message, apply all six edits in one
   message, commit all six, move all six, comment on all six. 2026-08-20 ran it in seven rounds.
4. `edit-design` with `update_fill` + `crop_media` + `update_title` in ONE call. **The `crop_media`
   is not optional.** `update_fill` alone leaves the image scaled up about 2.1 percent, a real crop
   that violates Section 1 rule 1. Pass left 0, top 0, width 1080, height 1350 and confirm the
   returned document shows `imageBox=(0,0 1080x1350 rotation=0)` before committing.
5. `edit-design` with `finalize: commit`, operations omitted.
6. `move-item-to-folder` to FAHR5ym_TeY, then `comment-on-design` with the CAPTION line.
No `resize-design` needed, the copied base is already 1080x1350.

## PUBLISH RECORD
- 2026-08-12: posts@main `2026-08-12/`. Canva: 01 DAHSD5hpuVk, 02 DAHSDxGJZFI, 03 DAHSD5MoXqY,
  04 DAHSD_UFbJ0, 05 DAHSD_eEKmw, 06 DAHSD6CSpkU.
- 2026-08-13: posts@main `2026-08-13/`. Canva: 01 DAHSJz6lZLs, 02 DAHSJwYAIv4, 03 DAHSJ10Bz5Q,
  04 DAHSJ5azjKM, 05 DAHSJ-n_5mU, 06 DAHSJ9sVuhY.
- 2026-08-15: brief only, per the then-current restructured pipeline. No PNG, no Canva design.
- 2026-08-16: brief only. The local automation produced exactly one Canva design,
  `DIFRESH 2026-08-16 01` (DAHScUDdPNA). The other five never appeared.
- 2026-08-17: FULL PRODUCTION restored in this routine. 01 DAHSfTEwIjY, 02 DAHSffjJBhM,
  03 DAHSfTCG3Ms, 04 DAHSfdr08Ds, 05 DAHSfUqXsqc, 06 DAHSfedDEb4.
- 2026-08-18: FULL PRODUCTION. 01 DAHSn-uiIfY, 02 DAHSn4Mla70, 03 DAHSn3IqQCM, 04 DAHSnw_Xu5s,
  05 DAHSn846-_o, 06 DAHSn3rQKJU. Greek on 01 and 06. Eight images consumed, CONSUMED to 41.
- 2026-08-19: FULL PRODUCTION. Seven PNGs pushed to difreshhellas-jpg/posts@main under
  `2026-08-19/`, all seven raw URLs verified HTTP 200 at exact byte length. Six posts reached Canva
  via the fallback path (import-design-from-url failed `invalid_file` again), all moved to folder
  FAHR5ym_TeY, each carrying exactly one CAPTION comment:
  01 DAHStyYeKyk, 02 DAHStzdQyEs, 03 DAHStxf-fLI,
  04 DAHSt7TBNOQ, 05 DAHSt1BSiq8, 06 DAHStyEln94.
  Greek on slots 02 and 04, English on 01, 03, 05, 06. Story `difresh_2026-08-19_story.png`
  (English, text only manifesto) rendered and pushed but, per Section 9c, never sent to Canva.
  Contact sheets at `outputs/contact-sheet-2026-08-19-A.png` and `-B.png`.
  Five images consumed, taking CONSUMED to 46 of 72.
- 2026-08-20: FULL PRODUCTION. Seven PNGs pushed to difreshhellas-jpg/posts@main under
  `2026-08-20/`, all seven raw URLs verified HTTP 200 at exact byte length before any Canva call.
  `import-design-from-url` failed `invalid_file` again on slot 01, so all six posts went through the
  fallback path, all moved to folder FAHR5ym_TeY, each carrying exactly one CAPTION comment:
  01 DAHSz339KyE, 02 DAHSz98aQ3U, 03 DAHSz0fyTQo,
  04 DAHSz1alydw, 05 DAHSz-veNV4, 06 DAHSz0mZYs8.
  Greek on slots 01 and 05, English on 02, 03, 04, 06. Story `difresh_2026-08-20_story.png`
  (Greek, plate in negative space) rendered and pushed but, per Section 9c, never sent to Canva.
  Contact sheet at `outputs/contact-sheet-2026-08-20.png`. Build script at
  `outputs/build-2026-08-20.py`. Six images consumed, taking CONSUMED to 52 of 77.
