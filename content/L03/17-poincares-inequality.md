---
id: s18
slide: Slides 18–19
title: Poincaré's inequality
---

::: definition {#def:width name=width}
The <em>width</em> $\class{ntn-L}{L}$ of $\Omega$ is a number such that, after a horizontal translation, $\Omega$ lies in the strip $\{(x,y):0\lt x\lt \class{ntn-L}{L}\}$. Such an $\class{ntn-L}{L}$ exists because $\Omega$ is bounded.
:::

::: theorem {#thm:poincares-inequality name="Poincaré's inequality"}
If $v$ is continuous on $\overline\Omega$, piecewise continuously differentiable, and $v=0$ on $\class{ntn-dOm}{\partial\Omega}$, then
\[ \class{ntn-L2}{\norm{v}_{L^2}}\le \class{ntn-L}{L}\,\class{ntn-L2}{\norm{\nabla v}_{L^2}}. \]
:::
::: proof

<ol>
<li><em>Extend by zero.</em> Set $v:=0$ outside $\Omega$. The extension is continuous: at a point of $\class{ntn-dOm}{\partial\Omega}$, values from inside tend to $v=0$ and values outside are $0$. It is still piecewise smooth, with $\nabla v=0$ outside $\Omega$, so integrals over the strip equal integrals over $\Omega$.</li>
<li><em>Recover $v$ from its $x$-derivative.</em> Fix $y$. The line $x=0$ lies outside $\Omega$, so $v(0,y)=0$. The function $s\mapsto v(s,y)$ is continuous and piecewise $C^1$, so by the [fundamental theorem of calculus](apx:A9)
\[ v(x,y)=v(0,y)+\int_0^x\partial_xv(s,y)\,ds=\int_0^x\partial_xv(s,y)\,ds. \]</li>
<li><em>[Cauchy–Schwarz](apx:A12)</em> with the functions $1$ and $\partial_xv(\cdot,y)$ on $[0,x]$, for $0\le x\le \class{ntn-L}{L}$:
\[ |v(x,y)|^2=\Big(\int_0^x1\cdot\partial_xv(s,y)\,ds\Big)^2\le\Big(\int_0^x1^2\,ds\Big)\Big(\int_0^x|\partial_xv(s,y)|^2ds\Big)\le x\int_0^{\class{ntn-L}{L}}|\partial_xv(s,y)|^2ds\le \class{ntn-L}{L}\int_0^{\class{ntn-L}{L}}|\partial_xv(s,y)|^2ds. \]
The middle steps use $\int_0^x1^2=x$ and enlarge the interval of a nonnegative integrand from $[0,x]$ to $[0,\class{ntn-L}{L}]$.</li>
<li><em>Integrate over $x\in(0,\class{ntn-L}{L})$.</em> The right side does not depend on $x$, so
\[ \int_0^{\class{ntn-L}{L}}|v(x,y)|^2dx\le \class{ntn-L}{L}\cdot \class{ntn-L}{L}\int_0^{\class{ntn-L}{L}}|\partial_xv(s,y)|^2ds. \]</li>
<li><em>Integrate over $y$</em> and use $|\partial_xv|^2\le|\partial_xv|^2+|\partial_yv|^2=|\nabla v|^2$:
\[ \iint|v|^2\,dA\le \class{ntn-L}{L}^2\iint|\partial_xv|^2\,dA\le \class{ntn-L}{L}^2\iint|\nabla v|^2\,dA. \]
Take square roots. <span class="qed">∎</span></li>
</ol>
The constant $\class{ntn-L}{L}$ is not the best possible; see [a sharper constant](apx:E11). Any constant independent of $n$ and $k$ is enough for what follows.
:::

::: corollary {#cor:it-applies-to-u-n-u name="it applies to $\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k}$"}
$\class{ntn-L2}{\norm{U_n-U_k}_{L^2}}\le \class{ntn-L}{L}\,\class{ntn-L2}{\norm{\nabla(U_n-U_k)}_{L^2}}$, i.e. Poincaré holds with $C=\class{ntn-L}{L}$.
:::
::: proof
Take $n\le k$. Both functions lie in $\class{ntn-Vg}{V^g_{\eps_k}}$ ([Lemma #(b)](@lem:nesting)), so $\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k}\in \class{ntn-Vz}{V^0_{\eps_k}}$ (@prop:v-g-eps-is-affine-not). It is continuous and bilinear on each square, hence piecewise smooth, and it is zero at every boundary node. On a boundary edge a bilinear function is linear (@prop:linear-along-grid-lines-not-on), and a linear function vanishing at both endpoints vanishes on the whole edge. So $\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k}=0$ on all of $\class{ntn-dOm}{\partial\Omega}$, and @thm:poincares-inequality applies with $v=\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k}$.
:::
