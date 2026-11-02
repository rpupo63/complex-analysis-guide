---
id: s21
slide: Slide 21
title: What has been proved
---

::: theorem {#thm:existence-of-a-weak-solution name="existence of a weak solution"}
Assume @hyp:for-now. Let $\class{ntn-Un}{U_0}\in \class{ntn-Vg}{V^g_{\eps_0}}$ be the coarsest discrete solution and $\class{ntn-Un}{U_n}$ the solution at level $n$; each equals $g$ on all of $\class{ntn-dOm}{\partial\Omega}$. Then:
<ol>
<li>$\class{ntn-Un}{U_n}\to u$ and $\nabla \class{ntn-Un}{U_n}\to\nabla u$ in $L^2(\Omega)$. So $u$ is a square-integrable function with a square-integrable weak gradient; in the standard notation, $u$ lies in the [Sobolev space](apx:D6) $\class{ntn-H1}{H^1}(\Omega)$.</li>
<li>$\class{ntn-a}{a}(u,w)=0$ for every smooth $w$ vanishing on $\class{ntn-dOm}{\partial\Omega}$.</li>
<li>The boundary condition is retained in this form: every $\class{ntn-Un}{U_n}-\class{ntn-Un}{U_0}$ vanishes on $\class{ntn-dOm}{\partial\Omega}$, while $\class{ntn-Un}{U_n}-\class{ntn-Un}{U_0}\to u-\class{ntn-Un}{U_0}$ and $\nabla(\class{ntn-Un}{U_n}-\class{ntn-Un}{U_0})\to\nabla(u-\class{ntn-Un}{U_0})$ in $L^2$.</li>
</ol>
Thus $u$ satisfies the weak form (@def:weak-form-of-the-dirichlet-problem) of the Dirichlet problem.
:::
::: proof
Item 1 is [Props. #](@prop:three-limits) and [#](@prop:and-weakly-write). Item 2 is @thm:smooth-test-functions. For item 3: $\class{ntn-Un}{U_0}\in \class{ntn-Vg}{V^g_{\eps_0}}\subset \class{ntn-Vg}{V^g_{\eps_n}}$ by [Lemma #(b)](@lem:nesting), so $\class{ntn-Un}{U_0}$ and $\class{ntn-Un}{U_n}$ both equal $g$ on $\class{ntn-dOm}{\partial\Omega}$ and their difference vanishes there. The convergence follows from item 1 by subtracting the fixed function $\class{ntn-Un}{U_0}$.
:::

::: remark {#rem:why-item-3-is-the-boundary name="why item 3 is the boundary condition"}
An $L^2$ function can be changed on a zero-area set without changing it as an element of $L^2$, and $\class{ntn-dOm}{\partial\Omega}$ has zero area. So "$u=g$ on $\class{ntn-dOm}{\partial\Omega}$" cannot be checked point by point yet. Item 3 is the substitute: $u$ differs from $\class{ntn-Un}{U_0}$, which does equal $g$ on the boundary, by a limit of functions that vanish on the boundary. The standard formalization is the [space $H^1_0$ and the trace operator](apx:D6).
:::

<h3>Missing pieces</h3>
<ul>
<li>$u$ is smooth and $\class{ntn-Delta}{\Delta} u=0$ pointwise: Weyl's lemma. <b>Done in Lecture 4</b>, @cor:the-lecture-3-limit-is-a.</li>
<li>$u(x)\to g(p)$ as $x\to p\in\class{ntn-dOm}{\partial\Omega}$, pointwise. <b>Done in Lecture 5</b>, @thm:step-4-boundary-values, by energy and comparison rather than [the random walk](apx:E9).</li>
</ul>
