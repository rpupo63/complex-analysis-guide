---
id: f3
slide: Slide 4
title: Cauchy's integral formula
---

::: theorem {#thm:cauchys-integral-formula name="Cauchy's integral formula"}
Let $f$ be holomorphic near $|z-z_0|\le r$. Then for every $w$ with $|w-z_0|\lt r$,
\[ f(w)=\frac1{2\pi i}\oint_{|z-z_0|=r}\frac{f(z)}{z-w}\,dz. \]
:::
::: proof

<ol>
<li><em>Shrink the circle to $w$.</em> Fix $0\lt\delta\lt r-|w-z_0|$. Every $z$ with $|z-w|\le\delta$ has $|z-z_0|\le|z-w|+|w-z_0|\lt r$, so the closed disk of radius $\delta$ about $w$ lies in the open disk of the big circle. The function $g(z):=f(z)/(z-w)$ is holomorphic, with $C^1$ parts, wherever $f$ is and $z\ne w$ (quotient rule); in particular near the region between the two circles. @lem:moving-the-circle gives
\[ \oint_{|z-z_0|=r}\frac{f(z)}{z-w}\,dz=\oint_{|z-w|=\delta}\frac{f(z)}{z-w}\,dz. \]</li>
<li><em>Parametrize.</em> Put $z=w+\delta e^{i\theta}$, $0\le\theta\le2\pi$. Then $dz=i\delta e^{i\theta}d\theta$ and $z-w=\delta e^{i\theta}$, so the right side is
\[ \int_0^{2\pi}\frac{f(w+\delta e^{i\theta})}{\delta e^{i\theta}}\,i\delta e^{i\theta}\,d\theta=i\int_0^{2\pi}f(w+\delta e^{i\theta})\,d\theta. \]</li>
<li><em>Let $\delta\to0$.</em> Since $i\int_0^{2\pi}f(w)\,d\theta=2\pi i\,f(w)$,
\[ \Big|\,i\int_0^{2\pi}f(w+\delta e^{i\theta})\,d\theta-2\pi i\,f(w)\Big|\le\int_0^{2\pi}|f(w+\delta e^{i\theta})-f(w)|\,d\theta\le2\pi\max_\theta|f(w+\delta e^{i\theta})-f(w)|, \]
which tends to $0$ because $f$ is continuous at $w$.</li>
<li><em>Conclude.</em> The left side of step 1 does not depend on $\delta$, and the right side tends to $2\pi i\,f(w)$. So the left side equals $2\pi i\,f(w)$. <span class="qed">∎</span></li>
</ol>
:::
<p>A holomorphic function on a disk is therefore determined by its values on the boundary circle. With $w=z_0$ and $z=z_0+re^{i\theta}$, the formula reads $f(z_0)=\frac1{2\pi}\int_0^{2\pi}f(z_0+re^{i\theta})\,d\theta$: the mean value property, @thm:mean-value-property, for the real and imaginary parts at once.</p>
