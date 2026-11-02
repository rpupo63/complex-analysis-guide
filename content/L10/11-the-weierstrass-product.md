---
id: k11
slide: Slide 12
title: The Weierstrass product
---

::: theorem {#thm:weierstrass name=Weierstrass}
Let $a_1,a_2,\dots$ be nonzero, with $|a_k|\to\infty$ (repetitions allowed). Then
\[ \class{ntn-Wz}{W}(z):=\prod_k\class{ntn-Ep}{E_k}(z/a_k) \]
converges uniformly on every closed disk to an entire function. Its zeros are the $a_k$, and the order of the zero at $a$ is $\#\{k:a_k=a\}$.
:::
::: proof
Fix $R\gt0$. As $|a_k|\to\infty$, all but finitely many $k$ have $|a_k|\ge2R$. For these, $|z/a_k|\le\frac12$ on $|z|\le R$, so @lem:convergence-factors (with $p=k$) gives
\[ \max_{|z|\le R}|1-\class{ntn-Ep}{E_k}(z/a_k)|\le4\cdot2^{-k-1}, \]
which is summable. The finitely many other terms are finite. So the product lemma (@lem:products) applies to $u_k:=\class{ntn-Ep}{E_k}(z/a_k)-1$. The only zero of $\class{ntn-Ep}{E_k}(z/a_k)$ is $z=a_k$, a simple one, so by the lemma the zero of $W$ at $a$ has order equal to the number of $k$ with $a_k=a$.
:::
<p>Using $\class{ntn-Ep}{E_k}$ with $k$ growing is crude but always works. Hadamard's theorem (@sec:k13) shows that a fixed $p$ suffices when the zeros come from a function of finite order.</p>
