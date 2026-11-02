---
id: h12
slide: Slide 13
title: 'The sampling theorem: proof'
---
::: proof {title="Proof of Theorem [#](=thm:whittaker-kotelnikov-shannon), Step 1: $f$ is entire, summable at the integers, and $\class{ntn-hat}{\hat f}=g$."}
Define $f(z):=\int_{-1/2}^{1/2}g(\xi)e^{2\pi iz\xi}d\xi$ for all $z\in\mathbb C$; this is $\class{ntn-hat}{\hat g}(-z)$. By Paley–Wiener (a) with $A=\frac12$, it is entire and
\[ (1+|z|^2)\,|f(z)|\le C\,e^{\pi|\operatorname{Im}z|}. \]
On $\R$ this gives $|f(x)|\le\frac{C}{1+x^2}$. Hence $\sum_n|f(n)|\le\sum_n\frac C{1+n^2}\lt\infty$, $f$ is integrable on $\R$, and since $f$ and $g$ are continuous and integrable, Fourier inversion (@fact:fourier-inversion, second form) gives $\class{ntn-hat}{\hat f}=g$.
:::

::: proof {title="Step 2: for $|\xi|\lt\frac12$, $\ \sum_nf(n)e^{-2\pi in\xi}=g(\xi)$."}
Fix such $\xi$ and let $F(z):=f(z)\,e^{-2\pi iz\xi}$.
<ol>
<li><em>$F$ meets the hypotheses of Poisson summation with $a=1$.</em> $F$ is entire. As $|\xi|\lt\frac12$, $|e^{-2\pi iz\xi}|=e^{2\pi\xi\operatorname{Im}z}\le e^{\pi|\operatorname{Im}z|}$. With Step 1 and $|z|^2\ge x^2$, for $|y|\lt1$:
\[ |F(x+iy)|\le\frac{Ce^{\pi|y|}e^{\pi|y|}}{1+|z|^2}\le\frac{Ce^{2\pi}}{1+x^2}. \]</li>
<li><em>Its transform.</em>
\[ \class{ntn-hat}{\hat F}(m)=\int f(x)e^{-2\pi ix\xi}e^{-2\pi ixm}dx=\class{ntn-hat}{\hat f}(m+\xi)=g(m+\xi). \]
For $m\ne0$, $|m+\xi|\ge|m|-|\xi|\gt1-\frac12=\frac12$, so $g(m+\xi)=0$. Only $\class{ntn-hat}{\hat F}(0)=g(\xi)$ survives.</li>
<li><em>Poisson summation</em> (@thm:poisson-summation):
\[ \sum_nf(n)e^{-2\pi in\xi}=\sum_nF(n)=\sum_m\class{ntn-hat}{\hat F}(m)=g(\xi). \]
<span class="qed">∎</span></li>
</ol>
:::
<p>Step 2 says that $g$ (restricted to $(-\frac12,\frac12)$) is the Fourier series whose coefficients are the samples $f(n)$. This is where the band limit is used: if $g$ were nonzero beyond $\pm\frac12$, other terms $g(m+\xi)$ would survive and mix into the sum (@sec:h14).</p>
