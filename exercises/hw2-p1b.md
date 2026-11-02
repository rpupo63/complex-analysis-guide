---
label: ex:hurwitzs-theorem
source: Homework 2, Problem 1(b)
title: Hurwitz's theorem
placement: m10
order: 2
---
Let $U$ be a connected open set, and $f_N\to f$ uniformly on every closed disk in $U$, each $f_N$ holomorphic on $U$ with no zeros in $U$. Show that either $f\equiv0$ or $f$ has no zeros in $U$.
<details class="sol"><summary>Hint</summary>
$f$ is holomorphic by @thm:uniform-limits. Suppose $f\not\equiv0$ and fix $a\in U$. Choose $r\gt0$ with $\overline{D(a,r)}\subset U$ and $f\ne0$ on $|z-a|=r$ (why is this possible?), and count the zeros of $f$ in $D(a,r)$ with Rouché.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li>$f$ is holomorphic on $U$ (@thm:uniform-limits). Suppose $f\not\equiv0$ and fix $a\in U$.</li>
<li><em>Choosing $r$.</em> Take $\overline{D(a,r_0)}\subset U$. As $U$ is connected and $f\not\equiv0$, only finitely many zeros of $f$ lie in the compact disk $\overline{D(a,r_0)}$: infinitely many would have a limit point in that disk ([C.5](apx:C5)), hence in $U$, and the identity theorem (@thm:identity-theorem-l10 with $g=0$) would give $f\equiv0$. Pick $r\in(0,r_0)$ different from all their distances to $a$: then $f\ne0$ on the circle $|z-a|=r$, and $\mu:=\min_{|z-a|=r}|f|\gt0$.</li>
<li><em>Rouché.</em> By uniform convergence on $\overline{D(a,r)}$, for large $N$, $|f_N-f|\lt\mu\le|f|$ on the circle ([A.17](apx:A17)). Rouché, @thm:rouche, applied to $f$ and $f_N$: $f$ and $f_N$ have equally many zeros in $D(a,r)$, namely none. In particular $f(a)\ne0$. As $a$ was arbitrary, $f$ has no zeros.</li>
</ol>
</details>
