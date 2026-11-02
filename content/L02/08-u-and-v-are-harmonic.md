---
id: w8
slide: Slides 16–17
title: $u$ and $v$ are harmonic
---

::: proposition {#prop:if-satisfy-the-cauchy-riemann}
If $u,v\in C^2$ satisfy the Cauchy–Riemann equations $u_x+v_y=0$, $v_x-u_y=0$, then $u_{xx}+u_{yy}=0$ and $v_{xx}+v_{yy}=0$.
:::
::: proof
Apply $\partial_x$ to the first equation and $\partial_y$ to the second, then <b>subtract</b>:
\[ (u_{xx}+v_{yx})-(v_{xy}-u_{yy})=u_{xx}+u_{yy}=0. \]
Apply $\partial_y$ to the first and $\partial_x$ to the second, then <b>add</b>:
\[ (u_{xy}+v_{yy})+(v_{xx}-u_{yx})=v_{xx}+v_{yy}=0. \]
In both, the mixed partials cancel because $v_{yx}=v_{xy}$ and $u_{xy}=u_{yx}$ for $C^2$ functions ([equality of mixed partials](apx:A2)). This is where $C^2$ is needed.
:::

::: definition {#def:harmonic name=harmonic}
A $C^2$ function $h$ is <em>harmonic</em> if $\class{ntn-Delta}{\Delta} h:=h_{xx}+h_{yy}=0$. The operator $\class{ntn-Delta}{\Delta}$ is the <em>Laplacian</em>; equivalently $\class{ntn-Delta}{\Delta} h=\class{ntn-divc}{\operatorname{div}}\nabla h$.
:::
<p>So $u$ and $v$ are harmonic. Note that $\class{ntn-Delta}{\Delta} h=0$ is the <b>heat equation</b> $\partial_th=\class{ntn-Delta}{\Delta} h$ in two dimensions, for a temperature distribution $h$ that no longer changes in time: harmonic functions are <em>equilibrium temperatures</em>. Examples: every linear function $a+bx+cy$, $x^2-y^2$, $e^x\cos y$ (the real part of the holomorphic $e^z$), and $\log|z|$ away from $0$ ([E.6](apx:E6)).</p>
