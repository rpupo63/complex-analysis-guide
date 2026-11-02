---
id: s20
slide: Slide 20
title: The limit satisfies the weak form
toc: The limit is a weak solution
---

::: proposition {#prop:three-limits name="three limits"}
$(\class{ntn-Un}{U_n})$, $(\partial_x\class{ntn-Un}{U_n})$ and $(\partial_y\class{ntn-Un}{U_n})$ are Cauchy in $L^2$. Call their limits $u$, $p$, $q\in L^2(\Omega)$.
:::
::: proof
Since $|\partial_xf|\le|\nabla f|$ at every point, $\class{ntn-L2}{\norm{\partial_x\class{ntn-Un}{U_n}-\partial_x\class{ntn-Un}{U_k}}}\le\class{ntn-L2}{\norm{\nabla(\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k})}}$, and likewise for $\partial_y$. @cor:it-applies-to-u-n-u gives $\class{ntn-L2}{\norm{\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k}}}\le \class{ntn-L}{L}\class{ntn-L2}{\norm{\nabla(\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k})}}$. All three right-hand sides tend to $0$ by @prop:for-consequently-is-a-cauchy. Limits exist because [$L^2$ is complete](apx:D3).
:::

::: definition {#def:weak-derivative name="weak derivative"}
Let $u,p\in L^2(\Omega)$. $p$ is the <em>weak $x$-derivative</em> of $u$, written $p=\partial_xu$, if
\[ \iint_\Omega u\,\partial_x\psi\,dA=-\iint_\Omega p\,\psi\,dA \]
for every continuously differentiable $\psi$ [supported inside $\Omega$](apx:C7). The weak $y$-derivative is defined the same way. For smooth $u$, integration by parts shows the weak and classical derivatives agree, which is why the slide can say "by definition".
:::

::: proposition {#prop:and-weakly-write}
$p=\partial_xu$ and $q=\partial_yu$ weakly. Write $\nabla u:=(p,q)$.
:::
::: proof
<em>Step 1: the identity holds for each $\class{ntn-Un}{U_n}$.</em> Extend $\class{ntn-Un}{U_n}\psi$ by $0$ outside $\Omega$. Because $\psi$ vanishes near $\class{ntn-dOm}{\partial\Omega}$, this is continuous and piecewise $C^1$ and vanishes outside a bounded set. For fixed $y$, the [fundamental theorem of calculus](apx:A9) over an interval containing that set gives $\int_{\R}\partial_x(\class{ntn-Un}{U_n}\psi)\,dx=0$. Off the grid lines the product rule gives $\partial_x(\class{ntn-Un}{U_n}\psi)=\partial_x\class{ntn-Un}{U_n}\,\psi+\class{ntn-Un}{U_n}\,\partial_x\psi$. Integrate in $y$:
\[ \iint \class{ntn-Un}{U_n}\,\partial_x\psi\,dA=-\iint\partial_x\class{ntn-Un}{U_n}\,\psi\,dA. \]
<em>Step 2: pass to the limit.</em> By [Cauchy–Schwarz](apx:A12),
\[ \Big|\iint \class{ntn-Un}{U_n}\partial_x\psi-\iint u\,\partial_x\psi\Big|\le\class{ntn-L2}{\norm{\class{ntn-Un}{U_n}-u}}\,\class{ntn-L2}{\norm{\partial_x\psi}}\to0,\qquad \Big|\iint\partial_x\class{ntn-Un}{U_n}\,\psi-\iint p\,\psi\Big|\le\class{ntn-L2}{\norm{\partial_x\class{ntn-Un}{U_n}-p}}\,\class{ntn-L2}{\norm{\psi}}\to0. \]
So the two sides of Step 1 converge to $\iint u\,\partial_x\psi$ and $-\iint p\,\psi$. Equal sequences have equal limits, which is the identity of @def:weak-derivative. The same argument works in $y$.
:::

::: proposition {#prop:test-functions-from-a-fixed-grid name="test functions from a fixed grid"}
For every $N$ and every $w\in \class{ntn-Vz}{V^0_{\eps_N}}$, $\ \class{ntn-a}{a}(u,w):=\iint(p\,\partial_xw+q\,\partial_yw)\,dA=0$.
:::
::: proof
For $n\ge N$, $w\in \class{ntn-Vz}{V^0_{\eps_n}}$ ([Lemma #(c)](@lem:nesting)), so $\class{ntn-a}{a}(\class{ntn-Un}{U_n},w)=0$ by @def:discrete-problem. By [Cauchy–Schwarz](apx:A12),
\[ |\class{ntn-a}{a}(\class{ntn-Un}{U_n},w)-\class{ntn-a}{a}(u,w)|=\Big|\iint(\nabla \class{ntn-Un}{U_n}-\nabla u)\cdot\nabla w\Big|\le\class{ntn-L2}{\norm{\nabla \class{ntn-Un}{U_n}-\nabla u}}\,\class{ntn-L2}{\norm{\nabla w}}\to0. \]
So $\class{ntn-a}{a}(u,w)=\lim_n \class{ntn-a}{a}(\class{ntn-Un}{U_n},w)=0$.
:::

::: lemma {#lem:the-slides-taylors-theorem-on-each name="the slide's \"Taylor's theorem on each square\""}
Let $\eta$ be twice continuously differentiable on $\overline\Omega$ with $\eta=0$ on $\class{ntn-dOm}{\partial\Omega}$, and let $M_2$ bound $|\nabla\partial_x\eta|$ and $|\nabla\partial_y\eta|$ on $\overline\Omega$. The nodal interpolant $\class{ntn-etaN}{\eta_N}:=\sum_{ij}\eta(x_i,y_j)\class{ntn-phi}{\varphi_{ij}}$ at level $N$ lies in $\class{ntn-Vz}{V^0_{\eps_N}}$, and
\[ \norm{\nabla(\eta-\class{ntn-etaN}{\eta_N})}_{L^2}^2\le4M_2^2\,\class{ntn-epsn}{\eps_N}^2\,|\Omega|\ \longrightarrow\ 0 \quad (N\to\infty), \]
where $|\Omega|$ is the area of $\Omega$.
:::
::: proof
$\class{ntn-etaN}{\eta_N}\in \class{ntn-Veps}{V_{\eps_N}}$, and its boundary-node values are $\eta=0$ because boundary nodes lie on $\class{ntn-dOm}{\partial\Omega}$. So $\class{ntn-etaN}{\eta_N}\in \class{ntn-Vz}{V^0_{\eps_N}}$.<br>
Fix a square with lower-left corner $(x_i,y_j)$ and side $h=\class{ntn-epsn}{\eps_N}$, and a point $(x,y)$ inside it with $t=(y-y_j)/h$. Differentiate the formulas of @lem:the-four-hats-on-one-square in $x$; each $\partial_s$ brings a factor $1/h$:
\[ \partial_x\class{ntn-etaN}{\eta_N}(x,y)=(1-t)\,\frac{\eta(x_{i+1},y_j)-\eta(x_i,y_j)}{h}+t\,\frac{\eta(x_{i+1},y_{j+1})-\eta(x_i,y_{j+1})}{h}. \]
By the [mean value theorem](apx:A3) the first quotient equals $\partial_x\eta(\xi_1,y_j)$ and the second equals $\partial_x\eta(\xi_2,y_{j+1})$, for some $\xi_1,\xi_2\in(x_i,x_{i+1})$. Both points lie in the same closed square as $(x,y)$, so each is within distance $\sqrt2h$ of it. The [two-variable bound](apx:A3) applied to $F=\partial_x\eta$ gives $|\partial_x\eta(\xi_1,y_j)-\partial_x\eta(x,y)|\le M_2\sqrt2h$, and likewise for $\xi_2$. The weights $1-t$ and $t$ are nonnegative and add to 1, so
\[ |\partial_x\class{ntn-etaN}{\eta_N}(x,y)-\partial_x\eta(x,y)|\le(1-t)M_2\sqrt2h+tM_2\sqrt2h=\sqrt2M_2h. \]
The same holds for $\partial_y$. So $|\nabla(\class{ntn-etaN}{\eta_N}-\eta)|^2\le2M_2^2h^2+2M_2^2h^2=4M_2^2h^2$ off the grid lines. Integrate over $\Omega$.
:::

::: theorem {#thm:smooth-test-functions name="smooth test functions"}
$\class{ntn-a}{a}(u,\eta)=0$ for every $\eta$ as in @lem:the-slides-taylors-theorem-on-each.
:::
::: proof
Split $\class{ntn-a}{a}(u,\eta)=\class{ntn-a}{a}(u,\class{ntn-etaN}{\eta_N})+\class{ntn-a}{a}(u,\eta-\class{ntn-etaN}{\eta_N})$. The first term is $0$ by @prop:test-functions-from-a-fixed-grid. The second is at most $\class{ntn-L2}{\norm{\nabla u}}\,\class{ntn-L2}{\norm{\nabla(\eta-\class{ntn-etaN}{\eta_N})}}$ in absolute value by [Cauchy–Schwarz](apx:A12), and this tends to $0$ as $N\to\infty$ by @lem:the-slides-taylors-theorem-on-each. The left side does not depend on $N$, so it is $0$.
:::
