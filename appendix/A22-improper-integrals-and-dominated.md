---
id: A22
title: Improper integrals and dominated convergence
status:
- defined
- cited
---
<p>A function $f$ on $\R$ (or on $(0,\infty)$) is <em>integrable</em> if $\int|f|\lt\infty$. Then $\int_{-\infty}^\infty f=\lim_{R\to\infty}\int_{-R}^Rf$, and the limit does not depend on how the endpoints go to infinity. For a merely convergent limit such as $\lim_R\int_{-R}^R$ this independence can fail, which is why the lectures check integrability.</p>
<div class="env"><span class="hd">Dominated convergence theorem (cited).</span> If $f_n\to f$ pointwise (or almost everywhere) and $|f_n|\le g$ for one integrable $g$, then $\int f_n\to\int f$.</div>
<p>Typical consequences: if $|f(x,\xi)|\le g(x)$ with $g$ integrable and $f$ continuous in $\xi$, then $\xi\mapsto\int f(x,\xi)\,dx$ is continuous; so the Fourier transform of an integrable function is continuous. @thm:hardy-and-ramanujan-1918 (@prop:the-major-arc) and @thm:weierstrass-product-for-1-gamma (@sec:m7) use the theorem directly, with dominating functions $2e^{-u^2/2}$ and $t^{x-1}e^{-t}$.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Dominated_convergence_theorem" target="_blank" rel="noopener">Dominated convergence theorem</a> · <a href="https://en.wikipedia.org/wiki/Improper_integral" target="_blank" rel="noopener">Improper integral</a></p>
