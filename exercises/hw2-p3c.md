---
label: ex:asymptotics-of-horse-races
source: Homework 2, Problem 3(c)
title: asymptotics of horse races
placement: f11
order: 3
---
Show that the poles of $\frac1{2-e^z}$ are the points $\log2+2\pi ik$, $k\in\mathbb Z$, all simple, and that $\frac1{2-e^z}-\frac1{2\log2}\cdot\frac1{1-z/\log2}$ extends holomorphically to $D(0,\rho)$, $\rho:=|\log2+2\pi i|=6.32\ldots$. Deduce $F_n=\frac{n!}{2(\log2)^{n+1}}+O(n!\,r^{-n})$ for every $r\lt\rho$.
<details class="sol"><summary>Hint</summary>
Residue at a simple pole: @prop:simple-poles-of-a-quotient (with $B=2-e^z$; the proof works for holomorphic $B$). Subtracting the principal part leaves a function holomorphic at $\log2$ (the $h$ of @prop:principal-part). Then Cauchy's estimate on $|z|=r$.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>Poles.</em> $2-e^z=0\iff e^z=2\iff z=\log2+2\pi ik$ ([C.8](apx:C8)). With $B:=2-e^z$ and $\zeta$ one of these points, $B'(\zeta)=-e^\zeta=-2\ne0$, so $B(z)=(z-\zeta)B_1(z)$ with $B_1$ holomorphic and $B_1(\zeta)=B'(\zeta)$ (a zero of order $1$, @def:order-of-a-zero). So $\frac1B=\frac{1/B_1}{z-\zeta}$ has a simple pole (@def:pole-of-order-m) with residue $\frac1{B_1(\zeta)}=-\frac12$ (@def:residue). This is @prop:simple-poles-of-a-quotient with $A=1$; there $B$ is a polynomial, but the proof only uses this factorization.</li>
<li><em>Principal part at $\log2$.</em> $\frac{-1/2}{z-\log2}=\frac{1/2}{\log2-z}=\frac1{2\log2}\cdot\frac1{1-z/\log2}$, exactly the subtracted term. Subtracting the principal part leaves the function $h$ of @prop:principal-part, holomorphic on a punctured disk about $\log2$ and bounded there, hence holomorphic at $\log2$ too (@lem:removable-singularities; or directly from the power series formula for $h$).</li>
<li><em>The disk.</em> The other poles have $|\log2+2\pi ik|\ge|\log2+2\pi i|=\rho$ for $k\ne0$ (the imaginary part is at least $2\pi$ in size). So the difference $D(z)$ is holomorphic on $D(0,\rho)$.</li>
<li><em>Coefficients.</em> $\frac{F_n}{n!}=[z^n]\frac1{2-e^z}=\frac1{2\log2}\cdot\frac1{(\log2)^n}+[z^n]D$ (Taylor coefficients at $0$, @thm:power-series, with $\frac1{1-z/\log2}=\sum(z/\log2)^n$). By Cauchy's estimate (@cor:cauchys-estimate) on $|z|=r$, $|[z^n]D|\le M_rr^{-n}$ for $r\lt\rho$. Multiply by $n!$. This is the same method as the stamp formula, @thm:the-stamp-formula: the poles nearest $0$ give the main term.</li>
</ol>
<p>The nearest singularity ($\log2\approx0.693$) gives the main term $\frac{n!}{2(\log2)^{n+1}}$; the next ones ($\log2\pm2\pi i$) control the error. This is the "analytic combinatorics" principle stated in the homework.</p>
</details>
