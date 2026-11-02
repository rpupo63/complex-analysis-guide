---
id: j8
slide: Slide 9
title: Polynomials with coefficients $\pm1$
---

::: proposition {#prop:let-with-all-and-at}
Let $f(z)=\sum_{k=0}^n\varepsilon_kz^k$ with all $\varepsilon_k=\pm1$, and $0\lt\delta\lt1$. At most $\frac2\delta\log\frac2\delta$ zeros of $f$ lie in $|z|\le1-\delta$, whatever $n$ is.
:::
::: proof
Apply @cor:counting-zeros with $r=1-\delta$ and $R=1-\frac\delta2$.
<ul>
<li>$|f(0)|=|\varepsilon_0|=1$, so $\log|f(0)|=0$.</li>
<li>On $|z|=R$: $|f(z)|\le\sum_kR^k\lt\frac1{1-R}=\frac2\delta$, so $\log \class{ntn-Mr}{M}(R)\lt\log\frac2\delta$.</li>
<li>
\[ \log\frac Rr=-\log\frac{1-\delta}{1-\delta/2}=-\log\Big(1-\frac{\delta/2}{1-\delta/2}\Big)=-\log\Big(1-\frac\delta{2R}\Big)\gt\frac\delta{2R}\gt\frac\delta2, \]
using $-\log(1-x)\gt x$ for $0\lt x\lt1$ and $R\lt1$.</li>
</ul>
So $\class{ntn-nr}{n}(1-\delta)\lt\log\frac2\delta\big/\frac\delta2=\frac2\delta\log\frac2\delta$.
:::
::: corollary {#cor:zeros-hug-the-unit-circle name="zeros hug the unit circle"}
All but at most $\frac4\delta\log\frac2\delta$ zeros of $f$ lie in the annulus $1-\delta\lt|z|\lt\frac1{1-\delta}$.
:::
::: proof
$z^nf(1/z)=\sum_k\varepsilon_kz^{n-k}$ is again a $\pm1$ polynomial (of degree $n$, as $\varepsilon_0\ne0$). Its zeros are the $1/a$ for the zeros $a$ of $f$ (all nonzero, as $f(0)\ne0$), with the same multiplicities. A zero $a$ with $|a|\ge\frac1{1-\delta}$ gives a zero $1/a$ with $|1/a|\le1-\delta$, and @prop:let-with-all-and-at allows at most $\frac2\delta\log\frac2\delta$ of those. Add the at most $\frac2\delta\log\frac2\delta$ zeros in $|z|\le1-\delta$.
:::
<figure>{{fig:j8-1}}<figcaption>The zeros of a random $\pm1$ polynomial of degree $200$. Red: $|z|=1$; dashed: $|z|=0.9$. This sample has 6 zeros in $|z|\le0.9$.</figcaption></figure>
<p>Example: for $n=200$ and $\delta=0.1$, the bound allows $\frac2{0.1}\log20\approx59.9$, so at most $59$ zeros in $|z|\le0.9$; the random sample in the figure has $6$. The bound does not depend on $n$, so as $n$ grows almost all the $n$ zeros crowd towards the unit circle.</p>
