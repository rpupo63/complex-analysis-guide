---
id: x5
slide: Slides 6–10
title: The Cauchy–Riemann equations
toc: Cauchy–Riemann equations
---

::: definition {#def:complex-functions-as-maps-of-the name="complex functions as maps of the plane"}
A map $f:\R^2\to\R^2$, $f(x,y)=\big(u(x,y),v(x,y)\big)$, is identified with the complex function
\[ f(x+iy)=u(x,y)+i\,v(x,y). \]
$u$ is the <em>real part</em> and $v$ the <em>imaginary part</em> of $f$. Partial derivatives are written $u_x=\partial u/\partial x$ and so on.
:::

::: theorem {#thm:cauchy-riemann name="Cauchy–Riemann"}
Let $f=(u,v)$ be [differentiable](apx:A1) at $(x_0,y_0)$ as a map $\R^2\to\R^2$, and $z_0=x_0+iy_0$. Then $f=u+iv$ is complex differentiable at $z_0$ if and only if
\[ \frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\qquad\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}\qquad\text{at }(x_0,y_0). \]
In that case $f'(z_0)=u_x+i\,v_x$.
:::
<p>The theorem says that for complex differentiability <b>only two directions matter</b>: top–bottom and left–right. If $f$ is differentiable as a real map, the derivatives in these two directions determine all the others, and Cauchy–Riemann is exactly the condition for them to fit together into a complex derivative.</p>

::: proof {title="Proof of (⇒)."}
Suppose $f$ is complex differentiable at $z_0$. Then the limit defining $f'(z_0)$ can be taken along any direction; take two.
<ul>
<li><em>Left–right:</em> $h=t\in\R$, $t\to0$. The quotient is $\frac{u(x_0+t,y_0)-u(x_0,y_0)}{t}+i\,\frac{v(x_0+t,y_0)-v(x_0,y_0)}{t}$, whose real and imaginary parts tend to the partial derivatives:
\[ f'(z_0)=\lim_{t\to0}\frac{f(z_0+t)-f(z_0)}{t}=u_x+i\,v_x. \]</li>
<li><em>Top–bottom:</em> $h=it$, $t\in\R$, $t\to0$. Now the numerator changes $y$, giving $u_y+iv_y$ in the limit, and we divide by $i$, using $\frac1i=-i$:
\[ f'(z_0)=\lim_{t\to0}\frac{f(z_0+it)-f(z_0)}{it}=\frac{u_y+i\,v_y}{i}=v_y-i\,u_y. \]</li>
</ul>
The two must agree: $u_x+iv_x=v_y-iu_y$. Comparing real parts gives $u_x=v_y$; comparing imaginary parts gives $v_x=-u_y$.
:::

::: proof {title="Proof of (⇐)."}
Assume the Cauchy–Riemann equations hold at $(x_0,y_0)$; all partial derivatives below are evaluated there.
<ol>
<li><em>Taylor expand, as real functions.</em> Since $u$ and $v$ are differentiable at $(x_0,y_0)$ ([A.1](apx:A1)), for $(h_1,h_2)\to(0,0)$:
\[ \begin{aligned} u(x_0+h_1,y_0+h_2)&=u(x_0,y_0)+h_1u_x+h_2u_y+o(|h|),\\ v(x_0+h_1,y_0+h_2)&=v(x_0,y_0)+h_1v_x+h_2v_y+o(|h|), \end{aligned} \]
where $|h|=\sqrt{h_1^2+h_2^2}$ and $o(|h|)$ is an error that is small compared with $|h|$.</li>
<li><em>Reinterpret as a complex function.</em> Put $h=h_1+ih_2$, so that $z_0+h$ corresponds to $(x_0+h_1,y_0+h_2)$. Then
\[ \begin{aligned} f(z_0+h)-f(z_0)&=\big[u(x_0+h_1,y_0+h_2)-u(x_0,y_0)\big]+i\big[v(x_0+h_1,y_0+h_2)-v(x_0,y_0)\big]\\ &=h_1(u_x+iv_x)+h_2(u_y+iv_y)+o(|h|). \end{aligned} \]</li>
<li><em>Use Cauchy–Riemann.</em> Substituting $u_y=-v_x$ and $v_y=u_x$,
\[ u_y+iv_y=-v_x+iu_x=i(u_x+iv_x). \]
So both coefficients are multiples of the same complex number $u_x+iv_x$:
\[ f(z_0+h)-f(z_0)=(h_1+ih_2)(u_x+iv_x)+o(|h|)=h\,(u_x+iv_x)+o(|h|). \]</li>
<li><em>Conclude.</em> Divide by $h$:
\[ \frac{f(z_0+h)-f(z_0)}{h}=(u_x+iv_x)+\frac{o(|h|)}{h}\longrightarrow u_x+iv_x \]
as $h\to0$ <em>from any direction</em>, since $|o(|h|)/h|=o(|h|)/|h|\to0$. So $f$ is complex differentiable at $z_0$, with $f'(z_0)=u_x+iv_x$. <span class="qed">∎</span></li>
</ol>
:::
<p>Step 3 is where the two directions "fit together": a general real-linear map $(h_1,h_2)\mapsto h_1a+h_2b$ is multiplication by a single complex number exactly when $b=ia$. Geometrically, a complex derivative acts on small displacements as a rotation combined with a scaling.</p>
