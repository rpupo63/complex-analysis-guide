---
id: k5
slide: Slide 6
title: 'Infinite products: zeros'
---
::: proof {title="Proof of the statement about zeros."}
Fix $D$, and $M$ with $s_n\le\frac12$ for $n\gt M$ (possible as $s_n\to0$).
<ol>
<li><em>Split off a finite product.</em> By the first part (applied to $u_{M+1},u_{M+2},\dots$), $T:=\prod_{n\gt M}(1+u_n)$ is holomorphic on $U$, and $F=F_M\,T$, as a limit of $F_M\prod_{M\lt n\le N}(1+u_n)$.</li>
<li><em>The tail has no zeros on $D$.</em> For $n\gt M$, on $D$: $|1+u_n|\ge1-s_n\ge e^{-2s_n}$, by the inequality below. Hence
\[ |T|=\lim_{N\to\infty}\prod_{M\lt n\le N}|1+u_n|\ge e^{-2\sum_{n\gt M}s_n}\gt0\qquad\text{on }D. \]</li>
<li><em>The inequality.</em> $1-t\ge e^{-2t}$ for $0\le t\le\frac12$: the function $\varphi(t):=1-t-e^{-2t}$ is concave ($\varphi''=-4e^{-2t}\lt0$), with $\varphi(0)=0$ and $\varphi(\frac12)=\frac12-e^{-1}\gt0$. A concave function lies above its chord, so $\varphi\ge0$ on $[0,\frac12]$.</li>
<li><em>Conclude.</em> On $D$, $F=F_M\,T$ with $T$ holomorphic and nonzero. So $F$ has the same zeros as the finite product $F_M$, with the same orders (multiplying by a nonzero holomorphic function does not change the order: $(z-z_0)^mh\cdot T$ with $h(z_0)T(z_0)\ne0$). The order of a zero of a finite product is the sum of the orders of the factors, by the same reasoning. And $1+u_n\ne0$ on $D$ for $n\gt M$.</li>
</ol>
Every $z\in U$ lies in such a closed disk $D$ (as $U$ is open), which proves all three claims.
:::
