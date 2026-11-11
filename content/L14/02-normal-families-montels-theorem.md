---
id: p2
slide: Reconstructed
title: "Normal families: Montel's theorem"
---

::: theorem {#thm:montel name="Montel"}
Let $V_1\subseteq V_2\subseteq\dots$ be open sets with union $\Omega$, and let $f_n$ be holomorphic on $V_n$ with $|f_n|\le M$. Then a subsequence $f_{n_k}$ converges uniformly on every [compact](apx:C5) subset of $\Omega$ to a function $f$ holomorphic on $\Omega$, and $f_{n_k}'\to f'$ uniformly on every compact subset of $\Omega$.
:::
<p>Every compact $K\subseteq\Omega$ lies in some $V_n$: the open sets $V_n$ cover $K$, finitely many of them suffice (Heine–Borel, [C.5](apx:C5)), and they are nested. So on $K$ all but finitely many $f_n$ are defined. With $V_n=\Omega$ for all $n$ this is the usual statement: a locally bounded family of holomorphic functions is <em>normal</em>.</p>
::: proof

<ol>
<li><em>Lipschitz near each point.</em> Let $z\in\Omega$ and $r\gt0$ with $\overline{D(z,2r)}\subseteq\Omega$; this closed disk lies in $V_N$ for some $N$. For $n\ge N$ and $\zeta\in D(z,r)$, $f_n$ is holomorphic near $\overline{D(\zeta,r)}\subseteq\overline{D(z,2r)}$ and bounded by $M$, so @cor:cauchys-estimate (the coefficient $a_1=f_n'(\zeta)$) gives $|f_n'(\zeta)|\le M/r$. Integrating $f_n'$ along the segment between two points of the disk $D(z,r)$ (ML estimate),
\[ |f_n(\zeta_1)-f_n(\zeta_2)|\le\frac Mr\,|\zeta_1-\zeta_2|\qquad(\zeta_1,\zeta_2\in D(z,r),\ n\ge N). \]</li>
<li><em>Convergence on a countable dense set.</em> List the points of $\Omega$ with rational coordinates as $s_1,s_2,\dots$. The numbers $f_n(s_1)$ (for the $n$ with $s_1\in V_n$) are bounded by $M$, so a subsequence converges (Bolzano–Weierstrass, [C.5](apx:C5)). From it extract a further subsequence along which $f_n(s_2)$ converges, and so on. Let $n_k$ be the $k$-th term of the $k$-th subsequence. For each $j$, the terms $n_k$ with $k\ge j$ form a subsequence of the $j$-th one, so $f_{n_k}(s_j)$ converges for every $j$.</li>
<li><em>Uniformly Cauchy on compact sets.</em> Let $K\subseteq\Omega$ be compact and $\varepsilon\gt0$. Finitely many disks $D(z_i,r_i)$ as in step 1 cover $K$. In each, finitely many points $s_j$ lie within $\delta_i:=\varepsilon r_i/(3M)$ of every point of the disk, since the $s_j$ are dense. Take $k,l$ so large that $|f_{n_k}(s_j)-f_{n_l}(s_j)|\lt\varepsilon/3$ at these finitely many $s_j$, and $n_k,n_l\ge N_i$ for every $i$. For $\zeta\in K$, pick $i$ with $\zeta\in D(z_i,r_i)$ and one of these $s_j$ with $|\zeta-s_j|\lt\delta_i$. By step 1,
\[ |f_{n_k}(\zeta)-f_{n_l}(\zeta)|\le|f_{n_k}(\zeta)-f_{n_k}(s_j)|+|f_{n_k}(s_j)-f_{n_l}(s_j)|+|f_{n_l}(s_j)-f_{n_l}(\zeta)|\lt\varepsilon. \]
So $f_{n_k}$ converges [uniformly](apx:A17) on $K$; call the limit $f$.</li>
<li><em>$f$ is holomorphic.</em> With $z,r,N$ as in step 1, the $f_{n_k}$ with $n_k\ge N$ are holomorphic on $D(z,2r)$ and converge uniformly on each closed disk in it, so $f$ is holomorphic on $D(z,2r)$ (@thm:uniform-limits). Hence $f$ is holomorphic on $\Omega$.</li>
<li><em>Derivatives.</em> For $w\in\overline{D(z,r)}$, by @thm:cauchys-formula-for-derivatives on the circle $|\zeta-z|=\frac32r$, where $|\zeta-w|\ge\frac r2$,
\[ |f_{n_k}'(w)-f'(w)|=\left|\frac1{2\pi i}\oint_{|\zeta-z|=3r/2}\frac{f_{n_k}(\zeta)-f(\zeta)}{(\zeta-w)^2}\,d\zeta\right|\le\frac{3r}2\cdot\frac{\max|f_{n_k}-f|}{(r/2)^2}\longrightarrow0, \]
the maximum taken over that circle. Finitely many such disks $\overline{D(z,r)}$ cover a compact set. <span class="qed">∎</span></li>
</ol>
:::
<p>Boundedness is what makes the family "compact": Cauchy's estimate turns a bound on $f_n$ into a bound on $f_n'$, so the $f_n$ cannot oscillate faster and faster. For real functions this fails: $\sin(nx)$ is bounded by $1$ and has no uniformly convergent subsequence.</p>
