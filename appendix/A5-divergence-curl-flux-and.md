---
id: A5
title: Divergence, curl, flux and circulation
status:
- defined
---
<p>Lecture 1 defines divergence and curl (@def:divergence-and-curl); this entry adds their meaning, flux, circulation and line integrals.</p>
<p>For a vector field $F=(F_1,F_2)$ in the plane:</p>
<ul>
<li>$\class{ntn-divc}{\operatorname{div}}F:=\partial_xF_1+\partial_yF_2$ (also written $\nabla\cdot F$): the rate at which $F$ spreads out from a point, the "source density".</li>
<li>$\class{ntn-divc}{\operatorname{curl}}F:=\partial_xF_2-\partial_yF_1$: the rate at which $F$ swirls around a point. (In three dimensions the curl is a vector; in the plane only its component perpendicular to the plane survives, a scalar.)</li>
</ul>
<p>Along an oriented curve $\gamma$ with unit tangent $t$ and unit normal $n$ (pointing to the right of the direction of travel, so outward for a positively oriented boundary):</p>
<ul>
<li><em>flux</em> $\oint_\gamma F\cdot n\,ds$ measures how much of $F$ crosses $\gamma$;</li>
<li><em>circulation</em> $\oint_\gamma F\cdot t\,ds$ measures how much of $F$ runs along $\gamma$.</li>
</ul>
<p>In coordinates, $t\,ds=(dx,dy)$ and $n\,ds=(dy,-dx)$, so flux $=\oint F_1\,dy-F_2\,dx$ and circulation $=\oint F_1\,dx+F_2\,dy$. A line integral $\oint P\,dx+Q\,dy$ is computed from a parametrization $s\mapsto(x(s),y(s))$ as $\int(P\,x'+Q\,y')\,ds$. The divergence theorem and Green's theorem ([A.6](apx:A6)) turn flux and circulation into area integrals of $\class{ntn-divc}{\operatorname{div}}F$ and $\class{ntn-divc}{\operatorname{curl}}F$.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Divergence" target="_blank" rel="noopener">Divergence</a> · <a href="https://en.wikipedia.org/wiki/Curl_(mathematics)" target="_blank" rel="noopener">Curl</a> · <a href="https://en.wikipedia.org/wiki/Line_integral" target="_blank" rel="noopener">Line integral</a> · <a href="https://en.wikipedia.org/wiki/Flux" target="_blank" rel="noopener">Flux</a></p>
