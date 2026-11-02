---
id: s10
slide: Slide 10
title: The system has exactly one solution
toc: Exactly one solution
---

::: lemma {#lem:symmetry name=symmetry}
$\class{ntn-A}{A_{kl,ij}}=\class{ntn-A}{A_{ij,kl}}$, so $A$ and $\class{ntn-AII}{A_{II}}$ are [symmetric matrices](apx:B4).
:::
::: proof
$\class{ntn-a}{a}(\class{ntn-phi}{\varphi_{ij}},\class{ntn-phi}{\varphi_{kl}})=\class{ntn-a}{a}(\class{ntn-phi}{\varphi_{kl}},\class{ntn-phi}{\varphi_{ij}})$ because $a$ is symmetric (@prop:properties-of-a). $\class{ntn-AII}{A_{II}}$ keeps the rows and columns of $A$ with the same index set $I$, so it inherits the symmetry.
:::

::: lemma {#lem:the-quadratic-form-is-the-energy name="the quadratic form is the energy"}
For any coefficient vector $c$ and $U=\sum c_{ij}\class{ntn-phi}{\varphi_{ij}}$,
\[ c^{\mathsf T}\class{ntn-A}{A}c=\class{ntn-a}{a}(U,U)=\iint_\Omega|\nabla U|^2\,dA\ \ge 0. \]
:::
::: proof
Expand using linearity in both slots:
\[ \class{ntn-a}{a}(U,U)=a\Big(\sum_{ij}c_{ij}\class{ntn-phi}{\varphi_{ij}},\ \sum_{kl}c_{kl}\class{ntn-phi}{\varphi_{kl}}\Big)=\sum_{ij}\sum_{kl}c_{kl}\,\class{ntn-a}{a}(\class{ntn-phi}{\varphi_{ij}},\class{ntn-phi}{\varphi_{kl}})\,c_{ij}=\sum_{kl,ij}c_{kl}\class{ntn-A}{A_{kl,ij}}c_{ij}=c^{\mathsf T}\class{ntn-A}{A}c. \]
Nonnegativity is @prop:properties-of-a.
:::

::: theorem {#thm:a-ii-is-positive-definite name="$\class{ntn-AII}{A_{II}}$ is positive definite"}
For every nonzero $\class{ntn-cI}{c_I}\in\R^n$, $\class{ntn-cI}{c_I}^{\mathsf T}\class{ntn-AII}{A_{II}}\class{ntn-cI}{c_I}\gt0$. So $\class{ntn-AII}{A_{II}}$ is [positive definite](apx:B4), hence invertible, and the system has exactly one solution $\class{ntn-cI}{c_I}$.
:::
::: proof
Extend $\class{ntn-cI}{c_I}$ by zeros at the boundary nodes to get $c$ ("$c$ supported on the interior nodes"). Then $c^{\mathsf T}\class{ntn-A}{A}c=\class{ntn-cI}{c_I}^{\mathsf T}\class{ntn-AII}{A_{II}}\class{ntn-cI}{c_I}$, since every term involving a boundary index is multiplied by $0$. The corresponding $U$ lies in $\class{ntn-Vz}{V^0_\eps}$. Suppose $\class{ntn-cI}{c_I}^{\mathsf T}\class{ntn-AII}{A_{II}}\class{ntn-cI}{c_I}=0$; we show $\class{ntn-cI}{c_I}=0$.
<ol>
<li><em>$\nabla U\equiv0$.</em> By @lem:the-quadratic-form-is-the-energy, $\iint_\Omega|\nabla U|^2=0$. On each open square $|\nabla U|^2$ is continuous (a polynomial) and nonnegative, and a [continuous nonnegative function with zero integral is zero](apx:A11). So $\nabla U\equiv0$ on every open square.</li>
<li><em>$U$ is constant on each square.</em> On a square, $U=\alpha+\beta s+\gamma t+\delta st$, and $\nabla U=\frac1\eps(\beta+\delta t,\ \gamma+\delta s)\equiv0$ forces $\beta=\gamma=\delta=0$.</li>
<li><em>$U$ is constant on each connected piece.</em> Two squares that share an edge have the same constant, because $U$ is continuous on the edge. So $U$ equals a single constant $\kappa$ on each <em>cluster</em> $C$ of squares linked through shared edges. These clusters are the slide's [connected components](apx:C4).</li>
<li><em>Each cluster has boundary points.</em> Pick a square $Q\in C$ whose left edge has the smallest $x$-coordinate among the squares of $C$. The square immediately left of $Q$ is not in $\Omega$: if it were, it would share an edge with $Q$ and belong to $C$, contradicting minimality. So the left edge of $Q$ is a boundary edge, its endpoints are boundary nodes ([Lemma #(b)](@lem:nodes-and-the-boundary)), and $U=0$ there. Hence $\kappa=0$.</li>
<li>So $U\equiv0$, and by @cor:the-coefficients-are-the-nodal-values every $c_{kl}=0$.</li>
</ol>
This proves positive definiteness. [Positive definite matrices are invertible](apx:B4), so $\class{ntn-AII}{A_{II}}\class{ntn-cI}{c_I}=-\class{ntn-AIB}{A_{IB}}\class{ntn-gB}{g_B}$ has exactly one solution.
:::

::: definition {#def:the-discrete-solution name="the discrete solution"}
$\class{ntn-Ue}{U_\eps}:=\sum_{ij}c_{ij}\class{ntn-phi}{\varphi_{ij}}$ with $\class{ntn-cB}{c_B}=\class{ntn-gB}{g_B}$ and $\class{ntn-cI}{c_I}=-\class{ntn-AII}{A_{II}}^{-1}\class{ntn-AIB}{A_{IB}}\class{ntn-gB}{g_B}$. By @thm:a-ii-is-positive-definite and @prop:the-equations-of-prop-3 it is the unique solution of the discrete problem (@def:discrete-problem).
:::
