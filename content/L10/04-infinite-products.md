---
id: k4
slide: Slide 5
title: Infinite products
---
<p>A polynomial is determined, up to a constant factor, by its zeros: $c\prod(z-a_j)$. The goal of the lecture is the analogue for entire functions, which may have infinitely many zeros. That needs infinite products.</p>

::: lemma {#lem:products name=products}
Let $u_1,u_2,\dots$ be holomorphic on an open set $U$, with $\sum_n\max_D|u_n|\lt\infty$ for every closed disk $D\subset U$. Then $F_N:=\prod_{n\le N}(1+u_n)$ converges uniformly on every closed disk $D\subset U$ to a holomorphic function $F$ on $U$. For $z\in U$: $F(z)=0$ if and only if some factor $1+u_n(z)=0$; only finitely many factors vanish at $z$; and the order of the zero of $F$ at $z$ is the sum of their orders.
:::
::: proof {title="Proof of convergence."}
Fix $D$ and let $s_n:=\max_D|u_n|$, so $\sum s_n\lt\infty$.
<ol>
<li><em>A uniform bound.</em> On $D$, using $1+s\le e^s$: $|F_N|\le\prod_{n\le N}(1+s_n)\le e^{\sum_ns_n}=:B$.</li>
<li><em>Successive differences.</em> $F_{N+1}-F_N=F_N\,u_{N+1}$, so $|F_{N+1}-F_N|\le B\,s_{N+1}$ on $D$.</li>
<li><em>Telescoping.</em> $F_N=F_1+\sum_{n\lt N}(F_{n+1}-F_n)$. The series has terms bounded on $D$ by $Bs_{n+1}$, which are summable, so it converges uniformly on $D$ ([M-test](apx:A21)).</li>
<li>Each $F_N$ is holomorphic, so the limit $F$ is holomorphic on $U$ by @thm:uniform-limits. <span class="qed">∎</span></li>
</ol>
:::
