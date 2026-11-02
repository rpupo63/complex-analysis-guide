---
id: f7
slide: Slide 8
title: Zeros are isolated
---

::: theorem {#thm:isolated-zeros name="isolated zeros"}
Let $f\not\equiv0$ be holomorphic on a [connected](apx:C4) open set $\Omega$, and $f(z_0)=0$. Then there is $\delta\gt0$ such that $f(w)\ne0$ for $0\lt|w-z_0|\lt\delta$.
:::
::: proof

<ol>
<li><em>Not all Taylor coefficients vanish.</em> Let $S:=\{z\in\Omega:f^{(n)}(z)=0\text{ for all }n\ge0\}$.
<ul>
<li>$S$ is closed in $\Omega$: it is the set where every one of the continuous functions $f^{(n)}$ (@cor:holomorphic-functions-are-smooth) vanishes, and a limit of zeros of a continuous function is a zero.</li>
<li>$S$ is open: if $z_1\in S$, take a closed disk $|z-z_1|\le r$ inside $\Omega$. By [Theorems #](@thm:power-series) and [#](@thm:cauchys-formula-for-derivatives), $f(z)=\sum_n\frac{f^{(n)}(z_1)}{n!}(z-z_1)^n=0$ on the open disk $|z-z_1|\lt r$. Then all derivatives of $f$ vanish on that open disk too, so the disk lies in $S$.</li>
<li>$S\ne\Omega$, since $f\not\equiv0$. As $\Omega$ is connected, the only subsets both open and closed are $\emptyset$ and $\Omega$, so $S=\emptyset$.</li>
</ul>
In particular $z_0\notin S$: the Taylor coefficients $a_n=f^{(n)}(z_0)/n!$ at $z_0$ are not all $0$.</li>
<li><em>The first nonzero term dominates.</em> Let $a_m$ be the first nonzero coefficient; $m\ge1$ because $a_0=f(z_0)=0$. Take $r$ with $|z-z_0|\le r$ inside $\Omega$ and $M:=\max_{|z-z_0|=r}|f|$. By @cor:taylor-remainder with $N=m+1$, and since $a_n=0$ for $n\lt m$, for $|w-z_0|\le r/2$:
\[ |f(w)-a_m(w-z_0)^m|\le2M\Big(\frac{|w-z_0|}r\Big)^{m+1}, \]
so
\[ |f(w)|\ge|w-z_0|^m\Big(|a_m|-\frac{2M}{r^{m+1}}|w-z_0|\Big)\gt0\qquad\text{if }0\lt|w-z_0|\lt\min\Big(\frac r2,\frac{|a_m|\,r^{m+1}}{2M}\Big). \]</li>
</ol>
<span class="qed">∎</span>
:::
<p>This proves @cor:isolated-zeros, stated in Lecture 1 without proof: if distinct zeros $z_n$ converge to $z\in\Omega$, then $f(z)=0$ by continuity, and $z$ is a zero that is not isolated, so $f\equiv0$. The stronger identity theorem is @thm:identity-theorem-l10.</p>
::: definition {#def:order-of-a-zero name="order of a zero"}
The number $m$ in step 2, the index of the first nonzero Taylor coefficient at $z_0$, is the <em>order</em> (or multiplicity) of the zero. @def:zero-of-order-m restates it.
:::
