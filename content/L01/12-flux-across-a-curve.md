---
id: x12
slide: Slide 21
title: How much fluid crosses a curve?
toc: Flux across a curve
---
<p>Pick a holomorphic $f=\class{ntn-vphi}{\varphi}+i\class{ntn-spsi}{\psi}$, with its flow $\class{ntn-Vfl}{V}=\nabla\class{ntn-vphi}{\varphi}$ (the flow described by $f'$), and a curve $C$ from $A$ to $B$. How much fluid passes through $C$ per unit time? This is the <b>flux</b> of $\class{ntn-Vfl}{V}$ across $C$. With $(dx,dy)$ the tangent displacement and $n\,ds:=(dy,-dx)$ the normal (pointing to the right of the direction of travel; [flux](apx:A5)),
\[ \text{flux}=\int_CV\cdot n\,ds=\int_C\class{ntn-vphi}{\varphi}_x\,dy-\class{ntn-vphi}{\varphi}_y\,dx. \]

::: proposition {#prop:the-flux-across-is-it}
The flux across $C$ is $\operatorname{Im}f(B)-\operatorname{Im}f(A)$: it depends only on the endpoints.
:::
::: proof
By Cauchy–Riemann, $\class{ntn-vphi}{\varphi}_x=\class{ntn-spsi}{\psi}_y$ and $-\class{ntn-vphi}{\varphi}_y=\class{ntn-spsi}{\psi}_x$, so the integrand is $\class{ntn-spsi}{\psi}_y\,dy+\class{ntn-spsi}{\psi}_x\,dx=d\class{ntn-spsi}{\psi}$, the change of $\class{ntn-spsi}{\psi}$ along the curve. Concretely, parametrize $C$ by $\gamma(s)$, $s\in[a,b]$; then
\[ \int_C\class{ntn-spsi}{\psi}_x\,dx+\class{ntn-spsi}{\psi}_y\,dy=\int_a^b\nabla\class{ntn-spsi}{\psi}(\gamma(s))\cdot\gamma'(s)\,ds=\int_a^b\frac{d}{ds}\class{ntn-spsi}{\psi}(\gamma(s))\,ds=\class{ntn-spsi}{\psi}(B)-\class{ntn-spsi}{\psi}(A) \]
by the chain rule and the [fundamental theorem of calculus](apx:A9).
:::
<p><b>Consequence.</b> Between two streamlines $\{\class{ntn-spsi}{\psi}=c_1\}$ and $\{\class{ntn-spsi}{\psi}=c_2\}$ the flow rate is $c_2-c_1$, wherever you cut across. So where streamlines come closer together, the fluid moves faster.</p>
