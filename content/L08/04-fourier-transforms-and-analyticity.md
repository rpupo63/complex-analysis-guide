---
id: h4
slide: Slide 5
title: Fourier transforms and analyticity
---

::: definition {#def:sinc name=sinc}
$\class{ntn-sinc}{\operatorname{sinc}}\xi:=\dfrac{\sin\pi\xi}{\pi\xi}$ for $\xi\ne0$, and $\class{ntn-sinc}{\operatorname{sinc}}0:=1$.
:::
<p>sinc is continuous (since $\sin\pi\xi/\pi\xi\to1$), entire (its power series $\sum_k(-1)^k(\pi\xi)^{2k}/(2k+1)!$ converges everywhere), and $|\class{ntn-sinc}{\operatorname{sinc}}\xi|\le1$ on $\R$ (as $|\sin x|\le|x|$). Its zeros are the nonzero integers.</p>

::: lemma {#lem:the-box name="the box"}
$\displaystyle\int_{-1/2}^{1/2}e^{-2\pi ix\xi}\,dx=\class{ntn-sinc}{\operatorname{sinc}}\xi$; that is, $\widehat{\mathbf 1_{[-1/2,1/2]}}=\class{ntn-sinc}{\operatorname{sinc}}$. Since sinc is even, also $\int_{-1/2}^{1/2}e^{2\pi ix\xi}dx=\class{ntn-sinc}{\operatorname{sinc}}\xi$.
:::
::: proof
For $\xi=0$ the integral is $1$. For $\xi\ne0$,
\[ \int_{-1/2}^{1/2}e^{-2\pi ix\xi}dx=\Big[\frac{e^{-2\pi ix\xi}}{-2\pi i\xi}\Big]_{-1/2}^{1/2}=\frac{e^{-\pi i\xi}-e^{\pi i\xi}}{-2\pi i\xi}=\frac{-2i\sin\pi\xi}{-2\pi i\xi}=\frac{\sin\pi\xi}{\pi\xi}. \]
<span class="qed">∎</span>
:::

<p>Three transforms side by side ($\mathbf 1_{[-1/2,1/2]}$ is $1$ on that interval and $0$ outside):</p>
<div class="tbl"><table>
<thead><tr><th>$f(x)$</th><th>$\class{ntn-hat}{\hat f}(\xi)$</th><th>Largest strip where $f$ is holomorphic</th><th>Where</th></tr></thead>
<tbody>
<tr><td>$e^{-\pi x^2}$</td><td>$e^{-\pi\xi^2}$</td><td>$\mathbb C$</td><td>@prop:the-gaussian-is-its-own-transform</td></tr>
<tr><td>$\dfrac1{1+x^2}$</td><td>$\pi e^{-2\pi|\xi|}$</td><td>$|\operatorname{Im}z|\lt1$ (poles at $\pm i$)</td><td>@prop:for</td></tr>
<tr><td>$\mathbf 1_{[-1/2,1/2]}(x)$</td><td>$\class{ntn-sinc}{\operatorname{sinc}}\xi$</td><td>none: $f$ jumps at $\pm\frac12$</td><td>@lem:the-box</td></tr>
</tbody></table></div>
<p>The pattern: <b>the wider the strip where $f$ is holomorphic, the faster $\class{ntn-hat}{\hat f}$ decays.</b> Entire: faster than any exponential. Strip of half-width $1$: like $e^{-2\pi|\xi|}$. Not even continuous: like $1/|\xi|$. And in the other direction, <b>if $f$ vanishes outside a bounded interval, $\class{ntn-hat}{\hat f}$ is entire</b> (sinc is). The next two theorems make both statements precise.</p>
