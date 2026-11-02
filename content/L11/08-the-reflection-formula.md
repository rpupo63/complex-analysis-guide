---
id: m8
slide: Slide 9
title: The reflection formula
---

::: theorem {#thm:eulers-reflection-formula name="Euler's reflection formula"}
For $z\in\mathbb C\setminus\mathbb Z$,
\[ \Gamma(z)\,\Gamma(1-z)=\frac\pi{\sin\pi z}. \]
:::
::: proof
Let $z\notin\mathbb Z$. Then $z,-z,1-z\in \class{ntn-Wset}{W}$, so $\frac1{\Gamma(\pm z)}=\class{ntn-Rg}{R}(\pm z)$ by @thm:weierstrass-product-for-1-gamma, and $\Gamma(1-z)=-z\,\Gamma(-z)$ by the functional equation. Multiplying the products for $\class{ntn-Rg}{R}(z)$ and $\class{ntn-Rg}{R}(-z)$ factor by factor (the product of two convergent products is the limit of the products of partial products):
\[ \class{ntn-Rg}{R}(z)\class{ntn-Rg}{R}(-z)=z e^{\class{ntn-gam}{\gamma} z}(-z)e^{-\class{ntn-gam}{\gamma} z}\prod_{n\ge1}\Big(1+\frac zn\Big)e^{-z/n}\Big(1-\frac zn\Big)e^{z/n}=-z^2\prod_{n\ge1}\Big(1-\frac{z^2}{n^2}\Big). \]
Hence, by Euler's product (@thm:euler),
\[ \frac1{\Gamma(z)\Gamma(1-z)}=\frac1{\Gamma(z)\cdot(-z)\Gamma(-z)}=\frac{\class{ntn-Rg}{R}(z)\class{ntn-Rg}{R}(-z)}{-z}=z\prod_{n\ge1}\Big(1-\frac{z^2}{n^2}\Big)=\frac{\sin\pi z}\pi. \]
<span class="qed">∎</span>
:::
<p>Both sides have simple poles exactly at the integers: on the left, the poles of $\Gamma(z)$ at $0,-1,\dots$ and of $\Gamma(1-z)$ at $1,2,\dots$.</p>
