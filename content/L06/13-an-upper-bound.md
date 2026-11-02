---
id: f13
slide: Slide 14
title: An upper bound
---

::: lemma {#lem:log-p-as-a-series name="$\log P$ as a series"}
For $|z|\lt1$ define, with [principal logarithms](apx:C8),
\[ \log \class{ntn-Pz}{P}(z):=\sum_{k\ge1}-\log(1-z^k). \]
Then $e^{\log \class{ntn-Pz}{P}(z)}=\class{ntn-Pz}{P}(z)$, and
\[ \log \class{ntn-Pz}{P}(z)=\sum_{k\ge1}\sum_{m\ge1}\frac{z^{km}}m=\sum_{m\ge1}\frac1m\cdot\frac{z^m}{1-z^m}. \]
:::
::: proof
For $|w|\lt1$, $-\log(1-w)=\sum_{m\ge1}\frac{w^m}m$ ([C.8](apx:C8)); take $w=z^k$. The double series converges absolutely:
\[ \sum_k\sum_m\frac{|z|^{km}}m\le\sum_k\frac{|z|^k}{1-|z|}=\frac{|z|}{(1-|z|)^2}. \]
So its terms may be summed in either order ([A.21](apx:A21)); summing over $k$ first, $\sum_kz^{km}=\frac{z^m}{1-z^m}$. Finally, $\exp$ is continuous and turns sums into products, so
\[ e^{\log \class{ntn-Pz}{P}(z)}=\lim_K\prod_{k\le K}e^{-\log(1-z^k)}=\lim_K\prod_{k\le K}\frac1{1-z^k}=\class{ntn-Pz}{P}(z) \]
by @prop:eulers-product.
:::

::: lemma {#lem:on-the-real-axis name="on the real axis"}
For $t\gt0$, $\ \log \class{ntn-Pz}{P}(e^{-t})\le\dfrac{\pi^2}{6t}$.
:::
::: proof
By @lem:log-p-as-a-series with $z=e^{-t}$, $\frac{z^m}{1-z^m}=\frac{1}{e^{mt}-1}$. Since $e^x-1\ge x$ for $x\ge0$,
\[ \log \class{ntn-Pz}{P}(e^{-t})=\sum_{m\ge1}\frac1m\cdot\frac1{e^{mt}-1}\le\sum_{m\ge1}\frac1m\cdot\frac1{mt}=\frac1t\sum_{m\ge1}\frac1{m^2}=\frac{\pi^2}{6t}, \]
using the [Basel sum](apx:E18) $\sum1/m^2=\pi^2/6$.
:::

::: theorem {#thm:upper-bound name="upper bound"}
$\class{ntn-pn}{p}(n)\le e^{\pi\sqrt{2n/3}}$ for every $n\ge1$.
:::
::: proof
For $0\lt r\lt1$, every term of $\class{ntn-Pz}{P}(r)=\sum_mp(m)r^m$ is positive, so one term is at most the sum: $\class{ntn-pn}{p}(n)r^n\le \class{ntn-Pz}{P}(r)$. With $r=e^{-t}$ and @lem:on-the-real-axis,
\[ \log \class{ntn-pn}{p}(n)\le\log \class{ntn-Pz}{P}(e^{-t})+nt\le\frac{\pi^2}{6t}+nt\qquad\text{for every }t\gt0. \]
The right side is smallest when its derivative $-\frac{\pi^2}{6t^2}+n$ vanishes, at $t=\pi/\sqrt{6n}$. There both terms equal $\pi\sqrt{n/6}$: $nt=\frac{\pi n}{\sqrt{6n}}=\pi\sqrt{n/6}$ and $\frac{\pi^2}{6t}=\frac{\pi\sqrt{6n}}6=\pi\sqrt{n/6}$. The sum is $2\pi\sqrt{n/6}=\pi\sqrt{2n/3}$.
:::
<p>The method (bound a coefficient by the function's size on a circle, then choose the radius well) is Cauchy's estimate, @cor:cauchys-estimate, applied with $r=e^{-t}$ and positive coefficients. It loses only a factor of order $n$: for $n=100$ the bound is about $1.4\times10^{11}$ against $\class{ntn-pn}{p}(100)\approx1.9\times10^8$. Recovering that factor needs the whole circle, not just its largest point.</p>
