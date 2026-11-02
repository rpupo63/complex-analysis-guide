---
id: w4
slide: Slides 7–9
title: What does a charge contribute?
toc: What a charge contributes
---

::: definition {#def:the-field-of-a-unit-charge name="the field of a unit charge"}
For $(x,y)\ne(0,0)$, with $r^2=x^2+y^2$,
\[ \class{ntn-E0}{E_0}:=\frac1{2\pi}\,\frac{(x,y)}{x^2+y^2},\qquad\text{i.e.}\qquad \class{ntn-f0}{f_0}=u_0-iv_0=\frac1{2\pi}\cdot\frac1z. \]
:::
<p>The two forms agree: $\frac1z=\frac{\bar z}{z\bar z}=\frac{x-iy}{x^2+y^2}$, so $u_0-iv_0=\frac1{2\pi}\cdot\frac{x-iy}{r^2}$ gives $u_0=\frac{x}{2\pi r^2}$ and $v_0=\frac{y}{2\pi r^2}$. $\class{ntn-E0}{E_0}$ points straight away from the origin and has length $\frac1{2\pi r}$: it weakens like $1/r$, the two-dimensional version of Coulomb's $1/r^2$.</p>

::: definition {#def:meaning-of-operatorname-div-e-0 name="meaning of \"$\class{ntn-divc}{\operatorname{div}}\class{ntn-E0}{E_0}=\class{ntn-dlt}{\delta_0}$\""}
"$\class{ntn-divc}{\operatorname{div}}\class{ntn-E0}{E_0}=\class{ntn-dlt}{\delta_0}$" is shorthand for: for every region $D$ with [smooth boundary](apx:C3) not passing through $0$,
\[ \oint_{\partial D}\class{ntn-E0}{E_0}\cdot n\,ds=\begin{cases}1&\text{if }0\in D,\\0&\text{if }0\notin\overline D.\end{cases} \]
This is what the [divergence theorem](apx:A6) would give for a unit charge concentrated at the origin: total "divergence" $1$ at the single point $0$, and none elsewhere. Similarly "$\class{ntn-divc}{\operatorname{curl}}\class{ntn-E0}{E_0}=0$" means: the circulation $\oint \class{ntn-E0}{E_0}\cdot t\,ds$ around every such boundary is $0$. The symbol $\class{ntn-dlt}{\delta_0}$ is the [Dirac delta](apx:E13), a unit mass at $0$.
:::

::: theorem {#thm:the-claim name="the claim"}
$\class{ntn-divc}{\operatorname{div}}\class{ntn-E0}{E_0}=\class{ntn-dlt}{\delta_0}$ and $\class{ntn-divc}{\operatorname{curl}}\class{ntn-E0}{E_0}=0$, in the sense of @def:meaning-of-operatorname-div-e-0.
:::
::: proof

<ol>
<li><em>Away from $0$ (slide 8).</em> With $r^2=x^2+y^2$, the quotient rule gives $\partial_x\frac{x}{r^2}=\frac{r^2-x\cdot2x}{r^4}$ and $\partial_y\frac{y}{r^2}=\frac{r^2-2y^2}{r^4}$, so
\[ 2\pi\class{ntn-divc}{\operatorname{div}}\class{ntn-E0}{E_0}=\frac{\partial}{\partial x}\frac{x}{r^2}+\frac{\partial}{\partial y}\frac{y}{r^2}=\frac{r^2-2x^2}{r^4}+\frac{r^2-2y^2}{r^4}=\frac{2r^2-2(x^2+y^2)}{r^4}=0, \]
\[ 2\pi\class{ntn-divc}{\operatorname{curl}}\class{ntn-E0}{E_0}=\frac{\partial}{\partial x}\frac{y}{r^2}-\frac{\partial}{\partial y}\frac{x}{r^2}=\frac{-2xy+2xy}{r^4}=0. \]</li>
<li><em>Regions not containing $0$.</em> If $0\notin\overline D$, then $\class{ntn-E0}{E_0}$ is $C^1$ on $\overline D$ with zero divergence and curl, so the divergence theorem gives flux $\iint_D\class{ntn-divc}{\operatorname{div}}\class{ntn-E0}{E_0}=0$, and [Green's theorem](apx:A6) gives circulation $\iint_D\class{ntn-divc}{\operatorname{curl}}\class{ntn-E0}{E_0}=0$.</li>
<li><em>Through a circle $|z|=r$ (slide 9).</em> The outward normal is $n=(x,y)/r$, so
\[ \class{ntn-E0}{E_0}\cdot n=\frac1{2\pi}\cdot\frac{x\cdot x+y\cdot y}{r^2\cdot r}=\frac1{2\pi r},\qquad\oint_{|z|=r}\class{ntn-E0}{E_0}\cdot n\,ds=\frac1{2\pi r}\cdot2\pi r=1\quad\text{for every }r. \]
Because $\class{ntn-E0}{E_0}$ is radial, it is perpendicular to the circle's tangent $t$, so $\class{ntn-E0}{E_0}\cdot t=0$ and the circulation around the circle is $0$.</li>
<li><em>Through any loop around $0$.</em> Let $0\in D$ and remove a small closed disk $|z|\le\epsilon$ inside $D$. On the remaining region $D_\epsilon$ (with a hole), $\class{ntn-E0}{E_0}$ is $C^1$ with zero divergence and curl. Its boundary is $\partial D$ (traversed with outward normal) together with the small circle, whose outward normal for $D_\epsilon$ points <em>towards</em> $0$. The divergence theorem on $D_\epsilon$ gives
\[ 0=\iint_{D_\epsilon}\class{ntn-divc}{\operatorname{div}}\class{ntn-E0}{E_0}=\oint_{\partial D}\class{ntn-E0}{E_0}\cdot n\,ds-\oint_{|z|=\epsilon}\class{ntn-E0}{E_0}\cdot n_{\text{away from }0}\,ds=\oint_{\partial D}\class{ntn-E0}{E_0}\cdot n\,ds-1, \]
so the flux out of $\partial D$ is $1$. Green's theorem on $D_\epsilon$ gives in the same way that the circulation around $\partial D$ equals the circulation around the small circle, which is $0$ by step 3. So no curl is concentrated at the origin. <span class="qed">∎</span></li>
</ol>
:::

::: remark {#rem:consequence-the-singularity-is-the-charge name="consequence: the singularity is the charge"}
Maxwell's equations are linear. So adding $q \class{ntn-f0}{f_0}=\frac{q}{2\pi}\cdot\frac1z$ to $f$ adds $q\,\class{ntn-dlt}{\delta_0}$ to $\rho$ and nothing to $\partial_tB$ (the magnetic term in Faraday's law, so the field stays static). Translating the origin to $z_0$:
<p style="text-align:center"><b>A point charge $q$ at $z_0$ is the term $\dfrac{q}{2\pi}\cdot\dfrac1{z-z_0}$ in $f$. The singularity is the charge.</b></p>
The voltage of the unit charge is $\class{ntn-Phi}{\Phi}_0=-\frac1{2\pi}\log|z|$, since $\nabla\log|z|=\frac{(x,y)}{r^2}=2\pi \class{ntn-E0}{E_0}$ and $\class{ntn-Ef}{E}=-\nabla\class{ntn-Phi}{\Phi}$. Lecture 5 uses exactly this logarithm as its barrier (@def:the-barrier; [logarithmic potential](apx:E6)).
:::
