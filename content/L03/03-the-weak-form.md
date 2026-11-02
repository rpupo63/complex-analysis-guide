---
id: s4
slide: Slide 4
title: The weak form
---

<p>The slide says "take any function $w$ vanishing on $\class{ntn-dOm}{\partial\Omega}$". Some regularity is needed for the integrals below to exist. Throughout, "test function" means an [admissible test function](apx:D4): continuous on $\overline\Omega$, piecewise continuously differentiable, and zero on $\class{ntn-dOm}{\partial\Omega}$. Hat functions (@sec:s5) and smooth functions both qualify.</p>

::: definition {#def:energy-form name="energy form"}
For functions $u,w$ whose gradients are square-integrable on $\Omega$,
\[ \class{ntn-a}{a}(u,w) := \iint_\Omega \nabla u\cdot\nabla w\,dA = \iint_\Omega \big(u_x w_x + u_y w_y\big)\,dA. \]
:::

::: proposition {#prop:properties-of-a name="properties of $a$"}
$a$ is a [symmetric bilinear form](apx:B1), and $\class{ntn-a}{a}(v,v)\ge 0$ for every $v$.
:::
::: proof
<em>Linear in the first slot:</em> $\nabla(\alpha u_1+\beta u_2)=\alpha\nabla u_1+\beta\nabla u_2$, the dot product is linear in each slot, and the integral is linear, so $\class{ntn-a}{a}(\alpha u_1+\beta u_2,w)=\alpha \class{ntn-a}{a}(u_1,w)+\beta \class{ntn-a}{a}(u_2,w)$. <em>Symmetric:</em> $\nabla u\cdot\nabla w=\nabla w\cdot\nabla u$ at every point. <em>Linear in the second slot:</em> this follows from the first two. <em>Nonnegative:</em> $\class{ntn-a}{a}(v,v)=\iint|\nabla v|^2\,dA$ is the integral of a nonnegative function.
:::

::: proposition {#prop:the-slides-computation name="the slide's computation"}
Let $u$ be twice continuously differentiable on $\overline\Omega$ with $\class{ntn-Delta}{\Delta} u=0$ in $\Omega$. Then $\class{ntn-a}{a}(u,w)=0$ for every test function $w$.
:::
::: proof
<em>Step 1 (product rule).</em> Put $F := w\nabla u = (w u_x,\, w u_y)$. Then
\[ \nabla\cdot F = \partial_x(w u_x)+\partial_y(w u_y) = (w_x u_x + w u_{xx}) + (w_y u_y + w u_{yy}) = \nabla w\cdot\nabla u + w\,\class{ntn-Delta}{\Delta} u. \]
<em>Step 2 (integrate).</em> Rearrange Step 1 as $w\,\class{ntn-Delta}{\Delta} u=\nabla\cdot F-\nabla w\cdot\nabla u$, integrate over $\Omega$, and apply the [divergence theorem](apx:A6) to the first term (the same computation as Steps 1–2 of @thm:uniqueness):
\[ \iint_\Omega w\,\class{ntn-Delta}{\Delta} u\,dA = \oint_{\class{ntn-dOm}{\partial\Omega}} w\,\nabla u\cdot n\,ds - \iint_\Omega \nabla w\cdot\nabla u\,dA. \]
This is the "integration by parts" of the slide.<br>
<em>Step 3.</em> The left side is $0$ because $\class{ntn-Delta}{\Delta} u=0$. The boundary integral is $0$ because $w=0$ on $\class{ntn-dOm}{\partial\Omega}$. So $0=-\class{ntn-a}{a}(u,w)$, which is the slide's display.<br>
<em>Step 4 (piecewise smooth $w$).</em> If $w$ is smooth only on pieces $P_1,\dots,P_m$ of $\Omega$, apply Steps 1–2 on each piece and add. A segment shared by two pieces appears in both boundary integrals with opposite outward normals and the same continuous integrand $w\nabla u$, so those contributions cancel. Only the outer boundary $\class{ntn-dOm}{\partial\Omega}$ remains, where $w=0$.
:::

::: definition {#def:weak-form-of-the-dirichlet-problem name="weak form of the Dirichlet problem"}
Find $u$ with $u=g$ on $\class{ntn-dOm}{\partial\Omega}$ such that
\[ \class{ntn-a}{a}(u,w)=0 \quad\text{for every test function } w. \]
:::

::: remark {#rem:proposition-3-3-3-proves}
[Proposition #](@prop:the-slides-computation) proves one direction only: a smooth solution is a weak solution. The weak form asks for first derivatives only, so it also admits the functions with corners built below. The converse, that a weak solution is smooth and harmonic, is [Weyl's lemma](@thm:weyls-lemma), proved in Lecture 4 (@sec:t7–@sec:t10).
:::
