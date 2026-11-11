---
id: q6
slide: Slide 7
title: Polygons
---

::: definition {#def:polygon name="polygon; interior angles"}
A <em>polygon</em> $P$ is a bounded closed set whose boundary is a simple closed polygonal curve. Its vertices $w_1,\dots,w_n$ are listed counterclockwise, and its interior angles are $\alpha_1\pi,\dots,\alpha_n\pi$ with $0\lt\alpha_k\lt2$.
:::
<figure>{{fig:q6-1}}<figcaption>At the vertex $w_k$ the interior angle is $\alpha_k\pi$, and going around counterclockwise one turns left by $(1-\alpha_k)\pi$.</figcaption></figure>
<p>Going around $\partial P$ counterclockwise, one turns left by $(1-\alpha_k)\pi$ at $w_k$, and by $2\pi$ in total:
\[ \sum_{k=1}^n(1-\alpha_k)=2. \]
This is the angle sum $\sum_k\alpha_k\pi=(n-2)\pi$. A turn is negative at a re-entrant corner ($\alpha_k\gt1$).</p>

::: fact {#fact:caratheodory name="Carathéodory" status=cited}
Let $F$ be a conformal map of $\mathbb H$ onto the interior of a polygon $P$ (it exists by @thm:riemann-mapping-theorem-stated and @prop:cayley-map). Then $F$ extends to a homeomorphism of $\overline{\mathbb H}\cup\{\infty\}$ onto $P$, which runs along $\partial P$ counterclockwise as $x$ runs along $\mathbb R$ from $-\infty$ to $\infty$. The <em>prevertices</em> are $x_k:=F^{-1}(w_k)$.
:::

::: proposition {#prop:automorphisms-of-h name="automorphisms of $\mathbb H$"}
For real $a,b,c,d$ with $ad-bc\gt0$, $\psi(z)=\dfrac{az+b}{cz+d}$ is an automorphism of $\mathbb H$.
:::
::: proof
$\operatorname{Im}\psi(z)=\dfrac{(ad-bc)\operatorname{Im}z}{|cz+d|^2}$, so $\psi$ maps $\mathbb H$ into $\mathbb H$. Its inverse $\dfrac{dw-b}{-cw+a}$ has the same form, with the same determinant $ad-bc$.
:::
<p>Replacing $F$ by $F\circ\psi$, and relabelling the vertices cyclically, we may assume that $\infty$ is not a prevertex. Then the prevertices are real: $x_1\lt\dots\lt x_n$.</p>
