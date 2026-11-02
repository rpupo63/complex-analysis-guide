---
label: ex:a-sector-onto-the-disk
source: Practice midterm 1, Problem 4(a)
title: a sector onto the disk
placement: n11
order: 1
---
Find a conformal map $F$ of the sector $\{z\ne0:0\lt\arg z\lt\frac\pi3\}$ onto $D(0,1)$.
<details class="sol"><summary>Hint</summary>
First map the sector onto $\mathbb H$ with a power of $z$ (compare @eg:z-2-doubles-angles-at-0), then use the Cayley map (@prop:cayley-map).
</details>
<details class="sol"><summary>Solution</summary>
$z\mapsto z^3$ maps the sector onto $\mathbb H$, as $z^2$ maps the quadrant onto $\mathbb H$ in @eg:z-2-doubles-angles-at-0: $z=re^{i\theta}$ with $0\lt\theta\lt\frac\pi3$ goes to $r^3e^{3i\theta}$, $3\theta\in(0,\pi)$, and every point of $\mathbb H$ has exactly one such preimage (modulus and argument determine $r$ and $\theta$). So $z^3$ is a holomorphic bijection of the sector onto $\mathbb H$, a conformal map (@def:conformal-map). Compose with the Cayley map $C$ (@prop:cayley-map), a conformal map of $\mathbb H$ onto $D(0,1)$:
\[ F(z)=\frac{z^3-i}{z^3+i}. \]
A composition of conformal maps is conformal (@def:conformal-map).
</details>
