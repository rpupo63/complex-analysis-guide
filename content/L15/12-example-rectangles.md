---
id: q12
slide: Slide 15
title: 'Example: rectangles'
---

::: motivation
<p>@eg:the-half-strip was an integral with two square-root factors. Four right angles call for two further factors and should give a rectangle. @thm:schwarz-christoffel-converse names the image once the vertices are known.</p>
:::

::: example {#eg:rectangles name="rectangles; elliptic integrals"}
For $0\lt k\lt1$, take the prevertices $\pm1$, $\pm\frac1k$, all with right angles ($\alpha=\frac12$), and the square root positive on $(-1,1)$:
\[ F(z)=\int_0^z\frac{d\zeta}{\sqrt{(1-\zeta^2)(1-k^2\zeta^2)}} \qquad(\arcsin z\text{ for }k=0). \]
Then
\[ F(\pm1)=\pm K,\qquad F\big(\pm\tfrac1k\big)=\pm K+iK',\qquad F(\infty)=iK', \]
\[ K:=\int_0^1\frac{dt}{\sqrt{(1-t^2)(1-k^2t^2)}},\qquad K':=\int_1^{1/k}\frac{dt}{\sqrt{(t^2-1)(1-k^2t^2)}}. \]
:::
::: proof {title="Why."}
On $(1,\frac1k)$, $\arg(1-\zeta)$ has reached $-\pi$, so the integrand is $i$ times a positive function; this gives $F(\frac1k)=K+iK'$. Beyond $\frac1k$ the factor $(1-k\zeta)^{-1/2}$ also picks up $i$, and the integrand is negative. The substitution $t=\frac1{ks}$ turns $\int_{1/k}^\infty\frac{dt}{\sqrt{(t^2-1)(k^2t^2-1)}}$ into $K$, so $F(\infty)=K+iK'-K=iK'$. The negative side follows by symmetry, $F(-z)=-F(z)$.
:::

::: plain
<p>This integral sends the upper half-plane onto a rectangle. The four vertices are the points $\pm K$ and $\pm K+iK'$ in the plane. Changing the parameter $k$ changes the ratio of height to width.</p>
:::

<p>So by @thm:schwarz-christoffel-converse, $F$ maps $\mathbb H$ conformally onto the rectangle $R$ with vertices $\pm K$, $\pm K+iK'$. With $k':=\sqrt{1-k^2}$, $K'(k)=K(k')$ (a standard identity, checked numerically for this guide). As $k$ runs over $(0,1)$, $K$ increases from $\frac\pi2$ to $\infty$ and $K'$ decreases from $\infty$ to $\frac\pi2$, so the ratio of height to width, $K'/2K$, decreases continuously from $\infty$ to $0$: every rectangle occurs, up to $Aw+B$.</p>
