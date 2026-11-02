---
id: h3
slide: Slide 4
title: 'Shifting the line: the Gaussian'
---
<p>A second technique: no poles at all, but the line of integration is moved.</p>

::: proposition {#prop:the-gaussian-is-its-own-transform name="the Gaussian is its own transform"}
For every $\xi\in\R$,
\[ \int_{-\infty}^\infty e^{-\pi x^2}e^{-2\pi ix\xi}\,dx=e^{-\pi\xi^2}. \]
:::
<p>We use $\int_{-\infty}^\infty e^{-\pi x^2}dx=1$: this is the Gaussian integral, proved in @sec:m9 (substitute $u=\sqrt\pi\,x$ in $\int e^{-u^2}du=\sqrt\pi$; or see [polar coordinates](apx:A8)).</p>
<figure>{{fig:h3-1}}<figcaption>@sec:h3: Cauchy's theorem on the rectangle with corners $\pm R$, $\pm R+i\xi$. The vertical sides contribute nothing as $R\to\infty$.</figcaption></figure>
::: proof

<ol>
<li><em>Complete the square.</em>
\[ -\pi x^2-2\pi ix\xi=-\pi(x^2+2ix\xi-\xi^2)-\pi\xi^2=-\pi(x+i\xi)^2-\pi\xi^2. \]
So the claim is $\int_{-\infty}^\infty e^{-\pi(x+i\xi)^2}dx=1$: the integral of the entire function $e^{-\pi z^2}$ along the horizontal line $\operatorname{Im}z=\xi$ equals its integral along $\R$.</li>
<li><em>Cauchy on a rectangle.</em> Take $\xi\gt0$ (for $\xi\lt0$ use the mirror rectangle below the axis; $\xi=0$ is the known integral). By @prop:other-contours, the integral of $e^{-\pi z^2}$ around the rectangle with corners $\pm R$, $\pm R+i\xi$ is $0$:
\[ \int_{-R}^Re^{-\pi x^2}dx+\int_{\text{right}}-\int_{-R}^Re^{-\pi(x+i\xi)^2}dx-\int_{\text{left}}=0, \]
the top side being traversed from right to left.</li>
<li><em>The vertical sides vanish.</em> On them $z=\pm R+iy$ with $0\le y\le\xi$, and $\operatorname{Re}\big((\pm R+iy)^2\big)=R^2-y^2$, so $|e^{-\pi z^2}|=e^{-\pi(R^2-y^2)}\le e^{-\pi(R^2-\xi^2)}$. Each side has length $\xi$, so each integral is at most $\xi e^{-\pi(R^2-\xi^2)}\to0$.</li>
<li>Letting $R\to\infty$ (both horizontal integrals converge absolutely, as $|e^{-\pi(x+i\xi)^2}|=e^{-\pi(x^2-\xi^2)}$), the two horizontal integrals are equal. <span class="qed">∎</span></li>
</ol>
:::
