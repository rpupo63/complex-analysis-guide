---
label: ex:integral-of-the-cube-of-the-real-part
source: Homework 3, Problem 2
title: integral of $(\operatorname{Re} z)^3$
placement: f9
order: 1
---
Compute $\displaystyle\oint_{|z|=1}(\operatorname{Re} z)^3\,dz$.
<details class="sol"><summary>Hint</summary>
On the unit circle, $\operatorname{Re} z=(z+1/z)/2$. Expand, and read off the coefficient of $1/z$.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>Agree on the circle.</em> If $|z|=1$, then $\bar z=1/z$, so $\operatorname{Re} z=(z+\bar z)/2=(z+1/z)/2$. The two integrands agree on the contour.</li>
<li><em>Expand.</em> \[ \Big(\frac{z+z^{-1}}2\Big)^3=\frac18(z+z^{-1})^3=\frac18\big(z^3+3z+3z^{-1}+z^{-3}\big). \] The coefficient of $1/z$ is $3/8$. That coefficient is the residue at $0$ (@def:residue): the integrand is holomorphic on $0\lt|z|\le1$, with a pole at $0$.</li>
<li><em>Integrate.</em> By @thm:residue-theorem, \[ \oint_{|z|=1}(\operatorname{Re} z)^3\,dz=2\pi i\cdot\frac38=\frac{3\pi i}4. \]</li>
</ol>
</details>
