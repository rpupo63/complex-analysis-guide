---
id: h16
slide: Slide 17
title: Exercises
---
<p>The slide lists five exercises with answers. Full solutions are below; try each one first.</p>

::: exercise {#ex:a-double-pole name="a double pole"}
Show $\displaystyle\int_{-\infty}^\infty\frac{dx}{(1+x^2)^2}=\frac\pi2$.
<details class="sol"><summary>Solution</summary>
<p>Close in the upper half-plane as in @sec:h1. Now $\frac1{(1+z^2)^2}=\frac{h(z)}{(z-i)^2}$ with $h(z)=(z+i)^{-2}$, a pole of order $2$ at $i$, so the residue is $h'(i)=-2(z+i)^{-3}\big|_{z=i}=\frac{-2}{(2i)^3}=\frac{-2}{-8i}=\frac1{4i}$ (@def:residue). The arc is at most $\frac{\pi R}{(R^2-1)^2}\to0$. So the integral is $2\pi i\cdot\frac1{4i}=\frac\pi2$.</p></details>
:::

::: exercise {#ex:show-hint-solution-as-runs}
Show $\displaystyle\int_0^{2\pi}\frac{d\theta}{2+\cos\theta}=\frac{2\pi}{\sqrt3}$. Hint: $z=e^{i\theta}$, $d\theta=\frac{dz}{iz}$.
<details class="sol"><summary>Solution</summary>
<p>As $\theta$ runs over $[0,2\pi]$, $z=e^{i\theta}$ runs once around $|z|=1$, with $\cos\theta=\frac12(z+z^{-1})$ and $d\theta=\frac{dz}{iz}$. So
\[ \int_0^{2\pi}\frac{d\theta}{2+\cos\theta}=\oint_{|z|=1}\frac{1}{2+\frac12(z+z^{-1})}\cdot\frac{dz}{iz}=\oint_{|z|=1}\frac{2\,dz}{i(z^2+4z+1)}. \]
The roots of $z^2+4z+1$ are $-2\pm\sqrt3$; only $z_1=-2+\sqrt3\approx-0.27$ is inside. It is a simple pole with residue $\frac{2}{i(z_1-z_2)}=\frac2{i\cdot2\sqrt3}=\frac1{i\sqrt3}$. The integral is $2\pi i\cdot\frac1{i\sqrt3}=\frac{2\pi}{\sqrt3}$.</p></details>
:::

::: exercise {#ex:a-sector name="a sector"}
Show $\displaystyle\int_0^\infty\frac{dx}{1+x^3}=\frac{2\pi}{3\sqrt3}$, using the sector $0\le\arg z\le\frac{2\pi}3$.
<details class="sol"><summary>Solution</summary>
<p>Let $\omega:=e^{2\pi i/3}$, so $\omega^3=1$. The sector of radius $R$ has three sides: $[0,R]$; the arc; and the ray from $R\omega$ back to $0$. On the ray $z=r\omega$, $z^3=r^3$ and $dz=\omega\,dr$, so that side contributes $-\omega\int_0^R\frac{dr}{1+r^3}$. The arc has length $\frac{2\pi R}3$ and $|1+z^3|\ge R^3-1$, so it vanishes as $R\to\infty$. The only pole inside is $\alpha:=e^{i\pi/3}$ (a root of $z^3=-1$), with residue $\frac1{3\alpha^2}=\frac{\alpha}{3\alpha^3}=-\frac\alpha3$ (@prop:simple-poles-of-a-quotient). Writing $I$ for the integral, as $R\to\infty$:
\[ (1-\omega)I=2\pi i\Big(-\frac\alpha3\Big). \]
Now $1-\omega=\alpha(\bar\alpha-\alpha)=\alpha\cdot(-2i\sin\frac\pi3)=-i\sqrt3\,\alpha$, using $\alpha^2=\omega$. So $I=\frac{-2\pi i\alpha/3}{-i\sqrt3\,\alpha}=\frac{2\pi}{3\sqrt3}$.</p></details>
:::

::: exercise {#ex:show-that-has-solution-for}
Show that $f(x)=(1+x^2)^{-2}$ has $\class{ntn-hat}{\hat f}(\xi)=\frac\pi2\big(1+2\pi|\xi|\big)e^{-2\pi|\xi|}$.
<details class="sol"><summary>Solution</summary>
<p>For $\xi\ge0$ close in the lower half-plane, clockwise, as in @prop:for: $\class{ntn-hat}{\hat f}(\xi)=-2\pi i\class{ntn-res}{\operatorname{Res}}_{-i}$. Write the integrand as $\frac{k(z)}{(z+i)^2}$ with $k(z)=\frac{e^{-2\pi iz\xi}}{(z-i)^2}$; the residue is $k'(-i)$. Now
\[ k'(z)=e^{-2\pi iz\xi}\Big(\frac{-2\pi i\xi}{(z-i)^2}-\frac{2}{(z-i)^3}\Big), \]
and at $z=-i$: $e^{-2\pi iz\xi}=e^{-2\pi\xi}$, $(z-i)^2=-4$, $(z-i)^3=8i$. So $k'(-i)=e^{-2\pi\xi}\big(\frac{\pi i\xi}2+\frac{i}4\big)=ie^{-2\pi\xi}\big(\frac{\pi\xi}2+\frac14\big)$, and $\class{ntn-hat}{\hat f}(\xi)=-2\pi i\cdot ie^{-2\pi\xi}\big(\frac{\pi\xi}2+\frac14\big)=\frac\pi2(1+2\pi\xi)e^{-2\pi\xi}$. By symmetry ($f$ is even, so $\class{ntn-hat}{\hat f}$ is even) the formula holds with $|\xi|$. Check: $\class{ntn-hat}{\hat f}(0)=\frac\pi2=\int f$, matching @ex:a-double-pole.</p></details>
:::

::: exercise {#ex:find-for-the-triangle-is}
Find $\class{ntn-hat}{\hat f}$ for the triangle $f(x)=\max(0,1-|x|)$. Is $\class{ntn-sinc}{\operatorname{sinc}}^2$ band-limited?
<details class="sol"><summary>Solution</summary>
<p>$f$ is even and vanishes outside $[-1,1]$, so $\class{ntn-hat}{\hat f}(\xi)=2\int_0^1(1-x)\cos(2\pi x\xi)\,dx$. For $\xi\ne0$, integrating by parts (the boundary term $\big[(1-x)\frac{\sin2\pi x\xi}{2\pi\xi}\big]_0^1$ vanishes),
\[ \class{ntn-hat}{\hat f}(\xi)=2\int_0^1\frac{\sin2\pi x\xi}{2\pi\xi}\,dx=\frac{1-\cos2\pi\xi}{2\pi^2\xi^2}=\frac{2\sin^2\pi\xi}{2\pi^2\xi^2}=\class{ntn-sinc}{\operatorname{sinc}}^2\xi, \]
and $\class{ntn-hat}{\hat f}(0)=\int f=1=\class{ntn-sinc}{\operatorname{sinc}}^20$. Both $f$ and $\class{ntn-sinc}{\operatorname{sinc}}^2$ are continuous and integrable, so Fourier inversion gives $f(x)=\int\class{ntn-sinc}{\operatorname{sinc}}^2(\xi)e^{2\pi ix\xi}d\xi$; that is, the transform of $\class{ntn-sinc}{\operatorname{sinc}}^2$ is $f(-x)=f(x)$, which vanishes outside $[-1,1]$. So yes: $\class{ntn-sinc}{\operatorname{sinc}}^2$ is band-limited, to $[-1,1]$. (Consistent with @cor:if-is-continuous-and-time: $\class{ntn-sinc}{\operatorname{sinc}}^2$ is not time-limited.)</p></details>
:::
