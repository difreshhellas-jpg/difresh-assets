#!/usr/bin/env python3
"""
Luxury Brand Post Library - Post Spec Generator

Generates premium Instagram post specifications for DIFRESH
by analyzing luxury brand patterns.

Usage:
    python generate_post_spec.py --brief "New product launch" --brand "difresh"
    python generate_post_spec.py --brief "Bistrot redesign" --mood "elegant" --goal "showcase"
"""

import json
import sys
from typing import Dict, Any

# Brand pattern templates
BRAND_PATTERNS = {
    "nike": {
        "name": "Nike",
        "layout": "asymmetric-hero-plus-text",
        "colors": ["#000000", "#FFFFFF", "#0055FF"],
        "typography": {
            "headline": "Helvetica Neue Bold, 80-120px, all caps",
            "body": "Clean sans-serif, 20-30px"
        },
        "copy_tone": "direct, motivational, action-oriented",
        "copy_structure": "Imperative headline + brief subtext + CTA",
        "best_for": ["announcements", "performance", "achievement", "direct CTA"],
        "post_type": "single-image or Reel",
        "best_time": "7-9am or 5-7pm",
    },
    "chanel": {
        "name": "Chanel",
        "layout": "centered-symmetrical",
        "colors": ["#000000", "#F5F5F5", "#D4AF37"],
        "typography": {
            "headline": "Garamond or Didot, 60-90px, title case",
            "body": "Serif or refined sans-serif, 16-24px"
        },
        "copy_tone": "sophisticated, understated, narrative",
        "copy_structure": "Elegant headline + heritage/craft narrative + soft CTA",
        "best_for": ["heritage", "craftsmanship", "timeless", "luxury"],
        "post_type": "single-image or carousel",
        "best_time": "2-4pm",
    },
    "dior": {
        "name": "Dior",
        "layout": "full-bleed-hero",
        "colors": ["#8B0000", "#000000", "#FFD700"],
        "typography": {
            "headline": "Bold serif or dramatic sans-serif, 70-120px",
            "body": "Refined serif or sans-serif, 18-28px"
        },
        "copy_tone": "artistic, narrative, poetic, seasonal",
        "copy_structure": "Dramatic headline + poetic narrative + discovery CTA",
        "best_for": ["launches", "seasonal", "artistic", "bold creative"],
        "post_type": "single-hero or carousel",
        "best_time": "6-8pm",
    },
    "valentino": {
        "name": "Valentino",
        "layout": "cinematic-asymmetric",
        "colors": ["#8B0000", "#000000", "#D4AF37"],
        "typography": {
            "headline": "Mixed-scale serif, large + small accents, 60-100px",
            "body": "Serif or decorative, 16-26px"
        },
        "copy_tone": "artistic, emotional, romantic, narrative",
        "copy_structure": "Artistic headline + emotional narrative + exploration CTA",
        "best_for": ["creative", "emotional", "artistic", "projects"],
        "post_type": "carousel or single-artistic",
        "best_time": "7-9pm",
    },
    "givenchy": {
        "name": "Givenchy",
        "layout": "clean-grid-minimal",
        "colors": ["#000000", "#FFFFFF", "#36454F"],
        "typography": {
            "headline": "Minimal sans-serif (Helvetica, Univers), 50-80px",
            "body": "Clean sans-serif, 14-20px"
        },
        "copy_tone": "refined, technical, poetic minimalism",
        "copy_structure": "Minimal headline + precise copy (1-2 lines) + soft/no CTA",
        "best_for": ["design", "technical", "minimal", "architecture"],
        "post_type": "single-image",
        "best_time": "3-5pm",
    },
    "hermes": {
        "name": "Hermès",
        "layout": "narrative-lifestyle",
        "colors": ["#FF6D00", "#8B6F47", "#FFF5E6"],
        "typography": {
            "headline": "Serif or elegant sans-serif, 55-85px",
            "body": "Serif, warm, 16-24px"
        },
        "copy_tone": "narrative, heritage-focused, artisanal, storytelling",
        "copy_structure": "Heritage headline + craft narrative + discovery CTA",
        "best_for": ["process", "craft", "heritage", "artisan"],
        "post_type": "single-image or carousel",
        "best_time": "9am-12pm",
    },
    "louis_vuitton": {
        "name": "Louis Vuitton",
        "layout": "mixed-monogram-lifestyle",
        "colors": ["#8B6F47", "#D4AF37", "#F5F5DC"],
        "typography": {
            "headline": "Serif or bold custom, 65-95px",
            "body": "Serif, 18-26px"
        },
        "copy_tone": "aspirational, global, iconic, lifestyle",
        "copy_structure": "Iconic headline + lifestyle narrative + shop CTA",
        "best_for": ["aspirational", "global", "iconic", "lifestyle"],
        "post_type": "single-image or carousel",
        "best_time": "10am-2pm",
    },
}

def generate_post_spec(brief: str, brand: str = "difresh", mood: str = None, goal: str = None) -> Dict[str, Any]:
    """
    Generate a complete post specification from a brief.
    
    Args:
        brief: Content description (what you're posting)
        brand: Which brand inspiration(s) to use (nike, chanel, dior, etc., or "difresh" for blend)
        mood: Optional mood/context (elegant, dramatic, minimal, artisanal, etc.)
        goal: Optional goal (awareness, engagement, credibility, traffic, etc.)
    
    Returns:
        Complete post spec dictionary
    """
    
    # Default DIFRESH blend (Givenchy + Chanel + Hermès)
    if brand.lower() == "difresh":
        primary = "givenchy"
        secondary = "chanel"
        tertiary = "hermes"
    else:
        primary = brand.lower()
        secondary = None
        tertiary = None
    
    # Validate brand
    if primary not in BRAND_PATTERNS:
        return {
            "error": f"Brand '{primary}' not found. Use one of: {', '.join(BRAND_PATTERNS.keys())}",
            "valid_brands": list(BRAND_PATTERNS.keys())
        }
    
    # Get primary pattern
    pattern = BRAND_PATTERNS[primary].copy()
    
    # Build spec
    spec = {
        "brief": brief,
        "brand_inspiration": pattern["name"],
        "layout": pattern["layout"],
        "colors": pattern["colors"],
        "typography": pattern["typography"],
        "copy_tone": pattern["copy_tone"],
        "copy_structure": pattern["copy_structure"],
        "best_for": pattern["best_for"],
        "post_type": pattern["post_type"],
        "best_posting_time": pattern["best_time"],
        "mood": mood or "premium-luxury",
        "goal": goal or "engagement",
    }
    
    # Add blended recommendations if using DIFRESH
    if brand.lower() == "difresh":
        spec["blend_inspiration"] = f"{BRAND_PATTERNS[primary]['name']} (primary) + {BRAND_PATTERNS[secondary]['name']} (secondary) + {BRAND_PATTERNS[tertiary]['name']} (accent)"
        spec["recommendation"] = "Use Givenchy's minimalism as structure, Chanel's heritage for copy, Hermès' artisanal warmth for image mood"
    
    return spec


def main():
    """CLI interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate premium post specs from luxury brand patterns")
    parser.add_argument("--brief", required=True, help="Content description/brief")
    parser.add_argument("--brand", default="difresh", help="Brand inspiration (nike, chanel, dior, etc., or difresh for blend)")
    parser.add_argument("--mood", help="Optional mood/context")
    parser.add_argument("--goal", help="Optional posting goal")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    # Generate spec
    spec = generate_post_spec(
        brief=args.brief,
        brand=args.brand,
        mood=args.mood,
        goal=args.goal
    )
    
    # Output
    if args.json or "--json" in sys.argv:
        print(json.dumps(spec, indent=2))
    else:
        print("=" * 60)
        print(f"POST SPECIFICATION: {spec.get('brief', 'Unknown')}")
        print("=" * 60)
        print(f"\n🎨 BRAND INSPIRATION: {spec.get('brand_inspiration')}")
        if "blend_inspiration" in spec:
            print(f"   Blended: {spec['blend_inspiration']}")
        print(f"\n📐 LAYOUT: {spec.get('layout')}")
        print(f"🎨 COLORS: {', '.join(spec.get('colors', []))}")
        print(f"\n✍️  COPY TONE: {spec.get('copy_tone')}")
        print(f"📋 COPY STRUCTURE: {spec.get('copy_structure')}")
        print(f"\n🎬 POST TYPE: {spec.get('post_type')}")
        print(f"⏰ BEST TIME: {spec.get('best_posting_time')}")
        print(f"🎯 GOAL: {spec.get('goal')}")
        print(f"😊 MOOD: {spec.get('mood')}")
        print(f"\n✨ BEST FOR: {', '.join(spec.get('best_for', []))}")
        if "recommendation" in spec:
            print(f"\n💡 RECOMMENDATION: {spec['recommendation']}")
        print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
