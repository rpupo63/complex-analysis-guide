---
id: n5
slide: Slide 6
title: Solution of the problem
---

::: proposition {#prop:the-plate-solved name="the plate solved"}
$u:=v\circ C^{-1}$ solves @eg:the-plate. Explicitly,
\[ u(w)=\frac1\pi\arg\Big(i\,\frac{1+w}{1-w}\Big)=\frac12+\frac1\pi\arg\frac{1+w}{1-w},\qquad\arg\in(-\tfrac\pi2,\tfrac\pi2), \]
and $u(0)=\frac12$.
:::
::: proof

<ol>
<li><em>Harmonic.</em> By @thm:harmonic-composed-with-holomorphic applied to $C^{-1}:D(0,1)\to\mathbb H$, $u=v\circ C^{-1}$ is harmonic on $D(0,1)$.</li>
<li><em>Where the boundary goes.</em> Using $e^{\pm i\theta/2}$,
\[ \frac{1+e^{i\theta}}{1-e^{i\theta}}=\frac{e^{-i\theta/2}+e^{i\theta/2}}{e^{-i\theta/2}-e^{i\theta/2}}=\frac{2\cos\frac\theta2}{-2i\sin\frac\theta2}=i\cot\frac\theta2,\qquad\text{so}\qquad C^{-1}(e^{i\theta})=-\cot\frac\theta2. \]
This is negative for $0\lt\theta\lt\pi$ and positive for $\pi\lt\theta\lt2\pi$.</li>
<li><em>Limits.</em> $C^{-1}$ is continuous at $e^{i\theta}$ ($\theta\ne0$). So as $w\to e^{i\theta}$ inside the disk, $C^{-1}(w)\to-\cot\frac\theta2$ from inside $\mathbb H$, and by @prop:the-same-problem-on-the-half $u(w)=v(C^{-1}(w))\to1$ on the upper half-circle and $\to0$ on the lower one.</li>
<li><em>Explicit formula.</em> $\frac{1+w}{1-w}=\frac{(1+w)(1-\bar w)}{|1-w|^2}=\frac{1-|w|^2+(w-\bar w)}{|1-w|^2}$ has real part $\frac{1-|w|^2}{|1-w|^2}\gt0$, so its argument lies in $(-\frac\pi2,\frac\pi2)$, and multiplying by $i$ adds $\frac\pi2$. At $w=0$: $\arg(i)=\frac\pi2$, so $u(0)=\frac12$. <span class="qed">∎</span></li>
</ol>
:::
<figure>{{fig:n5-1}}<figcaption>Isotherms $u=0.1,0.25,0.5,0.75,0.9$ of @prop:the-plate-solved: arcs of circles through $\pm1$; $u=\frac12$ is the diameter.</figcaption></figure>
<p>Check: $u(0)=\frac12$ is the average of the boundary values (half the circle at $1$, half at $0$), as the mean value property (@thm:mean-value-property) demands. The level curves $\arg\frac{1+w}{1-w}=\text{const}$ are arcs of circles through $\pm1$, because the Möbius map $w\mapsto\frac{1+w}{1-w}$ sends them to rays from $0$.</p>
<p>Other regions need other holomorphic bijections, and each needs a holomorphic inverse for @cor:transporting-harmonic-functions to apply. That inverse comes for free: the inverse theorem, @sec:n9.</p>
