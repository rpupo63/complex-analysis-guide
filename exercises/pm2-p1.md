---
label: ex:a-trigonometric-integral-l8
source: Practice midterm 2, Problem 1
title: a trigonometric integral
placement: h16
order: 2
---
Compute $\displaystyle\int_0^{2\pi}\frac{d\theta}{5-4\sin\theta}$.
<details class="sol"><summary>Hint</summary>
$\sin\theta=\frac1{2i}(z-z^{-1})$, $d\theta=\frac{dz}{iz}$. Find which root of the denominator is inside $|z|=1$.
</details>
<details class="sol"><summary>Solution</summary>
$5-4\sin\theta=5+2i(z-z^{-1})$, and multiplying by $iz$: $i(5z+2iz^2-2i)=-(2z^2-5iz-2)$. So the integral is $-\oint_{|z|=1}\frac{dz}{2z^2-5iz-2}$. The roots of $2z^2-5iz-2$ are $\frac{5i\pm3i}4=2i,\frac i2$; only $\frac i2$ is inside. With $2z^2-5iz-2=2(z-2i)(z-\frac i2)$, the residue of $\frac{-1}{2(z-2i)(z-i/2)}$ at the simple pole $\frac i2$ is $\frac{-1}{2(-\frac{3i}2)}=\frac1{3i}$ (@prop:simple-poles-of-a-quotient). By @thm:residue-theorem the integral is $2\pi i\cdot\frac1{3i}=\frac{2\pi}3$. (Check: $\frac{2\pi}{\sqrt{25-16}}$.)
</details>
