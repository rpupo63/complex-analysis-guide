---
id: s5
slide: Slide 5
title: A grid and hat functions
toc: Grid and hat functions
---

::: hypothesis {#hyp:fix-and-grid-lines-with kind="Grid hypothesis"}
Fix $\eps>0$ and grid lines $x_i = x_0+i\eps$, $y_j=y_0+j\eps$ with $i,j\in\mathbb Z$. $\overline\Omega$ is a finite union of closed grid squares $[x_i,x_{i+1}]\times[y_j,y_{j+1}]$, and $\Omega$ is the interior of that union.
:::
<p>Consequently $\class{ntn-dOm}{\partial\Omega}$ is made of grid edges. An edge of a square in $\Omega$ lies on $\class{ntn-dOm}{\partial\Omega}$ exactly when the square on its other side is not in $\Omega$. Call such an edge a <em>boundary edge</em>.</p>

::: definition {#def:nodes name=nodes}
A <em>node</em> is a corner $(x_i,y_j)$ of some grid square contained in $\overline\Omega$.
:::

::: definition {#def:tent-and-hat-functions name="tent and hat functions"}
The tent function in one variable is $\class{ntn-Lam}{\Lambda}(t):=\max(0,\,1-|t|)$. The hat (basis) function at the node $(x_i,y_j)$ is
\[ \class{ntn-phi}{\varphi_{ij}}(x,y) := \class{ntn-Lam}{\Lambda}\!\Big(\frac{x-x_i}{\eps}\Big)\,\class{ntn-Lam}{\Lambda}\!\Big(\frac{y-y_j}{\eps}\Big). \]
:::

<figure>
{{fig:s5-1}}
<figcaption>The tent $\class{ntn-Lam}{\Lambda}$: height 1 at $0$, zero outside $[-1,1]$, slope $\pm1$ in between.</figcaption>
</figure>

::: lemma {#lem:the-tent name="the tent"}
$\class{ntn-Lam}{\Lambda}$ is continuous, $0\le\class{ntn-Lam}{\Lambda}\le1$, $\class{ntn-Lam}{\Lambda}(0)=1$, $\class{ntn-Lam}{\Lambda}(m)=0$ for every nonzero integer $m$, and $\class{ntn-Lam}{\Lambda}(t)=0$ for $|t|\ge1$. Away from $t\in\{-1,0,1\}$ it is differentiable, with
\[ \class{ntn-Lam}{\Lambda}'(t)=\begin{cases} 1, & -1\lt t\lt 0,\\ -1, & 0\lt t\lt 1,\\ 0, & |t|\gt 1.\end{cases} \]
:::
::: proof
If $|t|\le1$ then $1-|t|\ge0$, so $\class{ntn-Lam}{\Lambda}(t)=1-|t|$. If $|t|\ge1$ then $1-|t|\le0$, so $\class{ntn-Lam}{\Lambda}(t)=0$. Every claim can be read off these two formulas; for a nonzero integer, $|m|\ge1$. The maximum of two continuous functions is continuous.
:::

::: proposition {#prop:the-hat name="the hat"}
$\class{ntn-phi}{\varphi_{ij}}$ is continuous, equals $1$ at $(x_i,y_j)$, and vanishes outside the $2\eps\times2\eps$ block $[x_{i-1},x_{i+1}]\times[y_{j-1},y_{j+1}]$ (its [support](apx:C7)). Off the grid lines it is differentiable, with
\[ \nabla\class{ntn-phi}{\varphi_{ij}}(x,y)=\frac1\eps\Big(\class{ntn-Lam}{\Lambda}'\big(\tfrac{x-x_i}{\eps}\big)\class{ntn-Lam}{\Lambda}\big(\tfrac{y-y_j}{\eps}\big),\ \class{ntn-Lam}{\Lambda}\big(\tfrac{x-x_i}{\eps}\big)\class{ntn-Lam}{\Lambda}'\big(\tfrac{y-y_j}{\eps}\big)\Big). \]
So $|\nabla\class{ntn-phi}{\varphi_{ij}}|\le\sqrt2/\eps$ and $\iint|\nabla\class{ntn-phi}{\varphi_{ij}}|^2\,dA\lt\infty$.
:::
::: proof
Continuity and the value $1\cdot1$ at the node follow from @lem:the-tent. If $|x-x_i|\ge\eps$ the first factor is $0$, and likewise in $y$, so the hat vanishes outside the block. The gradient comes from the product rule and the chain rule (inner derivative $1/\eps$). The kinks of $\class{ntn-Lam}{\Lambda}$ at $t\in\{-1,0,1\}$ correspond to $x\in\{x_{i-1},x_i,x_{i+1}\}$, which are grid lines, so off the grid lines both factors are differentiable. Each component has absolute value at most $1\cdot1/\eps$, so $|\nabla\class{ntn-phi}{\varphi_{ij}}|^2\le 2/\eps^2$. Integrating over the block, of area $4\eps^2$, gives at most $8$. The grid lines are finitely many segments, which have [zero area](apx:A11), so leaving them out changes no integral. @sec:s11 computes the exact value, $8/3$.
:::
