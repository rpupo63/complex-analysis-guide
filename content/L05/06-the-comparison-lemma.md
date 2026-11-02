---
id: v7
slide: Slide 7
title: The comparison lemma
---

::: lemma {#lem:comparison name=comparison}
Let $u$ be the function of Lecture 3: harmonic in $\Omega$, the $L^2$ limit of the $\class{ntn-Un}{U_n}$, with $\nabla \class{ntn-Un}{U_n}\to\nabla u$ in $L^2$ and $\class{ntn-Un}{U_n}=g$ on $\class{ntn-dOm}{\partial\Omega}$. Let $\class{ntn-vc}{v}$ be continuous on $\overline\Omega$ and harmonic in $\Omega$. If $\class{ntn-vc}{v}\ge g$ on $\class{ntn-dOm}{\partial\Omega}$, then $\class{ntn-vc}{v}\ge u$ in $\Omega$. If $\class{ntn-vc}{v}\le g$ on $\class{ntn-dOm}{\partial\Omega}$, then $\class{ntn-vc}{v}\le u$ in $\Omega$.
:::
<p>Compare the maximum principle, @cor:maximum-principle: it would give $\class{ntn-vc}{v}\ge u$ from $\class{ntn-vc}{v}\ge u$ on $\class{ntn-dOm}{\partial\Omega}$. Here the boundary comparison is made with $g$ instead, because $u$ has no known boundary values yet. The proof runs through @sec:v7–@sec:v10; the complete argument is collected at the end of @sec:v10.</p>

::: definition {#def:the-functions-z-n-and-z name="the functions $\class{ntn-zn}{z_n}$ and $\class{ntn-zf}{z}$"}
Fix $\class{ntn-sig}{\sigma}\gt0$ and put
\[ \class{ntn-zn}{z_n}:=\class{ntn-Un}{U_n}-\class{ntn-sig}{\sigma}-\class{ntn-vc}{v},\qquad \class{ntn-zf}{z}:=u-\class{ntn-sig}{\sigma}-\class{ntn-vc}{v}. \]
Careful: in @sec:v7–@sec:v10 the letter $\class{ntn-zf}{z}$ names this <em>function</em>, not a point of the plane.
:::
<p>We show $\class{ntn-zf}{z}\le0$ in $\Omega$. Then $u\le \class{ntn-vc}{v}+\class{ntn-sig}{\sigma}$, and letting $\class{ntn-sig}{\sigma}\downarrow0$ gives $u\le \class{ntn-vc}{v}$. The constant $\class{ntn-sig}{\sigma}$ buys a margin: on $\class{ntn-dOm}{\partial\Omega}$, $\class{ntn-zn}{z_n}=g-\class{ntn-sig}{\sigma}-\class{ntn-vc}{v}\le-\class{ntn-sig}{\sigma}\lt0$ strictly.</p>

<figure>
{{fig:v7-1}}
<figcaption>On $\class{ntn-dOm}{\partial\Omega}$, $\class{ntn-zn}{z_n}\le-\class{ntn-sig}{\sigma}$, so the set $\{\class{ntn-zn}{z_n}\ge0\}$ stays strictly inside $\Omega$.</figcaption>
</figure>

<p>Everything rests on the <em>positive part</em> $\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}:=\max(\class{ntn-zn}{z_n},0)$. It vanishes near $\class{ntn-dOm}{\partial\Omega}$, its energy tends to zero, and it tends to $\class{ntn-zf}{z}^{\class{ntn-pos}{+}}$. First, a list of what is needed about $t\mapsto t^{\class{ntn-pos}{+}}$.</p>
