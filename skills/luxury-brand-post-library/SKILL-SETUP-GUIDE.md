# Luxury Brand Post Library - Setup & Usage Guide

**Created for:** DIFRESH  
**Purpose:** Generate premium Instagram posts by learning from luxury brand patterns (Nike, Chanel, Dior, Valentino, Givenchy, Hermès, Louis Vuitton)  
**Status:** Ready to use in Claude or integrate into your routine

---

## 📦 What's Included

```
luxury-brand-post-library/
├── SKILL.md                           # Main skill definition
├── references/
│   └── luxury-brand-patterns.md       # Detailed brand pattern library
├── scripts/
│   └── generate_post_spec.py          # Python script for generating specs
└── test-cases.json                    # Test cases for validation
```

---

## 🚀 Quick Start

### Option 1: Use in Claude (Recommended)

1. **Install the skill in Claude**
   - Copy `luxury-brand-post-library/SKILL.md` to your `.claude/skills/` folder
   - Or upload via Claude's skill interface

2. **Use it immediately**
   ```
   "Make a premium DIFRESH post about our new Bistrot menu redesign"
   "Generate a post spec for A Sip of Art seasonal collection launch"
   "How would Chanel post this behind-the-scenes content?"
   ```

3. **Get back:** Complete post specification (layout, colors, copy tone, typography, image direction)

### Option 2: Use Python Script Directly

```bash
# Navigate to skill directory
cd luxury-brand-post-library

# Generate a post spec
python scripts/generate_post_spec.py \
  --brief "New DIFRESH automation tool launch" \
  --brand "nike" \
  --mood "bold-empowering" \
  --goal "conversion"

# Output as JSON for your routine
python scripts/generate_post_spec.py \
  --brief "Behind-the-scenes design process" \
  --brand "hermes" \
  --json
```

### Option 3: Integrate Into Your Routine

```python
# In your instagram_daily_poster.py
import sys
sys.path.append('/path/to/luxury-brand-post-library/scripts')
from generate_post_spec import generate_post_spec

brief = "Teacasso Iced Tea fall collection launch"
spec = generate_post_spec(
    brief=brief,
    brand="difresh",  # Use DIFRESH blend (Givenchy + Chanel + Hermès)
    mood="seasonal-artistic",
    goal="engagement"
)

# Now use spec to guide Canva design, copy writing, image generation
print(json.dumps(spec, indent=2))
```

---

## 📋 How It Works

### 1. You Provide a Brief

```
"We just redesigned Bistrot Creperie's menu. 
It went from 5 pages to 4, dark chalkboard aesthetic, 
gold accents, baroque frames. We want to show the design 
but also tell the story of the process."
```

### 2. Skill Analyzes & Matches

The skill looks at your brief and matches it to relevant luxury brand patterns:
- **Layout architects** (where elements sit)
- **Color palettes** (psychology, luxury feel)
- **Typography choices** (serif vs sans, scale, weight)
- **Copy tones** (sophisticated, direct, emotional, etc.)
- **Engagement mechanics** (what makes people stop scrolling)

### 3. You Get Back a Complete Spec

```json
{
  "brief": "Bistrot menu redesign...",
  "brand_inspiration": "Chanel + Valentino",
  "layout": "split-asymmetric",
  "colors": ["#0A0908", "#C9A24B", "#FFF5E6"],
  "typography": {
    "headline": "Cormorant Display, 48px",
    "body": "Playfair Display, 24px"
  },
  "copy_tone": "sophisticated, storytelling-driven",
  "copy_structure": "Hook + Process narrative + CTA",
  "image_direction": "Hero design photo + process detail shot",
  "post_type": "carousel",
  "best_posting_time": "7-9pm",
  "engagement_hooks": ["before/after", "process visibility", "craftsmanship"]
}
```

### 4. You Execute

Use the spec to:
- **Design in Canva** (layout, colors, typography)
- **Write copy** (tone, structure, CTA)
- **Generate or source images** (mood, composition, lighting)
- **Post at optimal time** (best_posting_time)

---

## 🎨 Brand Inspirations Quick Reference

### Nike
**For:** Bold announcements, performance-focused, direct CTAs  
**Vibe:** Minimalist, high-contrast, empowering  
**Colors:** Black, white, + bright accent (blue/red)  
**Copy:** Short, punchy, motivational ("Just Do It")

### Chanel
**For:** Heritage storytelling, craft, timeless positioning  
**Vibe:** Elegant, centered, sophisticated  
**Colors:** Black, gold, cream  
**Copy:** Narrative, understated, reverent of craft

### Dior
**For:** Bold launches, seasonal campaigns, artistic  
**Vibe:** Dramatic, full-bleed, theatrical  
**Colors:** Deep red, black, gold, seasonal variations  
**Copy:** Poetic, narrative-driven, emotional

### Valentino
**For:** Creative projects, emotional storytelling, artistic vision  
**Vibe:** Romantic, editorial, cinematic  
**Colors:** Deep reds, blacks, golds  
**Copy:** Artistic, emotional, expressive

### Givenchy
**For:** Design thinking, technical craft, minimalist  
**Vibe:** Architectural, minimal, intentional  
**Colors:** Black, white, grays, taupe  
**Copy:** Precise, refined, short

### Hermès
**For:** Artisanal process, craft storytelling, heritage  
**Vibe:** Warm, intimate, documentary  
**Colors:** Orange, warm brown, cream  
**Copy:** Narrative, storytelling, "made by hands"

### Louis Vuitton
**For:** Aspirational, global reach, iconic  
**Vibe:** Mixed monogram + lifestyle  
**Colors:** Monogram brown, gold, cream  
**Copy:** Aspirational, lifestyle-focused

### DIFRESH Blend (Default)
**Combines:** Givenchy (minimalism) + Chanel (heritage) + Hermès (artisanal warmth)  
**Best for:** Core DIFRESH posts that want premium, refined, craft-focused aesthetic

---

## 📊 Example Workflows

### Example 1: Bistrot Menu Redesign

**Input Brief:**
```
"New Bistrot Creperie menu design - 5 pages condensed to 4, 
dark chalkboard aesthetic, baroque gold frames, design-focused"
```

**Skill Output:**
```json
{
  "brand_inspiration": "Chanel + Valentino",
  "layout": "split-asymmetric",
  "colors": ["#0A0908", "#C9A24B", "#FFF5E6"],
  "copy_tone": "sophisticated, craft-focused",
  "copy_structure": "Headline: 'Crafted in Constraint' → Story of condensing → Before/After visual"
}
```

**Execution:**
1. Design in Canva: Split layout, dark left side (design) + right side (copy)
2. Copy: "From 5 pages to 4. From chaos to clarity." + process narrative
3. Image: High-contrast detail of final design (gold frame prominent)
4. Post at 7-9pm (dinner-hour engagement)

---

### Example 2: DIFRESH Automation Tool Launch

**Input Brief:**
```
"Launching new Python automation tool for creative studios.
Positions efficiency + creativity. Want to feel bold, empowering, direct."
```

**Skill Output:**
```json
{
  "brand_inspiration": "Nike + Givenchy",
  "layout": "asymmetric-minimal",
  "colors": ["#000000", "#FFFFFF", "#0055FF"],
  "copy_tone": "direct, motivational, technical",
  "copy_structure": "Bold headline → Tool benefit → Strong CTA"
}
```

**Execution:**
1. Design: Asymmetric hero (tool interface or code) + bold headline
2. Copy: "Automate Creation" or "Efficiency Unleashed" + brief benefit statement
3. Image: Clean, minimal, high-contrast (code screenshot, interface demo)
4. Post at 7-9am (morning productivity time)

---

### Example 3: Behind-the-Scenes Design Process

**Input Brief:**
```
"Behind-the-scenes: A Sip of Art packaging design process.
Show hands, sketches, refinement, artisanal approach."
```

**Skill Output:**
```json
{
  "brand_inspiration": "Hermès + Valentino",
  "layout": "narrative-carousel",
  "colors": ["#FF6D00", "#8B6F47", "#FFF5E6"],
  "copy_tone": "storytelling, artisanal, emotional",
  "copy_structure": "Process narrative → Step-by-step → CTA to 'see more'"
}
```

**Execution:**
1. Design: Carousel with multiple shots (raw materials → hands → sketches → refined design)
2. Copy: Storytelling narrative ("Here's how we craft...")
3. Images: Warm lighting, intimate close-ups, hands visible
4. Post at 11am (lifestyle browsing time)

---

## 🔧 Integration Paths

### Path 1: Standalone Skill (Recommended)

Install in Claude and use for **every post**:
- "Make a premium DIFRESH post for [content]"
- Skill returns spec
- You design/write based on spec
- Post

**Pros:**
- Quick, conversational
- Can adapt spec on the fly
- Leverages Claude's full context

**Cons:**
- Manual execution each time

---

### Path 2: Python Automation

Integrate into `instagram_daily_poster.py`:

```python
import json
from luxury_brand_library import generate_post_spec

# For each day's post
today_content = {
    "product": "Teacasso Iced Tea",
    "brief": "New fall collection launch",
    "goal": "awareness"
}

# Generate spec
spec = generate_post_spec(
    brief=today_content['brief'],
    brand="difresh",
    mood="seasonal",
    goal=today_content['goal']
)

# Use spec to guide downstream tools
# 1. Image generation (use image_direction)
leo_prompt = build_prompt_from_image_direction(spec['image_direction'])
image = leonardo_api.generate(leo_prompt)

# 2. Copy writing (use copy_structure + copy_tone)
caption = write_caption(
    structure=spec['copy_structure'],
    tone=spec['copy_tone'],
    product=today_content['product']
)

# 3. Design in Canva (use layout + colors + typography)
# Push to Canva with spec as template

# 4. Post at optimal time
post_at_time(image, caption, spec['best_posting_time'])
```

**Pros:**
- Fully automated
- Consistent quality
- Can log which specs perform best (feedback loop)

**Cons:**
- Requires Python integration
- Less flexibility for one-off tweaks

---

### Path 3: Hybrid (Best Practice)

Use **skill for creative briefs** + **Python for automation**:

1. Claude skill → generates spec + strategic advice
2. Python automation → reads spec, executes template, posts
3. Feedback loop → track engagement, improve specs over time

---

## 📈 Feedback Loop (Optional)

Once you've used specs to create posts, **track what works**:

```python
# Log performance
engagement_data = {
    "post_id": "teacasso_fall_2026",
    "spec_brand": "difresh",
    "layout": "split-asymmetric",
    "engagement": 1240,
    "saves": 340,
    "shares": 85,
    "conversion": "link clicks: 45"
}

# Analyze patterns
# "Posts with Chanel + layout:centered get 35% more saves"
# "Nike-inspired posts get highest shares"
# "Hermès specs drive longest dwell time"

# Update future specs based on performance
```

---

## 🎯 Tips for Best Results

1. **Be specific in your brief**
   - ❌ "Make a cool post"
   - ✅ "New Bistrot menu redesign, show design quality and process"

2. **Match brief to brand inspiration**
   - Nike for bold announcements
   - Chanel for heritage/craft
   - Dior for seasonal launches
   - Hermès for process/behind-the-scenes

3. **Use DIFRESH blend for general posts**
   - Givenchy's minimalism (clean, intentional)
   - Chanel's heritage (craft, storytelling)
   - Hermès' warmth (approachable luxury)

4. **Execute the full spec**
   - Don't skip layout advice (it's tested by luxury brands)
   - Use color palette (it's psychologically chosen)
   - Follow copy structure (it's engagement-optimized)

5. **A/B test different specs**
   - Try Nike for one week, Chanel for another
   - Track engagement
   - Build hypothesis about what works for your audience

---

## 🚨 Troubleshooting

### "The spec doesn't feel right for my brand"
- You're matching correctly but overthinking execution
- Adapt the spec, don't ignore it—it's designed by experts
- Consider which brand resonates vs which doesn't

### "My audience doesn't respond to the recommended copy tone"
- Try different brand inspirations
- Log engagement by tone type
- Build preference data over time

### "I don't have time to execute specs manually"
- Use Python integration (automates the execution)
- Or use this skill + Canva bulk create
- Build a workflow that fits your schedule

### "I want to customize/improve the skill"
- All brand patterns are in `references/luxury-brand-patterns.md`
- Edit color palettes, copy tones, layouts
- Rebuild Python script with your customizations

---

## 📚 Reference Files

- **`SKILL.md`** - Main skill definition (what to install)
- **`references/luxury-brand-patterns.md`** - Full brand pattern library (detailed analysis)
- **`scripts/generate_post_spec.py`** - Python script (for automation)
- **`test-cases.json`** - Test scenarios (for validation)

---

## 🎬 Next Steps

1. **Install the skill** in Claude
2. **Try one brief** ("Make a premium post for [your content]")
3. **Review the spec** (does it make sense for your brand?)
4. **Execute one post** (design, write, image, post)
5. **Track engagement** (compare with your regular posts)
6. **Build feedback** (what worked? what didn't?)
7. **Scale** (use for all future posts, integrate into Python routine)

---

## Questions?

- **How to use:** See examples above, start with Option 1
- **How to customize:** Edit `references/luxury-brand-patterns.md`
- **How to integrate:** See Python integration path
- **How to improve:** Track engagement, build feedback loop

**Made for DIFRESH** 🎨  
**Premium posts by design, not luck.**

---

**Version:** 1.0  
**Date:** August 13, 2026  
**Status:** Production-Ready
