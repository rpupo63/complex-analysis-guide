---
id: m6
slide: Slide 7
title: $1/\Gamma$ is entire
---

::: theorem {#thm:weierstrass-product-for-1-gamma name="Weierstrass product for $1/\Gamma$"}
Let $\class{ntn-gam}{\gamma}:=\lim_{N\to\infty}\class{ntn-aN}{a_N}$, where $\class{ntn-aN}{a_N}:=\sum_{n\le N}\frac1n-\log N$ (Euler's constant, $\class{ntn-gam}{\gamma}\approx0.5772$). Then
\[ \class{ntn-Rg}{R}(z):=z\,e^{\class{ntn-gam}{\gamma} z}\prod_{n\ge1}\Big(1+\frac zn\Big)e^{-z/n} \]
is entire, with zeros exactly at $0,-1,-2,\dots$ (all simple), and $\Gamma(z)\class{ntn-Rg}{R}(z)=1$ for $z\in \class{ntn-Wset}{W}$. Hence $\Gamma$ has no zeros, and $1/\Gamma$ extends to the entire function $R$.
:::
<p><b>Idea.</b> For $x\gt0$, the integrals $\int_0^Nt^{x-1}(1-\frac tN)^Ndt$ tend to $\Gamma(x)$, since $(1-\frac tN)^N\to e^{-t}$, and they can be computed exactly. Their reciprocals are the partial products of $R$.</p>
::: proof {title="Proof, part 1: $\class{ntn-gam}{\gamma}$ exists."}
Since $\log(N+1)=\sum_{n\le N}\log(1+\frac1n)$ (telescoping: $\log\frac{n+1}n=\log(n+1)-\log n$),
\[ \class{ntn-aN}{a_N}-\log\Big(1+\frac1N\Big)=\sum_{n\le N}\frac1n-\log(N+1)=\sum_{n\le N}\Big(\frac1n-\log\Big(1+\frac1n\Big)\Big). \]
From $x-\frac{x^2}2\le\log(1+x)\le x$ for $x\ge0$, the terms lie in $[0,\frac1{2n^2}]$: they are $O(n^{-2})$, so the series converges. As $\log(1+\frac1N)\to0$, $\class{ntn-aN}{a_N}$ converges.
:::
::: proof {title="Part 2: $R$ is entire, with the stated zeros."}
On each disk $|z|\le\rho$, for $n\ge2\rho$ we have $|z/n|\le\frac12$, and $(1+\frac zn)e^{-z/n}=\class{ntn-Ep}{E_1}(-\frac zn)$ (@def:weierstrass-factors), so by @lem:convergence-factors
\[ \Big|\Big(1+\frac zn\Big)e^{-z/n}-1\Big|=\Big|1-\class{ntn-Ep}{E_1}\Big(-\frac zn\Big)\Big|\le4\frac{\rho^2}{n^2}, \]
which is summable. By the product lemma (@lem:products), $R$ is entire, and its zeros are those of its factors: $z=0$, and $z=-n$ from $1+\frac zn$; each simple.
:::
