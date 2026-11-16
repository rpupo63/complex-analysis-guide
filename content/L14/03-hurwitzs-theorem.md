---
id: p3
slide: Reconstructed
title: "Hurwitz's theorem"
---

::: motivation
<p>A limit produced by @thm:montel is holomorphic, yet it might be constant. Each approximating map is injective, but the limit might repeat a value. Injectivity has to be checked before the limit can be a bijection.</p>
:::

::: theorem {#thm:hurwitz name="Hurwitz"}
Let $\Omega$ be [connected](apx:C4), $V_1\subseteq V_2\subseteq\dots$ open sets with union $\Omega$, and $f_n$ holomorphic and injective on $V_n$, with $f_n\to f$ uniformly on every compact subset of $\Omega$. Then $f$ is constant or injective.
:::
::: proof
Suppose $f$ is not constant, and $f(a)=f(b)=c$ with $a\ne b$. The function $g:=f-c$ is holomorphic on $\Omega$ (@thm:uniform-limits) and not identically zero, so its zeros are isolated (@thm:identity-theorem-l10). Choose $r\gt0$ such that the closed disks $\overline{D(a,r)}$ and $\overline{D(b,r)}$ lie in $\Omega$, are disjoint, and contain no zero of $g$ other than their centres. Let $m\gt0$ be the minimum of $|g|$ on the two circles ([C.5](apx:C5)). For $n$ large, both closed disks lie in $V_n$ (compact sets lie in some $V_n$; see after @thm:montel) and $|f_n-f|\lt m$ on both circles. There
\[ |(f_n-c)-g|=|f_n-f|\lt m\le|g|, \]
so by Rouché (@thm:rouche) $f_n-c$ has as many zeros in $D(a,r)$ as $g$, at least one, and likewise in $D(b,r)$. So $f_n$ takes the value $c$ twice, which contradicts its injectivity.
:::

::: plain
<p>A limit of injective holomorphic functions is either constant or still injective. The functions may live on expanding domains when convergence is uniform on compact sets. A non-constant limit does not repeat any value.</p>
:::

<p>Both cases occur: $f_n(z)=z/n$ is injective, and its limit $0$ is constant. The same argument shows that a limit of functions without zeros either has no zeros or is identically $0$.</p>
