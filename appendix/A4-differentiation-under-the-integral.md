---
id: A4
title: Differentiation under the integral sign
status:
- cited
---
<div class="env"><span class="hd">Theorem (two versions).</span>
<ol>
<li><em>Continuous version.</em> If $f(t,\theta)$ and $\partial_tf(t,\theta)$ are continuous on a rectangle $[a,b]\times[0,2\pi]$, then $F(t)=\int_0^{2\pi}f(t,\theta)\,d\theta$ is differentiable and $F'(t)=\int_0^{2\pi}\partial_tf(t,\theta)\,d\theta$.</li>
<li><em>Integrable version.</em> Let $u$ be integrable over a bounded set $B$, and let $k(z,\zeta)$ be zero for $\zeta\notin B$, with every $z$-derivative continuous and bounded. Then $z\mapsto\iint u(\zeta)\,k(z,\zeta)\,dA(\zeta)$ is smooth, and each derivative may be taken inside the integral, on $k$.</li>
<li><em>Unbounded intervals, complex parameter.</em> Let $h(z,\xi)$ be continuous for $z$ in an open set $U\subset\mathbb C$ and $\xi$ in an interval $J$ (possibly infinite), holomorphic in $z$ for each $\xi$, with $\partial_zh$ continuous, and suppose $|h|\le H(\xi)$ and $|\partial_zh|\le H(\xi)$ on $U\times J$ for an integrable $H$. Then $F(z)=\int_Jh(z,\xi)\,d\xi$ is holomorphic on $U$, with $F'=\int_J\partial_zh\,d\xi$. (The partial derivatives in $x$ and $y$ pass under the integral by dominated convergence, [A.22](apx:A22), and satisfy Cauchy–Riemann because $h$ does.)</li>
</ol></div>
<p>Version 1 is used in @thm:mean-value-property; version 2, with $k(z,\zeta)=\chi_\delta(z-\zeta)$, in @prop:u-delta-is-smooth and @thm:converse-of-the-mean-value-property; version 3 in Lectures 8 and 11 (@thm:strips-and-decay, @thm:paley-wiener-a-simple-form, @prop:the-gamma-function). Version 2 is a consequence of the dominated convergence theorem, applied to difference quotients.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Leibniz_integral_rule" target="_blank" rel="noopener">Leibniz integral rule</a> · <a href="https://en.wikipedia.org/wiki/Dominated_convergence_theorem" target="_blank" rel="noopener">Dominated convergence theorem</a></p>
