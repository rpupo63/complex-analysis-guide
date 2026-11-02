---
id: f6
slide: Slide 7
title: Derivatives of all orders
---

::: theorem {#thm:cauchys-formula-for-derivatives name="Cauchy's formula for derivatives"}
Let $f$ be holomorphic near $|z-z_0|\le r$, and $|w-z_0|\lt r$. Then $f$ has complex derivatives of all orders at $w$, and
\[ f^{(n)}(w)=\frac{n!}{2\pi i}\oint_{|z-z_0|=r}\frac{f(z)}{(z-w)^{n+1}}\,dz\qquad(n\ge0). \]
In particular $a_n=f^{(n)}(z_0)/n!$ (take $w=z_0$).
:::
<p>The slide's justification is "differentiate Cauchy's formula $n$ times in $w$ under the integral sign; the difference quotients of $(z-w)^{-k}$ converge uniformly for $|z-z_0|=r$". Here is that argument in full.</p>
::: proof
By induction on $n$. The case $n=0$ is @thm:cauchys-integral-formula. Assume the formula for some $n$ and every $w$ in the open disk, and put $k:=n+1$.
<ol>
<li><em>The kernel's difference quotient.</em> Fix $w$ and let $\delta:=r-|w-z_0|\gt0$. For $|z-z_0|=r$ write $a:=z-w$, so $|a|\ge\delta$. For $|h|\le\delta/2$ let $\phi(h):=(a-h)^{-k}$; along the segment from $0$ to $h$, $|a-sh|\ge\delta/2$, and $\phi'(h)=k(a-h)^{-k-1}$, $\phi''(h)=k(k+1)(a-h)^{-k-2}$. Using $\frac{d}{ds}\phi(sh)=h\,\phi'(sh)$ twice (the [fundamental theorem of calculus](apx:A9) along the segment),
\[ \phi(h)-\phi(0)-h\phi'(0)=\int_0^1h\big(\phi'(sh)-\phi'(0)\big)\,ds=\int_0^1\!\!\int_0^1h^2s\,\phi''(tsh)\,dt\,ds, \]
so
\[ \Big|\frac{(z-w-h)^{-k}-(z-w)^{-k}}{h}-k(z-w)^{-k-1}\Big|\le\frac{|h|}2\,k(k+1)\Big(\frac\delta2\Big)^{-k-2}. \]
The bound does not depend on $z$: the difference quotients converge [uniformly](apx:A17) on the circle.</li>
<li><em>Pass it through the integral.</em> By the induction hypothesis,
\[ \frac{f^{(n)}(w+h)-f^{(n)}(w)}{h}-\frac{n!}{2\pi i}\oint\frac{k\,f(z)}{(z-w)^{k+1}}\,dz=\frac{n!}{2\pi i}\oint f(z)\Big[\frac{(z-w-h)^{-k}-(z-w)^{-k}}{h}-k(z-w)^{-k-1}\Big]dz, \]
whose modulus is at most $n!\,r\,M\cdot\frac{|h|}{2}k(k+1)(\delta/2)^{-k-2}\to0$ as $h\to0$ (ML estimate, $M=\max|f|$ on the circle).</li>
<li>So $f^{(n+1)}(w)$ exists and equals $\frac{n!\,k}{2\pi i}\oint\frac{f(z)}{(z-w)^{k+1}}dz=\frac{(n+1)!}{2\pi i}\oint\frac{f(z)}{(z-w)^{n+2}}dz$.</li>
</ol>
For the last claim, compare with @thm:power-series at $w=z_0$: $\frac{f^{(n)}(z_0)}{n!}=\frac1{2\pi i}\oint f(z)(z-z_0)^{-n-1}dz=a_n$.
:::

::: corollary {#cor:holomorphic-functions-are-smooth name="holomorphic functions are smooth"}
If $f=u+iv$ is holomorphic with $C^1$ parts on an open set $\Omega$, then $f'$ is holomorphic on $\Omega$, $u$ and $v$ are $C^\infty$, and $u$, $v$ are harmonic. So Standing @asm:from-now-on-holomorphic-functions holds automatically.
:::
::: proof
Each point of $\Omega$ is the centre of a closed disk inside $\Omega$, and @thm:cauchys-formula-for-derivatives applies there: every $f^{(n)}$ exists, so each is holomorphic, hence continuous. By @thm:cauchy-riemann, $u_x+iv_x=f'$ and $u_y+iv_y=if'$; repeating, every partial derivative of $u$ or $v$ of order $k$ is the real or imaginary part of $i^jf^{(k)}$ for some $j$, hence continuous. So $u,v\in C^\infty$, and @prop:if-satisfy-the-cauchy-riemann makes them harmonic.
:::
<p>Contrast with real analysis: a differentiable function of a real variable need not have a second derivative. Here one complex derivative (with continuous parts) gives all of them.</p>
