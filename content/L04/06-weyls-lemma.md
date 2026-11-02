---
id: t7
slide: Slide 7
title: Weyl's lemma
---

::: definition {#def:test-function-lecture-4 name="test function, Lecture 4"}
A <em>test function</em> is a smooth function $\eta$ on $\Omega$ that vanishes outside a [compact](apx:C5) subset of $\Omega$, hence on a whole band near $\class{ntn-dOm}{\partial\Omega}$. This is the class of $\psi$ in @def:weak-derivative (weak derivative), now required to be smooth rather than $C^1$.
:::

::: theorem {#thm:weyls-lemma name="Weyl's lemma"}
Let $u\in L^2(\Omega)$ ([square-integrable on $\Omega$](apx:D2)) satisfy $\iint_\Omega u\,\class{ntn-Delta}{\Delta}\eta\,dA=0$ for every test function $\eta$. Then $u$ agrees [almost everywhere](apx:A11) with a smooth harmonic function.
:::
<p>The proof occupies @sec:t9–@sec:t10 (@thm:proof-of-weyls-lemma). First, what the hypothesis says.</p>

::: proposition {#prop:what-the-hypothesis-means name="what the hypothesis means"}
If $u$ is $C^2$ on $\Omega$, then for every test function $\eta$
\[ \iint_\Omega u\,\class{ntn-Delta}{\Delta}\eta\,dA=\iint_\Omega(\class{ntn-Delta}{\Delta} u)\,\eta\,dA, \]
and this vanishes for every test function exactly when $\class{ntn-Delta}{\Delta} u=0$ on $\Omega$.
:::
::: proof
<em>Integrate by parts twice.</em> Fix $y$ and work on the horizontal line through $\Omega$. The functions $u\,\partial_x\eta$ and $(\partial_xu)\,\eta$ are $C^1$ and vanish near $\class{ntn-dOm}{\partial\Omega}$ (because $\eta$ does); extend them by zero, as in @prop:and-weakly-write. The [fundamental theorem of calculus](apx:A9) gives $\int\partial_x(u\,\partial_x\eta)\,dx=0$ and $\int\partial_x(\partial_xu\,\eta)\,dx=0$; expanding with the product rule,
\[ \int u\,\partial_x^2\eta\,dx=-\int\partial_xu\,\partial_x\eta\,dx=\int\partial_x^2u\,\eta\,dx. \]
There are no boundary terms because $\eta$ vanishes near $\class{ntn-dOm}{\partial\Omega}$. Do the same in $y$, add, and integrate over the other variable: $\iint u\,\class{ntn-Delta}{\Delta}\eta=\iint(\class{ntn-Delta}{\Delta} u)\,\eta$.<br>
<em>"Exactly when".</em> If $\class{ntn-Delta}{\Delta} u=0$, the right side is $0$ for every $\eta$. Conversely, suppose $\class{ntn-Delta}{\Delta} u(z_0)\ne0$, say $\class{ntn-Delta}{\Delta} u(z_0)\gt0$. By continuity $\class{ntn-Delta}{\Delta} u\gt c\gt0$ on some disk of radius $\rho$ about $z_0$ inside $\Omega$. Take $\eta(\zeta):=\class{ntn-chid}{\chi_\rho}(\zeta-z_0)$: it is a test function, $\ge0$, zero outside that disk, with integral $1$ (@lem:is-smooth-radial-zero-outside). Then $\iint(\class{ntn-Delta}{\Delta} u)\eta\ge c\iint\eta=c\gt0$, so the integral does not vanish. The case $\class{ntn-Delta}{\Delta} u(z_0)\lt0$ is the same with signs reversed.
:::

::: remark {#rem:the-weakest-form-of-the-equation name="the weakest form of the equation"}
For $u$ only in $L^2$ ([square-integrable](apx:D2)), the right side $\iint(\class{ntn-Delta}{\Delta} u)\eta$ makes no sense, but the left side does. So the hypothesis of Weyl's lemma is "$\class{ntn-Delta}{\Delta} u=0$ with <em>both</em> derivatives moved onto $\eta$". Compare the weak form of Lecture 3, $\class{ntn-a}{a}(u,\eta)=0$, which moves only one derivative. Weyl's lemma says that even this weakest version of the equation forces $u$ to be smooth. In the language of [distributions](apx:E13), $u$ is a distributional solution of $\class{ntn-Delta}{\Delta} u=0$.
:::
