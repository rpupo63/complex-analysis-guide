---
id: m1
slide: Slide 2
title: Analytic continuation
---

::: definition {#def:continuation name=continuation}
Let $U\subset W$ be open, and $f$ holomorphic on $U$. A <em>continuation</em> of $f$ to $W$ is a holomorphic $F$ on $W$ with $F=f$ on $U$.
:::

::: proposition {#prop:gluing-and-uniqueness name="gluing and uniqueness"}
Let $U$, $V$, $W$ be open.<br>
(1) <b>Gluing.</b> If $f$ is holomorphic on $U$, $g$ on $V$, and $f=g$ on $U\cap V$, then $F:=f$ on $U$, $F:=g$ on $V$ defines a holomorphic function on $U\cup V$.<br>
(2) <b>Uniqueness.</b> If $W$ is connected, and $F,G$ are holomorphic on $W$ and agree on a nonempty open set or on a real interval $[a,b]$ $(a\lt b)$ in $W$, then $F=G$ on $W$.
:::
::: proof
(1) On $U\cap V$ the two definitions agree, so $F$ is well defined. Holomorphy is a local property (a limit of difference quotients at each point), and near each point of $U\cup V$, $F$ coincides with $f$ or with $g$ on an open set.<br>
(2) Either set contains a point $x$ and points $x_n\ne x$ with $x_n\to x$: for $[a,b]$, take $x:=a$ and $x_n:=a+\frac{b-a}n$; an open set contains a small disk around any of its points. Apply the identity theorem (@thm:identity-theorem-l10) to $F$ and $G$.
:::
<p>Consequences. If $W$ is connected and $U\ne\emptyset$, a continuation of $f$ to $W$ is unique, if it exists; so it makes sense to speak of <em>the</em> continuation. And <b>identities continue</b>: $\sin^2z+\cos^2z-1$ is entire and vanishes on $\R$, hence on $\mathbb C$.</p>
