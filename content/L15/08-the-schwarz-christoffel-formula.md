---
id: q8
slide: Slides 9–11
title: The Schwarz–Christoffel formula
---

::: theorem {#thm:schwarz-christoffel name="Christoffel 1867, Schwarz 1869"}
Let $P$ be a polygon (@def:polygon), $F$ a conformal map of $\mathbb H$ onto its interior, and $x_1\lt\dots\lt x_n$ its real prevertices (@sec:q6). There are $A\ne0$ and $B$ such that for $z\in\mathbb H$
\[ F(z)=A\int_0^z\prod_{k=1}^n(\zeta-x_k)^{\alpha_k-1}\,d\zeta+B, \]
with the branches $0\le\arg(\zeta-x_k)\le\pi$ (@conv:powers-of-x-minus-xk), along any path in $\mathbb H$ (its ends may lie on $\mathbb R$).
:::
<p>The integrand is holomorphic on $\mathbb H$ and integrable near each $x_k$, because $\alpha_k-1\gt-1$.</p>
<p><b>Plan.</b> $F'\ne0$ on $\mathbb H$ (@thm:inverse), so $g:=F''/F'$ is holomorphic on $\mathbb H$. We show that
\[ g(z)=\sum_{k=1}^n\frac{\alpha_k-1}{z-x_k}, \]
the logarithmic derivative of $\prod_k(z-x_k)^{\alpha_k-1}$. Then $F'/\prod_k(z-x_k)^{\alpha_k-1}$ has derivative $0$ on the connected set $\mathbb H$, so it is a constant $A\ne0$; integrate.</p>
::: proof

<ol>
<li><em>Sides.</em> Let $J\subseteq\mathbb R$ be an open interval between consecutive prevertices; $F$ is continuous on $\mathbb H\cup J$ (@fact:caratheodory) and maps $J$ into a line $L$, the line of one side. By @cor:reflection-in-a-line, $F$ extends holomorphically across $J$, and sends points below $J$ to the mirror images in $L$ of points of $P$. Let $x\in J$. $F(x)$ is not a vertex, so near $F(x)$ the interior of $P$ lies on one side of $L$ and its mirror image on the other. So for a small disk $D$ about $x$, $F$ maps $D^+$, $D\cap\mathbb R$ and $D^-$ into three disjoint sets, injectively on each: $F$ is injective on $D$, and $F'(x)\ne0$ (@cor:local-injectivity). On $J$, $F'(x)=e^{i\theta}|F'(x)|$ points along $L$ in the direction of travel, with $\theta$ fixed, so $F''(x)=e^{i\theta}\frac d{dx}|F'(x)|$, and $g$ is real on $J$. Applying @thm:schwarz-reflection to $g$ on $\Omega=\mathbb C\setminus\{x_1,\dots,x_n\}$, $g$ extends holomorphically to $\mathbb C\setminus\{x_1,\dots,x_n\}$.</li>
<li><em>Vertices.</em> Near $x_k$, $F-w_k$ takes values in a sector of opening $\alpha_k\pi\lt2\pi$ at $0$. Choose a branch $h:=(F-w_k)^{1/\alpha_k}$ near $x_k$; it maps $\mathbb H$ near $x_k$ injectively into a half-plane, and $\mathbb R$ near $x_k$ into the line bounding it. As in step 1, $h$ extends holomorphically and injectively to a disk about $x_k$, with $h(x_k)=0$, so $h'(x_k)\ne0$: $h$ has a simple zero at $x_k$. From $F=w_k+h^{\alpha_k}$, $F'=\alpha_kh^{\alpha_k-1}h'$, so near $x_k$
\[ g=(\alpha_k-1)\frac{h'}{h}+\frac{h''}{h'}=\frac{\alpha_k-1}{z-x_k}+\text{(holomorphic near }x_k). \]</li>
<li><em>At $\infty$.</em> $F(\infty)$ lies on the side $[w_n,w_1]$ and is not a vertex. $\zeta\mapsto-1/\zeta$ is an automorphism of $\mathbb H$ (@prop:automorphisms-of-h), so $G(\zeta):=F(-1/\zeta)$ is a conformal map of $\mathbb H$ onto $P$ for which $0$ is not a prevertex. By step 1, $G$ is holomorphic near $0$ with $G'(0)\ne0$: $G(\zeta)=b_0+b_1\zeta+b_2\zeta^2+\dots$ with $b_1\ne0$ (@thm:power-series). So for large $|z|$,
\[ F(z)=G(-1/z)=b_0-\frac{b_1}z+\frac{b_2}{z^2}-\cdots,\qquad g(z)=\frac{F''(z)}{F'(z)}=\frac{-2b_1z^{-3}+O(z^{-4})}{b_1z^{-2}+O(z^{-3})}=-\frac2z+O\Big(\frac1{z^2}\Big). \]</li>
<li><em>The end.</em> By steps 1 and 2, $g(z)-\sum_k\frac{\alpha_k-1}{z-x_k}$ is holomorphic on $\mathbb C$ minus the $x_k$ and bounded near each $x_k$, so it is entire (@lem:removable-singularities). By step 3 it tends to $0$ as $z\to\infty$, so it is bounded, hence constant (@thm:liouville), hence $0$. <span class="qed">∎</span></li>
</ol>
:::
<p><b>A check.</b> Comparing the coefficients of $1/z$ at $\infty$ gives $\sum_k(\alpha_k-1)=-2$: the proof recovers the angle sum of @sec:q6.</p>
