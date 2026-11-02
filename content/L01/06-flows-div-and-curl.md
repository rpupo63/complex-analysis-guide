---
id: x6
slide: Slides 11–14
title: 'The meaning of the Cauchy–Riemann equations: flows'
toc: 'Flows: div and curl'
---
<p>The simplest interpretation is a two-dimensional fluid with velocity field $(x,y)\longmapsto\big(u(x,y),v(x,y)\big)$.</p>

::: definition {#def:divergence-and-curl name="divergence and curl"}
For a planar vector field $(u,v)$,
\[ \class{ntn-divc}{\operatorname{div}}(u,v):=\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y},\qquad\class{ntn-divc}{\operatorname{curl}}(u,v):=\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}. \]
In two dimensions the curl is a scalar: it is the $z$-component of the three-dimensional curl $\nabla\times(u,v,0)$, the only component that can be nonzero for a planar field. (More on [flux and circulation](apx:A5).)
:::
<p>To check the curl claim:
\[ \nabla\times(u,v,0)=\big(\partial_y0-\partial_zv,\ \partial_zu-\partial_x0,\ \partial_xv-\partial_yu\big)=(0,0,v_x-u_y), \]
because $u,v$ do not depend on the third coordinate.</p>

::: proposition {#prop:cauchy-riemann-in-the-language-of name="Cauchy–Riemann in the language of flows"}
The pair $(u,-v)$ satisfies the Cauchy–Riemann equations if and only if
\[ \class{ntn-divc}{\operatorname{div}}(u,v)=0\qquad\text{and}\qquad\class{ntn-divc}{\operatorname{curl}}(u,v)=0. \]
Equivalently: for $u,v$ of class $C^1$, $f=u-iv$ is holomorphic if and only if $(u,v)$ is divergence-free and curl-free.
:::
::: proof
@thm:cauchy-riemann's equations for real part $u$ and imaginary part $-v$ read $u_x=(-v)_y$ and $u_y=-(-v)_x$, that is $u_x+v_y=0$ and $v_x-u_y=0$: $\class{ntn-divc}{\operatorname{div}}(u,v)=0$ and $\class{ntn-divc}{\operatorname{curl}}(u,v)=0$. For the second sentence, $C^1$ functions are differentiable ([A.1](apx:A1)), so @thm:cauchy-riemann applies at every point.
:::
<p><b>The minus sign is forced.</b> Cauchy–Riemann for $(u,v)$ itself would say $u_x=v_y$ and $u_y=-v_x$, which is neither $\class{ntn-divc}{\operatorname{div}}=0$ nor $\class{ntn-divc}{\operatorname{curl}}=0$; flipping the sign of $v$ turns them into exactly those two. (See [sign conventions](apx:E1).)</p>

::: proposition {#prop:incompressible-and-irrotational name="incompressible and irrotational"}
Write $V=(u,v)$, of class $C^1$, and let $D$ be any small region with boundary $\partial D$, inside the domain.
<br>(a) <b>Incompressible:</b> if $\class{ntn-divc}{\operatorname{div}}V=0$, then $\oint_{\partial D}V\cdot n\,ds=0$: as much fluid flows into $D$ as flows out. No sources, no sinks.
<br>(b) <b>Irrotational:</b> if $\class{ntn-divc}{\operatorname{curl}}V=0$, then $\oint_{\partial D}V\cdot t\,ds=0$: the circulation around $\partial D$ vanishes, so the fluid does not swirl around any point.
:::
::: proof
(a) By the [divergence theorem](apx:A6), $\oint_{\partial D}V\cdot n\,ds=\iint_D\class{ntn-divc}{\operatorname{div}}V\,dA=0$. (b) By [Green's theorem](apx:A6), $\oint_{\partial D}V\cdot t\,ds=\iint_D\class{ntn-divc}{\operatorname{curl}}V\,dA=0$.
:::
<p>$\class{ntn-divc}{\operatorname{div}}V=0$ is <em>conservation of mass</em> for a fluid of constant density. <b>Upshot:</b> holomorphic functions $f=u-iv$ are the same thing as incompressible, irrotational plane flows.</p>

::: example {#eg:which-flows-come-from-holomorphic-functions name="which flows come from holomorphic functions?" status=derived}

<b>Rotation</b> $(u,v)=(-y,x)$: $\class{ntn-divc}{\operatorname{curl}}=2\ne0$, and indeed $u-iv=-i\bar z$ is not holomorphic.<br>
<b>Source</b> $(u,v)=(x,y)$: $\class{ntn-divc}{\operatorname{div}}=2\ne0$, and indeed $u-iv=\bar z$ is not holomorphic.<br>
<b>Stagnation point</b> $(u,v)=(x,-y)$: $\class{ntn-divc}{\operatorname{div}}=0$ and $\class{ntn-divc}{\operatorname{curl}}=0$, and $u-iv=x+iy=z$ is holomorphic.
:::
<figure><div class="fpanels"><div class="fpanel">{{fig:x6-1}}<div class="flab">rotation $(-y,x)$</div></div><div class="fpanel">{{fig:x6-2}}<div class="flab">source $(x,y)$</div></div><div class="fpanel">{{fig:x6-3}}<div class="flab">stagnation $(x,-y)$</div></div></div><figcaption>The three fields of @eg:which-flows-come-from-holomorphic-functions. Only the third is divergence- and curl-free.</figcaption></figure>
::: proof
Rotation: $\class{ntn-divc}{\operatorname{curl}}=\partial_x(x)-\partial_y(-y)=1-(-1)=2$, the fluid circulating in closed loops (vorticity); and $u-iv=-y-ix=-i(x-iy)=-i\bar z$. Source: $\class{ntn-divc}{\operatorname{div}}=\partial_xx+\partial_yy=2$, fluid pouring out of the origin; $u-iv=x-iy=\bar z$. Stagnation point: $\class{ntn-divc}{\operatorname{div}}=1-1=0$, $\class{ntn-divc}{\operatorname{curl}}=\partial_x(-y)-\partial_y(x)=0-0=0$; $u-iv=x-i(-y)=z$. Finally, $\bar z=x-iy$ is not holomorphic: its real part $x$ and imaginary part $-y$ have $\partial_x(x)=1\ne-1=\partial_y(-y)$, violating Cauchy–Riemann everywhere; and $-i\bar z$ is not holomorphic either, since $\bar z=i\cdot(-i\bar z)$ would then be.
:::
