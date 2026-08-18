#!/usr/bin/env python3
# DIFRESH daily batch renderer, 2026-08-18. House philosophy: Standing Reserve.
import os, json, math, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

DATE   = "2026-08-18"
ASSETS = "/home/user/difresh-assets"
FONTS  = "/home/user/fonts"
OUT    = "/home/user/render"
os.makedirs(OUT, exist_ok=True)
REM = json.load(open('/tmp/claude-0/-home-user/62c82543-9d3f-5a35-b4b1-f5f77f9dc8ae/scratchpad/remaining.json'))

# ---------- colour ----------
def hx(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
def lum(rgb):
    return 0.2126*_lin(rgb[0]) + 0.7152*_lin(rgb[1]) + 0.0722*_lin(rgb[2])
def contrast(a, b):
    la, lb = lum(a), lum(b); hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

# ---------- fonts ----------
_FCACHE = {}
def font(path, size, **axes):
    key = (path, size, tuple(sorted(axes.items())))
    if key in _FCACHE: return _FCACHE[key]
    f = ImageFont.truetype(os.path.join(FONTS, path), size)
    if axes:
        try:
            names = [a['name'].decode() if isinstance(a['name'], bytes) else str(a['name'])
                     for a in f.get_variation_axes()]
            tags = []
            for a in f.get_variation_axes():
                t = a.get('axisTag')
                tags.append(t.decode() if isinstance(t, bytes) else (t if t else None))
            cur = []
            for i, a in enumerate(f.get_variation_axes()):
                tag = tags[i]
                nm = names[i].lower()
                val = None
                for k, v in axes.items():
                    if (tag and tag.lower() == k.lower()) or k.lower() in nm:
                        val = v; break
                cur.append(val if val is not None else a['default'])
            f.set_variation_by_axes(cur)
        except Exception as e:
            print("  ! axis set failed on", path, e)
    _FCACHE[key] = f
    return f

_MEAS = ImageDraw.Draw(Image.new('RGB', (10, 10)))
def ink(text, fnt):
    """Ink bounding box (x0,y0,x1,y1) of text drawn at origin."""
    return _MEAS.textbbox((0, 0), text, font=fnt)
def ink_wh(text, fnt):
    b = ink(text, fnt); return b[2]-b[0], b[3]-b[1]

def draw_ink(dr, xy, text, fnt, fill):
    """Place so the INK top-left lands exactly at xy. Returns ink rect on canvas."""
    b = ink(text, fnt)
    x, y = xy[0] - b[0], xy[1] - b[1]
    dr.text((x, y), text, font=fnt, fill=fill)
    return (xy[0], xy[1], xy[0] + (b[2]-b[0]), xy[1] + (b[3]-b[1]))

def draw_ink_right(dr, xy, text, fnt, fill):
    """xy = ink TOP-RIGHT."""
    w, h = ink_wh(text, fnt)
    return draw_ink(dr, (xy[0]-w, xy[1]), text, fnt, fill)

def draw_ink_center(dr, cx, y, text, fnt, fill):
    w, h = ink_wh(text, fnt)
    return draw_ink(dr, (cx - w/2, y), text, fnt, fill)

def fit_lines(lines, path, maxw, maxcap, axes, lo=20, hi=340):
    """Largest size where every line's ink width <= maxw and cap height <= maxcap."""
    best = lo
    while lo <= hi:
        mid = (lo + hi) // 2
        f = font(path, mid, **axes)
        ws = [ink_wh(l, f)[0] for l in lines]
        cs = [ink_wh(l, f)[1] for l in lines]
        if max(ws) <= maxw and max(cs) <= maxcap:
            best = mid; lo = mid + 1
        else:
            hi = mid - 1
    return font(path, best, **axes), best

def wrap(text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if ink_wh(t, fnt)[0] <= maxw or not cur: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

# ---------- plate ----------
def place(canvas, img_rel, box, ground):
    """Contain-fit img into box (never crop, never stretch). Mat with ground.
       Bleed ground into the image edges at 4-8% so plate and field share one surface.
       Returns the fitted plate rect."""
    src = Image.open(os.path.join(ASSETS, img_rel)).convert('RGB')
    bx0, by0, bx1, by1 = box
    bw, bh = bx1-bx0, by1-by0
    s = min(bw / src.width, bh / src.height)
    nw, nh = max(1, int(round(src.width*s))), max(1, int(round(src.height*s)))
    im = src.resize((nw, nh), Image.LANCZOS)
    px, py = int(bx0 + (bw-nw)/2), int(by0 + (bh-nh)/2)

    # ground bleed: ramp from 8% at the very edge to 0 at BAND px inward
    BAND = 46
    a = np.zeros((nh, nw), np.float32)
    yy = np.arange(nh)[:, None]; xx = np.arange(nw)[None, :]
    d = np.minimum(np.minimum(xx, nw-1-xx), np.minimum(yy, nh-1-yy)).astype(np.float32)
    a = np.clip(1.0 - d / BAND, 0, 1) * 0.08
    arr = np.asarray(im, np.float32)
    g = np.array(ground, np.float32)[None, None, :]
    arr = arr*(1-a[..., None]) + g*a[..., None]
    canvas.paste(Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)), (px, py))
    return (px, py, px+nw, py+nh)

def rects_overlap(a, b):
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])

def grain(im, sigma=1.8):
    a = np.asarray(im, np.float32)
    n = np.random.default_rng(20260818).normal(0, sigma, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))

# ---------- asset scaffold ----------
class Frame:
    def __init__(self, slot, W, H, ground, text, accent):
        self.slot, self.W, self.H = slot, W, H
        self.gnd, self.txt, self.acc = hx(ground), hx(text), hx(accent)
        self.gnd_hex, self.txt_hex, self.acc_hex = ground, text, accent
        self.base = Image.new('RGB', (W, H), self.gnd)   # ground + plates, NO type
        self.plates, self.textboxes = [], []
    def plate(self, img_rel, box):
        r = place(self.base, img_rel, box, self.gnd); self.plates.append(r); return r
    def render_type(self, fn):
        self.canvas = self.base.copy()
        dr = ImageDraw.Draw(self.canvas)
        fn(dr, self)
        return self.canvas
    def reg(self, rect, colour):
        self.textboxes.append((rect, colour))
        return rect

def verify(f, min_margin=64, safe=None):
    """Section 10 mechanics: margins, no type/plate overlap, real-pixel contrast."""
    errs = []
    base = np.asarray(f.base, np.float32)
    for rect, col in f.textboxes:
        x0, y0, x1, y1 = [int(round(v)) for v in rect]
        if x0 < min_margin or y0 < min_margin or x1 > f.W-min_margin or y1 > f.H-min_margin:
            errs.append(f"margin<{min_margin}: {rect}")
        if safe:
            t, b, s = safe
            if y0 < t or y1 > f.H-b or x0 < s or x1 > f.W-s:
                errs.append(f"safe-zone violation: {rect}")
        for p in f.plates:
            if rects_overlap(rect, p):
                errs.append(f"type/plate overlap: text {rect} vs plate {p}")
        # sample ACTUAL rendered pixels behind this text box (type suppressed)
        patch = base[max(0,y0):min(f.H,y1)+1, max(0,x0):min(f.W,x1)+1]
        if patch.size:
            px = patch.reshape(-1, 3)
            crs = [contrast(tuple(p), col) for p in px[::max(1, len(px)//400)]]
            if min(crs) < 4.5:
                errs.append(f"contrast {min(crs):.2f} < 4.5 at {rect}")
    return errs

def finish(f, name):
    im = grain(f.canvas, 1.8)
    p = os.path.join(OUT, name)
    im.save(p, "PNG")
    print(f"  saved {name}  {im.size}")
    return p

WM = "DIFRESH"
results = {}

# =====================================================================
# SLOT 01 - GR - Souvenir toothbrush paste combo tube, bedsheets
# angle: beside the pillow, not in the bathroom
# archetype: portrait plate centred with headline below
# =====================================================================
def slot01():
    f = Frame("01", 1080, 1350, "#BAE6FD", "#0C4A6E", "#EA580C")
    f.plate(REM[26], (190, 104, 890, 804))
    HL = ["ΔΙΠΛΑ ΣΤΟ", "ΜΑΞΙΛΑΡΙ"]
    hf, hs = fit_lines(HL, "SofiaSans[wght].ttf", 620, 200, {"wght": 800})
    bf = font("Ubuntu-Regular.ttf", 20)
    BODY = ["Οδοντόβουρτσα και οδοντόκρεμα σε ένα σωληνάριο.", "Ταξιδιωτικό μέγεθος, 1 ευρώ."]
    wf = font("SofiaSans[wght].ttf", 30, wght=300)
    def paint(dr, f):
        dr.rectangle([96, 856, 252, 864], fill=f.acc)          # accent, single structural bar
        y = 900
        for l in HL:
            r = f.reg(draw_ink(dr, (96, y), l, hf, f.txt), f.txt); y = r[3] + 22
        y += 34
        for l in BODY:
            r = f.reg(draw_ink(dr, (96, y), l, bf, f.txt), f.txt); y = r[3] + 12
        f.reg(draw_ink_right(dr, (984, 1246), WM, wf, f.txt), f.txt)
    f.render_type(paint)
    print("01 headline size", hs, "errs:", verify(f) or "NONE")
    return f, verify(f)

# =====================================================================
# SLOT 02 - EN - Frozen Force, burlap window
# angle: it fits where a bottle will not
# archetype: plate flush left with a type column right
# =====================================================================
def slot02():
    f = Frame("02", 1080, 1350, "#C2410C", "#FFFFFF", "#059669")
    p = f.plate(REM[24], (64, 330, 564, 950))
    HL = ["FITS WHERE", "A BOTTLE", "WILL NOT"]
    hf, hs = fit_lines(HL, "Antonio[wght].ttf", 396, 200, {"wght": 700})
    bf = font("Karla[wght].ttf", 19, wght=400)
    BODY = ["Frozen Force mouthwash.", "20ml, travel size, 2 euro."]
    wf = font("Antonio[wght].ttf", 26, wght=400)
    def paint(dr, f):
        dr.rectangle([24, p[1], 44, p[3]], fill=f.acc)          # accent column, tied to plate height
        f.reg(draw_ink(dr, (620, 210), WM, wf, f.txt), f.txt)
        y = 430
        for l in HL:
            r = f.reg(draw_ink(dr, (620, y), l, hf, f.txt), f.txt); y = r[3] + 20
        y += 40
        for l in BODY:
            r = f.reg(draw_ink(dr, (620, y), l, bf, f.txt), f.txt); y = r[3] + 12
    f.render_type(paint)
    print("02 headline size", hs, "errs:", verify(f) or "NONE")
    return f, verify(f)

# =====================================================================
# SLOT 03 - EN - Atom atomiser, window burlap
# angle: carried all season, refilled once
# archetype: large plate, caption-scale type only, no headline  (image hero)
# =====================================================================
def slot03():
    f = Frame("03", 1080, 1350, "#164E63", "#ECFEFF", "#22D3EE")
    f.plate(REM[20], (140, 96, 940, 1088))
    cf = font("InstrumentSans[wdth,wght].ttf", 21, wght=400, wdth=100)
    wf = font("BricolageGrotesque[opsz,wdth,wght].ttf", 34, wght=700, wdth=100, opsz=24)
    def paint(dr, f):
        y = 1152
        r = f.reg(draw_ink(dr, (140, y), "Atom refillable atomiser.", cf, f.acc), f.acc)
        y = r[3] + 14
        for l in ["Refill it once, carry it all season.", "Travel size, 2 euro."]:
            r = f.reg(draw_ink(dr, (140, y), l, cf, f.txt), f.txt); y = r[3] + 14
        f.reg(draw_ink_right(dr, (940, 1240), WM, wf, f.txt), f.txt)
    f.render_type(paint)
    print("03 errs:", verify(f) or "NONE")
    return f, verify(f)

# =====================================================================
# SLOT 04 - EN - toothbrush paste combo tubes, colour triptych
# angle: the range reads as a colour system
# archetype: triptych of equal plates  (image hero, minimal type)
# =====================================================================
def slot04():
    f = Frame("04", 1080, 1350, "#F2F3F4", "#0F172A", "#059669")
    for i, idx in enumerate((2, 4, 7)):
        top = 110 + i*295
        f.plate(REM[idx], (290, top, 790, top+279))
    HL = ["TEN SHADES,", "TEN FLAVORS"]
    hf, hs = fit_lines(HL, "WixMadeforDisplay[wght].ttf", 560, 200, {"wght": 800}, hi=74)
    bf = font("SchibstedGrotesk[wght].ttf", 19, wght=400)
    wf = font("WixMadeforDisplay[wght].ttf", 24, wght=500)
    def paint(dr, f):
        dr.rectangle([860, 1030, 980, 1150], fill=f.acc)        # accent mass, balances the type
        f.reg(draw_ink(dr, (96, 128), WM, wf, f.txt), f.txt)
        y = 1030
        for l in HL:
            r = f.reg(draw_ink(dr, (96, y), l, hf, f.txt), f.txt); y = r[3] + 12
        y += 20
        r = f.reg(draw_ink(dr, (96, y), "Toothbrush and paste in one tube. Travel size, 1 euro.",
                            bf, f.txt), f.txt)
    f.render_type(paint)
    print("04 headline size", hs, "errs:", verify(f) or "NONE")
    return f, verify(f)

# =====================================================================
# SLOT 05 - EN - vending category, NO PHOTOGRAPH
# angle: the decision takes ten seconds
# archetype: type only
# =====================================================================
def slot05():
    f = Frame("05", 1080, 1350, "#0B0B10", "#F8FAFC", "#3B82F6")
    HL = ["TEN SECONDS", "IS THE WHOLE", "DECISION"]
    hf, hs = fit_lines(HL, "Gabarito[wght].ttf", 620, 200, {"wght": 700})
    bf = font("Mulish[wght].ttf", 20, wght=400)
    wf = font("Gabarito[wght].ttf", 42, wght=300)
    def paint(dr, f):
        y = 392
        for l in HL:
            r = f.reg(draw_ink(dr, (96, y), l, hf, f.txt), f.txt); y = r[3] + 18
        y += 68
        for l in ["DIFRESH vending.", "Travel size hygiene and personal care products."]:
            r = f.reg(draw_ink(dr, (96, y), l, bf, f.txt), f.txt); y = r[3] + 12
        y += 30
        f.reg(draw_ink(dr, (96, y), "No queue. No conversation.", bf, f.acc), f.acc)
        f.reg(draw_ink_right(dr, (984, 1190), WM, wf, f.txt), f.txt)
    f.render_type(paint)
    print("05 headline size", hs, "errs:", verify(f) or "NONE")
    return f, verify(f)

# =====================================================================
# SLOT 06 - GR - Souvenir custom branded oral care line, books and candle
# angle: the souvenir that gets used up
# archetype: plate flush right with a type column left
# =====================================================================
def slot06():
    f = Frame("06", 1080, 1350, "#3F3F46", "#FAFAFA", "#EC4899")
    f.plate(REM[27], (700, 300, 1016, 866))
    HL = ["ΤΟ", "ΕΝΘΥΜΙΟ", "ΠΟΥ", "ΤΕΛΕΙΩΝΕΙ"]
    hf, hs = fit_lines(HL, "Vollkorn[wght].ttf", 540, 200, {"wght": 700})
    bf = font("SourceSans3[wght].ttf", 19, wght=400)
    wf = font("Vollkorn[wght].ttf", 28, wght=500)
    BODY = ["Σειρά σουβενίρ με τη δική σας επωνυμία.",
            "Οδοντόβουρτσα και οδοντόκρεμα σε ένα",
            "σωληνάριο, ταξιδιωτικό μέγεθος, 2 ευρώ."]
    def paint(dr, f):
        dr.rectangle([96, 250, 106, 330], fill=f.acc)           # accent, vertical mark
        y = 386
        for l in HL:
            r = f.reg(draw_ink(dr, (96, y), l, hf, f.txt), f.txt); y = r[3] + 18
        y += 46
        for l in BODY:
            r = f.reg(draw_ink(dr, (96, y), l, bf, f.txt), f.txt); y = r[3] + 12
        f.reg(draw_ink(dr, (96, 1232), WM, wf, f.txt), f.txt)
    f.render_type(paint)
    print("06 headline size", hs, "errs:", verify(f) or "NONE")
    return f, verify(f)

# =====================================================================
# STORY - GR - Frozen Force
# archetype: big centred statement on flat colour   hook: product spotlight
# safe zones: 250 top, 300 bottom, 60 sides
# =====================================================================
def story():
    f = Frame("story", 1080, 1920, "#4338CA", "#FFFFFF", "#7C3AED")
    # accent as a structural mass, set BEHIND the plate and offset, so the tonal
    # shift reads as a deliberate act rather than a hairline that vanishes.
    ImageDraw.Draw(f.base).rectangle([272, 852, 712, 1398], fill=f.acc)
    f.plate(REM[25], (320, 900, 760, 1446))
    HL = ["ΧΩΡΑΕΙ", "ΠΑΝΤΟΥ"]
    hf, hs = fit_lines(HL, "Literata[opsz,wght].ttf", 620, 200, {"wght": 700, "opsz": 72})
    bf = font("AdventPro[wdth,wght].ttf", 22, wght=500, wdth=100)
    wf = font("Literata[opsz,wght].ttf", 30, wght=400, opsz=14)
    def paint(dr, f):
        f.reg(draw_ink_center(dr, 540, 300, WM, wf, f.txt), f.txt)
        y = 430
        for l in HL:
            r = f.reg(draw_ink_center(dr, 540, y, l, hf, f.txt), f.txt); y = r[3] + 24
        y = 1510
        for l in ["Frozen Force στοματικό διάλυμα.", "20ml, ταξιδιωτικό μέγεθος, 2 ευρώ."]:
            r = f.reg(draw_ink_center(dr, 540, y, l, bf, f.txt), f.txt); y = r[3] + 12
    f.render_type(paint)
    e = verify(f, safe=(250, 300, 60))
    print("story headline size", hs, "errs:", e or "NONE")
    return f, e

BUILD = [("01", slot01), ("02", slot02), ("03", slot03), ("04", slot04),
         ("05", slot05), ("06", slot06), ("story", story)]

if __name__ == "__main__":
    allerr = {}
    for name, fn in BUILD:
        print(f"--- slot {name} ---")
        f, errs = fn()
        allerr[name] = errs
        fname = f"difresh_{DATE}_{name}.png" if name != "story" else f"difresh_{DATE}_story.png"
        finish(f, fname)
    print("\n===== VERIFY SUMMARY =====")
    bad = {k: v for k, v in allerr.items() if v}
    print("ALL CLEAN" if not bad else json.dumps(bad, indent=1))
