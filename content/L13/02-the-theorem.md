---
id: o2
slide: Slide 3
title: The theorem
---

::: theorem {#thm:riemann-mapping-theorem name="Riemann mapping theorem"}
Let $\Omega$ be a bounded connected open set such that<br>
<b>(D)</b> for every continuous $g$ on $\partial\Omega$ there is $u$ harmonic on $\Omega$ and continuous on $\overline\Omega$, with $u=g$ on $\partial\Omega$;<br>
<b>(C)</b> every harmonic function on $\Omega$ is the real part of a holomorphic function on $\Omega$.<br>
Then for every $z_0\in\Omega$ there is exactly one conformal map $f$ of $\Omega$ onto $D(0,1)$ with $f(z_0)=0$ and $f'(z_0)\gt0$: the <em>Riemann map</em> of $\Omega$ at $z_0$.
:::
<p>Uniqueness is [Prop. #(b)](@prop:what-a-riemann-map-must-look); existence is proved in @sec:o4. When do the conditions hold?</p>
<ul>
<li><b>(D)</b> holds when $\Omega$ is the interior of a finite union of closed grid squares: that is the existence theorem for the Dirichlet problem, @thm:the-dirichlet-problem-on-a-union, the main result of Part I.</li>
<li><b>(C)</b> holds when $\Omega$ is <em>star-shaped</em> about some point $c$: the segment $[c,z]$ lies in $\Omega$ for every $z\in\Omega$ (@lem:star-shaped-sets-satisfy-c). In general (C) holds exactly when $\Omega$ is simply connected (stated without proof).</li>
</ul>
<p>So the theorem applies to rectangles, and to L-shapes and plus-shapes made of grid squares: each is a union of squares, and star-shaped about a point of its "central" square.</p>
<p>Here Part I pays off: Lectures 3–5 built the solution of the Dirichlet problem, and that solution is exactly what produces the conformal map.</p>
