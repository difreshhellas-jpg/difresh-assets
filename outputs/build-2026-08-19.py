#!/usr/bin/env python3
"""DIFRESH 2026-08-19 batch. House philosophy: Standing Reserve.
6 posts 1080x1350 (4 EN, 2 GR) + 1 story 1080x1920. Nothing cropped, nothing stretched."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from fontTools.ttLib import TTFont as FTFont
import numpy as np

ROOT, FONTS, OUT = "/home/user/difresh-assets", "/home/user/fonts", "/home/user/out-2026-08-19"
DATE = "2026-08-19"
os.makedirs(OUT, exist_ok=True)
WM = "DIFRESH"

# ------------------------------------------------------------------ font plumbing
_ax = {}
def axis_tags(p):
    if p not in _ax:
        f = FTFont(p)
        try: _ax[p] = [(a.axisTag, a.defaultValue) for a in f["fvar"].axes]
        except KeyError: _ax[p] = None
    return _ax[p]

def load(name, size, **axes):
    path = os.path.join(FONTS, name)
    f = ImageFont.truetype(path, size)
    tags = axis_tags(path)
    if tags:                                   # match axes by TAG, never by position
        f.set_variation_by_axes([axes.get(t, d) for (t, d) in tags])
    return f

_p = ImageDraw.Draw(Image.new("RGB", (8, 8)))
def ink(t, f):
    b = _p.textbbox((0, 0), t, font=f)
    return (0, 0, 0, 0) if (b[2] <= b[0] or b[3] <= b[1]) else b

def fit(lines, name, max_w, max_cap, lo=8, hi=460, **axes):
    """Largest size where every line's INK width <= max_w and ink height <= max_cap."""
    best = lo
    while lo <= hi:
        mid = (lo + hi) // 2
        f = load(name, mid, **axes)
        bs = [ink(l, f) for l in lines]
        if max(b[2] - b[0] for b in bs) <= max_w and max(b[3] - b[1] for b in bs) <= max_cap:
            best, lo = mid, mid + 1
        else:
            hi = mid - 1
    return best

def wrap(text, name, size, max_w, **axes):
    f = load(name, size, **axes)
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        b = ink(t, f)
        if b[2] - b[0] <= max_w or not cur:
            cur = t
        else:
            out.append(cur); cur = w
    if cur: out.append(cur)
    return out

# ------------------------------------------------------------------ colour utils
def hx(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def lum(c):
    def f(v):
        v /= 255.0
        return v/12.92 if v <= 0.04045 else ((v+0.055)/1.055)**2.4
    return 0.2126*f(c[0]) + 0.7152*f(c[1]) + 0.0722*f(c[2])
def contrast(a, b):
    la, lb = lum(a), lum(b); hi, lo = max(la, lb), min(la, lb)
    return (hi+0.05)/(lo+0.05)

def grain(img, sigma=1.8, amp=3.6, seed=11):
    rng = np.random.default_rng(seed)
    n = rng.normal(0, 1, (img.height, img.width)).astype("float32")
    n = (n - n.min())/(n.max()-n.min()+1e-9)*255
    n = np.asarray(Image.fromarray(n.astype("uint8")).filter(ImageFilter.GaussianBlur(sigma)),
                   dtype="float32")
    n = (n - n.mean())/(n.std()+1e-6)*amp
    return Image.fromarray(np.clip(np.asarray(img, "float32") + n[..., None], 0, 255).astype("uint8"))

def hits(a, b):
    return b is not None and not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])

# ------------------------------------------------------------------ frame
REPORT = []
class Frame:
    def __init__(self, w, h, ground):
        self.w, self.h, self.ground = w, h, hx(ground)
        self.img = Image.new("RGB", (w, h), self.ground)
        self.d = ImageDraw.Draw(self.img)
        self.tb, self.plate, self.bg = [], None, None

    def place(self, rel, box, bleed=0.04):
        """Contain fit at native aspect ratio. Never cropped. Ground bleeds into edges."""
        x0, y0, x1, y1 = box; bw, bh = x1-x0, y1-y0
        im = Image.open(os.path.join(ROOT, rel)).convert("RGB")
        s = min(bw/im.width, bh/im.height)
        nw, nh = int(round(im.width*s)), int(round(im.height*s))
        im = im.resize((nw, nh), Image.LANCZOS)
        band = max(3, int(round(min(nw, nh)*bleed)))
        m = Image.new("L", (nw, nh), 0); md = ImageDraw.Draw(m)
        for i in range(band):
            md.rectangle([i, i, nw-1-i, nh-1-i], outline=int(round(255*(1-i/band)**2.6)))
        m = m.filter(ImageFilter.GaussianBlur(band*0.12))
        im = Image.composite(Image.new("RGB", (nw, nh), self.ground), im, m)
        px, py = x0+(bw-nw)//2, y0+(bh-nh)//2
        self.img.paste(im, (px, py))
        self.plate = (px, py, px+nw, py+nh)
        return self.plate

    def rect(self, box, color): self.d.rectangle(box, fill=hx(color))
    def snap(self): self.bg = self.img.copy()

    def block(self, lines, name, size, color, x, y, align="left", lead=1.34, label="", **axes):
        """Draw a block positioned by INK bbox. Returns (top, bottom) of the ink."""
        f = load(name, size, **axes); col = hx(color)
        greek = any(0x370 <= ord(c) <= 0x3FF for l in lines for c in l)
        ref = ink("ΗΞΗ" if greek else "HXH", f)
        step = int(round((ref[3]-ref[1])*lead))
        cy, top, bot = y, y, y
        for ln in lines:
            b = ink(ln, f); w = b[2]-b[0]
            ox = x-b[0] if align == "left" else (x-w/2-b[0] if align == "center" else x-w-b[0])
            self.d.text((ox, cy-b[1]), ln, font=f, fill=col)
            self.tb.append((ox+b[0], cy, ox+b[0]+w, cy+(b[3]-b[1]), col, label or ln[:24]))
            bot = cy+(b[3]-b[1]); cy += step
        return top, bot

def finish(fr, fname, story=False, seed=11):
    bg = grain(fr.bg, 1.8, 3.6, seed)
    out = grain(fr.img, 1.8, 3.6, seed)
    arr = np.asarray(bg); probs = []; worst = 99.0
    for (x0, y0, x1, y1, col, lab) in fr.tb:
        X0, Y0 = max(0, int(x0)-2), max(0, int(y0)-2)
        X1, Y1 = min(fr.w, int(x1)+2), min(fr.h, int(y1)+2)
        if X1 <= X0 or Y1 <= Y0: continue
        patch = arr[Y0:Y1, X0:X1].reshape(-1, 3)
        step = max(1, len(patch)//1200)
        c = min(contrast(col, tuple(int(v) for v in px)) for px in patch[::step])
        worst = min(worst, c)
        if c < 4.5: probs.append(f"CONTRAST {lab!r} {c:.2f}")
        if x0 < 64 or y0 < 64 or x1 > fr.w-64 or y1 > fr.h-64:
            probs.append(f"MARGIN {lab!r} ({x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f})")
        if story and (y0 < 250 or y1 > fr.h-300 or x0 < 60 or x1 > fr.w-60):
            probs.append(f"SAFEZONE {lab!r}")
        if hits((x0, y0, x1, y1), fr.plate): probs.append(f"OVERLAP-PLATE {lab!r}")
    out.save(os.path.join(OUT, fname))
    REPORT.append((fname, out.size, worst, probs))

# ==================================================================== 01  EN
# Givenchy voice. Frozen Force. Large plate, caption scale type only, no headline.
f = Frame(1080, 1350, "#E2E8F0")
f.place("leonardo-generated/2026-08-18/frozen-force.jpg", (96, 96, 984, 1010))
f.rect((860, 1064, 1080, 1204), "#0369A1")                 # accent plane, bleeds off right edge
f.snap()
f.block(["Frozen Force mouthwash. 20ml, travel size."], "Chivo[wght].ttf", 21,
        "#020617", 96, 1076, wght=600, label="s01 lead")
f.block(["Cold enough to notice.", "Small enough to forget you packed it."],
        "Chivo[wght].ttf", 21, "#020617", 96, 1130, lead=1.62, wght=400, label="s01 body")
f.block([WM], "Questrial-Regular.ttf", 23, "#020617", 984, 1244, align="right", label="s01 wm")
finish(f, f"difresh_{DATE}_01.png")

# ==================================================================== 02  GR
# Hermes voice. Toothbrush paste combo. Portrait plate centred, headline below.
f = Frame(1080, 1350, "#312E81")
f.place("leonardo-generated/2026-08-18/toothbrush-combo.jpg", (260, 172, 820, 688))
f.rect((812, 1180, 1080, 1350), "#F97316")                 # accent plane, bottom right corner
f.snap()
f.block([WM], "Piazzolla[opsz,wght].ttf", 31, "#F8FAFC", 96, 92, wght=600, opsz=30, label="s02 wm")
hl = ["ΚΑΝΕΙΣ ΔΕΝ", "ΖΗΤΑΕΙ", "ΟΔΟΝΤΟΒΟΥΡΤΣΑ."]
s = fit(hl, "Piazzolla[opsz,wght].ttf", 620, 118, wght=700, opsz=30)
_, bot = f.block(hl, "Piazzolla[opsz,wght].ttf", s, "#F8FAFC", 96, 822,
                 lead=1.30, wght=700, opsz=30, label="s02 head")
f.block(["Οδοντόβουρτσα και οδοντόκρεμα στον ίδιο σωλήνα.",
         "Μέγεθος ταξιδιού. Δέκα αποχρώσεις και γεύσεις."],
        "SourceSans3[wght].ttf", 20, "#F8FAFC", 96, bot+62, lead=1.72, wght=400, label="s02 body")
finish(f, f"difresh_{DATE}_02.png")

# ==================================================================== 03  EN
# Nike voice. Atom atomiser. Plate high, long void beneath.
f = Frame(1080, 1350, "#37414F")
f.place("leonardo-generated/2026-08-18/atom.jpg", (300, 150, 780, 910))
f.rect((0, 0, 296, 430), "#22C55E")                        # accent mass, top left corner
f.snap()
f.block([WM], "RedHatText[wght].ttf", 20, "#F8FAFC", 984, 92, align="right", wght=500, label="s03 wm")
hl = ["USED,", "NOT SAVED."]
s = fit(hl, "ArchivoBlack-Regular.ttf", 620, 92)
_, bot = f.block(hl, "ArchivoBlack-Regular.ttf", s, "#F8FAFC", 96, 1004, lead=1.30, label="s03 head")
f.block(["The Atom refillable spray atomiser. Travel size, 2 euro.",
         "Fill it with what you already own."],
        "RedHatText[wght].ttf", 20, "#F8FAFC", 96, bot+48, lead=1.62, wght=400, label="s03 body")
finish(f, f"difresh_{DATE}_03.png")

# ==================================================================== 04  GR
# Valentino voice. Souvenir custom branded line. Plate flush right, type column left.
f = Frame(1080, 1350, "#831843")
f.place("souvenir/souvenir-green-kraftpaper.jpg", (560, 150, 1016, 1200))
f.snap()
hl = ["ΔΕΝ ΤΟ", "ΠΑΙΡΝΕΙΣ", "ΓΙΑ ΣΕΝΑ."]
s = fit(hl, "AdventPro[wdth,wght].ttf", 404, 112, wght=700, wdth=100)
_, bot = f.block(hl, "AdventPro[wdth,wght].ttf", s, "#FFFFFF", 96, 300,
                 lead=1.30, wght=700, wdth=100, label="s04 head")
body = wrap("Οδοντόβουρτσα και οδοντόκρεμα με το δικό σου σήμα. Μέγεθος ταξιδιού, "
            "2 ευρώ το τεμάχιο.", "Ubuntu-Regular.ttf", 20, 404)
f.block(body, "Ubuntu-Regular.ttf", 20, "#FFFFFF", 96, bot+64, lead=1.72, label="s04 body")
f.block([WM], "AdventPro[wdth,wght].ttf", 27, "#FFFFFF", 96, 1204, wght=600, wdth=100, label="s04 wm")
finish(f, f"difresh_{DATE}_04.png")

# ==================================================================== 05  EN
# Dior voice. Souvenir, tropical. Square plate centred, headline above.
f = Frame(1080, 1350, "#09090B")
hl = ["YOU SHOWERED", "AT EIGHT.", "IT IS NOW TWO."]
s = fit(hl, "DMSerifDisplay-Regular.ttf", 620, 84)
tmp = Frame(1080, 1350, "#09090B")                          # measure only
_, hb = tmp.block(hl, "DMSerifDisplay-Regular.ttf", s, "#FAFAFA", 540, 112, align="center", lead=1.30)
f.place("souvenir/souvenir-green-tropical.jpg", (180, 430, 900, 1130))
f.snap()
f.block(hl, "DMSerifDisplay-Regular.ttf", s, "#FAFAFA", 540, 112, align="center",
        lead=1.30, label="s05 head")
f.block(["Travel size oral care, for the eighteen hours after the shower."],
        "AlbertSans[wght].ttf", 20, "#EC4899", 540, 1182, align="center", wght=500, label="s05 body")
f.block([WM], "DMSerifDisplay-Regular.ttf", 25, "#FAFAFA", 540, 1242, align="center", label="s05 wm")
finish(f, f"difresh_{DATE}_05.png")

# ==================================================================== 06  EN
# Louis Vuitton voice, the line as a collection. Type only, no photograph.
f = Frame(1080, 1350, "#F0F8F6")
f.rect((0, 1140, 1080, 1350), "#059669")                   # accent foot, full width
f.snap()
f.block([WM], "LeagueSpartan[wght].ttf", 46, "#0F172A", 96, 96, wght=700, label="s06 wm")
hl = ["FIVE THINGS.", "FIVE PRICES."]
s = fit(hl, "LeagueSpartan[wght].ttf", 620, 104, wght=800)
f.block(hl, "LeagueSpartan[wght].ttf", s, "#0F172A", 96, 246, lead=1.32, wght=800, label="s06 head")
rows = [("Toothbrush paste combo tube", "1 euro"),
        ("Souvenir custom branded tube", "2 euro"),
        ("Frozen Force mouthwash, 20ml", "2 euro"),
        ("Atom refillable atomiser", "2 euro"),
        ("Durex condoms", "3 euro")]
y = 618
for name, price in rows:
    f.block([name], "Urbanist[wght].ttf", 21, "#0F172A", 96, y, wght=500, label=f"s06 {name[:14]}")
    f.block([price], "Urbanist[wght].ttf", 21, "#0F172A", 984, y, align="right", wght=700,
            label=f"s06 price {price}")
    y += 62
f.block(["All travel size."], "Urbanist[wght].ttf", 21, "#0F172A", 96, y+34, wght=500, label="s06 foot")
finish(f, f"difresh_{DATE}_06.png")

# ==================================================================== STORY  EN
# Chanel voice. Text only manifesto, use case moment. No photograph.
f = Frame(1080, 1920, "#FAF5FF")
f.snap()
hl = ["SIX", "IN THE", "MORNING."]
s = fit(hl, "Marcellus-Regular.ttf", 620, 180)
_, bot = f.block(hl, "Marcellus-Regular.ttf", s, "#0F172A", 540, 600, align="center",
                 lead=1.28, label="story head")
f.block(["On the deck, before anyone is awake.", "Travel size oral care."],
        "Karla[wght].ttf", 22, "#0F172A", 540, bot+118, align="center", lead=1.62,
        wght=400, label="story body")
f.block([WM], "Marcellus-Regular.ttf", 26, "#0F172A", 96, 1498, label="story wm")
finish(f, f"difresh_{DATE}_story.png", story=True)

# ==================================================================== report
print(f"{'file':34} {'size':11} {'min contrast':>12}  issues")
ok = True
for fn, sz, w, probs in REPORT:
    print(f"{fn:34} {str(sz):11} {w:11.2f}:1  {'; '.join(probs) if probs else 'clean'}")
    if probs: ok = False
print("\nALL CHECKS PASS" if ok else "\nFAILURES PRESENT")
