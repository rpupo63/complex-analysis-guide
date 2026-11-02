---
id: k13
slide: Slide 14
title: Hadamard's theorem
---

::: theorem {#thm:hadamard name=Hadamard status=cited}
Let $f\not\equiv0$ be entire of finite order $\class{ntn-rhoo}{\rho}$, with a zero of order $m\ge0$ at $0$ and other zeros $a_k$, each listed as often as its order. Let $p:=\lfloor\class{ntn-rhoo}{\rho}\rfloor$. Then
\[ f(z)=z^m\,e^{h(z)}\prod_k\class{ntn-Ep}{E_p}(z/a_k),\qquad h\text{ a polynomial of degree}\le\class{ntn-rhoo}{\rho}. \]
:::
<p>The slides state this without proof; the idea is in [E.20](apx:E20). What can be checked here is that the product converges:</p>
::: proof {title="Why the product converges."}
$f/z^m$ is entire of the same order, with nonzero value at $0$ and zeros $a_k$. As $p+1\gt\class{ntn-rhoo}{\rho}$, @thm:zeros-versus-order(2) with $\sigma=p+1$ gives $\sum_k|a_k|^{-p-1}\lt\infty$. On $|z|\le R$, for the $k$ with $|a_k|\ge2R$, @lem:convergence-factors gives $|1-\class{ntn-Ep}{E_p}(z/a_k)|\le4R^{p+1}|a_k|^{-p-1}$, which is summable; so @lem:products applies.
:::
<p>Compared with Weierstrass, Hadamard gains two things for functions of finite order: one fixed $p$ for all factors, and $h$ a polynomial, not just entire. The proof of the second uses @lem:no-zeros together with lower bounds for the product away from its zeros.</p>
