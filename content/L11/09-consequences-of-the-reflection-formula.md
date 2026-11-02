---
id: m9
slide: Slide 10
title: Consequences of the reflection formula
---

::: corollary {#cor:the-value-at-frac12-and-the name="the value at $\frac12$, and the Gaussian integral"}
$\Gamma(\frac12)=\sqrt\pi$, and $\displaystyle\int_{-\infty}^\infty e^{-u^2}du=\sqrt\pi$, $\displaystyle\int_{-\infty}^\infty e^{-\pi x^2}dx=1$.
:::
::: proof
With $z=\frac12$ the reflection formula gives $\Gamma(\frac12)^2=\frac\pi{\sin(\pi/2)}=\pi$. Also $\Gamma(\frac12)=\int_0^\infty t^{-1/2}e^{-t}dt\gt0$, so $\Gamma(\frac12)=\sqrt\pi$. Substituting $t=u^2$, $dt=2u\,du$:
\[ \sqrt\pi=\int_0^\infty\frac{e^{-u^2}}{u}\,2u\,du=2\int_0^\infty e^{-u^2}du=\int_{-\infty}^\infty e^{-u^2}du. \]
Finally substitute $u=\sqrt\pi\,x$: $\int e^{-\pi x^2}dx=\frac1{\sqrt\pi}\int e^{-u^2}du=1$.
:::
<p>These are the facts used in @prop:the-gaussian-is-its-own-transform and @prop:the-major-arc.</p>

::: corollary {#cor:on-the-line-operatorname-re-z name="on the line $\operatorname{Re}z=\frac12$"}
For real $y$,
\[ \Big|\Gamma\Big(\frac12+iy\Big)\Big|^2=\frac\pi{\cosh\pi y},\qquad\text{so}\qquad\Big|\Gamma\Big(\frac12+iy\Big)\Big|\sim\sqrt{2\pi}\,e^{-\pi|y|/2}\quad(|y|\to\infty). \]
:::
::: proof

<ol>
<li><em>Conjugate symmetry.</em> For $\operatorname{Re}z\gt0$, $\Gamma(\bar z)=\overline{\Gamma(z)}$: conjugate the integrand, using $\overline{t^{z-1}}=\overline{e^{(z-1)\log t}}=e^{(\bar z-1)\log t}=t^{\bar z-1}$ for real $t\gt0$.</li>
<li>For $z=\frac12+iy$: $1-z=\frac12-iy=\bar z$, and $\sin(\frac\pi2+i\pi y)=\cos(i\pi y)=\cosh\pi y$. So
\[ \Big|\Gamma\Big(\frac12+iy\Big)\Big|^2=\Gamma(z)\,\overline{\Gamma(z)}=\Gamma(z)\Gamma(\bar z)=\Gamma(z)\Gamma(1-z)=\frac\pi{\sin\pi z}=\frac\pi{\cosh\pi y}. \]</li>
<li>As $|y|\to\infty$, $\cosh\pi y=\frac12e^{\pi|y|}(1+e^{-2\pi|y|})\sim\frac12e^{\pi|y|}$, so $|\Gamma|^2\sim2\pi e^{-\pi|y|}$. Take square roots. <span class="qed">∎</span></li>
</ol>
:::
<p>So $\Gamma$ decays exponentially along vertical lines, unlike its factorial growth along the real axis. This kind of estimate is what makes $\Gamma$ useful in the theory of the Riemann zeta function.</p>
