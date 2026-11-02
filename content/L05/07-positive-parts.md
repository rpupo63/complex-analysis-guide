---
id: v8
slide: Slide 8
title: What we need about $t\mapsto t^{\class{ntn-pos}{+}}$
toc: Positive parts
---

::: definition {#def:positive-part name="positive part"}
For a real number $t$, $t^{\class{ntn-pos}{+}}:=\max(t,0)$. For a function, $f^{\class{ntn-pos}{+}}:=\max(f,0)$ pointwise. Throughout @sec:v8, $f$ is continuous on $\overline\Omega$, $f\le-\sigma$ on $\class{ntn-dOm}{\partial\Omega}$ for some $\sigma\gt0$, and smooth in $\Omega$ on each closed square of some grid. (In mind: $f=z_n=\class{ntn-Un}{U_n}-\sigma-v$.)
:::

::: proposition {#prop:properties-of-f name="properties of $f^{\class{ntn-pos}{+}}$"}

(a) <b>Support.</b> $f^{\class{ntn-pos}{+}}=0$ outside the compact set $\class{ntn-Kc}{K}:=\{z\in\overline\Omega:f(z)\ge0\}$, and $\class{ntn-Kc}{K}\subset\Omega$.<br>
(b) <b>Contraction.</b> $|a^{\class{ntn-pos}{+}}-b^{\class{ntn-pos}{+}}|\le|a-b|$ for real $a,b$.<br>
(c) <b>Gradient.</b> $\nabla f^{\class{ntn-pos}{+}}=\nabla f$ where $f\gt0$, and $\nabla f^{\class{ntn-pos}{+}}=0$ where $f\le0$, almost everywhere. So $\nabla f\cdot\nabla f^{\class{ntn-pos}{+}}=|\nabla f^{\class{ntn-pos}{+}}|^2$ almost everywhere.<br>
(d) <b>Green.</b> $\iint_\Omega\nabla w\cdot\nabla f^{\class{ntn-pos}{+}}\,dA=-\iint_\Omega f^{\class{ntn-pos}{+}}\,\class{ntn-Delta}{\Delta} w\,dA$ for $w$ smooth in $\Omega$; so $=0$ if $w$ is harmonic.<br>
(e) <b>Poincaré.</b> $\class{ntn-L2}{\norm{f^+}_{L^2}}\le \class{ntn-L}{L}\,\class{ntn-L2}{\norm{\nabla f^+}_{L^2}}$, with $\class{ntn-L}{L}$ the width of $\Omega$.
:::
::: proof

<ol type="a">
<li><em>Support.</em> $\class{ntn-Kc}{K}$ is closed (points where a continuous function is $\ge0$, inside the closed set $\overline\Omega$) and bounded, hence [compact](apx:C5). On $\class{ntn-dOm}{\partial\Omega}$, $f\le-\sigma\lt0$, so $\class{ntn-Kc}{K}$ misses $\class{ntn-dOm}{\partial\Omega}$; hence $\class{ntn-Kc}{K}\subset\Omega$. Outside $\class{ntn-Kc}{K}$, $f\lt0$ and $f^{\class{ntn-pos}{+}}=0$. Since compact $\class{ntn-Kc}{K}$ stays a positive distance from $\class{ntn-dOm}{\partial\Omega}$ ([C.5](apx:C5)(a)), $f^{\class{ntn-pos}{+}}$ vanishes on a whole band around $\class{ntn-dOm}{\partial\Omega}$, not just on $\class{ntn-dOm}{\partial\Omega}$.</li>
<li><em>Contraction.</em> By cases. If $a,b\ge0$: $|a^{\class{ntn-pos}{+}}-b^{\class{ntn-pos}{+}}|=|a-b|$. If $a,b\le0$: $|a^{\class{ntn-pos}{+}}-b^{\class{ntn-pos}{+}}|=0$. If $a\gt0\ge b$: $|a^{\class{ntn-pos}{+}}-b^{\class{ntn-pos}{+}}|=a\le a-b=|a-b|$; the case $b\gt0\ge a$ is symmetric. Geometrically, $t\mapsto t^{\class{ntn-pos}{+}}$ has slope $0$ or $1$, so it never stretches distances: it is [1-Lipschitz](apx:A10).</li>
<li><em>Gradient.</em> Inside each open square, $f$ is smooth, so $f^{\class{ntn-pos}{+}}$ is [Lipschitz](apx:A10) there (by (b)) and differentiable almost everywhere. At a point of differentiability:
<ul>
<li>if $f\gt0$ there, then $f^{\class{ntn-pos}{+}}=f$ on a neighbourhood, so $\nabla f^{\class{ntn-pos}{+}}=\nabla f$;</li>
<li>if $f\lt0$ there, then $f^{\class{ntn-pos}{+}}=0$ on a neighbourhood, so $\nabla f^{\class{ntn-pos}{+}}=0$;</li>
<li>if $f=0$ there, then $f^{\class{ntn-pos}{+}}$ has a minimum ($f^{\class{ntn-pos}{+}}\ge0$ everywhere, $=0$ here), and a differentiable function has zero gradient at a minimum: $\nabla f^{\class{ntn-pos}{+}}=0$.</li>
</ul>
Grid lines have zero area. So almost everywhere, $\nabla f^{\class{ntn-pos}{+}}$ is either $\nabla f$ (where $f\gt0$) or $0$, and in both cases $\nabla f\cdot\nabla f^{\class{ntn-pos}{+}}=|\nabla f^{\class{ntn-pos}{+}}|^2$. Along any line the same reasoning applies in one variable: $f$ is piecewise $C^1$ near $\class{ntn-Kc}{K}$, $f^{\class{ntn-pos}{+}}$ is Lipschitz there, and $(f^{\class{ntn-pos}{+}})'=f'$ where $f\gt0$, $=0$ where $f\lt0$, and $=0$ on $\{f=0\}$ wherever it exists.</li>
<li><em>Green.</em> Fix a horizontal line. On each interval where the line crosses $\Omega$, $f^{\class{ntn-pos}{+}}$ vanishes near both ends by (a). The product $w_x f^{\class{ntn-pos}{+}}$ is Lipschitz on the part of the interval where $f^{\class{ntn-pos}{+}}\ne0$ ($w$ is smooth there; $f^{\class{ntn-pos}{+}}$ is Lipschitz), and zero near the ends, so the [fundamental theorem of calculus for Lipschitz functions](apx:A10) gives $\int\partial_x(w_xf^{\class{ntn-pos}{+}})\,dx=0$. Expanding with the product rule,
\[ \int w_x\,(f^{\class{ntn-pos}{+}})_x\,dx=-\int w_{xx}\,f^{\class{ntn-pos}{+}}\,dx. \]
Do the same along vertical lines with $w_y$, integrate over the other variable, and add: $\iint\nabla w\cdot\nabla f^{\class{ntn-pos}{+}}=-\iint f^{\class{ntn-pos}{+}}\,\class{ntn-Delta}{\Delta} w$. There are no boundary terms because $f^{\class{ntn-pos}{+}}$ vanishes near the ends. This is Step 1 of @prop:and-weakly-write with the test function $f^{\class{ntn-pos}{+}}$, which is not smooth but vanishes near $\class{ntn-dOm}{\partial\Omega}$. If $\class{ntn-Delta}{\Delta} w=0$ the right side is $0$.</li>
<li><em>Poincaré.</em> $f^{\class{ntn-pos}{+}}$ is continuous on $\overline\Omega$ and $0$ on $\class{ntn-dOm}{\partial\Omega}$. The proof of @thm:poincares-inequality only used the fundamental theorem of calculus along horizontal lines and Cauchy–Schwarz; the first holds for Lipschitz functions ([A.10](apx:A10)), so the same proof gives $\class{ntn-L2}{\norm{f^{\class{ntn-pos}{+}}}}\le \class{ntn-L}{L}\class{ntn-L2}{\norm{\nabla f^{\class{ntn-pos}{+}}}}$. <span class="qed">∎</span></li>
</ol>
:::
<p>A small point on (a)–(e) as applied to $f=z_n$: $v$ is smooth inside $\Omega$ but may not be smooth on the boundary edges of squares touching $\class{ntn-dOm}{\partial\Omega}$. This does no harm, because every step above takes place on or near $\class{ntn-Kc}{K}$, which stays inside $\Omega$.</p>
