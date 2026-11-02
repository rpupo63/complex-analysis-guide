---
id: k8
slide: Slide 9
title: 'Euler''s sine product: growth on circles'
---
::: proof {title="Step 2: on $|z|=r:=N+\frac12$ $(N=0,1,2,\dots)$, $\ \log|f(z)|\le O(r\log r)$."}

<ol>
<li><em>$z$ stays away from the integers.</em> For $n\in\mathbb Z$, $|z-n|\ge\big||z|-|n|\big|=|r-|n||\ge\frac12$, as $r$ is a half-integer.</li>
<li><em>Factors with $1\le n\le2r$</em> (at most $2r$ of them): $\big|1-\frac{z^2}{n^2}\big|=\frac{|n-z|\,|n+z|}{n^2}\ge\frac{1/4}{n^2}\ge\frac1{16r^2}$.</li>
<li><em>Factors with $n\gt2r$:</em> $\frac{r^2}{n^2}\le\frac14\le\frac12$, so by the inequality of @sec:k5, $\big|1-\frac{z^2}{n^2}\big|\ge1-\frac{r^2}{n^2}\ge e^{-2r^2/n^2}$.</li>
<li><em>Lower bound for $|\class{ntn-Ps}{P}|$.</em> $\sum_{n\gt2r}\frac{2r^2}{n^2}\le2r^2\int_{2r}^\infty\frac{dt}{t^2}=r$ (the sum starts at $n=2r+1$, as $2r=2N+1$ is an integer, and $\frac1{n^2}\le\int_{n-1}^n\frac{dt}{t^2}$), and $|\pi z|=\pi r\gt1$. So
\[ \log|\class{ntn-Ps}{P}(z)|\ge\log(\pi r)-2r\log(16r^2)-r\ge-2r\log(16r^2)-r. \]</li>
<li><em>Upper bound for $|\sin|$.</em> $|\sin w|=\frac12|e^{iw}-e^{-iw}|\le e^{|w|}$, so $\log|\sin\pi z|\le\pi r$.</li>
<li>So
\[ \log|f|=\log|\sin\pi z|-\log|\class{ntn-Ps}{P}|\le\pi r+2r\log(16r^2)+O(r)=O(r\log r). \]
<span class="qed">∎</span></li>
</ol>
:::

::: proof {title="Step 3: $f\equiv1$."}
By Step 2, $\class{ntn-Ar}{A}(r)=\max_{|z|=r}\log|f|\le Cr\log r$ on the circles $r_j=j+\frac12$. As $r\log r=o(r^2)$, take $\varepsilon_j:=C\log r_j/r_j\to0$: the no-zeros lemma with $k=1$ shows $G(z)=a+bz$. As $f$ is even, $e^{a+bz}=e^{a-bz}$, so $e^{2bz}=1$ for all $z$; differentiating at $0$ gives $2b=0$. As $f(0)=1$, $e^a=1$. So $f\equiv1$, i.e. $\sin\pi z=\class{ntn-Ps}{P}(z)$.
:::
<p>Notice why the circles were chosen with half-integer radii: on them $|\sin\pi z|$ is not small and the factors of $\class{ntn-Ps}{P}$ are not small, so the ratio can be controlled. And the no-zeros lemma only needs control on <em>some</em> sequence of circles.</p>
<p>A first dividend: comparing the coefficients of $z^2$ on both sides of $\frac{\sin\pi z}{\pi z}=\prod(1-\frac{z^2}{n^2})$ gives $\sum1/n^2=\pi^2/6$, the [Basel sum](apx:E18) used in @lem:on-the-real-axis.</p>
