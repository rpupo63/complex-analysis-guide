---
id: j5
slide: Slide 6
title: Jensen's formula
---

::: motivation
<p>The zeros inside the disk are factored out by @prop:factorization-in-a-disk, leaving a zero-free quotient. The mean value property in @thm:mean-value-property controls averages of harmonic functions. The circle average of the log of the modulus should record the zeros inside.</p>
:::

::: theorem {#thm:jensens-formula name="Jensen's formula"}
Let $f$ be holomorphic near $|z|\le R$, with $f(0)\ne0$, zeros $a_1,\dots,a_N$ in $|z|\lt R$ (repeated by multiplicity) and none on $|z|=R$. Then
\[ \frac1{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta=\log|f(0)|+\sum_{j=1}^N\log\frac{R}{|a_j|}. \]
:::
::: proof
Average
\[ \log|f|=\sum_j\log|z-a_j|+\log|g| \]
(@sec:j3) over $|z|=R$:
<ul>
<li>each $\log|z-a_j|$ gives $\log R$, by @lem:the-mean-of-a-logarithmic-potential, since $|a_j|\lt R$;</li>
<li>$\log|g|$ is harmonic near $|z|\le R$ (@lem:if-is-holomorphic-and-zero), so by the mean value property (@thm:mean-value-property) it gives $\log|g(0)|$. From $f(0)=\prod_j(0-a_j)\cdot g(0)$, $\log|g(0)|=\log|f(0)|-\sum_j\log|a_j|$. (Each $a_j\ne0$, as $f(0)\ne0$.)</li>
</ul>
The total is
\[ N\log R+\log|f(0)|-\sum_j\log|a_j|=\log|f(0)|+\sum_j\log\frac R{|a_j|}. \]
<span class="qed">∎</span>
:::

::: plain
<p>The average of $\log|f|$ on the circle equals the value $\log|f(0)|$ at the centre, plus a positive term for each zero inside. A zero near the centre adds more than a zero near the circle. If there are no zeros, the formula is the mean value of the log of the modulus.</p>
:::
<p>Each term $\log\frac R{|a_j|}$ is positive. So zeros inside the disk raise the average of $\log|f|$ on the circle above its value $\log|f(0)|$ at the centre, and the closer a zero is to $0$, the more it raises it. With no zeros, Jensen's formula is the mean value property for $\log|f|$. Read backwards, the formula bounds the number of zeros by the size of $f$; that is the next corollary.</p>
