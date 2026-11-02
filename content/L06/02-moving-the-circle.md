---
id: f2
slide: Slide 3
title: Moving the circle
---
<p>The first consequence: an integral around a big circle can be traded for integrals around small circles surrounding the trouble spots.</p>

::: lemma {#lem:moving-the-circle name="moving the circle"}
Let $C$ be a circle and $C_1,\dots,C_p$ circles whose closed disks are pairwise disjoint and lie in the open disk of $C$, all oriented anticlockwise. Let $g$ be holomorphic near the closed region $A$ inside $C$ and outside the $C_j$. Then
\[ \oint_Cg\,dz=\sum_{j=1}^p\oint_{C_j}g\,dz. \]
:::
<figure>{{fig:f2-1}}<figcaption>@lem:moving-the-circle: the region $A$ lies inside $C$ and outside the $C_j$. With $A$ on its left, $\partial A$ runs anticlockwise around $C$ and clockwise around each $C_j$.</figcaption></figure>
::: proof
$A$ is the closed disk of $C$ with the open disks of the $C_j$ removed. It is bounded by the circles $C,C_1,\dots,C_p$, so @thm:cauchys-theorem applies to it. With $A$ on its left, $\partial A$ consists of $C$ anticlockwise and each $C_j$ clockwise. Reversing the direction of a curve changes the sign of the integral, so
\[ 0=\oint_{\partial A}g\,dz=\oint_Cg\,dz-\sum_{j=1}^p\oint_{C_j}g\,dz. \]
<span class="qed">∎</span>
:::
<p>Note what is <em>not</em> assumed: $g$ may be singular inside the small disks. The lemma is used in two ways. With one small circle around a singular point, it shows the integral does not depend on the radius (@thm:cauchys-integral-formula, @lem:logarithmic-derivative). With several, it splits a global integral into local contributions (@thm:residue-theorem, @thm:argument-principle).</p>
