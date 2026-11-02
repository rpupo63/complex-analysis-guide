---
id: A25
title: The ML estimate for contour integrals
status:
- derived
---
<div class="env"><span class="hd">Proposition.</span> If $\gamma$ is a piecewise $C^1$ curve of length $L$ and $|f|\le M$ on $\gamma$, then $\Big|\displaystyle\int_\gamma f(z)\,dz\Big|\le ML$.</div>
::: proof
Parametrize $\gamma$ by $z(s)$, $a\le s\le b$ (@def:contour-integral). For a complex-valued integral, $|\int h|\le\int|h|$: write $\int h=|\int h|e^{i\alpha}$; then $|\int h|=\int\operatorname{Re}(e^{-i\alpha}h)\le\int|h|$. So
\[ \Big|\int_a^bf(z(s))\,z'(s)\,ds\Big|\le\int_a^b|f(z(s))|\,|z'(s)|\,ds\le M\int_a^b|z'(s)|\,ds=ML, \]
since $\int|z'(s)|\,ds$ is the length.
:::
<p>The name comes from "$M$ times $L$". Every "the arc contributes at most…" in Parts II–IV is this estimate. Typical shapes: a circle of radius $r$ has $L=2\pi r$; a semicircle, $\pi R$; a vertical side of a rectangle, its height.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Estimation_lemma" target="_blank" rel="noopener">Estimation lemma</a></p>
