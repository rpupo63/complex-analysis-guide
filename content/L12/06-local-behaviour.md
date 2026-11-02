---
id: n6
slide: Slide 7
title: Local behaviour
---

::: theorem {#thm:local-behaviour name="local behaviour"}
Let $f$ be holomorphic near $z_0$, $w_0:=f(z_0)$, and let $f-w_0$ have a zero of order $m\ge1$ at $z_0$. Then for every small enough $r\gt0$ there is $\delta\gt0$ such that for each $w\in D(w_0,\delta)$, $f-w$ has exactly $m$ zeros in $D(z_0,r)$, counted with multiplicity.
:::
<p>So near $z_0$, $f$ behaves like $w_0+a_m(z-z_0)^m$, which takes each value $w$ near $w_0$ exactly $m$ times (the $m$ roots of $(z-z_0)^m=\frac{w-w_0}{a_m}$).</p>
::: proof

<ol>
<li><em>Taylor.</em> The Taylor coefficients of $f-w_0$ at $z_0$ vanish below order $m$, and $a_m\ne0$. By @cor:taylor-remainder there are $\rho,C\gt0$ with
\[ f(z)-w=\big[a_m(z-z_0)^m-(w-w_0)\big]+E(z),\qquad|E(z)|\le C|z-z_0|^{m+1}\ \ (|z-z_0|\le\rho). \]</li>
<li><em>Choose $r$ and $\delta$.</em> Take $r\le\rho$ with $Cr\lt\frac{|a_m|}2$, and $\delta:=\frac{|a_m|r^m}2$. Let $|w-w_0|\lt\delta$.</li>
<li><em>The model has $m$ zeros in the disk.</em> The bracket vanishes when $(z-z_0)^m=\frac{w-w_0}{a_m}$: $m$ roots (one root of order $m$ if $w=w_0$), all of modulus $\big(\frac{|w-w_0|}{|a_m|}\big)^{1/m}\lt\big(\frac{r^m}2\big)^{1/m}\lt r$.</li>
<li><em>Compare on the circle.</em> On $|z-z_0|=r$,
\[ \big|a_m(z-z_0)^m-(w-w_0)\big|\ge|a_m|r^m-|w-w_0|\gt\frac{|a_m|r^m}2\gt Cr^{m+1}\ge|E(z)|, \]
using $Cr\lt\frac{|a_m|}2$ in the third step.</li>
<li><em>Rouché.</em> By @thm:rouche, with the bracket in the role of $f$ and $f-w$ in the role of $g$ (their difference is $E$), $f-w$ has as many zeros in $D(z_0,r)$ as the bracket: $m$. <span class="qed">∎</span></li>
</ol>
:::
