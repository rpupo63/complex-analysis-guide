---
id: n9
slide: Slide 10
title: The inverse theorem; conformal maps
---

::: theorem {#thm:inverse name=inverse}
Let $f$ be holomorphic and injective on an open set $U$. Then $f'\ne0$ on $U$, $V:=f(U)$ is open, and $g:=f^{-1}$ is holomorphic on $V$, with $g'(f(z))=1/f'(z)$.
:::
::: proof

<ol>
<li><em>$f'\ne0$.</em> Being injective, $f$ is not constant near any point, and it is injective on every disk, so $f'\ne0$ everywhere by @cor:local-injectivity.</li>
<li><em>$V$ open and $g$ continuous.</em> Apply the open mapping theorem on disks inside $U$ (each disk is connected): $f$ maps every open subset $W\subseteq U$ to an open set, a union of open images of disks. With $W=U$, $V$ is open. And $g^{-1}(W)=f(W)$ is open for every open $W$, which is continuity of $g$.</li>
<li><em>Derivative.</em> Let $w_1=f(z_1)\in V$ and $w=f(z)\to w_1$, $w\ne w_1$. Then $z=g(w)\to z_1$ (continuity of $g$), $z\ne z_1$ (injectivity), and
\[ \frac{g(w)-g(w_1)}{w-w_1}=\frac{z-z_1}{f(z)-f(z_1)}\longrightarrow\frac1{f'(z_1)}, \]
which exists since $f'(z_1)\ne0$. So $g$ is complex differentiable, and $g'=1/(f'\circ g)$ is continuous: $g$ is holomorphic with $C^1$ parts. <span class="qed">∎</span></li>
</ol>
:::
<p>In real analysis the first claim fails: $x^3$ is injective with derivative $0$ at $0$, and its inverse $\sqrt[3]x$ is not differentiable there.</p>

::: definition {#def:conformal-map name="conformal map"}
For $U,V$ open, a <em>conformal map of $U$ onto $V$</em> is a holomorphic bijection $f:U\to V$. By @thm:inverse, $f^{-1}$ is then a conformal map of $V$ onto $U$, and by @cor:transporting-harmonic-functions it transports harmonic functions both ways. Compositions of conformal maps are conformal maps (chain rule).
:::
