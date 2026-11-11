---
id: q10
slide: Slide 13
title: 'Example: a half-strip'
---

::: example {#eg:the-half-strip name="the half-strip; $\arcsin$"}
Let $P=\{|\operatorname{Re}w|\lt\frac\pi2,\ \operatorname{Im}w\gt0\}$. Its vertices are $\pm\frac\pi2$ (right angles, $\alpha=\frac12$) and $\infty$ (a channel, $\alpha=0$); the turns add up to $\frac12+\frac12+1=2$. With prevertices $-1,1,\infty$, @thm:schwarz-christoffel and @rem:vertices-at-infinity give
\[ F'(z)=A(z+1)^{-1/2}(z-1)^{-1/2}. \]
On $(-1,1)$, $(x+1)^{-1/2}(x-1)^{-1/2}=\dfrac{-i}{\sqrt{1-x^2}}$ (@conv:powers-of-x-minus-xk). With $A=i$ and $B=0$, so that $F(\pm1)=\pm\frac\pi2$,
\[ F(z)=\int_0^z\frac{d\zeta}{\sqrt{1-\zeta^2}}=\arcsin z. \]
:::

::: proposition {#prop:sin-maps-the-half-strip name="a direct check"}
$\sin$ maps $P$ conformally onto $\mathbb H$.
:::
::: proof

<ol>
<li><em>Into $\mathbb H$.</em> $\sin(x+iy)=\sin x\cosh y+i\cos x\sinh y$, and on $P$, $\cos x\gt0$ and $\sinh y\gt0$.</li>
<li><em>Boundary to $\mathbb R$.</em> $\sin(\pm\frac\pi2+iy)=\pm\cosh y$ runs over $\pm[1,\infty)$ for $y\ge0$, and $\sin x$ runs over $(-1,1)$ for $|x|\lt\frac\pi2$.</li>
<li><em>Injective.</em> $\sin w_1-\sin w_2=2\cos\frac{w_1+w_2}2\sin\frac{w_1-w_2}2$, so $\sin w_1=\sin w_2$ means $w_1-w_2\in2\pi\mathbb Z$ or $w_1+w_2\in\pi+2\pi\mathbb Z$. On $P$, $|\operatorname{Re}(w_1\pm w_2)|\lt\pi$, so only $w_1=w_2$ is possible.</li>
<li><em>Onto.</em> $\sin(P)$ is open (@thm:open-mapping). It is also closed in $\mathbb H$: if $w_n\in P$ and $\sin w_n\to\zeta\in\mathbb H$, then $|\sin w_n|\ge\sinh\operatorname{Im}w_n$ keeps $\operatorname{Im}w_n$ bounded, so a subsequence converges to $w\in\overline P$ with $\sin w=\zeta$; and $w\notin\partial P$ since $\sin(\partial P)\subseteq\mathbb R$. $\mathbb H$ is [connected](apx:C4), so $\sin(P)=\mathbb H$. By @thm:inverse the map is conformal. <span class="qed">∎</span></li>
</ol>
:::
