---
label: ex:charges-dipoles-and-contour-integrals
source: Homework 1, Problem 2
title: charges, dipoles and contour integrals
placement: w8
order: 1
---
Consider the complex electric field
\[ f(z)=\frac1{2\pi}\Big(\frac2{z-1}-\frac1{z+1}\Big)+\frac1{(z-i)^2}. \]
All curves are positively oriented.
<ol>
<li>Locate and state the strengths of the point charges. What does the term $1/(z-i)^2$ represent, and what is its net charge?</li>
<li>Compute $\oint_\gamma f\,dz$ for $\gamma_1:|z-1|=\frac14$, $\gamma_2:|z-i|=\frac14$, $\gamma_3:|z|=2$.</li>
<li>For each curve, state the corresponding circulation and flux.</li>
<li>Explain why the real and imaginary parts of $f$ are harmonic away from the three singular points.</li>
</ol>
<details class="sol"><summary>Hint</summary>
<ul>
<li>A term $\frac{q}{2\pi(z-z_0)}$ represents a point charge $q$ at $z_0$ (@rem:consequence-the-singularity-is-the-charge).</li>
<li>A second-order pole represents a dipole and has zero net charge (@prop:1-z-2-has-zero-charge, @prop:a-dipole).</li>
<li>$\oint_{|z-a|=r}\frac{dz}{z-a}=2\pi i$, and $\oint_{|z-a|=r}\frac{dz}{(z-a)^m}=0$ for $m\ge2$.</li>
<li>A term holomorphic on and inside a curve contributes zero (@cor:cauchys-theorem).</li>
<li>With $f=u-iv$, $\oint_\gamma f\,dz=\text{circulation}+i\cdot\text{flux}$ (@prop:contour-integral-circulation-i-cdot-flux).</li>
</ul>
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li>A term $\frac q{2\pi(z-z_0)}$ is the field of a charge $q$ at $z_0$ (@def:the-field-of-a-unit-charge, @rem:consequence-the-singularity-is-the-charge). So $\frac{2}{2\pi(z-1)}$: charge $+2$ at $z=1$; $\frac{-1}{2\pi(z+1)}$: charge $-1$ at $z=-1$. $\frac1{(z-i)^2}$ is a dipole at $i$ (@prop:a-dipole) with net charge $0$ (@prop:1-z-2-has-zero-charge).</li>
<li>$\gamma_1$ encloses only $1$: the charge term gives $\frac{2}{2\pi}\cdot2\pi i=2i$ (@cor:the-residue-theorem-point-charge-form: $\oint\frac{dz}{z-z_j}=2\pi i$), and the other terms are holomorphic inside, so contribute $0$ (@cor:cauchys-theorem): $\oint_{\gamma_1}f\,dz=2i$. $\gamma_2$ encloses only $i$: $\oint\frac{dz}{(z-i)^2}=0$ (the residue is $0$: @def:the-residue, @prop:the-contour-integral-sees-only-the) and the rest is holomorphic inside, so $0$. $\gamma_3$ encloses all three: by @cor:the-residue-theorem-point-charge-form and @prop:the-contour-integral-sees-only-the, $\frac1{2\pi}(2\cdot2\pi i-2\pi i)+0=i$.</li>
<li>By @prop:contour-integral-circulation-i-cdot-flux, write each answer as circulation $+\,i\cdot$flux: $\gamma_1$: $2i$, circulation $0$, flux $2$. $\gamma_2$: circulation $0$, flux $0$. $\gamma_3$: $i$, circulation $0$, flux $1=2-1$, the total enclosed charge (Gauss, @thm:gausss-theorem).</li>
<li>Away from $1,-1,i$, $f$ is holomorphic: each term is, as in @eg:a-charge-just-outside. Write $f=u-iv$. By Cauchy–Riemann (@thm:cauchy-riemann) $u_x=-v_y$ and $u_y=v_x$, i.e. $u_x+v_y=0$ and $v_x-u_y=0$: the field $(u,v)$ has no divergence and no curl, as in @prop:no-charge-means-holomorphic. Here $u,v$ are smooth, being rational functions of $x,y$ away from the poles (in general, @cor:holomorphic-functions-are-smooth). So @prop:if-satisfy-the-cauchy-riemann gives $\Delta u=\Delta v=0$: $u$ and $v$ are harmonic (@def:harmonic), and so are $\operatorname{Re}f=u$ and $\operatorname{Im}f=-v$.</li>
</ol>
</details>
