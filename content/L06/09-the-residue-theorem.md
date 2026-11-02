---
id: f9
slide: Slide 10
title: The residue theorem
---

::: theorem {#thm:residue-theorem name="residue theorem"}
Let $f$ be holomorphic near $\{|z|\le R\}\setminus\{\zeta_1,\dots,\zeta_p\}$, with poles at $\zeta_1,\dots,\zeta_p\in\{|z|\lt R\}$. Then
\[ \oint_{|z|=R}f(z)\,dz=2\pi i\sum_{j=1}^p\class{ntn-res}{\operatorname{Res}}_{\zeta_j}f. \]
:::
::: proof

<ol>
<li><em>Isolate the poles.</em> Choose $r\gt0$ so small that the closed disks $|z-\zeta_j|\le r$ are pairwise disjoint, lie in $|z|\lt R$, and serve in @def:pole-of-order-m for each pole (if a radius works in that definition, so does every smaller one).</li>
<li><em>Move the circle.</em> For $0\lt\delta\le r/2$, @lem:moving-the-circle (with $C_j:|z-\zeta_j|=\delta$) gives $\oint_{|z|=R}f\,dz=\sum_j\oint_{|z-\zeta_j|=\delta}f\,dz$. The left side does not depend on $\delta$.</li>
<li><em>One pole at a time.</em> Drop the index $j$. On $|z-\zeta|=\delta$ use @prop:principal-part: $f$ is $\sum_{k=1}^mb_{m-k}(z-\zeta)^{-k}$ plus $h$. With $z=\zeta+\delta e^{i\theta}$, $dz=i\delta e^{i\theta}d\theta$,
\[ \oint_{|z-\zeta|=\delta}\frac{dz}{(z-\zeta)^k}=i\delta^{1-k}\int_0^{2\pi}e^{i(1-k)\theta}\,d\theta=\begin{cases}2\pi i,&k=1,\\0,&k\ge2,\end{cases} \]
because $\int_0^{2\pi}e^{il\theta}d\theta=0$ for every integer $l\ne0$ (as in @prop:1-z-2-has-zero-charge). Only $k=1$ survives, with coefficient $b_{m-1}=\class{ntn-res}{\operatorname{Res}}_\zeta f$. And $h$ is bounded, say by $H$, so $|\oint h\,dz|\le2\pi\delta H$ (ML estimate). Hence
\[ \oint_{|z-\zeta|=\delta}f\,dz=2\pi i\class{ntn-res}{\operatorname{Res}}_\zeta f+O(\delta). \]</li>
<li><em>Let $\delta\to0$.</em> Summing over $j$, the constant left side of step 2 equals $2\pi i\sum_j\class{ntn-res}{\operatorname{Res}}_{\zeta_j}f+O(\delta)$ for every small $\delta$, so it equals $2\pi i\sum_j\class{ntn-res}{\operatorname{Res}}_{\zeta_j}f$. <span class="qed">∎</span></li>
</ol>
:::
<p>Lecture 2 found the same rule physically (@cor:the-residue-theorem-point-charge-form, @prop:the-contour-integral-sees-only-the): a contour integral sees only the $\frac1{z-\zeta}$ terms, the "charges". Here it is proved for poles of any order. @prop:other-contours extends it to contours that are not circles, and [Laurent series](apx:E5) handle singularities that are not poles.</p>
