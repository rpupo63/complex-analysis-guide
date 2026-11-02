---
id: E6
title: The logarithmic potential
status:
- derived
---
<div class="env"><span class="hd">Proposition.</span> For a fixed point $y$, the function $z\mapsto\log|z-y|$ is harmonic on the plane minus $y$.</div>
::: proof
$\nabla\log|z-y|=\frac{z-y}{|z-y|^2}$ (as a vector) is $2\pi$ times the unit-charge field $E_0$ of @def:the-field-of-a-unit-charge, moved to $y$. So $\class{ntn-Delta}{\Delta}\log|z-y|=\operatorname{div}\nabla\log|z-y|=2\pi\operatorname{div}E_0(\cdot-y)$, which is $0$ away from $y$ by @thm:the-claim, step 1.
:::
<p>Physically, $\log|z-y|$ is (up to a constant factor) the electrostatic potential of a point charge at $y$ in the plane, and the <em>fundamental solution</em> of the Laplacian: $\frac1{2\pi}\log|z|$ satisfies $\class{ntn-Delta}{\Delta}=\delta_0$ in the sense of distributions. It grows slowly, like $\log$ of the distance, and is $-\infty$ only at $y$ itself. Lecture 5 uses it as a barrier by putting the charge just outside $\Omega$. Its gradient is $\nabla\log|z|=2\pi E_0$, the field of a unit charge from Lecture 2 (@def:the-field-of-a-unit-charge).</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Fundamental_solution#Example" target="_blank" rel="noopener">Fundamental solution</a> · <a href="https://en.wikipedia.org/wiki/Logarithmic_potential" target="_blank" rel="noopener">Logarithmic potential</a></p>
