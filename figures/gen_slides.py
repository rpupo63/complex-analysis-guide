#!/usr/bin/env python3
"""Generate the slide figures that the guide was missing (L9 slides 2 and 5, L10 slide 2,
L15 slides 3, 4, 7, 16 and 19).

    python figures/gen_slides.py   # writes j1-1, j4-1, k1-1, q2-1, q3-1, q6-1, q13-1, q15-1 (.svg)

Colours are CSS variables (currentColor, --accent, --muted, --asm-ink, --def-bg, --asm-bg,
--paper) so dark mode works.
"""
import cmath
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent


def svg(w, h, label, body):
    return ('<svg viewBox="0 0 %d %d" width="%d" role="img" aria-label="%s" style="max-width:100%%;height:auto">%s</svg>'
            % (w, h, w, label, body))


def text(x, y, s, size=12, italic=True, color='currentColor', anchor='middle'):
    return ('<text x="%.1f" y="%.1f" font-size="%d"%s text-anchor="%s" fill="%s" font-family="var(--f-text)">%s</text>'
            % (x, y, size, ' font-style="italic"' if italic else '', anchor, color, s))


def dot(x, y, color='currentColor', r=2.2):
    return '<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>' % (x, y, r, color)


def circle(x, y, r, stroke='currentColor', fill='none', width=1.2, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ''
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (x, y, r, fill, stroke, width, d))


def line(x1, y1, x2, y2, color='currentColor', width=1.2, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ''
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"%s/>'
            % (x1, y1, x2, y2, color, width, d))


def path(pts, color='currentColor', width=1.2, fill='none', close=False, dash=None):
    d = 'M' + ' L'.join('%.1f %.1f' % p for p in pts) + (' Z' if close else '')
    dd = ' stroke-dasharray="%s"' % dash if dash else ''
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (d, fill, color, width, dd)


# ------------------------------------------------------------ L9 slide 2: removable singularities
def removable():
    b = circle(90, 75, 62, 'currentColor', 'var(--def-bg)')
    b += circle(70, 82, 11, 'var(--accent)', 'var(--paper)', 1.4) + dot(70, 82, 'var(--accent)', 1.8)
    b += text(52, 86, 'a', color='var(--accent)')
    b += circle(118, 58, 10, 'currentColor', 'var(--paper)') + dot(118, 58, r=1.8)
    b += text(136, 60, 'w')
    b += text(90, 152, '|z − a| = r′', 11)
    return svg(180, 160, 'A shaded disk of radius r prime about a, with two small disks removed: a circle of radius '
               'epsilon about a and a small circle about w. g(z)/(z minus w) is holomorphic on the shaded region.', b)


# ------------------------------------------------------------ L9 slide 5: the mean of log|Re^{it} - a|
def mean_of_log():
    b = circle(80, 80, 55, 'var(--accent)', 'var(--def-bg)', 1.6)
    b += dot(80, 80, r=1.8) + text(80, 95, '0', 11, False)
    b += dot(108, 60, 'var(--asm-ink)', 2.6) + text(102, 52, '|a| &lt; R', 11, color='var(--asm-ink)')
    b += dot(168, 128, 'var(--asm-ink)', 2.6) + text(168, 146, '|a| &gt; R', 11, color='var(--asm-ink)')
    b += text(38, 22, '|z| = R', 11, color='var(--accent)')
    return svg(210, 155, 'The circle |z| = R about 0, with a point a inside it and a point a outside it.', b)


# ------------------------------------------------------------ L10 slide 2: the identity theorem
def identity():
    blob = [(20, 60), (40, 22), (110, 12), (190, 18), (232, 50), (226, 100), (170, 122), (80, 120), (28, 102)]
    # a smooth closed curve through the blob points (Catmull-Rom to cubic Bezier)
    n = len(blob)
    d = 'M%.1f %.1f' % blob[0]
    for i in range(n):
        p0, p1, p2, p3 = blob[i - 1], blob[i], blob[(i + 1) % n], blob[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += ' C%.1f %.1f %.1f %.1f %.1f %.1f' % (c1 + c2 + p2)
    b = '<path d="%s Z" fill="var(--def-bg)" stroke="currentColor" stroke-width="1.4"/>' % d
    centres = [(62, 72), (100, 58), (140, 52), (180, 50)]
    for k, (x, y) in enumerate(centres):
        b += circle(x, y, 24, 'var(--accent)', 'none', 1.1, None if k == 0 else '3 2')
    b += dot(62, 72, 'var(--accent)') + text(50, 76, 'x', color='var(--accent)')
    for t in (0.35, 0.55, 0.75, 0.9):
        b += dot(62 + 14 * t, 72 + 10 * t, r=1.2)
    b += dot(82, 86, r=1.5) + text(94, 98, 'x<tspan font-size="8" dy="3">n</tspan>', 11)
    b += dot(184, 52) + text(184, 42, 'w')
    b += text(200, 104, 'U', 13)
    return svg(250, 135, 'A connected open set U, with a chain of overlapping disks from x to a point w. '
               'Zeros x_n of h tend to x.', b)


# ------------------------------------------------------------ L15 slide 3: the method of images
def images():
    s, ox, oy = 18, 110, 112           # 1 unit = s px; the real axis is y = oy
    P = lambda z: (ox + s * z.real, oy - s * z.imag)
    b = '<rect x="0" y="0" width="220" height="%d" fill="var(--def-bg)" opacity="0.5"/>' % oy
    for k in (1.8, 2.6, 4, 8):        # |z - conj(a)| / |z - a| = k, with a = i
        c, r = (k * k + 1) / (k * k - 1), 2 * k / (k * k - 1)
        x, y = P(complex(0, c))
        b += circle(x, y, s * r, 'var(--accent)', 'none', 1.1)
        x, y = P(complex(0, -c))
        b += circle(x, y, s * r, 'var(--asm-ink)', 'none', 1.1, '3 2')
    b += line(0, oy, 220, oy, 'currentColor', 1.6)
    b += text(205, oy - 6, 'u = 0', 11, anchor='end')
    x, y = P(1j)
    b += dot(x, y, 'var(--accent)', 2.6) + text(x - 46, y - 2, 'a', color='var(--accent)')
    x, y = P(-1j)
    b += dot(x, y, 'var(--asm-ink)', 2.6) + text(x - 46, y + 8, 'ā', color='var(--asm-ink)')
    return svg(220, 224, 'A charge at a above the grounded line u = 0 and its image charge at a bar below. '
               'The equipotentials are circles around a, mirrored by dashed circles around a bar.', b)


# ------------------------------------------------------------ L15 slide 4: a symmetric open set
def symmetric():
    cx, cy, rx, ry = 110, 70, 80, 48
    b = ('<path d="M%d %d A %d %d 0 0 1 %d %d Z" fill="var(--def-bg)"/>' % (cx - rx, cy, rx, ry, cx + rx, cy))
    b += ('<path d="M%d %d A %d %d 0 0 0 %d %d Z" fill="var(--asm-bg)"/>' % (cx - rx, cy, rx, ry, cx + rx, cy))
    b += '<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="none" stroke="currentColor" stroke-width="1.4"/>' % (cx, cy, rx, ry)
    b += line(5, cy, 215, cy, 'var(--muted)', 1)
    b += line(cx - rx, cy, cx + rx, cy, 'var(--accent)', 2.4)
    b += text(cx + rx - 10, cy - 6, 'I', color='var(--accent)')
    b += text(cx - 40, cy - 18, 'Ω<tspan font-size="8" dy="-6">+</tspan>', 13, False)
    b += text(cx - 40, cy + 30, 'Ω<tspan font-size="8" dy="-6">−</tspan>', 13, False)
    b += dot(cx + 20, cy - 22) + text(cx + 32, cy - 18, 'z')
    b += dot(cx + 20, cy + 22) + text(cx + 32, cy + 26, 'z̄')
    return svg(220, 140, 'A region symmetric about the real axis: the upper part Omega plus, the lower part Omega minus, '
               'and the segment I on the real axis. A point z and its mirror point z bar.', b)


# ------------------------------------------------------------ L15 slide 7: a polygon and its turns
def polygon():
    pts = [(40, 120), (150, 132), (175, 60), (100, 18), (25, 55)]        # counterclockwise on screen
    b = path(pts, 'currentColor', 1.4, 'var(--def-bg)', True)
    # vertex w_k = pts[1]: incoming side from pts[0], outgoing to pts[2]
    (x0, y0), (x1, y1), (x2, y2) = pts[0], pts[1], pts[2]
    ain = math.atan2(y1 - y0, x1 - x0)
    aout = math.atan2(y2 - y1, x2 - x1)
    b += line(x1, y1, x1 + 40 * math.cos(ain), y1 + 40 * math.sin(ain), 'var(--muted)', 1, '3 2')
    r = 22                                                              # the turn (1 - alpha_k) pi
    b += ('<path d="M%.1f %.1f A %d %d 0 0 0 %.1f %.1f" fill="none" stroke="var(--asm-ink)" stroke-width="1.3"/>'
          % (x1 + r * math.cos(ain), y1 + r * math.sin(ain), r, r, x1 + r * math.cos(aout), y1 + r * math.sin(aout)))
    r = 14                                                              # the interior angle alpha_k pi
    back = math.atan2(y0 - y1, x0 - x1)
    b += ('<path d="M%.1f %.1f A %d %d 0 0 0 %.1f %.1f" fill="none" stroke="currentColor" stroke-width="1"/>'
          % (x1 + r * math.cos(aout), y1 + r * math.sin(aout), r, r, x1 + r * math.cos(back), y1 + r * math.sin(back)))
    b += text(x1 - 26, y1 - 12, 'α<tspan font-size="8" dy="3">k</tspan><tspan dy="-3">π</tspan>', 11)
    b += text(x1 + 4, y1 + 16, 'w<tspan font-size="8" dy="3">k</tspan>', 12)
    b += text(x1 + 34, y1 - 22, '(1 − α<tspan font-size="8" dy="3">k</tspan><tspan dy="-3">)π</tspan>', 11,
              color='var(--asm-ink)', anchor='start')
    return svg(250, 150, 'A pentagon with a vertex w_k. The interior angle there is alpha_k pi, and going around the '
               'boundary counterclockwise one turns left by (1 minus alpha_k) pi.', b)


# ------------------------------------------------------------ L15 slide 16: reflections of the rectangle
def checkerboard():
    w, h, x0, y0 = 70, 40, 10, 10
    b = ''
    for i in range(3):
        for j in range(3):
            up = (i + j) % 2 == 0
            b += ('<rect x="%d" y="%d" width="%d" height="%d" fill="var(--%s)" stroke="var(--muted)" stroke-width="1"/>'
                  % (x0 + j * w, y0 + i * h, w, h, 'def-bg' if up else 'asm-bg'))
            label = 'ℍ' if up else '−ℍ'
            if (i, j) == (1, 1):
                label = '<tspan font-style="italic">R</tspan>: ℍ'
            b += text(x0 + j * w + w / 2, y0 + i * h + h / 2 + 5, label, 13, False)
    b += ('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="currentColor" stroke-width="2"/>'
          % (x0 + w, y0 + h, w, h))
    yb = y0 + 2 * h
    b += text(x0 + w, y0 + 3 * h + 14, '−K', 10) + text(x0 + 2 * w, y0 + 3 * h + 14, 'K', 10)
    b += text(x0 + 3 * w + 4, y0 + h + 4, 'iK′', 10, anchor='start') + text(x0 + 3 * w + 4, yb + 4, '0', 10, False, anchor='start')
    return svg(250, 156, 'The rectangle R with corners minus K, K, K plus i K prime, minus K plus i K prime, and its eight '
               'neighbours. sn takes values in the upper half-plane on R and on the corner rectangles, and in the '
               'lower half-plane on the four rectangles that share a side with R.', b)


# ------------------------------------------------------------ L15 slide 19: the fringing field
def fringing():
    xmin, xmax, ymin, ymax, s = -7.0, 4.0, -7.0, 7.0, 17
    W, H = int((xmax - xmin) * s), int((ymax - ymin) * s)
    P = lambda w: (s * (w.real - xmin), s * (ymax - w.imag))
    inside = lambda w: xmin <= w.real <= xmax and ymin <= w.imag <= ymax

    def curve(zs, color, width, dash=None):
        out, run = '', []
        for z in zs:
            w = z + cmath.exp(z)
            if inside(w):
                run.append(P(w))
            else:
                if len(run) > 1:
                    out += path(run, color, width, dash=dash)
                run = []
        if len(run) > 1:
            out += path(run, color, width, dash=dash)
        return out

    N = 500
    xs = [-10 + 14 * k / N for k in range(N + 1)]
    b = ''
    for x0 in [-3, -2, -1, -0.5, 0, 0.5, 1, 1.5, 2]:            # field lines Re z = x0
        b += curve([complex(x0, -math.pi + 2 * math.pi * k / N) for k in range(1, N)], 'var(--muted)', 0.8)
    for k in range(-5, 6):                                         # equipotentials Im z = k pi / 6
        if k in (-3, 3):
            continue
        b += curve([complex(x, k * math.pi / 6) for x in xs], 'var(--accent)', 1.1)
    for k in (-3, 3):                                              # Rogowski electrodes, u = 1/2 and -1/2
        b += curve([complex(x, k * math.pi / 6) for x in xs], 'var(--asm-ink)', 1.6)
    for sgn in (1, -1):                                            # the plates
        x1, y1 = P(complex(xmin, sgn * math.pi))
        x2, y2 = P(complex(-1, sgn * math.pi))
        b += line(x1, y1, x2, y2, 'currentColor', 3)
    x, y = P(complex(-6.6, math.pi + 0.4))
    b += text(x, y, 'u = 1', 11, anchor='start')
    x, y = P(complex(-6.6, -math.pi - 0.9))
    b += text(x, y, 'u = −1', 11, anchor='start')
    return svg(W, H, 'Equipotentials (blue) and field lines (grey) near the edge of a capacitor whose plates are the '
               'thick half-lines at height plus and minus pi. Between the plates the field is uniform. Near the tips '
               'the lines crowd together. The two brown curves are the Rogowski electrodes, the equipotentials u = 1/2 '
               'and u = -1/2.', b)


FIGS = {'j1-1': removable, 'j4-1': mean_of_log, 'k1-1': identity, 'q2-1': images, 'q3-1': symmetric,
        'q6-1': polygon, 'q13-1': checkerboard, 'q15-1': fringing}

if __name__ == '__main__':
    for name, f in FIGS.items():
        (OUT / (name + '.svg')).write_text(f() + '\n')
        print('wrote figures/%s.svg' % name)
