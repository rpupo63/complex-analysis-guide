---
id: h1
slide: Slide 2
title: 'Warm-up: $\int dx/(1+x^2)$'
---
<p>The idea of the lecture: a real integral $\int_{-\infty}^\infty$ is the limit of $\int_{-R}^R$; close the segment $[-R,R]$ into a loop in $\mathbb C$, evaluate the loop integral by residues, and show the added piece vanishes as $R\to\infty$. The loops used are half-disks, rectangles and sectors, not circles, so we first extend Part II's two theorems to them.</p>

::: proposition {#prop:other-contours name="other contours"}
@thm:cauchys-theorem and @thm:residue-theorem hold for every bounded closed region $D$ whose boundary consists of finitely many piecewise $C^1$ closed curves (a half-disk, a rectangle, a circular sector), oriented with $D$ on the left: if $f$ is holomorphic near $D$ then $\oint_{\partial D}f\,dz=0$; and if $f$ is holomorphic near $D$ except for poles $\zeta_j$ in the interior of $D$, then $\oint_{\partial D}f\,dz=2\pi i\sum_j\class{ntn-res}{\operatorname{Res}}_{\zeta_j}f$.
:::
::: proof
[Green's theorem](apx:A6) holds for such regions, and the proof of @thm:cauchys-theorem used nothing else. For the residue form, remove from $D$ small open disks $|z-\zeta_j|\lt\delta$ (disjoint, inside the interior of $D$). Cauchy's theorem on what remains gives $\oint_{\partial D}f\,dz=\sum_j\oint_{|z-\zeta_j|=\delta}f\,dz$, exactly as in @lem:moving-the-circle, and step 3 of the proof of @thm:residue-theorem evaluates each small circle as $\delta\to0$.
:::
<p>The slides use this without comment ("by the residue theorem").</p>

::: proposition {#prop:x}
$\displaystyle\int_{-\infty}^\infty\frac{dx}{1+x^2}=\pi$.
:::
<figure>{{fig:h1-1}}<figcaption>@sec:h1: the contour $[-R,R]$ followed by the semicircle $\class{ntn-SR}{S_R}$. Only the pole at $i$ is enclosed.</figcaption></figure>
::: proof

<ol>
<li><em>Poles.</em> $f(z)=\frac1{1+z^2}=\frac1{(z-i)(z+i)}$ has simple poles at $\pm i$. For $R\gt1$ close $[-R,R]$ by the semicircle $\class{ntn-SR}{S_R}$ of radius $R$ in the upper half-plane, traversed anticlockwise. Only $i$ is inside, and $\class{ntn-res}{\operatorname{Res}}_if=\frac1{2i}$ (@prop:simple-poles-of-a-quotient: $A=1$, $B=1+z^2$, $B'(i)=2i$).</li>
<li><em>Residue theorem</em> (@prop:other-contours):
\[ \int_{-R}^R\frac{dx}{1+x^2}+\int_{\class{ntn-SR}{S_R}}\frac{dz}{1+z^2}=2\pi i\cdot\frac1{2i}=\pi. \]</li>
<li><em>The arc vanishes.</em> On $\class{ntn-SR}{S_R}$, $|1+z^2|\ge|z|^2-1=R^2-1$, and $\class{ntn-SR}{S_R}$ has length $\pi R$. By the [ML estimate](apx:A25),
\[ \Big|\int_{\class{ntn-SR}{S_R}}f\,dz\Big|\le\frac{\pi R}{R^2-1}\longrightarrow0\qquad(R\to\infty). \]</li>
<li>So $\int_{-R}^R\frac{dx}{1+x^2}\to\pi$. The integrand is positive and integrable ($\le1/x^2$ for large $|x|$), so this limit is the [improper integral](apx:A22). <span class="qed">∎</span></li>
</ol>
:::
<p>The answer is no surprise ($\arctan x$ runs from $-\pi/2$ to $\pi/2$), but the method needs no antiderivative, and the next sections apply it where none is available.</p>
