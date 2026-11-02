---
id: j2
slide: Slide 3
title: Factoring out zeros
---

::: proposition {#prop:factorization-in-a-disk name="factorization in a disk"}
Let $f$ be holomorphic near $|z|\le R$, with no zeros on $|z|=R$. Then $f$ has finitely many zeros $a_1,\dots,a_N$ in $|z|\lt R$ (repeated by multiplicity), and
\[ f(z)=(z-a_1)\cdots(z-a_N)\,g(z), \]
with $g$ holomorphic and zero-free near $|z|\le R$.
:::
::: proof

<ol>
<li><em>No zeros near the circle.</em> The set where $f\ne0$ is open (by continuity) and contains the compact circle $|z|=R$, so it contains an annulus $R-\eta\lt|z|\lt R+\eta$ ([C.5](apx:C5)(a), applied to the circle inside that open set). Shrinking the open set on which $f$ is holomorphic, we may assume it is a disk $|z|\lt R+\eta$, which is connected, and $f\not\equiv0$ there.</li>
<li><em>$N\lt\infty$.</em> All zeros lie in the compact disk $|z|\le R-\eta$. Infinitely many would have a limit point there (Bolzano–Weierstrass), which would be a non-isolated zero, contradicting @thm:isolated-zeros. Each zero has finite order (step 1 of that proof).</li>
<li><em>Define $g$.</em> Let $g:=f/\prod_j(z-a_j)$ off the zeros. It is holomorphic there, and nonzero there (as $f$ is).</li>
<li><em>At a zero $a$ of order $m$.</em> By the Taylor remainder (@cor:taylor-remainder), $f(z)=c(z-a)^m+O(|z-a|^{m+1})$ with $c=a_m\ne0$. Exactly $m$ of the $a_j$ equal $a$, so $\prod_j(z-a_j)=(z-a)^mq(z)$ with $q$ a polynomial and $q(a)\ne0$. Hence
\[ g(z)=\frac{c+O(|z-a|)}{q(z)}\longrightarrow\frac c{q(a)}\ne0\qquad(z\to a). \]
So $g$ is bounded near $a$, @lem:removable-singularities extends it holomorphically to $a$, and by continuity $g(a)=c/q(a)\ne0$. <span class="qed">∎</span></li>
</ol>
:::
