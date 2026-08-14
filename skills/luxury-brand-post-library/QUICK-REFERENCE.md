# Luxury Brand Post Library - Quick Reference

## 🎯 What It Does

**Input:** Content brief  
**Output:** Premium post specification  
**Result:** Professional-quality Instagram posts based on luxury brand patterns

---

## 🏢 7 Brand Patterns

| Brand | Style | Best For | Copy Tone |
|-------|-------|----------|-----------|
| **Nike** | Bold, Minimal | Announcements, CTAs | Direct, Motivational |
| **Chanel** | Elegant, Timeless | Heritage, Craft | Sophisticated, Understated |
| **Dior** | Dramatic, Artistic | Launches, Seasonal | Poetic, Narrative |
| **Valentino** | Romantic, Editorial | Creative, Projects | Artistic, Emotional |
| **Givenchy** | Minimal, Architectural | Design, Technical | Refined, Precise |
| **Hermès** | Artisanal, Warm | Process, Storytelling | Narrative, Heartfelt |
| **Louis Vuitton** | Aspirational, Global | Lifestyle, Collections | Iconic, Inspiring |

---

## 🚀 3 Ways to Use

### 1. Claude Skill (Easiest)
```
"Make a premium DIFRESH post for [content]"
→ Get complete spec instantly
```

### 2. Python Script
```bash
python generate_post_spec.py --brief "..." --brand "chanel"
→ JSON output for automation
```

### 3. Python Routine Integration
```python
from generate_post_spec import generate_post_spec
spec = generate_post_spec(brief="...", brand="difresh")
# Use spec to guide design, copy, images
```

---

## 📋 What a Spec Includes

```json
{
  "brand_inspiration": "Chanel + Valentino",
  "layout": "split-asymmetric",
  "colors": ["#0A0908", "#C9A24B", "#FFF5E6"],
  "typography": {"headline": "Serif, 48px", "body": "Serif, 24px"},
  "copy_tone": "sophisticated, storytelling",
  "copy_structure": "Hook → Narrative → CTA",
  "image_direction": "Hero design + process detail",
  "best_posting_time": "7-9pm",
  "engagement_hooks": ["before/after", "process", "craftsmanship"]
}
```

---

## 🎨 DIFRESH Default Blend

**Givenchy** (structure, minimal, architectural)  
**+** **Chanel** (heritage, storytelling, craft)  
**+** **Hermès** (warmth, artisanal, intimate)  
**=** Premium, refined, professional DIFRESH posts

---

## 💡 Brand Matching Cheat Sheet

**Use Nike when:** Announcing something bold, need direct action, empowerment  
**Use Chanel when:** Telling heritage story, showcasing craft, timeless positioning  
**Use Dior when:** Launching bold creative, seasonal campaigns, artistic work  
**Use Valentino when:** Creative project, emotional story, artistic vision  
**Use Givenchy when:** Design focus, technical detail, minimal positioning  
**Use Hermès when:** Behind-scenes, artisanal process, hands-on storytelling  
**Use Louis Vuitton when:** Aspirational, global reach, iconic moments  
**Use DIFRESH Blend when:** Not sure, general posts, safe premium aesthetic

---

## 🎬 Execution Workflow

```
1. Write brief (what are you posting?)
2. Get spec (run skill or script)
3. Design (layout + colors + typography from spec)
4. Write copy (tone + structure from spec)
5. Source/generate images (mood + direction from spec)
6. Post (at best_posting_time from spec)
7. Track engagement (log what works)
```

---

## 📍 File Guide

| File | Purpose | For |
|------|---------|-----|
| `SKILL.md` | Main skill definition | Installing in Claude |
| `SKILL-SETUP-GUIDE.md` | Full setup & usage guide | Reading before using |
| `QUICK-REFERENCE.md` | This file | Quick lookups |
| `luxury-brand-patterns.md` | Detailed brand analysis | Deep dives, customization |
| `generate_post_spec.py` | Python automation script | Integrating into routine |
| `test-cases.json` | Test scenarios | Validation, examples |

---

## ✅ Quick Checklist

- [ ] Review QUICK-REFERENCE.md (this file) ← You are here
- [ ] Read SKILL-SETUP-GUIDE.md (full setup)
- [ ] Install skill in Claude OR save Python script
- [ ] Try one example ("Make premium post for...")
- [ ] Execute one complete post
- [ ] Track engagement
- [ ] Build feedback (what worked?)
- [ ] Scale to all posts
- [ ] Integrate into automation routine

---

## 🎯 Success Indicators

✅ Your posts look professional, not generic  
✅ Consistent aesthetic across all DIFRESH content  
✅ Higher engagement (saves, shares, comments)  
✅ Posts feel intentional and premium  
✅ Copy aligns with visual direction  
✅ Audience sees you as premium creative studio  

---

## 🔧 Customization Tips

**Want different colors?** Edit `luxury-brand-patterns.md`, update hex codes  
**Want new brands?** Add to `BRAND_PATTERNS` dict in Python script  
**Want different copy tones?** Modify `copy_tone` field per brand  
**Want custom layouts?** Update `layout` descriptions in patterns file  

---

## 💬 Quick Examples

### Example 1: Bistrot Menu Redesign
```
Brief: "Menu redesign from 5→4 pages, dark + gold"
→ Spec: Chanel + Valentino, split-asymmetric, story-driven
→ Post: "Crafted in Constraint" + before/after + process shots
```

### Example 2: New Tool Launch
```
Brief: "Automation tool for studios, efficiency + creativity"
→ Spec: Nike + Givenchy, bold minimal, direct CTA
→ Post: Hero image + "Automate Creation" + strong CTA
```

### Example 3: Behind-the-Scenes
```
Brief: "Packaging design process, hands + sketches + refinement"
→ Spec: Hermès + Valentino, carousel storytelling, warm mood
→ Post: Multi-shot carousel, artisanal narrative, process visible
```

---

## 📊 Performance Tracking Template

```json
{
  "post_id": "bistrot_menu_aug2026",
  "spec_brand_blend": "Chanel + Valentino",
  "engagement": 1240,
  "saves": 340,
  "shares": 85,
  "comments": 23,
  "link_clicks": 45,
  "notes": "High saves indicate strong emotional resonance"
}
```

Track by brand + layout combination to discover what resonates with your audience.

---

**Ready to make premium posts?** Start with `SKILL-SETUP-GUIDE.md` →

**Need deep dive?** See `luxury-brand-patterns.md` →

**Want to automate?** Use `generate_post_spec.py` →

---

**Version 1.0 | August 13, 2026 | DIFRESH Premium Post Library**
