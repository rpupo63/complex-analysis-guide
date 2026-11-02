---
id: x10
slide: Slide 19
title: Holomorphic functions as flows
toc: Complex potential and velocity
---

::: definition {#def:complex-potential-and-complex-velocity name="complex potential and complex velocity"}
Take any holomorphic $f=\class{ntn-vphi}{\varphi}+i\class{ntn-spsi}{\psi}$ and consider the flow with velocity field
\[ \class{ntn-Vfl}{V}=\nabla\class{ntn-vphi}{\varphi}=(\class{ntn-vphi}{\varphi}_x,\class{ntn-vphi}{\varphi}_y). \]
$f$ is the <em>complex potential</em> of the flow, and $f'$ its <em>complex velocity</em>. $\class{ntn-vphi}{\varphi}$ is the velocity potential and $\class{ntn-spsi}{\psi}$ the stream function, as in @prop:velocity-potential-stream-function-primitive.
:::

::: proposition {#prop:so-is-the-flow-associated}
$f'=\class{ntn-vphi}{\varphi}_x-i\class{ntn-vphi}{\varphi}_y$. So $\class{ntn-Vfl}{V}$ is the flow associated to $f'$ in the sense of @sec:x6 ($f'=u-iv$ with $(u,v)=\class{ntn-Vfl}{V}$); the velocity vector is $\class{ntn-Vfl}{V}=\overline{f'}$, and the speed is $|f'|$.
:::
::: proof
By @thm:cauchy-riemann and the Cauchy–Riemann equation $\class{ntn-spsi}{\psi}_x=-\class{ntn-vphi}{\varphi}_y$: $f'=\class{ntn-vphi}{\varphi}_x+i\class{ntn-spsi}{\psi}_x=\class{ntn-vphi}{\varphi}_x-i\class{ntn-vphi}{\varphi}_y$. Its complex conjugate is $\class{ntn-vphi}{\varphi}_x+i\class{ntn-vphi}{\varphi}_y$, which corresponds to the vector $(\class{ntn-vphi}{\varphi}_x,\class{ntn-vphi}{\varphi}_y)=\class{ntn-Vfl}{V}$. The speed is $|\class{ntn-Vfl}{V}|=|\overline{f'}|=|f'|$.
:::
<p>Two things to explain: the curves $\{\operatorname{Im}f=c\}$ are the <b>streamlines</b>, the paths the particles follow (@sec:x11); and the <b>flux</b> across a curve from $A$ to $B$ is $\operatorname{Im}f(B)-\operatorname{Im}f(A)$ (@sec:x12).</p>
