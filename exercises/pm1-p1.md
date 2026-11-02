---
label: ex:a-trigonometric-integral
source: Practice midterm 1, Problem 1
title: a trigonometric integral
placement: h16
order: 1
---
Compute $\displaystyle\int_0^{2\pi}\frac{d\theta}{5+3\cos\theta}$.
<details class="sol"><summary>Hint</summary>
Write it as a contour integral over $|z|=1$ with $z=e^{i\theta}$, $\cos\theta=\frac12(z+z^{-1})$, $d\theta=\frac{dz}{iz}$, as in @ex:show-hint-solution-as-runs.
</details>
<details class="sol"><summary>Solution</summary>
The integral becomes (as in @ex:show-hint-solution-as-runs) $\oint_{|z|=1}\frac{2\,dz}{i(3z^2+10z+3)}=\oint\frac{2\,dz}{3i(z+\frac13)(z+3)}$. Only $-\frac13$ is inside, a simple pole with residue $\frac{2}{3i(-\frac13+3)}=\frac{2}{8i}=\frac1{4i}$ (@prop:simple-poles-of-a-quotient). By the residue theorem (@thm:residue-theorem), the integral is $2\pi i\cdot\frac1{4i}=\frac\pi2$. (Check: $\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}=\frac{2\pi}{\sqrt{a^2-b^2}}=\frac{2\pi}4$.)
</details>
