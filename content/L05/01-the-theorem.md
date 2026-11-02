---
id: v2
slide: Slide 2
title: The theorem
---

::: theorem {#thm:the-dirichlet-problem-on-a-union name="the Dirichlet problem on a union of squares"}
Let $\Omega$ be a finite union of grid squares and $g$ continuous on $\class{ntn-dOm}{\partial\Omega}$. There is exactly one $u\in C^2(\Omega)\cap C(\overline\Omega)$ with $\class{ntn-Delta}{\Delta} u=0$ in $\Omega$ and $u=g$ on $\class{ntn-dOm}{\partial\Omega}$.
:::
<p>"Finite union of grid squares" is Grid hypothesis 4.1. Note what is <em>not</em> assumed: $g$ need not be linear on boundary edges. $C^2(\Omega)\cap C(\overline\Omega)$ is the class of [twice differentiable inside, continuous up to the boundary](apx:D1); this is the classical Dirichlet problem of @def:dirichlet-problem. The proof has four steps.</p>
<div class="tbl"><table>
<thead><tr><th>Step</th><th>Statement</th><th>Where</th></tr></thead>
<tbody>
<tr><td>1. Reduction</td><td>It suffices to treat $g$ linear on each boundary edge of the coarsest grid.</td><td>@sec:v3, @prop:the-reduction</td></tr>
<tr><td>2. A candidate</td><td>For such $g$, the finite element solutions $\class{ntn-Un}{U_n}$ converge in energy to a function $u$.</td><td>Lecture 3, @thm:existence-of-a-weak-solution</td></tr>
<tr><td>3. Harmonic, and unique</td><td>$u$ is smooth and harmonic in $\Omega$; a harmonic function in $C(\overline\Omega)$ is determined by its boundary values.</td><td>Lecture 4, @cor:the-lecture-3-limit-is-a and @cor:stability</td></tr>
<tr><td>4. Boundary values</td><td>$u(z)\to g(p)$ as $z\to p\in\class{ntn-dOm}{\partial\Omega}$.</td><td>Today: @sec:v5–@sec:v12, @thm:step-4-boundary-values</td></tr>
</tbody></table></div>
<p>This lecture proves step 4, by <b>energy</b> and a <b>comparison</b> of $u$ with explicit harmonic functions. Steps 1 to 3 are used as they stand; step 1 is proved in @sec:v3. The full proof of @thm:the-dirichlet-problem-on-a-union is assembled in @sec:v13.</p>
