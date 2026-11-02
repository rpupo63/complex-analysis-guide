---
id: A8
title: Polar coordinates and change of variables
status:
- cited
- derived
---
<div class="env"><span class="hd">Change of variables (cited).</span> If $\Phi$ maps a region one-to-one and smoothly onto another, then $\iint f(\zeta)\,dA(\zeta)=\iint f(\Phi(w))\,|\det D\Phi(w)|\,dA(w)$.</div>
<div class="env"><span class="hd">Consequences (proved).</span>
<ul>
<li><em>Polar coordinates.</em> $\Phi(t,\theta)=(x_0+t\cos\theta,\ y_0+t\sin\theta)$ has $\det D\Phi=\cos\theta\cdot t\cos\theta-(-t\sin\theta)\sin\theta=t$. So $dA=t\,dt\,d\theta$.</li>
<li><em>Arc length on a circle.</em> $\theta\mapsto z_0+te^{i\theta}$ has velocity $t(-\sin\theta,\cos\theta)$, of length $t$. So $ds=t\,d\theta$, and the circle has length $2\pi t$.</li>
<li><em>Scaling.</em> $\zeta=\delta w$ has $\det D\Phi=\delta^2$, so $dA(\zeta)=\delta^2\,dA(w)$.</li>
<li><em>Shifts and reflections</em> $\zeta=w+c$, $\zeta=c-w$ have $|\det D\Phi|=1$: they preserve area.</li>
</ul></div>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Polar_coordinate_system" target="_blank" rel="noopener">Polar coordinates</a> · <a href="https://en.wikipedia.org/wiki/Integration_by_substitution#Substitution_for_multiple_variables" target="_blank" rel="noopener">Change of variables</a></p>
