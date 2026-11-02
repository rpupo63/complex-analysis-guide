---
id: f8
slide: Slide 9
title: Poles and residues
---

::: definition {#def:pole-of-order-m name="pole of order $m$"}
$f$ has a <em>pole of order $m\ge1$</em> at $\zeta$ if, for some $r\gt0$, $f(z)=\dfrac{g(z)}{(z-\zeta)^m}$ on $0\lt|z-\zeta|\le r$, where $g$ is holomorphic near $|z-\zeta|\le r$ and $g(\zeta)\ne0$. A pole of order $1$ is <em>simple</em>.
:::
<p>The order is well defined: $(z-\zeta)^mf(z)=g(z)\to g(\zeta)\ne0$ as $z\to\zeta$, while $(z-\zeta)^{m'}f(z)$ tends to $0$ for $m'\gt m$ and is unbounded for $m'\lt m$. Then $g=(z-\zeta)^mf$ is determined off $\zeta$, and at $\zeta$ by continuity.</p>

::: proposition {#prop:principal-part name="principal part"}
With $g(z)=\sum_{i\ge0}b_i(z-\zeta)^i$ for $|z-\zeta|\lt r$ (@thm:power-series), on $0\lt|z-\zeta|\lt r$
\[ f(z)=\frac{b_0}{(z-\zeta)^m}+\dots+\frac{b_{m-1}}{z-\zeta}+h(z),\qquad h(z):=\frac{g(z)-\sum_{i\lt m}b_i(z-\zeta)^i}{(z-\zeta)^m}, \]
and $h$ is holomorphic and bounded on $0\lt|z-\zeta|\le r/2$.
:::
::: proof
The identity is algebra: divide $g=\sum_{i\lt m}b_i(z-\zeta)^i+\big(g-\sum_{i\lt m}b_i(z-\zeta)^i\big)$ by $(z-\zeta)^m$. $h$ is holomorphic off $\zeta$ as a quotient. By @cor:taylor-remainder applied to $g$ with $N=m$ and $M_g:=\max_{|z-\zeta|=r}|g|$, the numerator of $h$ is at most $2M_g(|z-\zeta|/r)^m$ for $|z-\zeta|\le r/2$, so $|h|\le2M_g/r^m$ there.
:::
<p>The terms with negative powers form the <em>principal part</em>: a finite combination of multipoles, as in @def:the-residue.</p>

::: definition {#def:residue name=residue}
The <em>residue</em> of $f$ at the pole $\zeta$ is the coefficient of $\frac1{z-\zeta}$:
\[ \class{ntn-res}{\operatorname{Res}}_\zeta f:=b_{m-1}=\frac{g^{(m-1)}(\zeta)}{(m-1)!}. \]
:::
<p>The second expression is @thm:cauchys-formula-for-derivatives applied to $g$. This agrees with @def:the-residue, where the residue was $a_1$.</p>

::: proposition {#prop:simple-poles-of-a-quotient name="simple poles of a quotient"}
Let $A$ be holomorphic near $\zeta$ with $A(\zeta)\ne0$, and $B$ a polynomial with $B(\zeta)=0\ne B'(\zeta)$. Then $A/B$ has a simple pole at $\zeta$, and
\[ \class{ntn-res}{\operatorname{Res}}_\zeta\frac AB=\frac{A(\zeta)}{B'(\zeta)}. \]
:::
::: proof
Since $B(\zeta)=0$, the factor theorem gives $B=(z-\zeta)B_1$ with $B_1$ a polynomial. Differentiating, $B'=B_1+(z-\zeta)B_1'$, so $B_1(\zeta)=B'(\zeta)\ne0$. By continuity $B_1\ne0$ near $\zeta$, so $g:=A/B_1$ is holomorphic near $\zeta$ with $g(\zeta)=A(\zeta)/B'(\zeta)\ne0$, and $A/B=g/(z-\zeta)$. This is @def:pole-of-order-m with $m=1$, and the residue is $g(\zeta)$.
:::
<p>Example: $\frac1{1+z^2}$ at $\zeta=i$: $A=1$, $B=1+z^2$, $B'(i)=2i$, so the residue is $\frac1{2i}$ (used in @sec:h1).</p>
