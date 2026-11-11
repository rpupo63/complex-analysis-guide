---
id: q15
slide: Slides 18–19
title: The edge of a capacitor
---

::: example {#eg:the-edge-of-a-capacitor name="the edge of a capacitor; Maxwell's map"}
Two plates $\{\operatorname{Im}w=\pm\pi,\ \operatorname{Re}w\le-1\}$ are held at the potentials $\pm1$, and $u$ is bounded. By symmetry $u=0$ on $\mathbb R$, so we need $u$ on
\[ \Omega^+=\{\operatorname{Im}w\gt0\}\setminus\{\operatorname{Im}w=\pi,\ \operatorname{Re}w\le-1\}, \]
with $u=1$ on the plate and $u=0$ on $\mathbb R$.
<ul>
<li><b>The map.</b> The vertices are the tip $-1+i\pi$ ($\alpha=2$), $\infty$ between the plate and $\mathbb R$ (a channel, $\alpha=0$), and $\infty$ outside ($\alpha=-1$, @rem:vertices-at-infinity). The turns add up to $-1+1+2=2$. With prevertices $-1$, $0$, $\infty$, $F'(\zeta)=A\frac{\zeta+1}\zeta$, so with $A=1$, $B=0$,
\[ F(\zeta)=\zeta+\log\zeta. \]
Check: $\zeta\gt0$ goes onto $\mathbb R$. For $\zeta=-s\lt0$, $F(\zeta)=-s+\log s+i\pi$ runs along both sides of the plate, and turns back at the tip when $s=1$, where $-s+\log s$ has its maximum $-1$.</li>
<li><b>The potential.</b> On $\mathbb H$ (variable $\zeta$), the bounded harmonic function equal to $1$ on $(-\infty,0)$ and $0$ on $(0,\infty)$ is $\frac1\pi\arg\zeta$. Put $\zeta=e^z$, with $z$ in the strip $0\lt\operatorname{Im}z\lt\pi$:
\[ w=z+e^z,\qquad u=\frac{\operatorname{Im}z}\pi. \]</li>
</ul>
:::

::: remark {#rem:correction-capacitor-uniqueness name="correction to the slide"}
"By symmetry $u=0$ on $\mathbb R$" and "the bounded harmonic function equal to $1$ on $(-\infty,0)$ and $0$ on $(0,\infty)$" both use the uniqueness of a bounded solution on an unbounded region. The maximum principle of Lecture 4 (@cor:maximum-principle) covers only bounded regions, and the slides do not prove this uniqueness. It is true (Phragmén–Lindelöf), and is assumed here.
:::

<p><b>The fringing field</b> (Slide 19). The equipotentials $u=0,\pm\frac16,\dots,\pm\frac56$ and the field lines are the images of horizontal and vertical lines under $w=z+e^z$, $-\pi\lt\operatorname{Im}z\lt\pi$ (the lower half by reflection). The map is Maxwell's (1873). From $\frac{dw}{dz}=1+e^z$,
\[ |E|=\frac1\pi\left|\frac{dz}{dw}\right|=\frac1{\pi|1+e^z|}. \]</p>
<ul>
<li>Far between the plates ($\operatorname{Re}z\to-\infty$): $w\approx z$, a uniform field $\frac1\pi$, which is the potential difference $2$ over the distance $2\pi$.</li>
<li>Far outside ($\operatorname{Re}z\to+\infty$): $|E|\to0$.</li>
<li>At the tip $z=i\pi$: $1+e^{i\pi}=0$, and $w-w_{\mathrm{tip}}\approx-\frac12(z-i\pi)^2$, so $|E|\approx c_1|w-w_{\mathrm{tip}}|^{-1/2}$, as @prop:the-field-near-a-corner predicts for $\alpha=2$.</li>
</ul>
<p><b>Rogowski electrodes</b> follow the equipotentials $u=\pm\frac12$, that is $\operatorname{Im}z=\pm\frac\pi2$. With $z=x\pm\frac{i\pi}2$, $e^z=\pm ie^x$, so the electrode is the curve $\operatorname{Im}w=\pm\big(\frac\pi2+e^{\operatorname{Re}w}\big)$. On it
\[ |E|=\frac1{\pi\sqrt{1+e^{2x}}}\lt\frac1\pi: \]
the field decreases along the electrode as it bends away. There is no edge enhancement.</p>
<p>Slide 20 summarizes the lecture.</p>
