---
id: x8
slide: Slide 16
title: The two potentials
---

::: proposition {#prop:velocity-potential-stream-function-primitive name="velocity potential, stream function, primitive"}
Let $f=u-iv$ be holomorphic on a disk $D$, with $u,v\in C^1$, so that the associated flow $V=(u,v)$ is curl-free and divergence-free. Then there are $C^2$ functions $\class{ntn-vphi}{\varphi},\class{ntn-spsi}{\psi}$ on $D$ with
\[ \nabla\class{ntn-vphi}{\varphi}=(u,v)\quad(\class{ntn-vphi}{\varphi}_x=u,\ \class{ntn-vphi}{\varphi}_y=v),\qquad\nabla\class{ntn-spsi}{\psi}=(-v,u)\quad(\class{ntn-spsi}{\psi}_x=-v,\ \class{ntn-spsi}{\psi}_y=u), \]
and $F:=\class{ntn-vphi}{\varphi}+i\class{ntn-spsi}{\psi}$ is holomorphic on $D$ with $F'=f$.
:::
::: proof

<ol>
<li><em>Velocity potential.</em> $\class{ntn-divc}{\operatorname{curl}}(u,v)=0$ (@prop:cauchy-riemann-in-the-language-of), so the Poincaré lemma (@fact:poincare-lemma-on-a-disk) gives $\class{ntn-vphi}{\varphi}$ with $\nabla\class{ntn-vphi}{\varphi}=(u,v)$.</li>
<li><em>Stream function.</em> Rotate by $90°$:
\[ \class{ntn-divc}{\operatorname{curl}}(-v,u)=\partial_xu-\partial_y(-v)=u_x+v_y=\class{ntn-divc}{\operatorname{div}}(u,v)=0. \]
So the Poincaré lemma gives $\class{ntn-spsi}{\psi}$ with $\nabla\class{ntn-spsi}{\psi}=(-v,u)$.</li>
<li><em>Put them together.</em> Comparing, $\class{ntn-vphi}{\varphi}_x=u=\class{ntn-spsi}{\psi}_y$ and $\class{ntn-vphi}{\varphi}_y=v=-\class{ntn-spsi}{\psi}_x$. These are the Cauchy–Riemann equations of @thm:cauchy-riemann for $F=\class{ntn-vphi}{\varphi}+i\class{ntn-spsi}{\psi}$. Since $\class{ntn-vphi}{\varphi},\class{ntn-spsi}{\psi}$ have continuous gradients, they are differentiable ([A.1](apx:A1)), so $F$ is holomorphic on $D$, and
\[ F'=\class{ntn-vphi}{\varphi}_x+i\,\class{ntn-spsi}{\psi}_x=u-iv=f. \]
<span class="qed">∎</span></li>
</ol>
:::
<p>So every holomorphic function on a disk has a holomorphic <em>primitive</em> (antiderivative). The disk is essential, through the Poincaré lemma; see @sec:x14.</p>
