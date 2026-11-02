---
id: v4
slide: Slide 4
title: 'Steps 2 and 3: what we may use'
toc: What we may use
---

::: setting {#set:from-now-on-is-linear kind="Standing setting"}
From now on $g$ is linear on each boundary edge of the coarsest grid (@hyp:for-now), and $\class{ntn-Un}{U_n}$ is the finite element solution on the grid of side $\class{ntn-epsn}{\eps_n}=2^{-n}\class{ntn-epsn}{\eps_0}$: equal to $g$ at the boundary nodes and bilinear on each square. Points of the plane are written $z=x+iy$ ([complex notation](apx:C1)).
:::

<p>Four facts are available.</p>
<ol>
<li><b>$\class{ntn-Un}{U_n}=g$ on all of $\class{ntn-dOm}{\partial\Omega}$.</b> On a boundary edge, $\class{ntn-Un}{U_n}$ is linear (@prop:linear-along-grid-lines-not-on) and agrees with $g$ at both ends; $g$ is linear on the edge too, so they agree on the whole edge. (This is [Lemma #(b)](@lem:nesting).)</li>
<li><b>$\class{ntn-Un}{U_n}\to u$ and $\nabla \class{ntn-Un}{U_n}\to\nabla u$ in $L^2(\Omega)$</b> (@prop:three-limits, @prop:and-weakly-write).</li>
<li><b>$u$ is smooth and harmonic in $\Omega$</b> (@cor:the-lecture-3-limit-is-a). As agreed after @thm:proof-of-weyls-lemma, $u$ denotes the smooth representative; changing $u$ on a set of area zero does not affect fact 2.</li>
<li><b>The maximum principle</b> for harmonic functions in $C^2(\Omega)\cap C(\overline\Omega)$ (@cor:maximum-principle).</li>
</ol>

::: definition {#def:the-goal-step-4 name="the goal, step 4"}
To be proved: for every $p\in\class{ntn-dOm}{\partial\Omega}$, $u(z)\to g(p)$ as $z\to p$ with $z\in\Omega$.
:::
<p>Why this finishes the theorem: let $\tilde u:=u$ on $\Omega$ and $\tilde u:=g$ on $\class{ntn-dOm}{\partial\Omega}$. At a boundary point $p$, values of $\tilde u$ at nearby interior points tend to $g(p)$ by step 4, and values at nearby boundary points tend to $g(p)$ because $g$ is continuous. So $\tilde u$ is continuous at $p$, and $\tilde u\in C^2(\Omega)\cap C(\overline\Omega)$ solves the problem.</p>
<p>Fact 4 cannot be applied to $u$ directly: it needs $u\in C(\overline\Omega)$, which is exactly what step 4 is meant to establish. The comparison lemma of @sec:v7 is the way around this.</p>
