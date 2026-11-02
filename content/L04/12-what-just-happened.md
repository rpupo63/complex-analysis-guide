---
id: t13
slide: Slide 13
title: 'Uniform limits: what just happened'
toc: What just happened
---

::: remark {#rem:uniform-limits-are-usually-not-smooth name="uniform limits are usually not smooth"}
Polynomials converge uniformly on $[-1,1]$ to $|x|$, which has a corner at $0$; this follows from the [Weierstrass approximation theorem](apx:A18). An explicit smooth example: $f_n(x):=\sqrt{x^2+1/n}$ is smooth and
\[ 0\le f_n(x)-|x|=\frac{1/n}{\sqrt{x^2+1/n}+|x|}\le\frac{1/n}{\sqrt{1/n}}=\frac1{\sqrt n}\to0 \]
uniformly in $x$. Yet the limit $|x|$ is not differentiable at $0$. Smoothness is not, in general, preserved by uniform limits.
:::

::: remark {#rem:why-harmonic-functions-escape name="why harmonic functions escape"}
The slide separates two reasons.
<ol>
<li><b>Harmonic = continuous + mean value property</b> ([Theorems #](@thm:mean-value-property) and [#](@thm:converse-of-the-mean-value-property)), and the right side has no derivative in it. A statement about values and integrals survives uniform convergence (Step 2 of @cor:uniform-limits); a statement about derivatives would not, as @rem:uniform-limits-are-usually-not-smooth shows.</li>
<li><b>The smoothness of the limit is not inherited</b> from the $h_n$. It is produced afresh by the identity $v=v\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}$ (@lem:averaging): an average of a continuous function against a smooth weight is smooth (@thm:converse-of-the-mean-value-property). The same mechanism made $\class{ntn-ud}{u_\delta}$ smooth in Weyl's lemma.</li>
</ol>
:::
<p>The slide closes with a preview: holomorphic functions behave the same way, for the same reason. Cauchy's integral formula (@thm:cauchys-integral-formula) is a statement about values and integrals, and @thm:uniform-limits is the holomorphic version of @cor:uniform-limits.</p>
