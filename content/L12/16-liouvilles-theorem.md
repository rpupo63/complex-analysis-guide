---
id: n16
slide: Slide 17
title: Liouville's theorem
---
<p>Not every open set $U$ has a conformal map onto $D(0,1)$.</p>

::: theorem {#thm:liouville name=Liouville}
A bounded entire function is constant.
:::
::: proof
Let $|f|\le M$ and $f(z)=\sum_na_nz^n$ (an entire function is one power series, @thm:power-series). Cauchy's estimate (@cor:cauchys-estimate) on $|z|=R$ gives $|a_n|\le MR^{-n}$ for every $R\gt0$. Letting $R\to\infty$, $a_n=0$ for $n\ge1$.
:::

::: corollary {#cor:fundamental-theorem-of-algebra name="fundamental theorem of algebra"}
Every non-constant polynomial $p$ has a zero in $\mathbb C$.
:::
::: proof
Otherwise $1/p$ is entire. It is bounded: $|p(z)|\to\infty$ as $|z|\to\infty$ (the leading term dominates), so $|1/p|\le1$ outside some disk, and $1/p$ is bounded on that compact disk by continuity. By Liouville $1/p$ is constant, and so is $p$.
:::

::: corollary {#cor:there-is-no-conformal-map}
There is no conformal map of $\mathbb C$ onto $D(0,1)$.
:::
::: proof
It would be a bounded entire function, hence constant, hence not a bijection.
:::

::: remark {#rem:growth-bounds-the-same-proof name="growth bounds, the same proof"}
The proof of Liouville gives more. If $f$ is entire and $|f(z)|\le C(1+|z|)^k$, then Cauchy's estimate on $|z|=R$ gives $|a_n|\le C(1+R)^kR^{-n}\to0$ for $n\gt k$: $f$ is a polynomial of degree at most $k$. This is the tool for Problem 2(a) of the practice midterms. (@lem:no-zeros is the version for $\log|f|$.)
:::
