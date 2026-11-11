---
id: q11
slide: Slide 14
title: 'Example: triangles'
---

::: example {#eg:triangles name="triangles"}
For $\alpha,\beta\gt0$ with $\alpha+\beta\lt1$, let
\[ F(z)=\int_0^z\zeta^{\alpha-1}(1-\zeta)^{\beta-1}\,d\zeta\qquad(z\in\mathbb H), \]
with $\arg\zeta\in[0,\pi]$ and $\arg(1-\zeta)\in[-\pi,0]$. The prevertices are $0$, $1$ and $\infty$ (no factor), with angles $\alpha\pi$, $\beta\pi$, $\gamma\pi$, $\gamma:=1-\alpha-\beta\gt0$. By @thm:schwarz-christoffel-converse, $F$ maps $\mathbb H$ conformally onto the triangle with vertices
\[ 0,\qquad F(1)=\int_0^1t^{\alpha-1}(1-t)^{\beta-1}\,dt\gt0,\qquad F(\infty), \]
in counterclockwise order, with angles $\alpha\pi$, $\beta\pi$, $\gamma\pi$ there. $F(\infty)$ is finite, as the integrand is $O(|\zeta|^{\alpha+\beta-2})$ and $\alpha+\beta-2\lt-1$.
:::
<p><b>No parameters.</b> Every triangle is, up to a map $Aw+B$, one of these: take $\alpha\pi$, $\beta\pi$ to be two of its angles, in counterclockwise order. For the equilateral triangle, $\alpha=\beta=\frac13$. $F(1)$ is the Beta integral $\mathrm B(\alpha,\beta)$, which is $\Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha+\beta)$ (stated without proof; compare @prop:the-gamma-function).</p>
