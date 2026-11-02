#!/usr/bin/env python3
"""Generate Lecture 1 figures that were missing from v17 (slides 3, 22 and 29).

    python figures/gen_l01.py      # writes figures/x2-1.svg, x2-2.svg, x13-2.svg, x16-1..4.svg

Colours are CSS variables (currentColor, --accent, --muted, --rule) so dark mode works.
"""
import cmath
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent


def svg(w, h, label, body):
    return ('<svg viewBox="0 0 %d %d" width="%d" role="img" aria-label="%s">%s</svg>'
            % (w, h, w, label, body))


def arrow(x1, y1, x2, y2, color='currentColor', width=1.2, head=4.0):
    """A line from (x1,y1) to (x2,y2) with an open head at the end."""
    a = math.atan2(y2 - y1, x2 - x1)
    p = [(x2 - head * math.cos(a - s), y2 - head * math.sin(a - s)) for s in (0.45, -0.45)]
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"/>'
            '<polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="%s"/>'
            % (x1, y1, x2, y2, color, width, p[0][0], p[0][1], x2, y2, p[1][0], p[1][1], color, width))


def text(x, y, s, size=11, italic=True):
    return ('<text x="%.1f" y="%.1f" font-size="%d"%s fill="currentColor" font-family="var(--f-text)">%s</text>'
            % (x, y, size, ' font-style="italic"' if italic else '', s))


# ---------------------------------------------------------------- slide 3: directions of approach
def directions():
    w, h = 170, 90
    b = '<line x1="15" y1="45" x2="155" y2="45" stroke="currentColor" stroke-width="1"/>'
    b += '<circle cx="85" cy="45" r="2.2" fill="currentColor"/>'
    b += arrow(45, 36, 77, 36, 'var(--accent)', 1.4) + arrow(125, 36, 93, 36, 'var(--accent)', 1.4)
    b += text(80, 66, 'x') + text(87, 70, '0', 8, False)
    left = svg(w, h, 'On the real line, a point x0 can be approached only from the left and from the right.', b)

    w, h = 150, 150
    c = 75
    b = arrow(10, c + 25, 140, c + 25, 'currentColor', 1) + arrow(c - 25, 140, c - 25, 10, 'currentColor', 1)
    b += '<circle cx="%d" cy="%d" r="2.2" fill="currentColor"/>' % (c, c)
    for k in range(16):
        t = 2 * math.pi * k / 16
        b += arrow(c + 34 * math.cos(t), c - 34 * math.sin(t), c + 9 * math.cos(t), c - 9 * math.sin(t),
                   'var(--accent)', 1.1, 3)
    b += text(c + 40, c - 30, 'z') + text(c + 46, c - 26, '0', 8, False)
    right = svg(w, h, 'In the complex plane, a point z0 can be approached from every direction.', b)
    return left, right


# ---------------------------------------------------------------- slide 22: uniform flow
def uniform():
    w = h = 200
    b = '<rect x="0.5" y="0.5" width="199" height="199" fill="none" stroke="var(--rule)"/>'
    for j in range(1, 10):
        y = 20 * j
        b += '<line x1="0" y1="%d" x2="200" y2="%d" stroke="var(--accent)" stroke-width="0.9" opacity="0.8"/>' % (y, y)
        for i in range(5):
            x = 12 + 40 * i + (20 if j % 2 else 0)
            b += arrow(x, y, x + 14, y, 'currentColor', 1, 3.5)
    return svg(w, h, 'Uniform flow: horizontal streamlines, every particle moving right at unit speed.', b)


# ---------------------------------------------------------------- slide 29: four flows
S, R = 150, 2.0          # panel size in px, half-width in the plane


def px(z):
    return S / 2 + z.real * S / (2 * R), S / 2 - z.imag * S / (2 * R)


def contours(F, levels, inside=None, n=64):
    """Marching squares for the level sets F = c; returns an SVG path 'd' string."""
    xs = [-R + 2 * R * i / n for i in range(n + 1)]
    val = [[F(complex(x, y)) if not (inside and inside(complex(x, y))) else None for x in xs] for y in xs]
    d = []
    for c in levels:
        for j in range(n):
            for i in range(n):
                q = [val[j][i], val[j][i + 1], val[j + 1][i + 1], val[j + 1][i]]
                if any(v is None for v in q):
                    continue
                corners = [(xs[i], xs[j]), (xs[i + 1], xs[j]), (xs[i + 1], xs[j + 1]), (xs[i], xs[j + 1])]
                pts = []
                for k in range(4):
                    a, b = q[k] - c, q[(k + 1) % 4] - c
                    if (a < 0) != (b < 0):
                        t = a / (a - b)
                        (x0, y0), (x1, y1) = corners[k], corners[(k + 1) % 4]
                        pts.append(complex(x0 + t * (x1 - x0), y0 + t * (y1 - y0)))
                for k in range(0, len(pts) - 1, 2):
                    (ax, ay), (bx, by) = px(pts[k]), px(pts[k + 1])
                    d.append('M%.1f,%.1fL%.1f,%.1f' % (ax, ay, bx, by))
    return ''.join(d)


def frame(label, stream, level, extra=''):
    b = '<rect x="0.5" y="0.5" width="149" height="149" fill="none" stroke="var(--rule)"/>'
    b += extra
    b += '<path d="%s" fill="none" stroke="var(--muted)" stroke-width="0.7" stroke-dasharray="3 2"/>' % level
    b += '<path d="%s" fill="none" stroke="var(--accent)" stroke-width="1.1"/>' % stream
    return svg(S, S, label, b)


def rays(k):
    d = ''
    for m in range(k):
        t = 2 * math.pi * m / k
        (ax, ay), (bx, by) = px(0.04 * cmath.exp(1j * t)), px(3 * cmath.exp(1j * t))
        d += 'M%.1f,%.1fL%.1f,%.1f' % (ax, ay, bx, by)
    return d


def circles(radii):
    return ''.join('M%.1f,%.1fa%.1f,%.1f 0 1,0 %.1f,0a%.1f,%.1f 0 1,0 %.1f,0'
                   % (S / 2 - r * S / (2 * R), S / 2, r * S / (2 * R), r * S / (2 * R), 2 * r * S / (2 * R),
                      r * S / (2 * R), r * S / (2 * R), -2 * r * S / (2 * R)) for r in radii)


def four_flows():
    lv = [k * 0.6 for k in range(-6, 7)]
    sq = frame('z squared: hyperbolic streamlines 2xy = c, dashed level sets x^2 - y^2 = c.',
               contours(lambda z: (z * z).imag, lv), contours(lambda z: (z * z).real, lv))
    radii = [math.exp(k / 3) for k in range(-9, 3)]
    src = frame('log z: streamlines are rays from 0, dashed level sets are circles.', rays(16), circles(radii))
    vor = frame('-i log z: streamlines are circles about 0, dashed level sets are rays.', circles(radii), rays(16))
    cyl_lv = [k * 0.3 for k in range(-7, 8)]
    outside = lambda z: abs(z) < 1  # noqa: E731
    disk = '<circle cx="75" cy="75" r="%.1f" fill="var(--rule)" stroke="currentColor" stroke-width="1"/>' % (S / (2 * R))
    cyl = frame('z + 1/z: streamlines of uniform flow bending around the unit disk, which is itself a streamline.',
                contours(lambda z: (z + 1 / z).imag, cyl_lv, outside),
                contours(lambda z: (z + 1 / z).real, cyl_lv, outside), disk)
    return sq, src, vor, cyl


def main():
    a, b = directions()
    files = {'x2-1': a, 'x2-2': b, 'x13-2': uniform()}
    files.update(zip(['x16-1', 'x16-2', 'x16-3', 'x16-4'], four_flows()))
    for name, s in files.items():
        (OUT / (name + '.svg')).write_text(s)
        print('wrote figures/%s.svg (%d bytes)' % (name, len(s)))


if __name__ == '__main__':
    main()
