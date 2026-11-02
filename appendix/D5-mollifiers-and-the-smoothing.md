---
id: D5
title: Mollifiers and the smoothing fact
status:
- defined
- cited
---
<p>A weight $\class{ntn-chi}{\chi}$ as in @def:the-averaging-weight-chi is called a <em>mollifier</em>. An explicit one:
\[ \class{ntn-chi}{\chi}(\zeta)=c\,\exp\!\Big(\frac{-1}{1-|\zeta|^2}\Big)\ \text{ for }|\zeta|\lt1,\qquad\class{ntn-chi}{\chi}(\zeta)=0\ \text{ otherwise}, \]
with $c$ chosen so the integral is $1$. It is smooth even across the unit circle, because $e^{-1/s}$ and all its derivatives tend to $0$ as $s\downarrow0$. It is radial and nonnegative.</p>
<div class="env"><span class="hd">Theorem (cited).</span> If $u\in L^2(\Omega)$ and $K\subset\Omega$ is compact, then $\norm{u\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}-u}_{L^2(K)}\to0$ as $\delta\to0$.</div>
<p>The idea: for continuous $u$ this is easy, since $u\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}(z)$ is an average of values within $\delta$ of $z$. A general $L^2$ function is an $L^2$-limit of continuous ones, and averaging never increases the $L^2$ norm, so the estimate passes to the limit.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Mollifier" target="_blank" rel="noopener">Mollifier</a> · <a href="https://en.wikipedia.org/wiki/Bump_function" target="_blank" rel="noopener">Bump function</a> · <a href="https://en.wikipedia.org/wiki/Convolution" target="_blank" rel="noopener">Convolution</a></p>
