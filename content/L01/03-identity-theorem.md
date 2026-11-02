---
id: x3
slide: Slide 4
title: This small difference is gigantic
toc: Identity theorem
---
<p>The difference is <em>very</em> constraining. Two basic theorems that the course proves later:</p>

::: theorem {#thm:identity-theorem name="identity theorem" status=cited}
Let $f$ and $g$ be holomorphic on open sets $U$ and $V$, with $U\cap V$ [connected](apx:C4). If $f=g$ on some nonempty open subset of $U\cap V$, then $f=g$ on all of $U\cap V$.
:::

::: corollary {#cor:isolated-zeros name="isolated zeros" status=cited}
Let $f$ be holomorphic on a connected open set $\Omega$. If $f(z_n)=0$ for a sequence of distinct points $z_n\to z\in\Omega$, then $f\equiv0$ on $\Omega$.
:::
<p>Both are stated here and proved later: @cor:isolated-zeros as @thm:isolated-zeros, and @thm:identity-theorem as @thm:identity-theorem-l10 (which also covers sequences with a limit point).</p>

::: corollary {#cor:constant-on-a-segment name="constant on a segment"}
A holomorphic function on a connected open set $\Omega$ that is constant on a nontrivial line segment contained in $\Omega$ is constant everywhere.
:::
::: proof
Say $f=c$ on the segment. Then $f-c$ is holomorphic and vanishes at infinitely many distinct points of the segment, for instance at points $z_n$ converging to one endpoint $z\in\Omega$. By @cor:isolated-zeros, $f-c\equiv0$.
:::
<p>Nothing like this holds for $C^\infty$ functions: a [bump function](apx:D5) is smooth, zero on a whole half-plane, and not zero everywhere. Holomorphic is a much more restricted class.</p>
