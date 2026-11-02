---
id: s7
slide: Slide 7
title: The spaces $\class{ntn-Vg}{V^g_\eps}$ and $\class{ntn-Vz}{V^0_\eps}$
toc: The spaces $V^g_\eps$ and $V^0_\eps$
---

::: definition {#def:interior-and-boundary-nodes name="interior and boundary nodes"}
A node is <em>interior</em> if all four grid squares having it as a corner lie in $\overline\Omega$, and a <em>boundary node</em> otherwise. Write $I$ and $B$ for the two sets and $n:=|I|$.
:::

::: lemma {#lem:nodes-and-the-boundary name="nodes and the boundary"}
(a) Every boundary node lies on $\class{ntn-dOm}{\partial\Omega}$. (b) Both endpoints of every boundary edge are boundary nodes. (c) An interior node lies in $\Omega$, and its hat vanishes on $\class{ntn-dOm}{\partial\Omega}$.
:::
::: proof
(a) A boundary node $P$ is a corner of some square in $\overline\Omega$ (it is a node) and of some square not in $\overline\Omega$ (it is not interior). Every disc around $P$ meets the interiors of both squares, so it meets $\Omega$ and its complement. That is the definition of a [boundary point](apx:C2).<br>
(b) A boundary edge separates a square in $\Omega$ from a square $Q'$ not in $\Omega$. Each endpoint is a corner of $Q'$, so it is not interior, and a corner of the square in $\Omega$, so it is a node.<br>
(c) If all four squares around $P$ are in $\overline\Omega$, the open $2\eps\times2\eps$ block around $P$ lies in $\Omega$. The hat $\class{ntn-phi}{\varphi_P}$ vanishes outside that open block (@prop:the-hat, and $\class{ntn-Lam}{\Lambda}(\pm1)=0$ on its rim), and $\class{ntn-dOm}{\partial\Omega}$ does not meet the open block.
:::

::: definition {#def:by-lemma-3-6-2}

\[ \class{ntn-Vg}{V^g_\eps} := \{U\in \class{ntn-Veps}{V_\eps} : U(x_i,y_j)=g(x_i,y_j)\ \text{at every boundary node}\},\qquad \class{ntn-Vz}{V^0_\eps} := \{U\in \class{ntn-Veps}{V_\eps} : U=0\ \text{at every boundary node}\}. \]
By [Lemma #(a)](@lem:nodes-and-the-boundary), boundary nodes lie where $g$ is defined, so $g(x_i,y_j)$ makes sense.
:::

::: proposition {#prop:v-g-eps-is-affine-not name="$\class{ntn-Vg}{V^g_\eps}$ is affine, not linear"}
If $U,V\in \class{ntn-Vg}{V^g_\eps}$ and $\lambda\in\R$, then $\lambda U+(1-\lambda)V\in \class{ntn-Vg}{V^g_\eps}$ and $U-V\in \class{ntn-Vz}{V^0_\eps}$. $\class{ntn-Vg}{V^g_\eps}$ is not closed under addition unless $g=0$ at every boundary node.
:::
::: proof
At a boundary node, $\lambda U+(1-\lambda)V$ takes the value $\lambda g+(1-\lambda)g=g$, and $U-V$ takes $g-g=0$. The sum $U+V$ takes $2g$, which equals $g$ only where $g=0$. Closure under combinations whose coefficients add to 1 is what makes a set [affine](apx:B3); $\lambda=\tfrac12$ gives the slide's "averages".
:::

::: proposition {#prop:the-space-v-0-eps name="the space $\class{ntn-Vz}{V^0_\eps}$"}
(a) $\class{ntn-Vz}{V^0_\eps}$ is a linear space. (b) Every $U\in \class{ntn-Vz}{V^0_\eps}$ vanishes on all of $\class{ntn-dOm}{\partial\Omega}$. (c) $\class{ntn-Vz}{V^0_\eps}=\operatorname{span}\{\class{ntn-phi}{\varphi_{kl}}:(k,l)\in \class{ntn-I}{I}\}$, so its [dimension](apx:B2) is $n$. (d) Every $U\in \class{ntn-Vg}{V^g_\eps}$ can be written $U=\class{ntn-Ug}{U_g}+W$, where $\class{ntn-Ug}{U_g}:=\sum_{\class{ntn-B}{B}}g(x_i,y_j)\class{ntn-phi}{\varphi_{ij}}$ is fixed and $W\in \class{ntn-Vz}{V^0_\eps}$.
:::
::: proof
(a) Sums and multiples preserve the zero condition.<br>
(b) $\class{ntn-dOm}{\partial\Omega}$ is a union of boundary edges. On a boundary edge $U$ is linear (@prop:linear-along-grid-lines-not-on) and vanishes at both endpoints ([Lemma #(b)](@lem:nodes-and-the-boundary)). A linear function of one variable that vanishes at two points is identically zero.<br>
(c) By @cor:the-coefficients-are-the-nodal-values, $U=\sum_{\text{all nodes}}U(x_i,y_j)\class{ntn-phi}{\varphi_{ij}}$, and the boundary coefficients are $0$, which leaves interior hats. Conversely, an interior hat is $0$ at every other node, in particular at every boundary node. Independence is @cor:the-coefficients-are-the-nodal-values.<br>
(d) $\class{ntn-Ug}{U_g}\in \class{ntn-Vg}{V^g_\eps}$ by @cor:the-coefficients-are-the-nodal-values, and $W:=U-\class{ntn-Ug}{U_g}\in \class{ntn-Vz}{V^0_\eps}$ by @prop:v-g-eps-is-affine-not.
:::
<p>So the search space $\class{ntn-Vg}{V^g_\eps}$ has exactly $n$ free parameters, the values at interior nodes: "finitely many unknowns, one per interior node."</p>
