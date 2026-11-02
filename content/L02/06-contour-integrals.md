---
id: w6
slide: Slides 12–13
title: What Gauss's theorem says about complex functions
toc: Contour integrals
---

::: definition {#def:contour-integral name="contour integral"}
For a closed curve $\gamma$ and $f=u-iv$,
\[ \oint_\gamma f(z)\,dz:=\oint_\gamma(u-iv)(dx+i\,dy), \]
a [line integral](apx:A5): parametrize $\gamma$ by $z(s)=x(s)+iy(s)$ and integrate $f(z(s))\,z'(s)\,ds$.
:::

::: proposition {#prop:contour-integral-circulation-i-cdot-flux name="contour integral = circulation + $i\cdot$flux"}
For a positively oriented closed curve, with $\class{ntn-Ef}{E}=(u,v)$,
\[ \oint_\gamma f\,dz=\oint_\gamma \class{ntn-Ef}{E}\cdot t\,ds+i\oint_\gamma \class{ntn-Ef}{E}\cdot n\,ds. \]
So, by Gauss's theorem, $\oint_\gamma f\,dz=\text{circulation}+i\cdot\text{flux}=i\sum_{z_j\in D}q_j$.
:::
::: proof
Multiply out, using $i^2=-1$:
\[ \begin{aligned} f\,dz&=(u-iv)(dx+i\,dy)=u\,dx+iu\,dy-iv\,dx+v\,dy\\ &=\underbrace{(u\,dx+v\,dy)}_{\class{ntn-Ef}{E}\cdot t\,ds}+i\,\underbrace{(u\,dy-v\,dx)}_{\class{ntn-Ef}{E}\cdot n\,ds}. \end{aligned} \]
On a curve, the tangent displacement is $t\,ds=(dx,dy)$, so $\class{ntn-Ef}{E}\cdot t\,ds=u\,dx+v\,dy$. For a positively oriented curve (region on the left), the outward normal is the tangent turned clockwise by $90°$: $n\,ds=(dy,-dx)$, so $\class{ntn-Ef}{E}\cdot n\,ds=u\,dy-v\,dx$ ([curves and orientation](apx:C3)). Integrate around $\gamma$ and apply @thm:gausss-theorem.
:::

::: corollary {#cor:cauchys-theorem name="Cauchy's theorem"}
No charge inside $\gamma$, i.e. $f$ holomorphic on $D$: $\oint_\gamma f(z)\,dz=0$.
:::
::: proof
No $z_j$ lies in $D$, so the sum is empty.
:::

::: corollary {#cor:the-residue-theorem-point-charge-form name="the residue theorem, point-charge form"}
If $f$ is holomorphic on $D$ except for terms $\frac{q_j}{2\pi}\cdot\frac1{z-z_j}$ at points $z_j\in D$, then $\oint_\gamma f(z)\,dz=i\sum_{z_j\in D}q_j$. For example $\oint_\gamma\frac{dz}{z-z_j}=2\pi i$ for any $\gamma$ around $z_j$.
:::
::: proof
The general statement is @prop:contour-integral-circulation-i-cdot-flux. For the example, $\frac1{z-z_j}=\frac{2\pi}{2\pi}\cdot\frac1{z-z_j}$ is a charge $q=2\pi$, giving $i\cdot2\pi$. Directly on a circle: $z=z_j+re^{i\theta}$, $dz=ire^{i\theta}d\theta$, so $\oint\frac{dz}{z-z_j}=\int_0^{2\pi}\frac{ire^{i\theta}}{re^{i\theta}}d\theta=\int_0^{2\pi}i\,d\theta=2\pi i$.
:::
<p>Only the enclosed charges matter, not the shape of $\gamma$.</p>
