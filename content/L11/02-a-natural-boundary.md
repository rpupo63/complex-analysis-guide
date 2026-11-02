---
id: m2
slide: Slide 3
title: A natural boundary
---
<p>Continuation is not always possible: a function can be holomorphic on a disk and impossible to continue across any point of its boundary circle.</p>

::: definition {#def:natural-boundary name="natural boundary"}
Let $f$ be holomorphic on $\class{ntn-Dar}{D}(0,1)$, where $\class{ntn-Dar}{D}(a,r):=\{z:|z-a|\lt r\}$. The unit circle is a <em>natural boundary</em> of $f$ if $f$ continues to $\class{ntn-Dar}{D}(0,1)\cup \class{ntn-Dar}{D}(w_0,\delta)$ for no $|w_0|=1$ and no $\delta\gt0$.
:::

::: proposition {#prop:the-unit-circle-is-a}
The unit circle is a natural boundary of $f(z):=\sum_{n\ge0}z^{2^n}$ $(|z|\lt1)$.
:::
<p>The series converges for $|z|\lt1$, since its terms are among those of $\sum_m|z|^m$; so $f$ is holomorphic there ([A.19](apx:A19)).</p>
::: proof
Suppose $F$ continues $f$ to $\class{ntn-Dar}{D}(0,1)\cup \class{ntn-Dar}{D}(w_0,\delta)$, with $|w_0|=1$ and $\delta\gt0$.
<ol>
<li><em>A dyadic root of unity near $w_0$.</em> The points $e^{2\pi ij/2^k}$ ($j,k\ge0$) are dense in the unit circle: for each $k$ they are $2^k$ equally spaced points, so every arc longer than $2\pi/2^k$ contains one. The arc of the circle inside $\class{ntn-Dar}{D}(w_0,\delta)$ has positive length, so it contains such a point $w=e^{2\pi ij/2^k}$.</li>
<li><em>$F(w)$ is a radial limit of $f$.</em> For $r\lt1$ close to $1$, $rw\in \class{ntn-Dar}{D}(0,1)\cap \class{ntn-Dar}{D}(w_0,\delta)$, where $F=f$. As $F$ is continuous at $w$, $F(w)=\lim_{r\to1^-}f(rw)$.</li>
<li><em>But $f$ blows up along that radius.</em> $w^{2^n}=e^{2\pi ij2^{n-k}}=1$ for $n\ge k$. So
\[ f(rw)=\sum_{n\lt k}(rw)^{2^n}+\sum_{n\ge k}r^{2^n}. \]
The first $k$ terms have modulus $\lt1$ each; the others are positive reals. Keeping only $M$ of them, for every integer $M\ge1$,
\[ |F(w)|=\lim_{r\to1^-}|f(rw)|\ge\lim_{r\to1^-}\Big(\sum_{k\le n\lt k+M}r^{2^n}-k\Big)=M-k. \]</li>
</ol>
As $M$ is arbitrary, $|F(w)|=\infty$, a contradiction.
:::
<p>The gaps in the exponents $2^n$ ("lacunary series") make $f$ behave the same way near a dense set of boundary points. Compare $\sum z^n=\frac1{1-z}$, which is singular only at $z=1$ and continues to $\mathbb C\setminus\{1\}$.</p>
