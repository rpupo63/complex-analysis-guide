---
id: n11
slide: Slide 12
title: 'Examples: a strip'
---

::: example {#eg:the-strip name="the strip" status=derived}
Let $S:=\{0\lt\operatorname{Im}z\lt\pi\}$. Then $e^z$ is a conformal map of $S$ onto $\mathbb H$, with inverse
\[ L(z)=\log|z|+i\arg z,\qquad\arg z\in(0,\pi), \]
holomorphic on $\mathbb H$. And $C(e^z)$ is a conformal map of $S$ onto $D(0,1)$.
:::
::: proof
$e^{x+iy}=e^xe^{iy}$ has modulus $e^x\in(0,\infty)$ and argument $y\in(0,\pi)$. Every point of $\mathbb H$ has a unique modulus in $(0,\infty)$ and a unique argument in $(0,\pi)$, each pair coming from exactly one $(x,y)$: so $e^z$ is a bijection $S\to\mathbb H$. It is holomorphic, so its inverse is holomorphic by @thm:inverse, and solving $e^{x+iy}=z$ gives $x=\log|z|$, $y=\arg z$. Composing with the Cayley map (@prop:cayley-map) gives a conformal map onto the disk.
:::
<p>Horizontal lines $y=c$ go to rays from $0$ at angle $c$; vertical segments $x=c$ go to half-circles of radius $e^c$ about $0$.</p>
<figure>{{fig:n11-1}}<figcaption>@eg:the-strip: $e^z$ maps the strip $S$ onto $\mathbb H$. Horizontal lines (blue) go to rays, vertical segments (brown) to half-circles.</figcaption></figure>
