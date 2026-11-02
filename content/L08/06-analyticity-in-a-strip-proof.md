---
id: h6
slide: Slide 7
title: 'Analyticity in a strip: proof'
---
::: proof {title="Proof of Theorem [#](=thm:strips-and-decay)(a)."}
Let $\xi\ge0$ and $0\lt b\lt a$.
<ol>
<li><em>Shift the line down by $b$.</em> The function $f(z)e^{-2\pi iz\xi}$ is holomorphic near the rectangle with corners $\pm R$, $\pm R-ib$ (it lies in the strip, as $b\lt a$). On its vertical sides, $|e^{-2\pi iz\xi}|=e^{2\pi\xi\operatorname{Im}z}\le1$ (since $\operatorname{Im}z\le0$) and $|f|\le\frac C{1+R^2}$, over a length $b$. So the vertical sides contribute at most $\frac{2bC}{1+R^2}\to0$, and Cauchy's theorem (@prop:other-contours) with $R\to\infty$ gives
\[ \class{ntn-hat}{\hat f}(\xi)=\int_{-\infty}^\infty f(x-ib)\,e^{-2\pi i(x-ib)\xi}\,dx=e^{-2\pi b\xi}\int_{-\infty}^\infty f(x-ib)\,e^{-2\pi ix\xi}\,dx, \]
using $e^{-2\pi i(-ib)\xi}=e^{-2\pi b\xi}$. Both integrals converge absolutely, since $|f(x-ib)|\le\frac C{1+x^2}$.</li>
<li><em>Estimate.</em> $|\class{ntn-hat}{\hat f}(\xi)|\le e^{-2\pi b\xi}\int\frac{C\,dx}{1+x^2}=\pi C\,e^{-2\pi b\xi}$ (@prop:x).</li>
<li><em>Let $b\to a$.</em> The bound holds for every $b\lt a$, hence for $b=a$. For $\xi\lt0$, shift up instead. <span class="qed">∎</span></li>
</ol>
:::

::: proof {title="Proof of Theorem [#](=thm:strips-and-decay)(b)."}
Let $0\lt b\lt a$, and define $F(z):=\int_{-\infty}^\infty\class{ntn-hat}{\hat f}(\xi)\,e^{2\pi iz\xi}\,d\xi$ for $|\operatorname{Im}z|\lt b$.
<ol>
<li><em>Domination.</em> For $z=x+iy$ with $|y|\lt b$: $|e^{2\pi iz\xi}|=e^{-2\pi y\xi}\le e^{2\pi b|\xi|}$. So the integrand is at most $Ce^{-2\pi(a-b)|\xi|}$, and its $z$-derivative $2\pi i\xi\,\class{ntn-hat}{\hat f}(\xi)e^{2\pi iz\xi}$ is at most $2\pi C|\xi|e^{-2\pi(a-b)|\xi|}$. Both bounds are integrable in $\xi$ and do not depend on $z$.</li>
<li><em>$F$ is holomorphic.</em> By [differentiation under the integral sign](apx:A4) (version 3), $F$ has continuous partial derivatives $F_x=\int2\pi i\xi\,\class{ntn-hat}{\hat f}e^{2\pi iz\xi}d\xi$ and $F_y=iF_x$, which are the Cauchy–Riemann equations; so $F$ is holomorphic on $|\operatorname{Im}z|\lt b$ (@thm:cauchy-riemann). As $b\lt a$ was arbitrary, on $|\operatorname{Im}z|\lt a$.</li>
<li><em>$F$ extends $f$.</em> $\class{ntn-hat}{\hat f}$ is continuous ([A.22](apx:A22)) and integrable (by the hypothesis), and so is $f$. By Fourier inversion (@fact:fourier-inversion), $F(x)=\int\class{ntn-hat}{\hat f}(\xi)e^{2\pi ix\xi}d\xi=f(x)$ for real $x$. <span class="qed">∎</span></li>
</ol>
:::
