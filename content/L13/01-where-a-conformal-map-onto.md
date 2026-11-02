---
id: o1
slide: Slide 2
title: Where a conformal map onto the disk comes from
---
<p>The strategy is to work backwards. Suppose a Riemann map exists. What must it look like? The answer is built from the solution of a Dirichlet problem, which Part I knows how to solve.</p>

::: setting {#set:is-a-bounded-connected-open}
$\Omega$ is a bounded connected open set and $z_0\in\Omega$. In this section, $f$ is a conformal map of $\Omega$ onto $D(0,1)$ with $f(z_0)=0$ and $f'(z_0)\gt0$.
:::

::: proposition {#prop:what-a-riemann-map-must-look name="what a Riemann map must look like"}
In @set:is-a-bounded-connected-open:<br>
(a) $|f(z)|=|z-z_0|\,e^{-h(z)}$, where $h$ is the harmonic function on $\Omega$, continuous on $\overline\Omega$, with $h(z)=\log|z-z_0|$ on $\partial\Omega$.<br>
(b) $f$ is unique.<br>
(c) If $h=\operatorname{Re}H$ with $H$ holomorphic on $\Omega$, then $f(z)=c\,(z-z_0)\,e^{-H(z)}$ for a constant $c$ with $|c|=1$, fixed by $f'(z_0)>0$: $c=e^{i\operatorname{Im}H(z_0)}$.
:::
::: proof

<ol>
<li><em>Divide out the zero.</em> $f$ is injective, so its only zero is $z_0$, and $f'(z_0)\ne0$ (@thm:inverse). So $g(z):=f(z)/(z-z_0)$ is holomorphic on $\Omega\setminus\{z_0\}$, tends to $f'(z_0)$ at $z_0$, and extends holomorphically there (@lem:removable-singularities) with $g(z_0)=f'(z_0)\ne0$. It has no zeros on $\Omega$. So $\log|g|$ is harmonic on $\Omega$: on each disk inside $\Omega$ this is @lem:if-is-holomorphic-and-zero, and harmonicity is local.</li>
<li><em>$|f|\to1$ at the boundary.</em> For $r\lt1$, $f^{-1}$ maps the closed disk $|w|\le r$ onto a compact set $K_r\subset\Omega$ ($f^{-1}$ is continuous, and continuous images of compact sets are compact). $K_r$ stays a positive distance from $\partial\Omega$ ([C.5](apx:C5)), and outside $K_r$, $|f|\gt r$. So as $z\to\partial\Omega$, eventually $|f(z)|\gt r$; since $r\lt1$ is arbitrary and $|f|\lt1$, $|f(z)|\to1$.</li>
<li><em>(a): a Dirichlet problem.</em> Let $h:=-\log|g|=\log|z-z_0|-\log|f|$ (the second form for $z\ne z_0$). It is harmonic on $\Omega$, and by step 2, $h(z)-\log|z-z_0|=-\log|f(z)|\to0$ as $z\to\partial\Omega$. So $h$, extended by $\log|z-z_0|$ on $\partial\Omega$, is continuous on $\overline\Omega$: it solves the Dirichlet problem with the continuous boundary data $\log|z-z_0|$ (continuous, as $z_0\notin\partial\Omega$). That solution is unique by @cor:stability. Rearranging $h=\log|z-z_0|-\log|f|$ gives $|f|=|z-z_0|e^{-h}$.</li>
<li><em>(b): uniqueness.</em> Two such maps $f_1,f_2$ have the same modulus by (a). Then $f_1/f_2$ (with the singularity at $z_0$ removed: it tends to $f_1'(z_0)/f_2'(z_0)\gt0$) is holomorphic on $\Omega$ with modulus $1$. Its image lies on the unit circle, which contains no open set, so by the open mapping theorem (@thm:open-mapping) it is constant; that constant is $f_1'(z_0)/f_2'(z_0)\gt0$ and has modulus $1$, so it is $1$.</li>
<li><em>(c): the formula.</em> $\frac{f(z)}{(z-z_0)e^{-H(z)}}$ is holomorphic (removable at $z_0$ as in step 1) with modulus $\frac{|f|}{|z-z_0|e^{-h}}=1$, hence a constant $c$ with $|c|=1$, as in step 4. Then $f'(z_0)=c\,e^{-H(z_0)}=c\,e^{-i\operatorname{Im}H(z_0)}e^{-h(z_0)}$, and this is $>0$ only for $c=e^{i\operatorname{Im}H(z_0)}$. <span class="qed">∎</span></li>
</ol>
:::
<p>So a Riemann map is determined by one Dirichlet problem: the one with boundary values $\log|z-z_0|$. Existence is the converse: solve that problem, find $H$, and define $f$ by the formula of (c).</p>
