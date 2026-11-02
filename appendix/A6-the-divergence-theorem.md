---
id: A6
title: The divergence theorem
status:
- cited
---
<div class="env"><span class="hd">Theorem.</span> Let $D\subset\R^2$ be a bounded region whose boundary is a piecewise smooth curve, with outward unit normal $n$. If $F=(F_1,F_2)$ is continuously differentiable on $\overline D$, then
\[ \iint_D \nabla\cdot F\,dA=\oint_{\partial D}F\cdot n\,ds,\qquad \nabla\cdot F=\partial_xF_1+\partial_yF_2. \]</div>
<div class="env"><span class="hd">Green's theorem (circulation form, cited).</span> Under the same hypotheses, with $t$ the unit tangent for the positive orientation (region on the left),
\[ \iint_D\operatorname{curl}F\,dA=\oint_{\partial D}F\cdot t\,ds,\qquad\operatorname{curl}F=\partial_xF_2-\partial_yF_1. \]
The divergence form is this one applied to the field turned by $90°$, since $F\cdot n=(F_2,-F_1)\cdot t$ when $n$ is $t$ turned clockwise.</div>
<div class="env"><span class="hd">Regions with holes.</span> Both theorems hold for a region bounded by several curves, such as a disk with a smaller disk removed, provided each boundary curve is traversed with the region on its left: the outer curve anticlockwise, each inner curve clockwise. On an inner circle the outward normal of the region points <em>towards</em> the centre of the hole. @thm:the-claim uses this.</div>
<p>In two dimensions this is a restatement of Green's theorem. Applied to $F=w\nabla u$ it gives <em>Green's first identity</em>, $\iint w\,\class{ntn-Delta}{\Delta} u=\oint w\,\partial_nu-\iint\nabla w\cdot\nabla u$, which is how @prop:the-slides-computation uses it. That identity is the two-dimensional form of integration by parts. The grid regions of this lecture have boundaries made of finitely many segments, so they meet the hypothesis.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Divergence_theorem" target="_blank" rel="noopener">Divergence theorem</a> · <a href="https://en.wikipedia.org/wiki/Green%27s_theorem" target="_blank" rel="noopener">Green's theorem</a> · <a href="https://en.wikipedia.org/wiki/Green%27s_identities" target="_blank" rel="noopener">Green's identities</a></p>
