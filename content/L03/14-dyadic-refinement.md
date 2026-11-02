---
id: s15
slide: Slide 15
title: 'Dyadic refinement: the minima decrease'
toc: Dyadic refinement
---

::: definition {#def:for-write-and-the-minimum}
$\class{ntn-epsn}{\eps_n}:=2^{-n}\class{ntn-epsn}{\eps_0}$ for $n=0,1,2,\dots$. Write $\class{ntn-Un}{U_n}:=U_{\class{ntn-epsn}{\eps_n}}$ and $\class{ntn-mn}{m_n}:=\class{ntn-E}{E}(\class{ntn-Un}{U_n})=\min_{\class{ntn-Vg}{V^g_{\eps_n}}}E$ (the minimum by @lem:among-all-is-the-unique).
:::
<p>Each square of one grid splits into four squares of half the side in the next, so $\Omega$ is a union of squares at every level and @hyp:fix-and-grid-lines-with holds for every $\class{ntn-epsn}{\eps_n}$.</p>

::: hypothesis {#hyp:for-now name="\"for now\""}
$\Omega$ is a finite union of squares of the coarsest grid ($\class{ntn-epsn}{\eps_0}$), and $g$ is linear along each boundary edge of the coarsest grid.
:::

::: lemma {#lem:nesting name=nesting}
For $n\le k$: (a) $\class{ntn-Veps}{V_{\eps_n}}\subset \class{ntn-Veps}{V_{\eps_k}}$. (b) Under [Hyp. #](@hyp:for-now), every $U\in \class{ntn-Vg}{V^g_{\eps_n}}$ equals $g$ on all of $\class{ntn-dOm}{\partial\Omega}$, and $\class{ntn-Vg}{V^g_{\eps_n}}\subset \class{ntn-Vg}{V^g_{\eps_k}}$. (c) $\class{ntn-Vz}{V^0_{\eps_n}}\subset \class{ntn-Vz}{V^0_{\eps_k}}$.
:::
::: proof
It is enough to take $k=n+1$ and repeat.<br>
(a) By @prop:the-slides-description-of-v-eps, $U\in \class{ntn-Veps}{V_{\eps_n}}$ is continuous and bilinear on each coarse square. On a sub-square, $a+bx+cy+dxy$ still has that form. So $U$ is continuous and bilinear on each fine square, and $U\in \class{ntn-Veps}{V_{\eps_{n+1}}}$ by @prop:the-slides-description-of-v-eps again.<br>
(b) Let $e$ be a boundary edge at level $n$. It lies inside a coarsest-level boundary edge, on which $g$ is linear. $U$ is linear on $e$ (@prop:linear-along-grid-lines-not-on) and equals $g$ at the endpoints of $e$. Two linear functions that agree at two points agree everywhere on $e$, so $U=g$ on $\class{ntn-dOm}{\partial\Omega}$. Every level-$(n+1)$ boundary node lies on $\class{ntn-dOm}{\partial\Omega}$ ([Lemma #(a)](@lem:nodes-and-the-boundary)), so $U$ equals $g$ there. With (a), $U\in \class{ntn-Vg}{V^g_{\eps_{n+1}}}$.<br>
(c) $U\in \class{ntn-Vz}{V^0_{\eps_n}}$ vanishes on $\class{ntn-dOm}{\partial\Omega}$ ([Prop. #(b)](@prop:the-space-v-0-eps)), hence at the finer boundary nodes.
:::

::: proposition {#prop:so-decreases-to-a-limit}
$\class{ntn-mn}{m_0}\ge \class{ntn-mn}{m_1}\ge \class{ntn-mn}{m_2}\ge\dots\ge0$, so $\class{ntn-mn}{m_n}$ decreases to a limit $\class{ntn-m}{m}:=\inf_n \class{ntn-mn}{m_n}\ge0$ (written $\class{ntn-mn}{m_n}\downarrow \class{ntn-m}{m}$).
:::
::: proof
$\class{ntn-mn}{m_{n+1}}$ is the minimum of $E$ over $\class{ntn-Vg}{V^g_{\eps_{n+1}}}$, a set that contains $\class{ntn-Vg}{V^g_{\eps_n}}$ ([Lemma #(b)](@lem:nesting)), and a minimum over a larger set is no larger. $E\ge0$ by @prop:properties-of-a. A non-increasing sequence that is bounded below converges to its infimum by the [monotone convergence theorem](apx:A15).
:::

::: remark {#rem:why-the-hypothesis-is-needed name="why the hypothesis is needed"}
Without [Hyp. #](@hyp:for-now), "equals $g$ at the boundary nodes" means different things on different grids. $\class{ntn-Un}{U_n}$ interpolates $g$ linearly between coarse nodes, which generally disagrees with $g$ at the new midpoints, so $\class{ntn-Un}{U_n}\notin \class{ntn-Vg}{V^g_{\eps_{n+1}}}$ and nesting fails. The slide's "for now" signals that the general case is handled later.
:::
