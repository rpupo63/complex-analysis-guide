---
id: n2
slide: Slide 3
title: Harmonic functions are real parts
---

::: lemma {#lem:harmonic-conjugate-on-a-disk name="harmonic conjugate on a disk"}
Let $u$ be harmonic on a disk $D:=D(z_0,r)$, $z_0=x_0+iy_0$. Then $u=\operatorname{Re}F$ for some $F$ holomorphic on $D$.
:::
::: proof

<ol>
<li><em>Define the candidate imaginary part.</em> For $x+iy\in D$ let
\[ v(x,y):=\int_{y_0}^yu_x(x,t)\,dt-\int_{x_0}^xu_y(s,y_0)\,ds, \]
integrating along the horizontal segment from $(x_0,y_0)$ to $(x,y_0)$ and then the vertical segment to $(x,y)$. Both segments lie in $D$: their points $(s,y_0)$ and $(x,t)$ are no farther from the centre than $(x,y)$ is, since $|s-x_0|\le|x-x_0|$ and $|t-y_0|\le|y-y_0|$.</li>
<li><em>$v_y=u_x$.</em> Only the first integral depends on $y$; by the [fundamental theorem of calculus](apx:A9), $v_y=u_x(x,y)$.</li>
<li><em>$v_x=-u_y$.</em> Differentiate the first integral in $x$ under the integral sign ([A.4](apx:A4); $u$ is $C^2$), and use $u_{xx}=-u_{yy}$:
\[ v_x=\int_{y_0}^yu_{xx}(x,t)\,dt-u_y(x,y_0)=-\int_{y_0}^yu_{yy}(x,t)\,dt-u_y(x,y_0)=-\big(u_y(x,y)-u_y(x,y_0)\big)-u_y(x,y_0)=-u_y(x,y). \]</li>
<li><em>Conclude.</em> $F:=u+iv$ has $C^1$ real and imaginary parts satisfying $u_x=v_y$, $u_y=-v_x$, so it is holomorphic by @thm:cauchy-riemann. <span class="qed">∎</span></li>
</ol>
:::
<p>This is Lecture 1's stream function again: there (@prop:velocity-potential-stream-function-primitive, [Poincaré lemma](apx:A7)) a curl-free, divergence-free flow on a disk had both a velocity potential and a stream function. Here the field is $\nabla u$, and $v$ is its stream function, the <em>harmonic conjugate</em> of $u$.</p>

::: remark {#rem:the-disk-matters name="the disk matters"}
$\log|z|$ is harmonic on $\mathbb C\setminus\{0\}$ ([E.6](apx:E6)), but it is not $\operatorname{Re}F$ for any $F$ holomorphic there. If it were, then, writing $F=U+iV$ with $U=\log|z|$, @thm:cauchy-riemann and Cauchy–Riemann give $F'=U_x+iV_x=U_x-iU_y=\frac{x-iy}{x^2+y^2}=\frac1z$. The integral of a derivative around a closed curve is $0$ (it is $F(\text{end})-F(\text{start})$), so $\oint_{|z|=1}\frac{dz}z=\oint_{|z|=1}F'(z)\,dz=0$, contradicting $\oint\frac{dz}z=2\pi i$ (@cor:the-residue-theorem-point-charge-form). The hole at $0$ is what goes wrong; compare @prop:no-global-primitive-on-mathbb-c, where $\frac1z$ has no global primitive.
:::
