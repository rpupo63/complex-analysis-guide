---
id: n1
slide: Slide 2
title: Harmonic functions with given boundary values
---
<p>The lecture opens with a Dirichlet problem (Part I's question) that is hard on a disk and easy on a half-plane, and asks how to move it from one to the other.</p>

::: example {#eg:the-plate name="the plate"}
A plate $D(0,1)$ has its upper edge held at temperature $1$ and its lower edge at $0$. The temperature solves the heat equation $u_t=\Delta u$; in equilibrium $u_t=0$, so $u$ is harmonic. Problem: find a harmonic $u$ on $D(0,1)$ with limit $1$ at each point $e^{i\theta}$, $0\lt\theta\lt\pi$, and limit $0$ at each point $e^{i\theta}$, $\pi\lt\theta\lt2\pi$.
:::
<p>The boundary data jump at $\pm1$, so this is not quite the continuous Dirichlet problem of @thm:the-dirichlet-problem-on-a-union; no value is prescribed at the two jump points.</p>
<figure>{{fig:n1-1}}<figcaption>The easy problem on $\mathbb H$ (left) and the plate problem on the disk (right). The Cayley map $C$ carries one to the other.</figcaption></figure>

::: proposition {#prop:the-same-problem-on-the-half name="the same problem on the half-plane"}
On the upper half-plane $\mathbb H:=\{\operatorname{Im}z\gt0\}$, write $z=x+iy$ with $\arg z\in(0,\pi)$, and let
\[ v(z):=\frac1\pi\arg z=\frac12-\frac1\pi\arctan\frac xy. \]
Then $v$ is harmonic on $\mathbb H$, with limit $0$ at each point of $(0,\infty)$ and limit $1$ at each point of $(-\infty,0)$.
:::
::: proof

<ol>
<li><em>The two formulas agree.</em> For $y\gt0$ the angle $\alpha=\arg z\in(0,\pi)$ has $\cot\alpha=x/y$. On $(0,\pi)$, $\alpha=\frac\pi2-\arctan(\cot\alpha)$ (both sides decrease from $\pi$ to $0$ and have the same cotangent). So $\frac1\pi\arg z=\frac12-\frac1\pi\arctan\frac xy$.</li>
<li><em>Harmonic, by direct computation.</em> Let $\phi:=\arctan\frac xy$. Then
\[ \phi_x=\frac{1/y}{1+x^2/y^2}=\frac{y}{x^2+y^2},\qquad\phi_y=\frac{-x/y^2}{1+x^2/y^2}=\frac{-x}{x^2+y^2}, \]
\[ \phi_{xx}=\frac{-2xy}{(x^2+y^2)^2},\qquad\phi_{yy}=\frac{2xy}{(x^2+y^2)^2}, \]
so $\Delta\phi=0$, and $v=\frac12-\frac1\pi\phi$ is harmonic.</li>
<li><em>Boundary limits.</em> Let $z\to x_0\ne0$ from $\mathbb H$, so $y\to0^+$ and $x\to x_0$. Then $x/y\to+\infty$ if $x_0\gt0$ and $\to-\infty$ if $x_0\lt0$, so $\arctan\frac xy\to\pm\frac\pi2$ and $v\to0$, respectively $1$. <span class="qed">∎</span></li>
</ol>
:::
<p>The plan: carry $v$ from $\mathbb H$ to $D(0,1)$ by a bijection that keeps functions harmonic. Two ingredients are needed: holomorphic maps preserve harmonicity (@sec:n3), and an explicit holomorphic bijection $\mathbb H\to D(0,1)$ (@sec:n4).</p>
