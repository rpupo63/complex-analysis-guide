---
label: ex:mahler-measure
source: Homework 2, Problem 2(b)
title: Mahler measure
placement: j5
order: 1
---
For $p(z)=a_d\prod_{j=1}^d(z-\alpha_j)$ with $a_d\ne0$, the Mahler measure is $M(p):=|a_d|\prod_j\max(1,|\alpha_j|)$. Show that if no $\alpha_j$ lies on $|z|=1$, then $\frac1{2\pi}\int_0^{2\pi}\log|p(e^{i\theta})|\,d\theta=\log M(p)$. Deduce that if $p$ has integer coefficients, the geometric mean of $|p|$ on the unit circle is at least $1$.
<details class="sol"><summary>Hint</summary>
Take logarithms of the product and use @lem:the-mean-of-a-logarithmic-potential with $R=1$ on each factor.
</details>
<details class="sol"><summary>Solution</summary>
$\log|p(e^{i\theta})|=\log|a_d|+\sum_j\log|e^{i\theta}-\alpha_j|$. By @lem:the-mean-of-a-logarithmic-potential with $R=1$ (allowed, as $|\alpha_j|\ne1$), each factor averages to $\log\max(1,|\alpha_j|)$. Summing gives $\log|a_d|+\sum_j\log\max(1,|\alpha_j|)=\log M(p)$. (When $p(0)\ne0$ this is Jensen's formula, @thm:jensens-formula, for $p$ on $|z|=1$.) The geometric mean is $\exp$ of the average of $\log|p|$, i.e. $M(p)\ge|a_d|\ge1$ when $a_d$ is a nonzero integer.
<p>Remark: for monic $p\in\mathbb Z[z]$ with $p(0)\ne0$, $M(p)=1$ exactly when $p$ is a product of cyclotomic polynomials (Kronecker). Whether $M(p)\ge1+\delta$ for some absolute $\delta\gt0$ otherwise is Lehmer's open problem (1933); the smallest known value is $1.17628\ldots$, for $z^{10}+z^9-z^7-z^6-z^5-z^4-z^3+z+1$.</p>
</details>
