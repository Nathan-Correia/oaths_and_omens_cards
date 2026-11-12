"""Make fonts/minicaps_kerned.ttf: Capitalis with tighter spacing after r / R.

Capitalis spaces r (and R) so the leg's foot never comes near the next letter,
which leaves a big wedge of space above it ("HER A", "AR ES"). For every pair
whose closest point is down at the foot, this sets the kern so the feet sit
FOOT_GAP units apart. Round letters, j, and pairs the designer already pulled
in (r+o, r+v, ...) are left alone.

Usage (from the repo root): python fonts/patch_capitalis.py [FOOT_GAP]
"""
import sys
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import otTables
from fontTools.pens.basePen import BasePen

SRC, DST = "fonts/minicaps.ttf", "fonts/minicaps_kerned.ttf"
FOOT_GAP = int(sys.argv[1]) if len(sys.argv) > 1 else 25   # font units (1000 per em)
FOOT_ZONE = 120          # "closest point is at the foot" = below this height
LEFT = ["r", "R"]
# Letters that start with a stem or a foot (round letters and j are left to the designer).
RIGHT = "abdefhiklmnprxz"

f = TTFont(SRC)
gs = f.getGlyphSet()
hmtx = f["hmtx"]
YS = range(5, 690, 10)


class Flatten(BasePen):
    """Turns a glyph outline into polygons so it can be scanned row by row."""
    def __init__(self, glyphset):
        super().__init__(glyphset)
        self.polys, self.cur = [], []
    def _moveTo(self, p): self.cur = [p]
    def _lineTo(self, p): self.cur.append(p)
    def _qCurveToOne(self, p1, p2):
        p0 = self.cur[-1]
        for i in range(1, 9):
            t = i / 8
            self.cur.append(((1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0],
                             (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]))
    def _curveToOne(self, p1, p2, p3):
        p0 = self.cur[-1]
        for i in range(1, 9):
            t = i / 8; u = 1 - t
            self.cur.append((u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0],
                             u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]))
    def _closePath(self):
        if self.cur: self.polys.append(self.cur)
        self.cur = []
    _endPath = _closePath


_profiles = {}
def profile(g):
    """Leftmost / rightmost ink x at each sampled height (None where there is no ink)."""
    if g not in _profiles:
        pen = Flatten(gs); gs[g].draw(pen)
        out = {}
        for y in YS:
            xs = [x0 + (y - y0) * (x1 - x0) / (y1 - y0)
                  for poly in pen.polys
                  for (x0, y0), (x1, y1) in zip(poly, poly[1:] + poly[:1])
                  if (y0 <= y < y1) or (y1 <= y < y0)]
            out[y] = (min(xs), max(xs)) if xs else None
        _profiles[g] = out
    return _profiles[g]


def closest(a, b, kern):
    """(gap, height) of the narrowest point between glyph a and glyph b."""
    pa, pb = profile(a), profile(b)
    return min((hmtx[a][0] + kern + pb[y][0] - pa[y][1], y)
               for y in YS if pa[y] and pb[y])


# Existing kerning: one PairPos (format 1) lookup.
sub = f["GPOS"].table.LookupList.Lookup[0].SubTable[0]
assert sub.Format == 1 and len(f["GPOS"].table.LookupList.Lookup[0].SubTable) == 1
order = {g: i for i, g in enumerate(f.getGlyphOrder())}
pairset = {g: sub.PairSet[i] for i, g in enumerate(sub.Coverage.glyphs)}

changes = []
for a in LEFT:
    ps = pairset[a]
    recs = {r.SecondGlyph: r for r in ps.PairValueRecord}
    for b in RIGHT:
        old = recs[b].Value1.XAdvance if b in recs else 0
        gap, y = closest(a, b, old)
        if y >= FOOT_ZONE or old < 0:
            continue                      # not foot-limited, or already pulled in: leave it
        new = old - round(gap - FOOT_GAP)
        if new == old:
            continue
        if b in recs:
            recs[b].Value1.XAdvance = new
        else:
            r = otTables.PairValueRecord()
            r.SecondGlyph = b
            r.Value1 = otTables.ValueRecord(); r.Value1.XAdvance = new
            r.Value2 = None
            recs[b] = r
        changes.append((a + b, old, new))
    ps.PairValueRecord = sorted(recs.values(), key=lambda r: order[r.SecondGlyph])
    ps.PairValueCount = len(ps.PairValueRecord)

# Rename so the patched copy is never confused with the original (OFL convention).
for rec in f["name"].names:
    if rec.nameID in (1, 3, 4, 6, 16):
        s = rec.toUnicode()
        rec.string = s.replace("Capitalis Minimalis", "Capitalis Minimalis Kerned") \
                      .replace("CapitalisMinimalis", "CapitalisMinimalisKerned") if "Minimalis" in s \
                     else s + (" Kerned" if rec.nameID != 6 else "-Kerned")
f.save(DST)

print(f"foot gap {FOOT_GAP} -> {DST}")
for pair, old, new in changes:
    print(f"  {pair}: {old:+} -> {new:+}")
