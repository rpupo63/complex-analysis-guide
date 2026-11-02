---
id: g1
slide: Slide 2
title: Zeros, poles and $f'/f$
---
<p>The residue theorem counts residues. Applied to $f'/f$, it counts zeros and poles. First, the two local pictures side by side.</p>

::: definition {#def:zero-of-order-m name="zero of order $m$"}
$f$ has a <em>zero of order $m\ge1$</em> at $a$ if $f$ is holomorphic near $a$ and its Taylor coefficients at $a$ satisfy $a_0=\dots=a_{m-1}=0\ne a_m$. (This is @def:order-of-a-zero.)
:::

::: definition {#def:pole-of-order-m-l7 name="pole of order $m$"}
$f$ has a <em>pole of order $m\ge1$</em> at $a$ if, for some $\rho\gt0$, $f=g/(z-a)^m$ on $0\lt|z-a|\lt\rho$, with $g$ holomorphic on $|z-a|\lt\rho$ and $g(a)\ne0$. (This is @def:pole-of-order-m, with an open disk.)
:::
<p>In both cases $f(z)$ behaves like a constant times $(z-a)^{\pm m}$ near $a$: a zero is a "pole of negative order". The lemma below makes this precise through the <em>logarithmic derivative</em> $f'/f$, so called because it is $(\log f)'$ wherever a branch of $\log f$ exists.</p>

::: lemma {#lem:logarithmic-derivative name="logarithmic derivative"}
Let $f$ be holomorphic and $\ne0$ on $0\lt|z-a|\lt r$, with a zero or a pole of order $m$ at $a$. Then for every $\epsilon\in(0,r)$,
\[ \frac1{2\pi i}\oint_{|z-a|=\epsilon}\frac{f'(z)}{f(z)}\,dz=\begin{cases}\ \ m&\text{at a zero},\\-m&\text{at a pole}.\end{cases} \]
:::
<p>Test case: $f(z)=(z-a)^m$ has $\frac{f'}{f}=\frac{m}{z-a}$, whose integral is $m$ (@cor:the-residue-theorem-point-charge-form); $f=(z-a)^{-m}$ gives $-m$. The lemma says that only this leading behaviour matters.</p>
