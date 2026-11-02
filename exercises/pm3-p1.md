---
label: ex:a-trigonometric-integral-l8-2
source: Practice midterm 3, Problem 1
title: a trigonometric integral
placement: h16
order: 3
---
Compute $\displaystyle\int_0^{2\pi}\frac{d\theta}{3+2\sin\theta}$.
<details class="sol"><summary>Hint</summary>
Put $z=e^{i\theta}$, so $\sin\theta=\frac1{2i}(z-z^{-1})$ and $d\theta=\frac{dz}{iz}$, and use the residue theorem on $|z|=1$; the roots of the denominator involve $\sqrt5$.
</details>
<details class="sol"><summary>Solution</summary>
$3+2\sin\theta=3-i(z-z^{-1})$; multiplying by $iz$ gives $z^2+3iz-1$. So the integral is $\oint_{|z|=1}\frac{dz}{z^2+3iz-1}$, with roots $z_{1,2}=\frac{(-3\pm\sqrt5)i}2$. Only $z_1=\frac{(-3+\sqrt5)i}2\approx-0.38i$ is inside; the residue at this simple pole is $\frac1{z_1-z_2}=\frac1{i\sqrt5}$ (@prop:simple-poles-of-a-quotient). By @thm:residue-theorem the integral is $2\pi i\cdot\frac1{i\sqrt5}=\frac{2\pi}{\sqrt5}$. (Check: $\frac{2\pi}{\sqrt{9-4}}$.)
</details>
