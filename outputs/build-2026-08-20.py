#!/usr/bin/env python3
"""DIFRESH 2026-08-19 batch. House philosophy: Standing Reserve.
6 posts 1080x1350 (4 EN, 2 GR) + 1 story 1080x1920. Nothing cropped, nothing stretched."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from fontTools.ttLib import TTFont as FTFont
import numpy as np

ROOT, FONTS, OUT = "/home/user/difresh-assets", "/home/user/fonts", "/home/user/out-2026-08-20"
DATE = "2026-08-20"
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


# ==================================================================== 01  GR
# Durex. Plate flush right, type column left. Amber field, deep indigo band off the top edge.
# Angle: it travels in the bag with everything else, it is not a drawer object.
f = Frame(1080, 1350, "#F97316")
f.rect((0, 0, 1080, 124), "#171939")                       # accent band, bleeds off the top edge
f.place("leonardo-generated/2026-08-19/durex.jpg", (560, 240, 984, 1120))
f.snap()
hl = ["ΣΤΗΝ", "ΤΣΑΝΤΑ,", "ΟΧΙ ΣΤΟ", "ΣΥΡΤΑΡΙ."]
s = fit(hl, "GFSDidot.ttf", 392, 116)
_, bot = f.block(hl, "GFSDidot.ttf", s, "#09090B", 96, 300, lead=1.34, label="s01 head")
f.block(["Durex, ταξιδιωτικό μέγεθος.", "3 ευρώ.", "Ταξιδεύει με τα υπόλοιπα."],
        "Lato-Regular.ttf", 20, "#09090B", 96, bot + 74, lead=1.72, label="s01 body")
f.block([WM], "Lato-Black.ttf", 22, "#09090B", 96, 1232, label="s01 wm")
finish(f, f"difresh_{DATE}_01.png", seed=3)

# ==================================================================== 02  EN
# Toothbrush paste combo. Square plate centred, headline above. Deep indigo field.
# Angle: the day the routine happens somewhere that is not your bathroom.
f = Frame(1080, 1350, "#171939")
f.rect((770, 1206, 1080, 1350), "#22C55E")                 # accent, bottom right corner
f.place("leonardo-generated/2026-08-19/toothbrush-combo.jpg", (270, 470, 810, 1010))
f.snap()
hl = ["BRUSH SOMEWHERE", "THAT ISN'T HOME."]
s = fit(hl, "BigShoulders.ttf", 620, 176, wght=800)
f.block(hl, "BigShoulders.ttf", s, "#F8FAFC", 96, 158, lead=1.16, wght=800, label="s02 head")
f.block(["Toothbrush and paste in one combo tube. Travel size.",
         "Ten shades and flavors, 1 euro."],
        "HankenGrotesk.ttf", 20, "#F8FAFC", 96, 1082, lead=1.70, wght=400, label="s02 body")
f.block([WM], "HankenGrotesk.ttf", 26, "#F8FAFC", 96, 1252, wght=600, label="s02 wm")
finish(f, f"difresh_{DATE}_02.png", seed=17)

# ==================================================================== 03  EN
# Atom atomiser. Plate high, long void beneath. Image is the hero, type is minimal.
# Angle: built for the part of the trip that has no mirror in it.
f = Frame(1080, 1350, "#E9EEF5")
f.rect((0, 880, 132, 1350), "#DC2626")                     # accent, bleeds off the left edge
f.place("leonardo-generated/2026-08-19/atom.jpg", (140, 96, 940, 800))
f.snap()
hl = ["NO MIRROR", "REQUIRED."]
s = fit(hl, "Newsreader.ttf", 600, 128, wght=600, opsz=36)
_, bot = f.block(hl, "Newsreader.ttf", s, "#09090B", 212, 986,
                 lead=1.28, wght=600, opsz=36, label="s03 head")
f.block(["Atom refillable spray atomiser. Travel size, 2 euro."],
        "FamiljenGrotesk.ttf", 19, "#09090B", 212, bot + 56, wght=400, label="s03 body")
f.block([WM], "FamiljenGrotesk.ttf", 34, "#09090B", 984, 1246, align="right",
        wght=500, label="s03 wm")
finish(f, f"difresh_{DATE}_03.png", seed=41)

# ==================================================================== 04  EN
# Souvenir custom branded line. Portrait plate centred, headline below. Mid slate field.
# Angle: a souvenir that starts working the same evening instead of waiting on a shelf.
f = Frame(1080, 1350, "#94A3B8")
f.rect((996, 96, 1080, 720), "#134E4A")                    # accent, bleeds off the right edge
f.place("souvenir/souvenir-green-dashboard-dusk-02.jpg", (340, 110, 740, 780))
f.snap()
f.block([WM], "Asap.ttf", 24, "#09090B", 96, 132, wght=600, wdth=100, label="s04 wm")
hl = ["MOST SOUVENIRS", "SIT ON A SHELF."]
s = fit(hl, "Anybody.ttf", 616, 96, wght=700, wdth=125)
_, bot = f.block(hl, "Anybody.ttf", s, "#09090B", 96, 892, lead=1.34,
                 wght=700, wdth=125, label="s04 head")
f.block(["The souvenir line. Custom branded toothbrush paste combo tubes.",
         "Travel size, 2 euro."],
        "Asap.ttf", 20, "#09090B", 96, bot + 62, lead=1.70, wght=400, wdth=100,
        label="s04 body")
finish(f, f"difresh_{DATE}_04.png", seed=59)

# ==================================================================== 05  GR
# Type only, no photograph. Two lines of overheard speech, split across a cyan field
# and a white plane that bleeds off the bottom edge.
f = Frame(1080, 1350, "#22D3EE")
f.rect((0, 772, 1080, 1350), "#F8FAFC")                    # accent plane, bleeds off the bottom
f.snap()
f.block([WM], "Cousine-Bold.ttf", 21, "#09090B", 984, 118, align="right", label="s05 wm")
q = ["«Ξέχασες", "τίποτα;»"]
s = fit(q, "RobotoSlab.ttf", 600, 132, wght=700)
f.block(q, "RobotoSlab.ttf", s, "#09090B", 96, 356, lead=1.30, wght=700, label="s05 q")
a = ["«Όχι.", "Το πήρα κάτω.»"]
s2 = fit(a, "RobotoSlab.ttf", 600, 118, wght=400)
_, bot = f.block(a, "RobotoSlab.ttf", s2, "#09090B", 96, 900, lead=1.30, wght=400,
                 label="s05 a")
f.block(["Είδη υγιεινής και προσωπικής φροντίδας", "σε ταξιδιωτικό μέγεθος."],
        "Cousine-Regular.ttf", 19, "#09090B", 96, bot + 78, lead=1.66, label="s05 body")
finish(f, f"difresh_{DATE}_05.png", seed=73)

# ==================================================================== 06  EN
# Frozen Force. Large plate, caption scale type only, no headline at all.
# Angle: 20ml is not a sample of a bigger bottle, there is no bigger bottle.
f = Frame(1080, 1350, "#E1F2ED")
f.rect((0, 1232, 432, 1350), "#38BDF8")                    # accent, bottom left corner
f.place("leonardo-generated/2026-08-19/frozen-force.jpg", (96, 96, 984, 1080))
f.snap()
f.block(["Frozen Force mouthwash. 20ml, travel size, 2 euro."],
        "ZillaSlab-Bold.ttf", 22, "#134E4A", 96, 1146, label="s06 lead")
f.block(["Not a trial size of something bigger. There is no bigger."],
        "Mulish.ttf", 20, "#134E4A", 96, 1190, wght=400, label="s06 body")
f.block([WM], "ZillaSlab-Bold.ttf", 30, "#134E4A", 984, 1252, align="right", label="s06 wm")
finish(f, f"difresh_{DATE}_06.png", seed=97)

# ==================================================================== STORY  GR
# Atom on travertine. Plate in negative space, deep slate void, amber block off the right edge.
f = Frame(1080, 1920, "#272F42")
f.rect((900, 432, 1080, 700), "#D97706")                   # accent, a cropped companion tile off the right edge
f.place("atom/editorial/atom-black-travertine.jpg", (300, 430, 780, 1030))
f.snap()
hl = ["ΑΠΟ ΤΗΝ ΑΘΗΝΑ", "ΩΣ ΤΟ ΝΗΣΙ"]
s = fit(hl, "GFSNeohellenic.ttf", 872, 166)
_, bot = f.block(hl, "GFSNeohellenic.ttf", s, "#F8FAFC", 96, 1180, lead=1.34, label="st head")
f.block(["Atom, επαναγεμιζόμενο σπρέι.", "Ταξιδιωτικό μέγεθος, 2 ευρώ."],
        "NotoSansDisplay.ttf", 21, "#F8FAFC", 96, bot + 76, lead=1.70,
        wght=400, wdth=100, label="st body")
f.block([WM], "NotoSansDisplay.ttf", 25, "#F8FAFC", 96, 268,
        wght=300, wdth=112, label="st wm")
finish(f, f"difresh_{DATE}_story.png", story=True, seed=131)

# ==================================================================== report
print("=" * 74)
for fn, size, worst, probs in REPORT:
    print(f"{fn:34} {size[0]}x{size[1]}  min-contrast {worst:5.2f}  " +
          ("OK" if not probs else "FAIL"))
    for p in probs: print("      ", p)
