---
id: h11
slide: Slide 12
title: The Poisson summation formula
---

::: theorem {#thm:poisson-summation name="Poisson summation" status=cited}
Let $a\gt0$, and let $F$ be holomorphic in the strip $|\operatorname{Im}z|\lt a$, with $|F(x+iy)|\le\dfrac{C}{1+x^2}$ for $|y|\lt a$. Then, both sums converging absolutely,
\[ \sum_{n\in\mathbb Z}F(n)=\sum_{m\in\mathbb Z}\class{ntn-hat}{\hat F}(m). \]
:::
<p>The slides refer to Homework 1, Problem 3 for the proof. A complete proof by residues, with the contour and the estimates, is in [E.16](apx:E16). Absolute convergence: $|F(n)|\le\frac C{1+n^2}$, and $|\class{ntn-hat}{\hat F}(m)|\le\pi C'e^{-2\pi b|m|}$ for any $b\lt a$ by [Theorem #(a)](@thm:strips-and-decay).</p>
<p>The formula says that sampling at the integers in "time" and summing equals sampling the transform at the integers in "frequency" and summing. The sampling theorem uses it with $F(x)=f(x)e^{-2\pi ix\xi}$.</p>
