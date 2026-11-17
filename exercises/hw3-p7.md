---
label: ex:radius-of-z-over-e-to-the-z-minus-one
source: Homework 3, Problem 7
title: radius of $z/(e^z-1)$ at $0$
placement: j1
order: 1
---
Without computing coefficients, find the radius of convergence of the Taylor series of $z/(e^z-1)$ at $0$.
<details class="sol"><summary>Hint</summary>
Fill in the value at $0$. The series then reaches as far as the function stays holomorphic (@thm:power-series), and it stops at the nearest point where $e^z=1$.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>A value at $0$.</em> The series $e^z-1=z+z^2/2!+\cdots=z\,g(z)$ has $g(0)=1$ and $g$ entire ([A.19](apx:A19)). So $z/(e^z-1)=1/g(z)$ for $z\ne0$ small, which stays bounded as $z\to0$. By @lem:removable-singularities the singularity at $0$ fills in. Call the resulting function $f$. Then $f(0)=1$.</li>
<li><em>Where $e^z=1$.</em> From the series, $e^{iy}=\cos y+i\sin y$ for real $y$ ([A.19](apx:A19)). So $e^z=1$ if and only if $z=2\pi ik$ for some integer $k$: writing $z=x+iy$ gives $e^x=1$ and $e^{iy}=1$, hence $x=0$ and $y\in 2\pi\mathbb Z$. The nearest such points to $0$, other than $0$ itself, are $\pm 2\pi i$, at distance $2\pi$. At those points the numerator is not $0$.</li>
<li><em>The radius is $2\pi$.</em> For every $r\lt 2\pi$, the closed disk $|z|\le r$ meets none of the points $2\pi ik$ with $k\ne0$, and $f$ is holomorphic near that disk. By @thm:power-series the Taylor series of $f$ at $0$ converges on $|z|\lt 2\pi$. If the radius were larger than $2\pi$, the sum would be holomorphic at $2\pi i$ ([A.19](apx:A19)). But as $z\to 2\pi i$ with $z\ne 2\pi i$, the numerator tends to $2\pi i\ne0$ and the denominator tends to $0$, so $|f(z)|\to\infty$. The sum equals $f$ on $|z|\lt 2\pi$, so it would be unbounded in every neighborhood of $2\pi i$. The radius is exactly $2\pi$.</li>
</ol>
</details>
