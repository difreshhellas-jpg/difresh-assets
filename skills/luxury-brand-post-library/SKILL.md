---
name: luxury-brand-post-library
description: Generate premium Instagram posts for DIFRESH by analyzing luxury brand patterns (Nike, Chanel, Dior, Valentino, Givenchy, Hermès, Louis Vuitton). Use this whenever the user wants to create a DIFRESH Instagram post that stands out with professional quality, needs layout/design direction, wants to "sound premium", or is looking for inspiration from luxury brands. Triggers include: "make a premium DIFRESH post", "design a luxury post for", "what's the best way to showcase [project]", "how would [luxury brand] post this", "generate a post spec", or any request to upgrade DIFRESH's visual/copy quality.
---

# Luxury Brand Post Library

Generate premium Instagram posts for DIFRESH by learning from the world's best luxury brands.

## Overview

This skill analyzes post patterns from Nike, Chanel, Dior, Valentino, Givenchy, Hermès, and Louis Vuitton, then generates a **complete post specification** for DIFRESH content. Output includes layout framework, color palette, typography, image direction, copy tone, and actionable Canva template suggestions.

## Quick Start

**Input:** Brief description of content
```
"New Bistrot Creperie menu redesign launch"
"Behind-the-scenes A Sip of Art production"
"Announcing automation tool for creative studios"
```

**Output:** Post spec (JSON format)
```json
{
  "brand_inspiration": "Chanel + Dior",
  "layout": "centered hero + bottom copy",
  "colors": ["#0A0908", "#C9A24B", "#F5F5F5"],
  "typography": {"headline": "Cormorant Display", "body": "DM Sans"},
  "image_mood": "moody-luxury-close-up",
  "copy_tone": "sophisticated, storytelling-driven",
  "copy_structure": "hook + narrative + cta",
  "reference_brand_style": "Chanel elegance meets Dior drama",
  "canva_template_type": "hero-centered-elegant"
}
```

---

## Luxury Brand Patterns (Reference Library)

Read `/references/luxury-brand-patterns.md` for detailed breakdown of each brand's:
- Layout architecture (where elements sit)
- Color psychology & palettes
- Typography choices
- Visual mood/composition
- Copy tone & structure
- Post frequency & strategy

### Quick Brand Snapshot

| Brand | Vibe | Colors | Layout | Copy Tone | Best For |
|-------|------|--------|--------|-----------|----------|
| **Nike** | Bold, Minimalist, Empowering | Black, White, 1 accent | Asymmetric hero + text | Punchy, direct, motivational | Performance, announcements |
| **Chanel** | Elegant, Timeless, Luxe | Gold, Black, Cream, White | Centered, symmetrical | Sophisticated, understated | Heritage, craft, timeless |
| **Dior** | Dramatic, Maximalist, Artistic | Rich saturation (reds, blacks, golds) | Full-bleed hero | Narrative-driven, poetic | New launches, seasonal |
| **Valentino** | Romantic, Editorial, Couture | Deep reds, blacks, golds | Cinematic, asymmetric | Artistic, emotional | Creative work, collections |
| **Givenchy** | Minimal Luxury, Architectural | Moody (blacks, grays), tonal | Clean, geometric | Technical, refined | Craft, design thinking |
| **Hermès** | Artisanal, Storytelling, Heritage | Warm neutrals, signature orange | Lifestyle, intimate | Narrative, heritage-focused | Process, making |
| **Louis Vuitton** | Bold Monogram, Travel, Luxury | Monogram brown, gold, black | Mixed (hero + detail shots) | Aspirational, lifestyle | Collections, campaigns |

---

## How to Use This Skill

### Step 1: Provide Content Brief

Tell me what you're posting about:
- **Product/Project:** What is it? (new design, process shot, announcement, etc.)
- **Brand:** Which DIFRESH sub-brand? (Bistrot Creperie, Dalí Coffee, Teacasso, Michaelangelo, or DIFRESH core)
- **Mood/Context:** Seasonal? Celebratory? Educational? Behind-the-scenes?
- **Goal:** What's the post trying to do? (awareness, engagement, credibility, link clicks?)

### Step 2: Skill Analyzes & Outputs

I'll:
1. **Match your brief** to relevant luxury brand patterns
2. **Extract the winning formula** (layout, colors, typography, tone)
3. **Output a complete post spec** (JSON + copy direction + image brief)
4. **Suggest Canva template type** for easy execution

### Step 3: Execute in Your Routine

Use the spec to:
- Create Canva design (or feed to automation routine)
- Write copy using the suggested tone/structure
- Source or generate images matching the mood
- Keep consistent with your brand library

---

## Example: Applying the Skill

**Input:**
```
"We just redesigned Bistrot Creperie's menu. 
It went from 5 pages to 4, dark chalkboard aesthetic, 
gold accents, baroque frames. We want to show the design 
but also tell the story of the process."
```

**Skill Output:**
```json
{
  "brief": "Bistrot Creperie menu redesign showcase",
  "matched_brands": ["Chanel", "Valentino"],
  "reasoning": "Heritage + craft (Chanel), romantic editorialization (Valentino)",
  
  "post_spec": {
    "layout": "split-asymmetric: design hero on left, process story on right",
    "colors": ["#0A0908", "#C9A24B", "#FFF5E6", "#8B8680"],
    "typography": {
      "headline": "Cormorant Display, 48px, #0A0908",
      "body": "Playfair Display, 24px, #8B8680",
      "accent": "DM Sans, 14px, #C9A24B"
    },
    "image_direction": "Hero: high-contrast photo of final menu design (gold frame detail prominent, dark chalkboard texture visible). Accent: small process shot (sketches, refinement stages) in corner.",
    "composition_mood": "moody-elegant-intimate",
    "copy_structure": {
      "headline": "Crafted in Constraint",
      "subheading": "From 5 pages to 4. From chaos to clarity.",
      "body": "The Bistrot Creperie menu redesign story: how we condensed complexity into a baroque-framed masterpiece. Every detail matters.",
      "cta": "Swipe to see the before, the process, and the gold-kissed final frame."
    },
    "copy_tone": "sophisticated, storytelling-driven, reverent of craft",
    "post_type": "carousel or single-hero-with-description",
    "best_time_to_post": "7-9pm (dinner vibes)",
    "hashtags": ["#bistrotcreperie", "#menudesign", "#designcraft", "#artisanbranding"],
    "engagement_hooks": "Process + result (people love before/after). Specificity ('5 to 4') creates curiosity."
  }
}
```

---

## Integration with Your Routine

### Option 1: Canva Template Builder
Use the post spec to create a reusable Canva template:
- Layout matches the recommended framework
- Colors pulled from the palette
- Typography locked in
- Ready for bulk content

### Option 2: Python Routine Integration
Embed in your `instagram_daily_poster.py`:
```python
from luxury_brand_library import generate_post_spec

brief = {
    "product": "Teacasso Iced Tea collection",
    "brand": "teacasso",
    "mood": "geometric-architectural",
    "goal": "showcase new flavor launch"
}

spec = generate_post_spec(brief)
# Output: complete post spec (layout, colors, copy tone, image direction)

# Feed to Leonardo AI for image generation
leo_prompt = build_prompt_from_spec(spec)
image = leonardo_api.generate(leo_prompt)

# Use spec for copy
caption = write_caption(spec['copy_structure'], spec['copy_tone'])

# Push to Canva template or Instagram
```

### Option 3: Manual Execution
Read the spec, use it as a creative brief, design in Canva, write copy, post.

---

## When to Use This Skill

✅ **Do use this skill when:**
- Creating a new DIFRESH Instagram post (any sub-brand)
- Wanting to "level up" the visual quality or copy sophistication
- Unsure how to position/frame new work
- Need layout inspiration from luxury brands
- Want to maintain consistent premium aesthetic across posts
- Building templates for bulk content generation
- Asking "how would [luxury brand] post this?"

❌ **Don't need this skill when:**
- Posting quick behind-the-scenes (snapshot aesthetic is fine)
- Just need to share news (straightforward announcement)
- Already have a full design in Canva ready to post

---

## Post Patterns Deep Dive

Read the full reference guide for:
- Detailed brand breakdowns (Nike minimalism, Chanel elegance, etc.)
- Color palette hex codes per brand
- Font pairings that work
- Layout templates (hero-left, centered, asymmetric, etc.)
- Post frequency strategies
- Engagement mechanics (what makes people stop scrolling)

👉 See: `/references/luxury-brand-patterns.md`

---

## Output Formats

All specs include:
- **Layout**: Visual framework (where headline, image, body text sit)
- **Colors**: Hex palette matched to brand inspiration
- **Typography**: Font families, sizes, weights for each text element
- **Image Direction**: Mood, composition, lighting, subject framing
- **Copy Tone**: Voice, style, emotional register
- **Copy Structure**: Template for headline → subheading → body → CTA
- **Post Type**: Single image, carousel, video, Reel
- **Best Posting Time**: Based on brand engagement patterns
- **Hashtags**: Luxury positioning + DIFRESH specifics
- **Engagement Hooks**: What makes this post stoppable/shareable

---

## Examples by Brand Type

### Givenchy-Inspired (Minimalist + Architectural)
*Best for: Technical announcements, process posts, design thinking*
- Clean grid, centered elements
- Tonal color palette (blacks, grays)
- Minimal text, maximum space
- Copy is SHORT and precise

### Chanel-Inspired (Elegant + Heritage)
*Best for: Heritage storytelling, craftsmanship, timeless products*
- Symmetrical, centered layout
- Gold + black + cream
- Serif typography (Cormorant, Playfair)
- Copy tells a story of heritage/craft

### Dior-Inspired (Dramatic + Seasonal)
*Best for: New launches, seasonal campaigns, bold creative work*
- Full-bleed hero image
- Rich, saturated colors
- Large, bold typography
- Narrative-driven, emotional copy

### Valentino-Inspired (Romantic + Editorial)
*Best for: Creative projects, collections, artistic collaborations*
- Cinematic composition
- Mixed typography scales
- Emotional storytelling
- Deep, rich colors (reds, blacks, golds)

### Nike-Inspired (Bold + Minimalist)
*Best for: Announcements, calls to action, empowering messages*
- Asymmetric layout
- High contrast (black/white + accent color)
- Punchy, motivational copy
- Direct CTA

---

## Notes

- All specs are **starting points**, not rigid rules. Adapt to DIFRESH's unique voice.
- The library is **static reference data**. Over time, you can log which specs perform best and build feedback.
- For **A Sip of Art sub-brands** (Dalí, Teacasso, Michaelangelo), pair this skill with `sip-of-art-image-prompts` for full automation.
- Color codes in specs are suggestions; adjust to match your brand guidelines.

---

**Next step:** Provide your content brief and I'll generate a complete post spec! 🎯
