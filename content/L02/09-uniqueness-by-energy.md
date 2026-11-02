---
id: w9
slide: Slides 18–20
title: Harmonic functions are determined by their boundary values
toc: Uniqueness by energy
---

::: theorem {#thm:uniqueness name=uniqueness}
Let $\Omega$ be a bounded open set with [piecewise $C^1$ boundary](apx:C3), and let $h_1,h_2\in C^2(\overline\Omega)$ be harmonic on $\Omega$. If $h_1=h_2$ on $\class{ntn-dOm}{\partial\Omega}$, then $h_1=h_2$ on all of $\Omega$.
:::
<p>Physically obvious for temperatures: hold the boundary of a plate at a prescribed temperature and wait; the equilibrium temperature inside is whatever it is, and nothing else. The proof is by the <b>energy method</b>. Here $C^2(\overline\Omega)$ means two continuous derivatives up to and including the boundary ([function classes](apx:D1)); this is what the divergence theorem on $\Omega$ needs.</p>
::: proof
Let $w=h_1-h_2$. It is harmonic on $\Omega$ (the Laplacian is linear), $C^2$ up to the boundary, and zero on $\class{ntn-dOm}{\partial\Omega}$.
<ol>
<li><em>A product rule.</em> For the vector field $w\nabla w=(w\,w_x,\ w\,w_y)$,
\[ \operatorname{div}(w\nabla w)=\partial_x(w\,w_x)+\partial_y(w\,w_y)=(w_x^2+w\,w_{xx})+(w_y^2+w\,w_{yy})=|\nabla w|^2+w\,\class{ntn-Delta}{\Delta} w. \]</li>
<li><em>The divergence theorem</em> applied to $w\nabla w$, which is $C^1$ on $\overline\Omega$:
\[ \iint_\Omega\operatorname{div}(w\nabla w)\,dA=\oint_{\class{ntn-dOm}{\partial\Omega}}w\,\nabla w\cdot n\,ds=0, \]
the boundary integral vanishing because $w=0$ at every point of $\class{ntn-dOm}{\partial\Omega}$.</li>
<li><em>Combine.</em> Integrating Step 1 over $\Omega$ and using Step 2,
\[ 0=\iint_\Omega|\nabla w|^2\,dA+\iint_\Omega w\,\class{ntn-Delta}{\Delta} w\,dA=\iint_\Omega|\nabla w|^2\,dA,\qquad\text{since }\class{ntn-Delta}{\Delta} w=0. \]</li>
<li><em>Conclude.</em> The integrand $|\nabla w|^2$ is continuous and $\ge0$ with integral $0$, so $\nabla w\equiv0$ on $\Omega$ ([zero integral forces zero](apx:A11)). Hence $w$ is constant on each [connected component](apx:C4) $\Omega'$ of $\Omega$: two points of $\Omega'$ can be joined by a path, and the derivative of $w$ along the path is $\nabla w\cdot(\text{velocity})=0$. Each constant is $0$: $\Omega'$ is bounded and nonempty, so it has a boundary point $p$, and $p\in\class{ntn-dOm}{\partial\Omega}$ (the argument of @cor:maximum-principle, step 5). By continuity $w(p)$ equals the constant, and $w(p)=0$. <span class="qed">∎</span></li>
</ol>
:::

::: remark {#rem:energy name=energy}
The quantity $\iint_\Omega|\nabla w|^2\,dA$ is the <b>energy</b> of $w$: the kinetic energy of the fluid, or the energy stored in the electric field. The proof says: a harmonic function with zero boundary values has zero energy, hence is zero. Lecture 3 builds on this: the same product rule is @prop:the-slides-computation, the energy is @def:energy, and the harmonic function turns out to be the one minimizing energy (@lem:among-all-is-the-unique). Lecture 4 reproves uniqueness by the maximum principle (@cor:stability), which needs $h$ only continuous up to the boundary rather than $C^2$.
:::
