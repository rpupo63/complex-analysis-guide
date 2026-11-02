---
id: w3
slide: Slide 6
title: Where are the charges?
---
<p>The condition $\class{ntn-rhoc}{\rho}=0$ does <b>not</b> force the field to vanish: a constant electric field $\class{ntn-Ef}{E}=(a,b)$ has $\class{ntn-divc}{\operatorname{div}}\class{ntn-Ef}{E}=\class{ntn-divc}{\operatorname{curl}}\class{ntn-Ef}{E}=0$ and is not zero. A field is determined only after boundary conditions or behaviour at infinity are also prescribed. (Lecture 2 makes this precise in @sec:w9: with boundary values prescribed, there is only one field.)</p>
<p>The right way to think about it: our holomorphic $f$ is defined on a region $D$ (a disk, say). The charges are <b>outside</b> $D$: on plates and wires surrounding it, at infinity, or at points we have excluded from $D$. Inside $D$ there is no charge, so $\class{ntn-rhoc}{\rho}=0$ there, and that is all the Cauchy–Riemann equations say.</p>

::: example {#eg:a-charge-just-outside name="a charge just outside" status=derived}
$f(z)=\dfrac1{z-a}$ is holomorphic on any disk $D$ not containing $a$. Its source is the point $a$, outside the region. Likewise $f=1/z$ is holomorphic on $D=\mathbb C\setminus\{0\}$, and the charge is at the one point we left out.
:::
::: proof
For $z\ne a$ and small $h$,
\[ \frac{1}{h}\Big(\frac1{z+h-a}-\frac1{z-a}\Big)=\frac1h\cdot\frac{(z-a)-(z+h-a)}{(z+h-a)(z-a)}=\frac{-1}{(z+h-a)(z-a)}\longrightarrow\frac{-1}{(z-a)^2} \]
as $h\to0$ in $\mathbb C$, by the same algebra as for real numbers. So $f'(z)=-1/(z-a)^2$ exists wherever $z\ne a$.
:::
<p style="text-align:center"><b>Holomorphic functions describe the electric field away from the charges.</b></p>
