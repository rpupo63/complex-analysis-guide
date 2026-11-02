---
id: t12
slide: Slide 12
title: Uniform limits of harmonic functions
toc: Uniform limits
---

::: corollary {#cor:uniform-limits name="uniform limits"}
Let $h_n$ be harmonic on $\Omega$ and let $h_n\to v$ [uniformly on every compact subset](apx:A17) of $\Omega$. Then $v$ is smooth and harmonic.
:::
::: proof

<ol>
<li><em>$v$ is continuous.</em> Each $z_0\in\Omega$ has a closed disk $D$ about it inside $\Omega$, which is compact. On $D$, $v$ is a uniform limit of continuous functions, hence continuous ([A.17](apx:A17)).</li>
<li><em>$v$ has the mean value property.</em> Let the closed disk $D$ of radius $r$ about $z_0$ lie in $\Omega$. Each $h_n$ is harmonic, so by @thm:mean-value-property
\[ h_n(z_0)=\frac1{2\pi}\int_0^{2\pi}h_n(z_0+re^{i\theta})\,d\theta. \]
As $n\to\infty$ the left side tends to $v(z_0)$. On the right, $D$ is compact, so the convergence is uniform on the circle:
\[ \Big|\frac1{2\pi}\int_0^{2\pi}h_n(z_0+re^{i\theta})\,d\theta-\frac1{2\pi}\int_0^{2\pi}v(z_0+re^{i\theta})\,d\theta\Big|\le\frac1{2\pi}\int_0^{2\pi}|h_n-v|\,d\theta\le\max_D|h_n-v|\longrightarrow0. \]
So both sides converge, and $v(z_0)$ equals the average of $v$ over the circle.</li>
<li><em>Conclude</em> by @thm:converse-of-the-mean-value-property. <span class="qed">∎</span></li>
</ol>
:::
