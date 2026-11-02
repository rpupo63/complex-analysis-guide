---
id: v3
slide: Slide 3
title: 'Step 1: reduction to piecewise linear boundary values'
toc: 'Step 1: reduction'
---
<p>Suppose for now that the theorem holds for boundary data that are linear on each boundary edge of <em>some</em> grid (any level may play the role of the coarsest grid). We deduce it for every continuous $g$.</p>

::: definition {#def:linearising-at-level-k name="linearising at level $k$"}
Let $\class{ntn-gk}{g_k}$ be the function on $\class{ntn-dOm}{\partial\Omega}$ that equals $g$ at the boundary nodes of level $k$ and is linear on each boundary edge of level $k$.
:::
<p>$\class{ntn-gk}{g_k}$ is well defined and continuous: $\class{ntn-dOm}{\partial\Omega}$ is a union of level-$k$ boundary edges, each edge is fixed by its two endpoint values, and two edges that meet share an endpoint, where both give the value $g$ there.</p>

::: lemma {#lem:uniformly-a-17-on}
$\class{ntn-gk}{g_k}\to g$ [uniformly](apx:A17) on $\class{ntn-dOm}{\partial\Omega}$.
:::
::: proof
$\class{ntn-dOm}{\partial\Omega}$ is [compact](apx:C5) and $g$ is continuous on it, so $g$ is [uniformly continuous](apx:A16): for every tolerance $\epsilon\gt0$ there is $\delta\gt0$ with $|g(q)-g(q')|\lt\epsilon$ whenever $q,q'\in\class{ntn-dOm}{\partial\Omega}$ and $|q-q'|\le\delta$. Take $k$ so large that the grid side $\class{ntn-epsn}{\eps_k}\le\delta$. A point $q\in\class{ntn-dOm}{\partial\Omega}$ lies on a level-$k$ boundary edge with endpoints $a,b$, both within $\class{ntn-epsn}{\eps_k}\le\delta$ of $q$. Linearity on the edge means $\class{ntn-gk}{g_k}(q)=\lambda g(a)+(1-\lambda)g(b)$ for some $\lambda\in[0,1]$, so
\[ |\class{ntn-gk}{g_k}(q)-g(q)|=|\lambda(g(a)-g(q))+(1-\lambda)(g(b)-g(q))|\le\lambda|g(a)-g(q)|+(1-\lambda)|g(b)-g(q)|\lt\epsilon. \]
This holds for every $q$ at once, which is uniform convergence.
:::

::: proposition {#prop:the-reduction name="the reduction"}
If @thm:the-dirichlet-problem-on-a-union holds for boundary data that are linear on each boundary edge of some grid, it holds for every continuous $g$.
:::
::: proof

<ol>
<li><em>Solve for $\class{ntn-gk}{g_k}$.</em> $\Omega$ is a union of level-$k$ squares too (each coarse square splits into level-$k$ squares), and $\class{ntn-gk}{g_k}$ is linear on each level-$k$ boundary edge. So @hyp:for-now holds with level $k$ as the coarsest grid, and by assumption there is $\class{ntn-uk}{u_k}\in C^2(\Omega)\cap C(\overline\Omega)$, harmonic in $\Omega$, with $\class{ntn-uk}{u_k}=\class{ntn-gk}{g_k}$ on $\class{ntn-dOm}{\partial\Omega}$.</li>
<li><em>The $\class{ntn-uk}{u_k}$ form a uniform Cauchy sequence.</em> $\class{ntn-uk}{u_k}-\class{ntn-uk}{u_j}$ is harmonic in $\Omega$ and continuous on $\overline\Omega$, so the stability corollary (@cor:stability) gives
\[ \max_{\overline\Omega}|\class{ntn-uk}{u_k}-\class{ntn-uk}{u_j}|=\max_{\class{ntn-dOm}{\partial\Omega}}|\class{ntn-gk}{g_k}-\class{ntn-gk}{g_j}|\le\max_{\class{ntn-dOm}{\partial\Omega}}|\class{ntn-gk}{g_k}-g|+\max_{\class{ntn-dOm}{\partial\Omega}}|g-\class{ntn-gk}{g_j}|\longrightarrow0\qquad(j,k\to\infty), \]
by @lem:uniformly-a-17-on and the triangle inequality.</li>
<li><em>Take the limit.</em> A uniformly Cauchy sequence converges uniformly ([A.17](apx:A17)), so $\class{ntn-uk}{u_k}\to u$ uniformly on $\overline\Omega$ for some function $u$.
<ul>
<li>$u$ is continuous on $\overline\Omega$: a uniform limit of continuous functions ([A.17](apx:A17)).</li>
<li>$u=g$ on $\class{ntn-dOm}{\partial\Omega}$: there $\class{ntn-uk}{u_k}=\class{ntn-gk}{g_k}\to g$.</li>
<li>$u$ is harmonic in $\Omega$: uniform convergence on $\overline\Omega$ is in particular uniform on every compact subset of $\Omega$, so @cor:uniform-limits applies. It also makes $u$ smooth, so $u\in C^2(\Omega)$.</li>
</ul></li>
</ol>
Uniqueness is @cor:stability in every case.
:::
<p>Notice the division of labour: Lecture 4's stability corollary turns uniform closeness of boundary data into uniform closeness of solutions, and its uniform-limits corollary keeps the limit harmonic.</p>
