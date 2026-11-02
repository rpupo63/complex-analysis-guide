---
id: k3
slide: Slide 4
title: Uniform limits
---

::: theorem {#thm:uniform-limits name="uniform limits"}
Let $f_N$ be holomorphic on an open set $U$, and $f_N\to f$ [uniformly](apx:A17) on every closed disk contained in $U$. Then $f$ is holomorphic on $U$.
:::
::: proof
Let $\overline{\class{ntn-Dar}{D}(z_0,r)}\subset U$, let $\gamma$ be the circle $|z-z_0|=r$, and $w\in \class{ntn-Dar}{D}(z_0,r)$.
<ol>
<li>$f$ is continuous on the closed disk: a uniform limit of continuous functions ([A.17](apx:A17)).</li>
<li>By Cauchy's formula (@thm:cauchys-integral-formula), $f_N(w)=\frac1{2\pi i}\oint_\gamma\frac{f_N(z)}{z-w}dz$. On $\gamma$, $|z-w|\ge r-|w-z_0|\gt0$, so by the ML estimate
\[ \Big|\frac1{2\pi i}\oint_\gamma\frac{f_N(z)-f(z)}{z-w}\,dz\Big|\le\frac{r\max_\gamma|f_N-f|}{r-|w-z_0|}\longrightarrow0. \]
Letting $N\to\infty$ on both sides,
\[ f(w)=\lim_{N\to\infty}\frac1{2\pi i}\oint_\gamma\frac{f_N(z)}{z-w}\,dz=\frac1{2\pi i}\oint_\gamma\frac{f(z)}{z-w}\,dz. \]</li>
<li>The right side is holomorphic in $w\in \class{ntn-Dar}{D}(z_0,r)$: differentiate under the integral sign, exactly as in the proof of @thm:cauchys-formula-for-derivatives, which only needed $f$ continuous on $\gamma$.</li>
</ol>
Every point of $U$ is the centre of such a disk, so $f$ is holomorphic on $U$.
:::
<p>Lecture 4 proved the same for harmonic functions (@cor:uniform-limits), by the same mechanism: an integral formula survives uniform limits. In real analysis this fails badly: by the [Weierstrass approximation theorem](apx:A18), polynomials converge uniformly on $[-1,1]$ to $|x|$, which is not differentiable.</p>
