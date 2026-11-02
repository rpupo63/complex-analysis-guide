---
id: f4
slide: Slide 5
title: Holomorphic functions are power series
---
<p>This answers the question left open in @sec:x1: every holomorphic function is analytic (@def:complex-analytic).</p>

::: theorem {#thm:power-series name="power series"}
Let $f$ be holomorphic near $|z-z_0|\le r$. Then
\[ f(w)=\sum_{n\ge0}a_n(w-z_0)^n\quad\text{for every }w\text{ with }|w-z_0|\lt r,\qquad a_n:=\frac1{2\pi i}\oint_{|z-z_0|=r}f(z)\,(z-z_0)^{-n-1}\,dz. \]
:::
::: proof
Fix $w$ and put $\rho:=|w-z_0|\lt r$.
<ol>
<li><em>A finite geometric series with remainder.</em> For any complex $q\ne1$ and $N\ge1$, $(1-q)\sum_{n\lt N}q^n=1-q^N$, so
\[ \frac1{1-q}=\sum_{n\lt N}q^n+\frac{q^N}{1-q}. \]</li>
<li><em>Expand the Cauchy kernel.</em> For $|z-z_0|=r$ put $q:=\frac{w-z_0}{z-z_0}$, so $|q|=\rho/r\lt1$. Since $z-w=(z-z_0)-(w-z_0)=(z-z_0)(1-q)$,
\[ \frac1{z-w}=\frac1{z-z_0}\cdot\frac1{1-q}=\sum_{n\lt N}\frac{(w-z_0)^n}{(z-z_0)^{n+1}}+\frac{q^N}{(z-z_0)(1-q)}=\sum_{n\lt N}\frac{(w-z_0)^n}{(z-z_0)^{n+1}}+\frac{q^N}{z-w}. \]</li>
<li><em>Integrate.</em> Multiply by $\frac{f(z)}{2\pi i}$ and integrate over $|z-z_0|=r$. By @thm:cauchys-integral-formula the left side gives $f(w)$, and each term of the sum gives $a_n(w-z_0)^n$:
\[ f(w)=\sum_{n\lt N}a_n(w-z_0)^n+R_N,\qquad R_N:=\frac1{2\pi i}\oint_{|z-z_0|=r}\frac{f(z)\,q^N}{z-w}\,dz. \]</li>
<li><em>The remainder tends to $0$.</em> Let $M:=\max_{|z-z_0|=r}|f|$, which exists because $|f|$ is continuous on the compact circle ([extreme value theorem](apx:C5)). On the circle, $|q|^N=(\rho/r)^N$ and $|z-w|\ge|z-z_0|-|w-z_0|=r-\rho$. The circle has length $2\pi r$, so by the [ML estimate](apx:A25)
\[ |R_N|=\Big|\frac1{2\pi i}\oint\frac{f(z)\,q^N}{z-w}\,dz\Big|\le\frac{1}{2\pi}\cdot2\pi r\cdot\frac{M(\rho/r)^N}{r-\rho}=\frac{rM}{r-\rho}\Big(\frac\rho r\Big)^N\longrightarrow0\qquad(N\to\infty). \]</li>
</ol>
So the partial sums converge to $f(w)$.
:::
<p>Two remarks. The coefficients $a_n$ do not depend on $w$, so one series represents $f$ on the whole open disk. And the radius is as large as holomorphy allows: if $f$ is holomorphic near every closed disk $|z-z_0|\le r$ with $r\lt R$, the series converges on $|w-z_0|\lt R$, because all these $r$ give the same coefficients (they are $f^{(n)}(z_0)/n!$, @thm:cauchys-formula-for-derivatives). Conversely, a convergent [power series](apx:A19) is holomorphic, so "holomorphic" and "analytic" are the same class.</p>
