---
id: j3
slide: Slide 4
title: $\log|f|$ after factoring out the zeros
---
<p>With $f=(z-a_1)\cdots(z-a_N)\,g$ as in @prop:factorization-in-a-disk, off the zeros,
\[ \log|f(z)|=\sum_{j=1}^N\log|z-a_j|+\log|g(z)|. \]
In the language of Part I, $\log|f|$ is the potential of unit point charges at the zeros (each $\log|z-a_j|$ is a [logarithmic potential](apx:E6)), plus a harmonic function:</p>

::: lemma {#lem:if-is-holomorphic-and-zero}
If $g$ is holomorphic and zero-free near $|z|\le R$, then $\log|g|$ is harmonic near $|z|\le R$.
:::
::: proof

<ol>
<li><em>A slightly bigger disk.</em> The open set where $g$ is holomorphic and zero-free contains the compact disk $|z|\le R$, hence a disk $|z|\lt R'$ with $R'\gt R$ ([C.5](apx:C5)(a)).</li>
<li><em>A primitive of $g'/g$.</em> $g'/g$ is holomorphic on $|z|\lt R'$. By @thm:power-series (applied on every closed disk $|z|\le r$, $r\lt R'$; the coefficients do not depend on $r$, by @thm:cauchys-formula-for-derivatives) it is a power series $\sum_nc_nz^n$ converging on $|z|\lt R'$. Then $G(z):=\sum_n\frac{c_n}{n+1}z^{n+1}$ converges on the same disk and $G'=g'/g$ ([power series](apx:A19) may be differentiated term by term). The slide phrases this as "Cauchy's theorem on a disk"; either way, a holomorphic function on a disk has a primitive there.</li>
<li><em>$g$ is an exponential.</em>
\[ (ge^{-G})'=g'e^{-G}-gG'e^{-G}=e^{-G}(g'-g\cdot g'/g)=0. \]
A holomorphic function with zero derivative on a connected open set is constant (its real and imaginary parts have zero gradient, by @thm:cauchy-riemann). So $g=c\,e^G$, and $c\ne0$ as $g\ne0$.</li>
<li><em>Take $\log|\cdot|$.</em> $|g|=|c|\,e^{\operatorname{Re}G}$, so $\log|g|=\log|c|+\operatorname{Re}G$, the real part of a holomorphic function plus a constant: harmonic, by @cor:holomorphic-functions-are-smooth. <span class="qed">∎</span></li>
</ol>
:::
