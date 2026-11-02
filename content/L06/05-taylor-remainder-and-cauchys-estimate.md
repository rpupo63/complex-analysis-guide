---
id: f5
slide: Slide 6
title: Taylor remainder and Cauchy's estimate
---
<p>Throughout this section, $f$ is holomorphic near $|z-z_0|\le r$, with the coefficients $a_n$ of @thm:power-series, and $M:=\max_{|z-z_0|=r}|f|$.</p>

::: corollary {#cor:taylor-remainder name="Taylor remainder"}
If $|w-z_0|\le r/2$, then
\[ \Big|f(w)-\sum_{n\lt N}a_n(w-z_0)^n\Big|\le2M\Big(\frac{|w-z_0|}{r}\Big)^N. \]
In [big-$O$ notation](apx:A20): $f(w)=\sum_{n\lt N}a_n(w-z_0)^n+O(|w-z_0|^N)$ as $w\to z_0$.
:::
::: proof
The left side is $|R_N|$ from the proof of @thm:power-series, which is at most $\frac{rM}{r-\rho}(\rho/r)^N$ with $\rho=|w-z_0|$. If $\rho\le r/2$ then $r-\rho\ge r/2$, so $\frac{r}{r-\rho}\le2$.
:::

::: corollary {#cor:cauchys-estimate name="Cauchy's estimate"}
$|a_n|\le M\,r^{-n}$ for every $n\ge0$.
:::
::: proof
On the circle, $|f(z)(z-z_0)^{-n-1}|\le M\,r^{-n-1}$. The circle has length $2\pi r$, so by the ML estimate $|a_n|\le\frac1{2\pi}\cdot2\pi r\cdot Mr^{-n-1}=Mr^{-n}$.
:::
<p>The Taylor remainder is the workhorse of this Part. Its typical use: if $a_0=\dots=a_{m-1}=0\ne a_m$, then $f(w)=a_m(w-z_0)^m+O(|w-z_0|^{m+1})$, so near $z_0$ the function behaves like its first nonzero term (@thm:isolated-zeros, @lem:logarithmic-derivative, @prop:factorization-in-a-disk, @thm:identity-theorem-l10). Cauchy's estimate controls coefficients by the size of $f$ on a circle; @lem:no-zeros is a refinement of it.</p>
