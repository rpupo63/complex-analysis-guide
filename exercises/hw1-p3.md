---
label: ex:poincares-inequality
source: Homework 1, Problem 3
title: Poincaré's inequality
placement: s18
order: 1
---
Let $\Omega$ be a finite union of grid squares in the strip $0\lt x\lt L$, and $v$ continuous, piecewise $C^1$, zero on $\partial\Omega$. Extend $v$ by zero outside $\Omega$.
<ol>
<li>Explain why the extension is continuous and piecewise $C^1$.</li>
<li>Prove $\norm{v}_{L^2(\Omega)}\le L\norm{\nabla v}_{L^2(\Omega)}$.</li>
<li>Suppose every $v_n$ vanishes on $\partial\Omega$ and $\nabla v_n$ is Cauchy in $L^2$. Prove that $v_n$ is Cauchy in $L^2$. Where was this used in Lecture 3?</li>
</ol>
<details class="sol"><summary>Hint</summary>
<ul>
<li>After extending by zero, fix $y$ and write $v(x,y)=\int_0^x\partial_xv(s,y)\,ds$.</li>
<li>Apply [Cauchy–Schwarz](apx:A12) to the one-dimensional integral.</li>
<li>Use $0\lt x\lt L$, then integrate first in $x$ and afterwards in $y$.</li>
<li>Bound $|\partial_xv|$ by $|\nabla v|$ after integrating.</li>
<li>For the last part, apply the inequality to $v_n-v_m$.</li>
</ul>
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li>(This is the extension used in the proof of @thm:poincares-inequality.) <em>Continuous:</em> inside $\Omega$ and outside $\overline\Omega$ there is nothing to check; at a point of $\partial\Omega$, $v=0$ there, $v\to0$ from inside by continuity, and $v=0$ outside. <em>Piecewise $C^1$:</em> the finitely many pieces on which $v$ is $C^1$ inside $\Omega$, together with the complement of $\overline\Omega$ (where the extension is $0$), are finitely many pieces covering the plane, and on each of them the extension is $C^1$.</li>
<li>This is @thm:poincares-inequality. Fix $y$. As $\Omega$ lies in $0\lt x\lt L$, $v(0,y)=0$, and by the [fundamental theorem of calculus](apx:A9) for piecewise $C^1$ functions, $v(x,y)=\int_0^x\partial_xv(s,y)\,ds$. By Cauchy–Schwarz, for $0\lt x\lt L$,
\[ |v(x,y)|^2\le x\int_0^x|\partial_xv(s,y)|^2ds\le L\int_0^L|\partial_xv(s,y)|^2ds. \]
Integrate over $x\in(0,L)$: $\int_0^L|v(x,y)|^2dx\le L^2\int_0^L|\partial_xv(s,y)|^2ds$. Integrate over $y$ ([Fubini](apx:A13)) and use $|\partial_xv|\le|\nabla v|$: $\norm{v}^2\le L^2\norm{\partial_xv}^2\le L^2\norm{\nabla v}^2$.</li>
<li>$v_n-v_m$ is continuous, piecewise $C^1$ and zero on $\partial\Omega$, so part 2 gives $\norm{v_n-v_m}\le L\norm{\nabla v_n-\nabla v_m}\to0$ (this is @cor:it-applies-to-u-n-u). In Lecture 3 this is how @prop:three-limits gets the $L^2$ limit $u$: the gradients $\nabla U_n$ are Cauchy (@prop:for-consequently-is-a-cauchy), and $U_n-U_k$ vanishes on $\partial\Omega$, so the $U_n$ themselves are Cauchy.</li>
</ol>
</details>
