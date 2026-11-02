---
id: A12
title: Cauchy–Schwarz inequality
status:
- derived
---
<div class="env"><span class="hd">Theorem.</span> (i) For vectors, $|a\cdot b|\le|a|\,|b|$. (ii) For square-integrable scalar or vector-valued $F,G$ on a region $D$,
\[ \Big|\iint_DF\cdot G\,dA\Big|\le\class{ntn-L2}{\norm{F}_{L^2}}\,\class{ntn-L2}{\norm{G}_{L^2}}. \]
The one-variable version $\big(\int fh\big)^2\le\int f^2\int h^2$ is proved the same way.</div>
::: proof
Write $\langle F,G\rangle$ for either $a\cdot b$ or $\iint F\cdot G$; the argument uses only that it is symmetric, bilinear and $\langle F,F\rangle\ge0$. For every real $\lambda$,
\[ 0\le\langle F+\lambda G,F+\lambda G\rangle=\langle F,F\rangle+2\lambda\langle F,G\rangle+\lambda^2\langle G,G\rangle. \]
If $\langle G,G\rangle\gt0$, this quadratic in $\lambda$ never goes negative, so its discriminant is $\le0$: $4\langle F,G\rangle^2-4\langle F,F\rangle\langle G,G\rangle\le0$. Take square roots. If $\langle G,G\rangle=0$, the expression is linear in $\lambda$ and bounded below, which forces $\langle F,G\rangle=0$, and the inequality holds trivially.
:::
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality" target="_blank" rel="noopener">Cauchy–Schwarz inequality</a></p>
