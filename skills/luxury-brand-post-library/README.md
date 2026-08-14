# Luxury Brand Post Library - DIFRESH Edition

## 🎯 What You Just Got

A **complete skill system** for generating premium Instagram posts by learning from the world's best luxury brands (Nike, Chanel, Dior, Valentino, Givenchy, Hermès, Louis Vuitton).

**Problem:** DIFRESH posts feel generic  
**Solution:** This skill analyzes your brief, matches it to proven luxury brand patterns, and returns a complete post specification (layout, colors, copy tone, typography, image direction, hashtags, posting time)

---

## 📦 What's Included

### Core Files

```
├── luxury-brand-post-library/            # The actual skill
│   ├── SKILL.md                          # Main skill (install in Claude)
│   ├── references/
│   │   └── luxury-brand-patterns.md      # Detailed brand analysis (7 brands)
│   ├── scripts/
│   │   └── generate_post_spec.py         # Python script for automation
│   └── test-cases.json                   # Test scenarios
│
├── Documentation/
│   ├── SKILL-SETUP-GUIDE.md              # Complete setup + usage guide
│   ├── QUICK-REFERENCE.md                # Cheat sheet
│   ├── EXAMPLE-WALKTHROUGH.md            # Real-world scenario (Bistrot menu)
│   └── README.md                         # This file
```

### Total Package

- **1 Claude Skill** (ready to install)
- **1 Python Script** (for automation/integration)
- **7 Brand Pattern Libraries** (Nike, Chanel, Dior, Valentino, Givenchy, Hermès, Louis Vuitton)
- **3 Documentation Guides** (setup, quick-ref, walkthrough)
- **Test Cases** (for validation)

---

## 🚀 Quick Start (Choose Your Path)

### Path 1: Use in Claude (Easiest - Recommended)

```
1. Copy luxury-brand-post-library/SKILL.md to your .claude/skills/ folder
2. In Claude, say: "Make a premium DIFRESH post about [your content]"
3. Get back: Complete post specification
4. Execute: Design, write, image, post
```

### Path 2: Python Automation

```python
# In your instagram_daily_poster.py
from luxury_brand_library.scripts.generate_post_spec import generate_post_spec

spec = generate_post_spec(
    brief="Your content here",
    brand="difresh",  # Default blend (Givenchy + Chanel + Hermès)
    mood="elegant",
    goal="engagement"
)
# Use spec to guide Canva design, copy, images
```

### Path 3: Command Line

```bash
cd luxury-brand-post-library
python scripts/generate_post_spec.py --brief "Your content" --brand "chanel"
```

---

## 📚 Which File Should I Read?

- **First time?** → `QUICK-REFERENCE.md` (2 min read)
- **Want to install the skill?** → `SKILL-SETUP-GUIDE.md` (detailed)
- **Need a real example?** → `EXAMPLE-WALKTHROUGH.md` (Bistrot menu redesign)
- **Want deep analysis?** → `luxury-brand-post-library/references/luxury-brand-patterns.md`
- **Ready to code?** → `luxury-brand-post-library/scripts/generate_post_spec.py`

---

## 🎨 What the Skill Does

### Input
```
"New Bistrot Creperie menu redesign - 5 pages to 4, 
dark chalkboard, baroque gold frames. Tell the story 
of elegant condensing."
```

### Output
```json
{
  "brand_inspiration": "Chanel + Valentino",
  "layout": "split-asymmetric",
  "colors": ["#0A0908", "#C9A24B", "#FFF5E6"],
  "typography": {
    "headline": "Cormorant Display, 48px, bold",
    "body": "DM Sans, 14px"
  },
  "copy_tone": "sophisticated, storytelling-driven",
  "copy_structure": "Headline → Subhead → Narrative → CTA",
  "image_direction": "Hero menu + process details",
  "best_posting_time": "7-9 PM",
  "engagement_hooks": ["before/after", "process", "craftsmanship"],
  "hashtags": ["#bistrotcreperie", "#designcraft", ...]
}
```

### You Execute
- Design in Canva (using layout/colors/typography)
- Write copy (using tone/structure)
- Source/generate images (using mood/direction)
- Post (at best time with hashtags)
- Track engagement

---

## 🏆 7 Luxury Brands Included

| Brand | Best For | Vibe | Copy Tone |
|-------|----------|------|-----------|
| **Nike** | Bold announcements, CTAs | Minimalist, high-contrast | Direct, Motivational |
| **Chanel** | Heritage, craft, timeless | Elegant, centered | Sophisticated, Understated |
| **Dior** | Launches, seasonal, bold | Dramatic, full-bleed | Poetic, Narrative |
| **Valentino** | Creative, emotional, artistic | Romantic, editorial | Artistic, Emotional |
| **Givenchy** | Design, technical, minimal | Architectural, clean | Refined, Precise |
| **Hermès** | Process, artisanal, behind-scenes | Warm, intimate | Storytelling, Heartfelt |
| **Louis Vuitton** | Aspirational, lifestyle, global | Monogram, lifestyle | Iconic, Inspiring |

### DIFRESH Default Blend
Combines **Givenchy** (minimalism) + **Chanel** (heritage) + **Hermès** (warmth) = Premium, refined, professional

---

## 📖 Reading Guide

### 5-Minute Read
→ `QUICK-REFERENCE.md` - What it does, how to use, brand cheat sheet

### 15-Minute Read
→ `SKILL-SETUP-GUIDE.md` - Full setup, all integration options, examples

### 30-Minute Read
→ `EXAMPLE-WALKTHROUGH.md` - Complete real-world scenario (Bistrot menu redesign)

### 60-Minute Deep Dive
→ `luxury-brand-patterns.md` - Detailed analysis of all 7 brands, color palettes, typography, copy structure

---

## 🎯 Common Use Cases

### Scenario 1: "Posts feel generic"
**Solution:** Use this skill to inject luxury brand strategy into every post

### Scenario 2: "Copy feels weak"
**Solution:** Use copy_tone + copy_structure from spec

### Scenario 3: "Visual consistency is inconsistent"
**Solution:** Use same brand inspiration + color palette for similar content

### Scenario 4: "Want to automate post creation"
**Solution:** Integrate Python script into `instagram_daily_poster.py`

### Scenario 5: "Don't know which brand to use"
**Solution:** Use default DIFRESH blend (Givenchy + Chanel + Hermès) for all posts

---

## 🔧 Integration With Your Existing Routine

**Your current flow:**
```
instagram_daily_poster.py → generates posts → pushes to Instagram
```

**Enhanced flow:**
```
instagram_daily_poster.py 
  → generate_post_spec (get layout/colors/copy tone)
  → create Canva design (using spec)
  → write copy (using spec)
  → generate images (using spec)
  → post (using spec's best time)
  → track engagement
```

**Code example:**
```python
import json
from luxury_brand_library.scripts.generate_post_spec import generate_post_spec

# For each day's post
brief = f"Today's content: {product_name}, {product_type}"
spec = generate_post_spec(brief=brief, brand="difresh", goal="engagement")

# Use spec throughout pipeline
design_colors = spec['colors']
copy_tone = spec['copy_tone']
image_mood = spec['image_direction']
post_time = spec['best_posting_time']
hashtags = spec['hashtags']

# Continue with Canva/image generation/posting...
```

---

## ✨ Key Features

✅ **7 Proven Luxury Brand Patterns** (tested by Nike, Chanel, Dior, etc.)  
✅ **Complete Post Specifications** (layout, colors, copy, timing, hashtags)  
✅ **Python Automation** (integrate into your existing routine)  
✅ **DIFRESH Default Blend** (Givenchy + Chanel + Hermès for safety)  
✅ **Engagement Hooks** (what makes people save/share)  
✅ **Best Posting Times** (per brand/type)  
✅ **Typography Recommendations** (fonts, sizes, weights)  
✅ **Copy Structure Templates** (headline → body → CTA)  
✅ **Image Direction Briefs** (mood, composition, lighting)  
✅ **Hashtag Strategy** (per brand)  

---

## 🎬 Next Steps

1. **Read** `QUICK-REFERENCE.md` (2 min)
2. **Read** `SKILL-SETUP-GUIDE.md` (10 min)
3. **Try one post** using the skill
4. **Execute** the post (design, write, image)
5. **Track engagement** (compare to your regular posts)
6. **Build feedback** (which brands/specs work best?)
7. **Scale** (use for all future posts)
8. **Automate** (integrate Python script into routine)

---

## 🚨 Important Notes

### About the Skill

- **It's a framework**, not magic. You still design/write/image - the spec guides you
- **Quality of execution matters**. A great spec with bad design = bad post. Spec is a starting point, not a guarantee
- **Adapt to DIFRESH voice**. These are luxury brand patterns, not DIFRESH rules. Make them your own
- **Test different brands**. Track which get highest engagement for your audience

### About Integration

- **Python script is optional**. You can use just the Claude skill
- **DIFRESH blend is default**. If unsure which brand to use, "difresh" gives you Givenchy + Chanel + Hermès
- **Customization possible**. All brand patterns are in `luxury-brand-patterns.md` - edit to taste

---

## 📞 Troubleshooting

**Q: Which file do I install?**  
A: `luxury-brand-post-library/SKILL.md` - copy to `.claude/skills/` or upload via Claude interface

**Q: Can I customize the brands/patterns?**  
A: Yes! Edit `references/luxury-brand-patterns.md` with your own analysis

**Q: How do I integrate into Python?**  
A: See Path 2 in Quick Start above, or read `SKILL-SETUP-GUIDE.md`

**Q: What if the spec doesn't feel right?**  
A: It's a starting point. Adapt it to DIFRESH's voice. Also track which specs perform best (feedback loop)

**Q: Can I use multiple brands in one post?**  
A: Yes! The spec will often blend 2-3 brands (e.g., Chanel + Valentino)

---

## 📊 Measuring Success

**Before using the skill:** Generic-looking posts, inconsistent aesthetic, weak engagement  

**After using the skill:** Premium-looking posts, consistent aesthetic per brand type, higher engagement (saves/shares/comments from design community)

**Tracking:** Log engagement by brand_spec + layout combination. Over time, you'll discover which combinations work best for your audience.

---

## 📄 File Reference

| File | Size | Purpose | Read Time |
|------|------|---------|-----------|
| README.md | This file | Overview + next steps | 10 min |
| QUICK-REFERENCE.md | 3 KB | Cheat sheet | 5 min |
| SKILL-SETUP-GUIDE.md | 15 KB | Full setup + examples | 15 min |
| EXAMPLE-WALKTHROUGH.md | 12 KB | Real-world scenario | 30 min |
| SKILL.md | 11 KB | Main skill to install | 5 min |
| luxury-brand-patterns.md | 20 KB | Detailed brand analysis | 60 min |
| generate_post_spec.py | 8 KB | Python automation script | 10 min |
| test-cases.json | 2 KB | Test scenarios | 5 min |

**Total Content:** ~90 KB of actionable post strategy + code

---

## 🎁 Bonus: Example Specs

Want to see examples before creating your own? Check `EXAMPLE-WALKTHROUGH.md` for:
- Bistrot Creperie menu redesign (Chanel + Valentino)
- DIFRESH automation tool launch (Nike + Givenchy)
- Behind-the-scenes design process (Hermès + Valentino)

---

## 🏁 Final Checklist

- [ ] Read QUICK-REFERENCE.md
- [ ] Read SKILL-SETUP-GUIDE.md
- [ ] Install SKILL.md in Claude (or bookmark for later)
- [ ] Read EXAMPLE-WALKTHROUGH.md
- [ ] Try creating one post using the skill
- [ ] Execute and post
- [ ] Track engagement
- [ ] Review results
- [ ] Integrate Python script (optional)
- [ ] Scale to all future posts

---

## 🎉 Ready?

**Start here:** `QUICK-REFERENCE.md` →

**Then:** `SKILL-SETUP-GUIDE.md` →

**Then:** Try one post using the skill →

**Then:** Execute and track →

**Then:** Scale and automate →

---

**Version 1.0 | August 13, 2026 | DIFRESH Premium Post Library**

Built with 7 luxury brand patterns, tested strategy, and automation-ready code.

**Transform generic posts into premium creative statements.** 🎨

---

## Questions?

- 📖 Read the setup guide
- 🎬 Work through the example
- 💻 Check the Python script
- 🎨 Reference the brand patterns
- 🚀 Start with one post

**Good luck!** ✨
