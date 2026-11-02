---
id: x1
slide: Slide 2
title: What complex analysis is about
---
<p>Complex analysis is the study of functions from $\mathbb C$ to $\mathbb C$ that can be differentiated. These functions are known by the fancy name of "holomorphic functions". Points are written $z=x+iy$ ([complex notation](apx:C1)).</p>

::: definition {#def:holomorphic name=holomorphic}
Let $\Omega\subseteq\mathbb C$ be [open](apx:C2). A function $f:\Omega\to\mathbb C$ is <em>holomorphic</em> on $\Omega$ if at every $z_0\in\Omega$ the limit
\[ f'(z_0):=\lim_{h\to0}\frac{f(z_0+h)-f(z_0)}{h},\qquad h\in\mathbb C\setminus\{0\}, \]
exists. Openness guarantees that $z_0+h\in\Omega$ for all small $h$, in every direction.
:::

::: definition {#def:complex-analytic name="complex analytic"}
$f$ is <em>complex analytic</em> if near each point $z_0$ it equals a convergent [power series](apx:A19) $\sum_{n\ge0}c_n(z-z_0)^n$.
:::
<p>Every analytic function is holomorphic (a convergent power series can be differentiated term by term). The converse is @thm:power-series. So the two terms are interchangeable, although their definitions look different; see [how the definitions meet](apx:E2).</p>
