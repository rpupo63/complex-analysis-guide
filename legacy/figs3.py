import json, cmath, math
C1, C3, C3 = 'var(--accent)', 'var(--res-ink)', 'var(--asm-ink)'
FIG = {}

def path(pts, tr, color, w=1.6, dash=None):
    d = 'M' + ' L'.join(f'{tr(z)[0]:.1f},{tr(z)[1]:.1f}' for z in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}"{da}/>'

def fig(svg, cap):
    return f'<figure>{svg}<figcaption>{cap}</figcaption></figure>'

# ---------- plate: half-plane data vs disk data ----------
s = []
# half-plane panel
s.append('<rect x="10" y="20" width="150" height="70" fill="var(--def-bg)"/>')
s.append(f'<line x1="10" y1="90" x2="85" y2="90" stroke="{C3}" stroke-width="3"/>')
s.append(f'<line x1="85" y1="90" x2="160" y2="90" stroke="{C1}" stroke-width="3"/>')
s.append('<text x="85" y="55" text-anchor="middle" font-size="14" font-style="italic" fill="currentColor">ℍ</text>')
s.append(f'<text x="45" y="108" text-anchor="middle" font-size="12" fill="{C3}">1</text><text x="125" y="108" text-anchor="middle" font-size="12" fill="{C1}">0</text>')
s.append('<text x="85" y="104" text-anchor="middle" font-size="11" fill="currentColor">0</text>')
s.append('<path d="M172 55 L208 55" stroke="currentColor" stroke-width="1.2"/><path d="M202 50 L208 55 L202 60" fill="none" stroke="currentColor" stroke-width="1.2"/>')
s.append('<text x="190" y="47" text-anchor="middle" font-size="11" font-style="italic" fill="currentColor">C</text>')
cx, cy, R = 265, 58, 42
s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="var(--def-bg)"/>')
s.append(f'<path d="M{cx-R} {cy} A {R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="{C3}" stroke-width="3"/>')
s.append(f'<path d="M{cx-R} {cy} A {R} {R} 0 0 0 {cx+R} {cy}" fill="none" stroke="{C1}" stroke-width="3"/>')
s.append(f'<text x="{cx}" y="{cy-R-5}" text-anchor="middle" font-size="12" fill="{C3}">1</text><text x="{cx}" y="{cy+R+14}" text-anchor="middle" font-size="12" fill="{C1}">0</text>')
FIG['plate'] = fig(f'<svg viewBox="0 0 320 118" width="320" role="img" aria-label="Left: the upper half-plane with boundary value 1 on the negative real axis and 0 on the positive one. Right: the unit disk with value 1 on the upper half-circle and 0 on the lower one. An arrow labelled C points from the first to the second." style="max-width:100%;height:auto">{"".join(s)}</svg>',
    'The easy problem on $\\mathbb H$ (left) and the plate problem on the disk (right). The Cayley map $C$ carries one to the other.')

# ---------- isotherms in the disk ----------
S = 220; c = S/2; Rr = 90
tr = lambda z: (c + Rr*z.real, c - Rr*z.imag)
s = [f'<circle cx="{c}" cy="{c}" r="{Rr}" fill="var(--def-bg)"/>']
s.append(f'<path d="M{c-Rr} {c} A {Rr} {Rr} 0 0 1 {c+Rr} {c}" fill="none" stroke="{C3}" stroke-width="3"/>')
s.append(f'<path d="M{c-Rr} {c} A {Rr} {Rr} 0 0 0 {c+Rr} {c}" fill="none" stroke="{C1}" stroke-width="3"/>')
for level in (0.1, 0.25, 0.5, 0.75, 0.9):
    # u = 1/2 + arg((1+w)/(1-w))/pi = level  ->  (1+w)/(1-w) = t e^{i a}, a = pi(level-1/2)
    a = math.pi*(level-0.5)
    pts = []
    for k in range(1, 400):
        t = math.exp(-7 + 14*k/400)
        zeta = t*cmath.exp(1j*a)
        w = (zeta-1)/(zeta+1)
        pts.append(w)
    s.append(path(pts, tr, 'currentColor', 1.1 if level != 0.5 else 1.6, None if level == 0.5 else '4 3'))
    p = (lambda t: (cmath.exp(1j*a)-1)/(cmath.exp(1j*a)+1))(1)
    x, y = tr(p)
    s.append(f'<text x="{x+4:.1f}" y="{y-3:.1f}" font-size="10" fill="currentColor">{level}</text>')
s.append(f'<text x="{c}" y="{c-Rr-6}" text-anchor="middle" font-size="11" fill="{C3}">u → 1</text>')
s.append(f'<text x="{c}" y="{c+Rr+14}" text-anchor="middle" font-size="11" fill="{C1}">u → 0</text>')
FIG['isotherms'] = fig(f'<svg viewBox="0 0 {S} {S+6}" width="{S}" role="img" aria-label="The unit disk, upper half-circle at temperature 1 and lower at 0, with level curves of the temperature: the diameter at 0.5 and circular arcs through -1 and 1 above and below it." style="max-width:100%;height:auto">{"".join(s)}</svg>',
    'Isotherms $u=0.1,0.25,0.5,0.75,0.9$ of Prop. 12.5.1: arcs of circles through $\\pm1$; $u=\\frac12$ is the diameter.')

# ---------- z^2 grid ----------
def panel(ox, oy, size, rng, lines, mapf, lab):
    sc = size/rng
    def T(z):
        w = mapf(z) if mapf else z
        return (ox + sc*w.real, oy + size - sc*w.imag)
    out = [f'<line x1="{ox}" y1="{oy+size}" x2="{ox+size}" y2="{oy+size}" stroke="currentColor" stroke-width="0.8" opacity="0.6"/>',
           f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy+size}" stroke="currentColor" stroke-width="0.8" opacity="0.6"/>']
    for pts, col in lines:
        out.append(path(pts, T, col, 1.5))
    return ''.join(out)
L = []
for a in (0.5, 1.0, 1.5):
    L.append(([complex(a, 0.02*k) for k in range(0, 101)], C3))
    L.append(([complex(0.02*k, a) for k in range(0, 101)], C1))
left = panel(10, 10, 110, 2.0, L, None, '')
# right: image under z^2, region u in [-4,4], v in [0,8]; draw centered axes
def Tr(z):
    w = z*z
    return (240 + 13*w.real, 120 - 13*w.imag)
right = [f'<line x1="170" y1="120" x2="310" y2="120" stroke="currentColor" stroke-width="0.8" opacity="0.6"/>',
         f'<line x1="240" y1="10" x2="240" y2="122" stroke="currentColor" stroke-width="0.8" opacity="0.6"/>']
for pts, col in L:
    pts2 = [z for z in pts if abs(z*z) < 8.5]
    right.append(path(pts2, Tr, col, 1.5))
arrow = '<path d="M128 65 L158 65" stroke="currentColor"/><path d="M152 60 L158 65 L152 70" fill="none" stroke="currentColor"/><text x="143" y="57" text-anchor="middle" font-size="11" font-style="italic" fill="currentColor">z²</text>'
FIG['zsq'] = fig(f'<svg viewBox="0 0 320 130" width="320" role="img" aria-label="Left: a grid of vertical (brown) and horizontal (blue) lines in the first quadrant. Right: their images under z squared, parabolas opening left and right in the upper half-plane, still crossing at right angles." style="max-width:100%;height:auto"><clipPath id="clipzsq"><rect x="168" y="5" width="146" height="117"/></clipPath>{left}{arrow}<g clip-path="url(#clipzsq)">{"".join(right)}</g></svg>',
    'Under $z^2$ the lines $\\operatorname{Re}z=a$ (brown) and $\\operatorname{Im}z=b$ (blue) of the quadrant become parabolas in $\\mathbb H$, still meeting at right angles.')

# ---------- strip -> half-plane ----------
s = ['<rect x="10" y="30" width="110" height="70" fill="var(--def-bg)"/>',
     '<line x1="10" y1="100" x2="120" y2="100" stroke="currentColor" stroke-width="0.8"/><line x1="10" y1="30" x2="120" y2="30" stroke="currentColor" stroke-width="0.8"/>']
for k, yy in enumerate((0.25, 0.5, 0.75)):
    y = 100 - 70*yy
    s.append(f'<line x1="10" y1="{y:.1f}" x2="120" y2="{y:.1f}" stroke="{C1}" stroke-width="1.4"/>')
for xx in (35, 65, 95):
    s.append(f'<line x1="{xx}" y1="30" x2="{xx}" y2="100" stroke="{C3}" stroke-width="1.4"/>')
s.append('<text x="65" y="116" text-anchor="middle" font-size="12" font-style="italic" fill="currentColor">S</text>')
s.append('<text x="124" y="34" font-size="10" fill="currentColor">iπ</text>')
s.append('<path d="M140 65 L170 65" stroke="currentColor"/><path d="M164 60 L170 65 L164 70" fill="none" stroke="currentColor"/><text x="155" y="57" text-anchor="middle" font-size="11" font-style="italic" fill="currentColor">e<tspan dy="-4" font-size="8">z</tspan></text>')
ox, oy = 245, 100
s.append(f'<line x1="180" y1="{oy}" x2="310" y2="{oy}" stroke="currentColor" stroke-width="0.8"/>')
for yy in (0.25, 0.5, 0.75):
    ang = math.pi*yy
    s.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+70*math.cos(ang):.1f}" y2="{oy-70*math.sin(ang):.1f}" stroke="{C1}" stroke-width="1.4"/>')
for rr in (18, 36, 60):
    s.append(f'<path d="M{ox-rr} {oy} A {rr} {rr} 0 0 1 {ox+rr} {oy}" fill="none" stroke="{C3}" stroke-width="1.4"/>')
s.append(f'<text x="{ox}" y="116" text-anchor="middle" font-size="12" font-style="italic" fill="currentColor">ℍ</text>')
FIG['strip'] = fig(f'<svg viewBox="0 0 320 122" width="320" role="img" aria-label="Left: the strip S between Im z = 0 and Im z = pi, with horizontal blue lines and vertical red segments. Right: under e^z, the blue lines become rays from 0 and the red segments become half-circles about 0 in the upper half-plane." style="max-width:100%;height:auto">{"".join(s)}</svg>',
    'Example 12.11.1: $e^z$ maps the strip $S$ onto $\\mathbb H$. Horizontal lines (blue) go to rays, vertical segments (brown) to half-circles.')

# ---------- Joukowski ----------
S = 320; sc = 52; cx, cy = 160, 95
T = lambda w: (cx + sc*w.real, cy - sc*w.imag)
s = [f'<line x1="10" y1="{cy}" x2="310" y2="{cy}" stroke="currentColor" stroke-width="0.8" opacity="0.5"/>',
     f'<line x1="{cx}" y1="10" x2="{cx}" y2="180" stroke="currentColor" stroke-width="0.8" opacity="0.5"/>']
for r in (1.25, 1.6, 2.2):
    pts = [(r*cmath.exp(1j*2*math.pi*k/300)) for k in range(301)]
    s.append(path([z + 1/z for z in pts], T, C3, 1.5))
for k in range(8):
    th = math.pi/8 + k*math.pi/4
    pts = [r*cmath.exp(1j*th) for r in [1 + 0.02*j for j in range(0, 90)]]
    pts = [z + 1/z for z in pts]
    pts = [w for w in pts if abs(w.real) < 2.9 and abs(w.imag) < 1.65]
    s.append(path(pts, T, C1, 1.2))
s.append(f'<line x1="{cx-2*sc}" y1="{cy}" x2="{cx+2*sc}" y2="{cy}" stroke="currentColor" stroke-width="3"/>')
s.append(f'<text x="{cx-2*sc}" y="{cy+16}" text-anchor="middle" font-size="11" fill="currentColor">−2</text><text x="{cx+2*sc}" y="{cy+16}" text-anchor="middle" font-size="11" fill="currentColor">2</text>')
FIG['jouk'] = fig(f'<svg viewBox="0 0 {S} 190" width="{S}" role="img" aria-label="Nested ellipses around a slit from -2 to 2 on the real axis, the images of circles of radius 1.25, 1.6 and 2.2, crossed by hyperbola branches, the images of rays." style="max-width:100%;height:auto">{"".join(s)}</svg>',
    'The Joukowski map: images of the circles $|z|=1.25,1.6,2.2$ (brown ellipses) and of rays from $0$ (blue hyperbola branches). The slit $[-2,2]$ is the image of the unit circle.')

json.dump(FIG, open('figs3.json', 'w'))
print({k: len(v) for k, v in FIG.items()})
