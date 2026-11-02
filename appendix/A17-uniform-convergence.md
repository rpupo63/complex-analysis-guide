---
id: A17
title: Uniform convergence
status:
- defined
- derived
---
<div class="env"><span class="hd">Definitions.</span> $f_n\to f$ <em>uniformly on a set $S$</em> if $\max_S|f_n-f|\to0$ (a supremum, if the maximum is not attained): one rate of convergence works at every point of $S$ at once. $f_n\to f$ <em>uniformly on every compact subset of $\Omega$</em> if this holds for each compact $K\subset\Omega$ separately; the rate may get worse near $\class{ntn-dOm}{\partial\Omega}$.</div>
<div class="env"><span class="hd">Proposition.</span> A uniform limit of continuous functions is continuous.</div>
::: proof
Let $f_n\to f$ uniformly on $S$, fix $z_0\in S$ and a tolerance $\epsilon\gt0$. Choose $n$ with $|f_n-f|\lt\epsilon/3$ on all of $S$, then (by continuity of $f_n$) a radius $\rho$ with $|f_n(z)-f_n(z_0)|\lt\epsilon/3$ for $|z-z_0|\lt\rho$. For such $z$,
\[ |f(z)-f(z_0)|\le|f(z)-f_n(z)|+|f_n(z)-f_n(z_0)|+|f_n(z_0)-f(z_0)|\lt\tfrac\epsilon3+\tfrac\epsilon3+\tfrac\epsilon3. \]
Uniformity is what lets one $n$ serve for both $z$ and $z_0$.
:::
<div class="env"><span class="hd">Proposition (uniformly Cauchy sequences converge uniformly).</span> If $\max_S|f_k-f_j|\to0$ as $j,k\to\infty$, then $f_k$ converges uniformly on $S$ to some $f$.</div>
::: proof
At each point $z$, the numbers $f_k(z)$ form a Cauchy sequence of reals, which converges (completeness of $\R$, cited); call the limit $f(z)$. Given $\epsilon\gt0$, pick $N$ with $|f_k-f_j|\lt\epsilon$ on $S$ for $j,k\ge N$. Letting $j\to\infty$ at each point gives $|f_k-f|\le\epsilon$ on $S$ for $k\ge N$: one $N$ for all points, which is uniform convergence.
:::
<p>Pointwise convergence is not enough: $x^n\to0$ for $0\le x\lt1$ but $1^n=1$, so the limit on $[0,1]$ jumps at $x=1$.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Uniform_convergence" target="_blank" rel="noopener">Uniform convergence</a> · <a href="https://en.wikipedia.org/wiki/Compact_convergence" target="_blank" rel="noopener">Compact convergence</a></p>
