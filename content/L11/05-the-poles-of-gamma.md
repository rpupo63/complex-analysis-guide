---
id: m5
slide: Slide 6
title: The poles of $\Gamma$
---
<p>Recall (@def:pole-of-order-m with $m=1$, and @def:residue): $f$ has a <em>simple pole</em> at $a$ with <em>residue</em> $c$ if $f(z)=\frac{g(z)}{z-a}$ near $a$, with $g$ holomorphic near $a$ and $g(a)=c\ne0$.</p>

::: proposition {#prop:poles-of-gamma name="poles of $\Gamma$"}
For each integer $n\ge0$, $\Gamma$ has a simple pole at $-n$, with residue $\dfrac{(-1)^n}{n!}$.
:::
::: proof
On $\class{ntn-Dar}{D}(-n,1)\setminus\{-n\}$: every point has real part $\gt-n-1$, and the only non-positive integer in $\class{ntn-Dar}{D}(-n,1)$ is $-n$. So this punctured disk lies in $\class{ntn-Wn}{W_{n+1}}$, where $\Gamma=\class{ntn-Gn}{\Gamma_{n+1}}$:
\[ \Gamma(z)=\frac{\Gamma(z+n+1)}{z(z+1)\cdots(z+n)}=\frac{g(z)}{z+n},\qquad g(z):=\frac{\Gamma(z+n+1)}{z(z+1)\cdots(z+n-1)}. \]
$g$ is holomorphic on all of $\class{ntn-Dar}{D}(-n,1)$: there $\operatorname{Re}(z+n+1)\gt0$, and $z\ne0,-1,\dots,-n+1$ (these are at distance $\ge1$ from $-n$). And
\[ g(-n)=\frac{\Gamma(1)}{(-n)(-n+1)\cdots(-1)}=\frac1{(-1)^nn!}=\frac{(-1)^n}{n!}\ne0. \]
<span class="qed">∎</span>
:::
