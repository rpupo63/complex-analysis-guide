---
id: m4
slide: Slide 5
title: Continuing $\Gamma$ by the functional equation
---

::: definition {#def:for-let-is-holomorphic-on}
For $n\ge0$ let
\[ \class{ntn-Wn}{W_n}:=\{\operatorname{Re}z\gt-n\}\setminus\{0,-1,\dots,-n+1\},\qquad\class{ntn-Gn}{\Gamma_n}(z):=\frac{\Gamma(z+n)}{z(z+1)\cdots(z+n-1)}. \]
$\class{ntn-Gn}{\Gamma_n}$ is holomorphic on $\class{ntn-Wn}{W_n}$: there $\operatorname{Re}(z+n)\gt0$, and the denominator does not vanish. $\class{ntn-Gn}{\Gamma_0}=\Gamma$ (empty product), and $\class{ntn-Wn}{W_0}=\{\operatorname{Re}z\gt0\}$.
:::
<figure>{{fig:m4-1}}<figcaption>$\Gamma(x)$ for $-4.6\le x\le4.6$, with poles at $0,-1,-2,\dots$ (dashed). Between consecutive poles the sign alternates.</figcaption></figure>

::: proposition {#prop:the-continuation-of-gamma name="the continuation of $\Gamma$"}
$\class{ntn-Wn}{W_n}\subset \class{ntn-Wn}{W_{n+1}}$ and $\class{ntn-Gn}{\Gamma_{n+1}}=\class{ntn-Gn}{\Gamma_n}$ on $\class{ntn-Wn}{W_n}$. So $\Gamma:=\class{ntn-Gn}{\Gamma_n}$ on $\class{ntn-Wn}{W_n}$ continues $\Gamma$ to
\[ \class{ntn-Wset}{W}:=\bigcup_n\class{ntn-Wn}{W_n}=\mathbb C\setminus\{0,-1,-2,\dots\}, \]
uniquely, and $\Gamma(z+1)=z\Gamma(z)$ on $\class{ntn-Wset}{W}$.
:::
::: proof

<ol>
<li><em>Consistency.</em> $\class{ntn-Wn}{W_n}\subset \class{ntn-Wn}{W_{n+1}}$ is clear. For $z\in \class{ntn-Wn}{W_n}$, $\operatorname{Re}(z+n)\gt0$, so the functional equation (@prop:the-gamma-function) gives $\Gamma(z+n+1)=(z+n)\Gamma(z+n)$, and
\[ \class{ntn-Gn}{\Gamma_{n+1}}(z)=\frac{(z+n)\,\Gamma(z+n)}{z(z+1)\cdots(z+n)}=\frac{\Gamma(z+n)}{z(z+1)\cdots(z+n-1)}=\class{ntn-Gn}{\Gamma_n}(z). \]</li>
<li><em>Gluing.</em> By induction and @prop:gluing-and-uniqueness(1), these define one holomorphic function on $\class{ntn-Wset}{W}$. It is unique because $\class{ntn-Wset}{W}$ is connected (a path between two of its points can detour around the isolated points $0,-1,-2,\dots$) and @prop:gluing-and-uniqueness(2).</li>
<li><em>Functional equation on $\class{ntn-Wset}{W}$.</em> If $z\in \class{ntn-Wset}{W}$ then $z+1\in \class{ntn-Wset}{W}$ (if $z+1=-m$ with $m\ge0$, then $z=-m-1\notin \class{ntn-Wset}{W}$). So both $\Gamma(z+1)$ and $z\Gamma(z)$ are holomorphic on $\class{ntn-Wset}{W}$, and they agree on $\{\operatorname{Re}z\gt0\}$; by uniqueness they agree on $\class{ntn-Wset}{W}$. <span class="qed">∎</span></li>
</ol>
:::
<p>The functional equation is used backwards: $\Gamma(z)=\Gamma(z+1)/z$ defines $\Gamma$ one strip further left, then $\Gamma(z+1)/z$ again, and so on. Division by $z,z+1,\dots$ produces the poles.</p>
