---
id: w1
slide: Slides 2–3
title: Recall from last time
toc: 'Recall: holomorphic functions'
---
<p>These two slides recap Lecture 1 (Part I). Points of the plane are written $z=x+iy$ ([complex notation](apx:C1)).</p>

::: definition {#def:holomorphic-l2 name=holomorphic}
A function $f$ on an open set $D\subseteq\mathbb C$ is <em>holomorphic</em> if the complex limit
\[ f'(z)=\lim_{h\to0}\frac{f(z+h)-f(z)}{h},\qquad h\in\mathbb C\setminus\{0\}, \]
exists at every $z\in D$. This restates @def:holomorphic.
:::

::: theorem {#thm:three-descriptions-from-lecture-1 name="three descriptions, from Lecture 1"}
Let $D\subseteq\mathbb C$ be an open disk and $u,v:D\to\R$ of class [$C^1$](apx:D1). The following are equivalent:
<ol>
<li>$f=u-iv$ is holomorphic on $D$;</li>
<li>the vector field $(u,v)$ is divergence-free and curl-free: $\class{ntn-divc}{\operatorname{div}}(u,v)=0$ and $\class{ntn-divc}{\operatorname{curl}}(u,v)=0$;</li>
<li>$u$ and $v$ satisfy the <em>Cauchy–Riemann equations</em>
\[ \frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}=0\qquad\text{and}\qquad\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}=0. \]</li>
</ol>
:::
::: proof
(2)⇔(3) is the definition of div and curl (@def:divergence-and-curl). (1)⇔(3): $C^1$ functions are differentiable as real maps ([A.1](apx:A1)), so @thm:cauchy-riemann applies to $f=u+i(-v)$ at every point, and its Cauchy–Riemann equations for the pair $(u,-v)$ are exactly (3). This is @prop:cauchy-riemann-in-the-language-of.
:::
<p>(2) and (3) say the same thing, since by definition $\class{ntn-divc}{\operatorname{div}}(u,v)=u_x+v_y$ and $\class{ntn-divc}{\operatorname{curl}}(u,v)=v_x-u_y$ ([divergence and curl](apx:A5)). The equivalence with (1) is @prop:cauchy-riemann-in-the-language-of. Note the minus sign in $f=u-iv$: it pairs the vector field $(u,v)$ with $f$ so that these equations come out in div/curl form. With the more common convention $f=U+iV$ one has $U=u$, $V=-v$.</p>
<p>In fluid terms, $(u,v)$ is the velocity field of an <b>incompressible</b> (divergence-free: no fluid created or destroyed) and <b>irrotational</b> (curl-free: no local spinning) flow.</p>
