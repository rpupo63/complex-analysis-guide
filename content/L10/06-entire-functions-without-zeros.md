---
id: k6
slide: Slide 7
title: Entire functions without zeros
---
<p>A product with the right zeros determines $f$ only up to a factor without zeros. This lemma pins such factors down by their growth.</p>

::: lemma {#lem:no-zeros name="no zeros"}
Let $F$ be entire with no zeros, and $\class{ntn-Ar}{A}(r):=\max_{|z|=r}\log|F(z)|$. Then $F=e^G$ with $G(z)=\sum_nc_nz^n$ entire, and
\[ |c_n|\,r^n\le2\class{ntn-Ar}{A}(r)-2\log|F(0)|\qquad\text{for all }r\gt0,\ n\ge1. \]
If $\class{ntn-Ar}{A}(r_j)\le\varepsilon_jr_j^{k+1}$ with $r_j\to\infty$ and $\varepsilon_j\to0$, then $G$ is a polynomial of degree $\le k$.
:::
::: proof

<ol>
<li><em>$F=e^G$.</em> $F'/F$ is entire (as $F\ne0$), so it is a power series converging on all of $\mathbb C$ (@thm:power-series on every disk); integrating term by term gives an entire primitive $G$ ([A.19](apx:A19)). Adjust the constant so that $e^{G(0)}=F(0)$ (choose $G(0)$ to be any logarithm of $F(0)\ne0$). Then $(Fe^{-G})'=e^{-G}(F'-FG')=0$, so $Fe^{-G}$ is constant, equal to its value $1$ at $0$.</li>
<li><em>A nonnegative function on the circle.</em> $|F|=e^{\operatorname{Re}G}$, so $\operatorname{Re}G=\log|F|$. Fix $r$; then $\varphi(\theta):=\class{ntn-Ar}{A}(r)-\operatorname{Re}G(re^{i\theta})\ge0$, by definition of $\class{ntn-Ar}{A}(r)$ as a maximum.</li>
<li><em>Fourier coefficients of $\operatorname{Re}G$.</em> Since $\operatorname{Re}w=\frac12(w+\bar w)$,
\[ \operatorname{Re}G(re^{i\theta})=\operatorname{Re}c_0+\tfrac12\sum_{n\ge1}\big(c_nr^ne^{in\theta}+\bar c_nr^ne^{-in\theta}\big), \]
uniformly convergent in $\theta$ (power series converge uniformly on circles inside their disk, [A.19](apx:A19)). Multiply by $e^{-in\theta}$ ($n\ge1$) and integrate term by term: $\int_0^{2\pi}e^{ik\theta}e^{-in\theta}d\theta$ is $2\pi$ for $k=n$ and $0$ otherwise, and the terms $\bar c_ke^{-ik\theta}e^{-in\theta}$ ($k\ge1$) and the constant all integrate to $0$. So $\int_0^{2\pi}\operatorname{Re}G(re^{i\theta})e^{-in\theta}d\theta=\pi c_nr^n$, and similarly $\int_0^{2\pi}\operatorname{Re}G\,d\theta=2\pi\operatorname{Re}c_0$.</li>
<li><em>Estimate.</em> As $\int_0^{2\pi}\class{ntn-Ar}{A}(r)e^{-in\theta}d\theta=0$,
\[ \pi|c_n|r^n=\Big|\int_0^{2\pi}\varphi(\theta)e^{-in\theta}d\theta\Big|\le\int_0^{2\pi}\varphi(\theta)\,d\theta=2\pi\big(\class{ntn-Ar}{A}(r)-\operatorname{Re}c_0\big), \]
where $\varphi\ge0$ was used to drop the absolute value. Finally $\operatorname{Re}c_0=\operatorname{Re}G(0)=\log|F(0)|$.</li>
<li><em>Polynomial.</em> For $n\gt k$, i.e. $n\ge k+1$, and $r_j\ge1$:
\[ |c_n|\le2r_j^{-n}\big(\varepsilon_jr_j^{k+1}-\log|F(0)|\big)\le2\varepsilon_j+2r_j^{-n}\big|\log|F(0)|\big|\longrightarrow0. \]
So $c_n=0$ for all $n\gt k$. <span class="qed">∎</span></li>
</ol>
:::
<p>The key idea is step 4: a bound on $\operatorname{Re}G$ from <em>above only</em> controls all of $G$, because $\varphi\ge0$ turns the absolute value of an integral into an integral. With $k=0$ it says a zero-free entire function with $\log|F|=o(r)$ along a sequence of circles is constant.</p>
