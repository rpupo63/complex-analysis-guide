---
id: v13
slide: Slide 13
title: What we have proved
---

::: theorem {#thm:step-4-restated name="step 4, restated"}
For $g$ linear on the coarse boundary edges, the energy limit $u$ of Lecture 3 satisfies $u(z)\to g(p)$ as $z\to p$, for every $p\in\class{ntn-dOm}{\partial\Omega}$.
:::

::: proof {title="Proof of Theorem [#](=thm:the-dirichlet-problem-on-a-union)."}

<ol>
<li><em>Linear-edge data.</em> Let $g$ be linear on each boundary edge of some grid, and take that grid as the coarsest. Lecture 3 gives the energy limit $u$ (@thm:existence-of-a-weak-solution); Lecture 4 makes it smooth and harmonic in $\Omega$ (@cor:the-lecture-3-limit-is-a); @thm:step-4-boundary-values gives the boundary values. As explained after @def:the-goal-step-4, $u$ extended by $g$ on $\class{ntn-dOm}{\partial\Omega}$ lies in $C^2(\Omega)\cap C(\overline\Omega)$ and solves the problem.</li>
<li><em>General continuous $g$.</em> @prop:the-reduction.</li>
<li><em>Uniqueness.</em> @cor:stability: two solutions with the same boundary values coincide. <span class="qed">∎</span></li>
</ol>
:::

::: remark {#rem:what-went-in name="what went in"}

<ul>
<li><b>Lecture 3:</b> the two limits $\class{ntn-Un}{U_n}\to u$ and $\nabla \class{ntn-Un}{U_n}\to\nabla u$, and $\class{ntn-Un}{U_n}=g$ on $\class{ntn-dOm}{\partial\Omega}$.</li>
<li><b>Lecture 4:</b> Weyl's lemma and the maximum principle.</li>
<li><b>Today:</b> integration by parts against $\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}$, and the logarithmic barrier.</li>
</ul>
:::

::: remark {#rem:beyond-grids name="beyond grids"}
The comparison lemma used nothing about the $\class{ntn-Un}{U_n}$ except the three properties above. Stripped of the grid, it says:
<p style="text-align:center"><b>A harmonic function that is an energy limit of functions with boundary values $\le v$ on $\class{ntn-dOm}{\partial\Omega}$ is $\le v$ in $\Omega$.</b></p>
With ["$H^1$" and "trace"](apx:D6) put in, this is the [weak maximum principle](apx:E14) of the modern theory of elliptic equations. The grid was used in only two places: to build the $\class{ntn-Un}{U_n}$ (Lecture 3), and to find an empty square next to each boundary point for the barrier (@lem:an-empty-coarse-square-at-p). On general domains the second can fail; see [barriers and regular points](apx:E15).
:::
