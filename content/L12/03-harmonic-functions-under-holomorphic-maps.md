---
id: n3
slide: Slide 4
title: Harmonic functions under holomorphic maps
---

::: theorem {#thm:harmonic-composed-with-holomorphic name="harmonic composed with holomorphic"}
Let $U,V$ be open, $f:U\to V$ holomorphic, and $u$ harmonic on $V$. Then $u\circ f$ is harmonic on $U$.
:::
::: proof
Harmonicity is a local property, so it suffices to check it near each $z_0\in U$. Let $D\subseteq V$ be a disk about $f(z_0)$. By @lem:harmonic-conjugate-on-a-disk, $u=\operatorname{Re}F$ on $D$ with $F$ holomorphic. The set $f^{-1}(D)$ is open (as $f$ is continuous) and contains $z_0$, and on it $u\circ f=\operatorname{Re}(F\circ f)$. The composition $F\circ f$ is holomorphic (chain rule), so its real part is harmonic (@cor:holomorphic-functions-are-smooth).
:::

::: corollary {#cor:transporting-harmonic-functions name="transporting harmonic functions"}
If $f:U\to V$ is a bijection and $f$, $f^{-1}$ are holomorphic, then $u\mapsto u\circ f$ is a bijection from the harmonic functions on $V$ onto those on $U$, with inverse $h\mapsto h\circ f^{-1}$.
:::
::: proof
@thm:harmonic-composed-with-holomorphic applies to $f$ and to $f^{-1}$, and $(u\circ f)\circ f^{-1}=u$, $(h\circ f^{-1})\circ f=h$.
:::

::: proposition {#prop:how-the-laplacian-transforms name="how the Laplacian transforms"}
For $f$ holomorphic and $u$ a $C^2$ function, $\Delta(u\circ f)=|f'|^2\,(\Delta u)\circ f$.
:::
::: proof
Write $f=p+iq$ and $u=u(p,q)$. By the chain rule, $\partial_x(u\circ f)=u_pp_x+u_qq_x$, and differentiating again,
\[ \Delta(u\circ f)=u_{pp}(p_x^2+p_y^2)+2u_{pq}(p_xq_x+p_yq_y)+u_{qq}(q_x^2+q_y^2)+u_p\,\Delta p+u_q\,\Delta q. \]
By Cauchy–Riemann, $p_x=q_y$ and $p_y=-q_x$. Then $p_xq_x+p_yq_y=q_yq_x-q_xq_y=0$; $p_x^2+p_y^2=q_x^2+q_y^2=|f'|^2$ (as $f'=p_x+iq_x$); and $\Delta p=\Delta q=0$ (@prop:if-satisfy-the-cauchy-riemann). What remains is $|f'|^2(u_{pp}+u_{qq})$.
:::
<p>So the <em>equation</em> $\Delta u=0$ is preserved, which is all that equilibria need. The heat equation $u_t=\Delta u$ is not: it becomes $u_t=|f'|^{-2}\Delta u$, heat flow in a material whose conductivity varies from point to point. Only the equilibrium problem transfers.</p>
