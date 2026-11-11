---
id: j1
slide: Slide 2
title: Removable singularities
---

::: lemma {#lem:removable-singularities name="removable singularities"}
If $g$ is holomorphic on $0\lt|z-a|\lt r$ and bounded near $a$, then $g$ extends holomorphically to $|z-a|\lt r$.
:::
<figure>{{fig:j1-1}}<figcaption>The proof: Cauchy's theorem on the shaded region, the disk $|z-a|\lt r'$ minus small disks about $a$ and $w$, where $g(z)/(z-w)$ is holomorphic.</figcaption></figure>
<p>Compare @thm:converse-of-the-mean-value-property and Lecture 4's moral: for harmonic and holomorphic functions, mild-looking hypotheses force full regularity. Here mere boundedness near $a$ rules out a singularity.</p>
::: proof
Fix $w$ and $r'$ with $0\lt|w-a|\lt r'\lt r$. Let $B$ bound $|g|$ on some punctured disk $0\lt|z-a|\le\epsilon_0$.
<ol>
<li><em>Three circles.</em> For small $\epsilon\gt0$ and $\delta\gt0$, the closed disks $|z-a|\le\epsilon$ and $|z-w|\le\delta$ are disjoint and inside $|z-a|\lt r'$. The function $\frac{g(z)}{z-w}$ is holomorphic near the region inside $|z-a|=r'$ and outside both small circles, so @lem:moving-the-circle gives
\[ \oint_{|z-a|=r'}\frac{g(z)\,dz}{z-w}=\oint_{|z-w|=\delta}\frac{g(z)\,dz}{z-w}+\oint_{|z-a|=\epsilon}\frac{g(z)\,dz}{z-w}. \]</li>
<li><em>The circle around $w$.</em> $g$ is holomorphic near $|z-w|\le\delta$, so Cauchy's formula (@thm:cauchys-integral-formula, centred at $w$) makes the first integral on the right $2\pi i\,g(w)$.</li>
<li><em>The circle around $a$ is $O(\epsilon)$.</em> For $\epsilon\le\min(\epsilon_0,\frac12|w-a|)$, on $|z-a|=\epsilon$ we have $|g|\le B$ and $|z-w|\ge|w-a|-\epsilon\ge\frac12|w-a|$, so by the ML estimate the integral is at most $2\pi\epsilon\cdot\frac{2B}{|w-a|}\to0$. Here boundedness is used.</li>
<li><em>Let $\epsilon\to0$.</em> The other two terms do not depend on $\epsilon$, so
\[ g(w)=G(w):=\frac1{2\pi i}\oint_{|z-a|=r'}\frac{g(z)\,dz}{z-w}. \]</li>
<li><em>$G$ is holomorphic on the whole disk $|w-a|\lt r'$,</em> including at $w=a$: this is the case $n=0\to1$ of the proof of @thm:cauchys-formula-for-derivatives, which only used that $g$ is continuous on the circle $|z-a|=r'$.</li>
</ol>
So setting $g(a):=G(a)$ makes $g=G$ on $|z-a|\lt r'$, holomorphic there. As $r'\lt r$ was arbitrary, $g$ is holomorphic on $|z-a|\lt r$.
:::
<p>The point $a$ is then called a <em>removable singularity</em>. With @def:pole-of-order-m this sorts the isolated singularities of a holomorphic function near $a$: bounded (removable), $|g|\to\infty$ like a power (a pole), or neither (an <em>essential singularity</em>, such as $e^{1/z}$ at $0$; see [Laurent series](apx:E5)).</p>
