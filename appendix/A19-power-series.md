---
id: A19
title: Power series
status:
- defined
- cited
---
<p>A <em>power series</em> about $z_0$ is $\sum_{n\ge0}c_n(z-z_0)^n$ with complex coefficients.</p>
<div class="env"><span class="hd">Theorem (cited).</span> There is a <em>radius of convergence</em> $\rho\in[0,\infty]$, namely $1/\rho=\limsup_n|c_n|^{1/n}$, such that:
<ol type="a">
<li>the series converges absolutely for $|z-z_0|\lt\rho$ and diverges for $|z-z_0|\gt\rho$;</li>
<li>it converges uniformly on every closed disk $|z-z_0|\le r$ with $r\lt\rho$;</li>
<li>its sum $f$ is holomorphic on $|z-z_0|\lt\rho$, and may be differentiated term by term: $f'(z)=\sum_{n\ge1}nc_n(z-z_0)^{n-1}$, a series with the same radius. Likewise $\sum_n\frac{c_n}{n+1}(z-z_0)^{n+1}$ has the same radius and is a primitive of $f$.</li>
</ol></div>
<p>Part (b) follows from the Weierstrass M-test ([A.21](apx:A21)): if $r\lt r_1\lt\rho$, the terms are eventually bounded by $(r/r_1)^n$. Part (c) says analytic functions (@def:complex-analytic) are holomorphic; @thm:power-series gives the converse. A series with $\rho=\infty$ defines an <em>entire</em> function. Examples: $e^z=\sum z^n/n!$, $\sin z=\sum(-1)^kz^{2k+1}/(2k+1)!$, $\cos z=\sum(-1)^kz^{2k}/(2k)!$, all with $\rho=\infty$, and $\sum z^n=\frac1{1-z}$ with $\rho=1$.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Power_series" target="_blank" rel="noopener">Power series</a> · <a href="https://en.wikipedia.org/wiki/Radius_of_convergence" target="_blank" rel="noopener">Radius of convergence</a></p>
