---
id: A11
title: Sets of zero area and vanishing integrals
status:
- defined
- derived
- cited
---
<div class="env"><span class="hd">Definition.</span> A set $Z\subset\R^2$ has <em>zero area</em> if for every $\delta\gt0$ it can be covered by finitely many rectangles whose total area is less than $\delta$.</div>
<div class="env"><span class="hd">(a) A line segment has zero area (proved).</span> A horizontal or vertical segment of length $\ell$ fits in an $\ell\times\delta/\ell$ rectangle, of area $\delta$; take a slightly smaller height. A finite union of zero-area sets has zero area, since the covers can be combined. So the grid lines inside a bounded region, and $\class{ntn-dOm}{\partial\Omega}$ itself, have zero area.</div>
<div class="env"><span class="hd">(b) Changing a bounded integrand on a zero-area set does not change the integral (cited).</span> This is a standard property of the Riemann (and Lebesgue) integral. It is why gradients defined only off grid lines can be integrated.</div>
<div class="env"><span class="hd">(c) Zero integral forces zero (proved).</span> If $f$ is continuous and nonnegative on an open set $Q$ and $\iint_Qf\,dA=0$, then $f\equiv0$ on $Q$. The same holds for a continuous nonnegative function on an interval, such as $\theta\mapsto\varphi(\theta)$ on $[0,2\pi]$, with an interval around the point in place of a disc.</div>
::: proof {title="Proof of (c)."}
Suppose $f(P)=2\mu\gt0$ at some $P\in Q$. By continuity there is $r\gt0$ such that the disc $D_r(P)$ lies in $Q$ and $f\gt\mu$ on it. Since $f\ge0$ everywhere, $\iint_Qf\ge\iint_{D_r(P)}f\ge\pi r^2\mu\gt0$, a contradiction.
:::
<div class="env"><span class="hd">(d) "Almost everywhere" (defined).</span> A statement holds <em>almost everywhere</em> (a.e.) if the set where it fails has zero area, in the Lebesgue sense: it can be covered by countably many rectangles of arbitrarily small total area. Two functions equal a.e. are the same element of $L^2$ ([D.2](apx:D2)). A countable union of such sets again has zero area, which is how @thm:proof-of-weyls-lemma passes from compact pieces to all of $\Omega$. A function with $\class{ntn-L2}{\norm{f}_{L^2}}=0$ is zero a.e. (cited).</div>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Almost_everywhere" target="_blank" rel="noopener">Almost everywhere</a> · <a href="https://en.wikipedia.org/wiki/Null_set" target="_blank" rel="noopener">Null set</a> · <a href="https://en.wikipedia.org/wiki/Jordan_measure" target="_blank" rel="noopener">Jordan measure</a></p>
