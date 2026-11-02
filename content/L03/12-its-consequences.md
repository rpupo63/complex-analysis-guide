---
id: s13
slide: Slide 13
title: Consequences of the maximum principle
toc: Its consequences
---

::: corollary {#cor:uniqueness-again name="uniqueness, again"}
If $g=0$ at every boundary node, then $\class{ntn-Ue}{U_\eps}\equiv0$.
:::
::: proof
@thm:discrete-maximum-principle gives $0\le \class{ntn-Ue}{U_\eps}\le0$. Applied to the difference of two discrete solutions with the same data, this reproves uniqueness without @thm:a-ii-is-positive-definite.
:::

::: corollary {#cor:a-bound name="a bound"}
$\min_{\class{ntn-dOm}{\partial\Omega}}g\le \class{ntn-Ue}{U_\eps}\le\max_{\class{ntn-dOm}{\partial\Omega}}g$, and the bounds do not depend on $\eps$.
:::
::: proof
This is the last line of @sec:s12. The bounds involve only $g$.
:::

::: proposition {#prop:a-weighted-average-of-the-boundary name="a weighted average of the boundary data"}
Let $\class{ntn-W}{W}:=-\class{ntn-AII}{A_{II}}^{-1}\class{ntn-AIB}{A_{IB}}$, an $n\times|B|$ matrix, so that $\class{ntn-cI}{c_I}=\class{ntn-W}{W}\class{ntn-gB}{g_B}$. Then
\[ \class{ntn-W}{W}_{pq}\ge0\quad\text{and}\quad\sum_{q\in \class{ntn-B}{B}}\class{ntn-W}{W}_{pq}=1\quad\text{for every }p\in \class{ntn-I}{I}. \]
So each interior value $c_p=\sum_qW_{pq}g_q$ is a weighted average of the boundary values, and the linear system computes the weights.
:::
::: proof
<em>Nonnegative.</em> Take data $\class{ntn-gB}{g_B}=e_q$: 1 at boundary node $q$, 0 at the others. Then $\class{ntn-cI}{c_I}$ is the $q$-th column of $\class{ntn-W}{W}$, and @thm:discrete-maximum-principle makes its entries $\ge\min(e_q)=0$.<br>
<em>Rows sum to 1.</em> Take $\class{ntn-gB}{g_B}\equiv1$. The constant vector $c\equiv1$ satisfies every equation of @cor:each-interior-value-is-the-average ($1=\frac18\cdot8$) and the boundary condition, so by uniqueness it is the solution. Hence $\class{ntn-W}{W}\mathbf 1=\mathbf 1$: every row of $\class{ntn-W}{W}$ sums to 1.
:::
<p>The slide calls this the concrete meaning of "harmonic functions are determined by their boundary values". The weights also have a [random-walk interpretation](apx:E9), which Lecture 3 announced for later. The course in the end proves the boundary behaviour without it (@thm:step-4-boundary-values).</p>
