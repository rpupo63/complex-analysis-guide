---
id: f10
slide: Slide 11
title: Postage stamps
---
<p>The rest of the lecture turns the residue theorem into a counting machine. A counting problem is encoded in a power series (a <em>generating function</em>); the count is a Taylor coefficient, which Cauchy's formula writes as a contour integral; the integral is evaluated by residues or estimated.</p>

::: definition {#def:stamp-counts name="stamp counts"}
Let $a,b\ge1$ be coprime integers. The number of ways to pay $n$ cents with $a$-cent and $b$-cent stamps is
\[ \class{ntn-cn}{c}(n):=\#\{(j,k)\in\mathbb Z_{\ge0}^2:\ ja+kb=n\}. \]
Its generating function is $\class{ntn-Fst}{F}(z):=\dfrac1{(1-z^a)(1-z^b)}$, and we put $\class{ntn-Gst}{G}(z):=\class{ntn-Fst}{F}(z)\,z^{-n-1}$ for a fixed $n\ge0$.
:::

::: lemma {#lem:the-generating-function name="the generating function"}
For $|z|\lt1$, $\class{ntn-Fst}{F}(z)=\sum_{j,k\ge0}z^{ja+kb}=\sum_{n\ge0}\class{ntn-cn}{c}(n)\,z^n$. Moreover $\class{ntn-cn}{c}(n)\le n+1$.
:::
::: proof
For $|z|\lt1$, $|z^a|\lt1$, so $\frac1{1-z^a}=\sum_{j\ge0}z^{ja}$, a geometric series converging absolutely; likewise for $b$. The product of two absolutely convergent series is the absolutely convergent double series of products ([A.21](apx:A21)), and its terms may be grouped by the value of the exponent: the terms $z^{ja+kb}$ with $ja+kb=n$ contribute $\class{ntn-cn}{c}(n)z^n$. For the bound: a solution of $ja+kb=n$ is fixed by $j\in\{0,1,\dots,n\}$, since then $k=(n-ja)/b$.
:::

::: proposition {#prop:counting-by-residues name="counting by residues"}
For $n\ge0$,
\[ \class{ntn-cn}{c}(n)=-\sum_{\zeta^a=1\text{ or }\zeta^b=1}\class{ntn-res}{\operatorname{Res}}_\zeta \class{ntn-Gst}{G}. \]
:::
::: proof

<ol>
<li><em>The poles.</em> $\class{ntn-Gst}{G}=\frac{1}{z^{n+1}(1-z^a)(1-z^b)}$ is a rational function with numerator $1$. Its poles are $0$ and the zeros of $(1-z^a)(1-z^b)$, namely the $\zeta$ with $\zeta^a=1$ or $\zeta^b=1$; these all lie on $|z|=1$. (At a zero $\zeta$ of the denominator of multiplicity $m$, the denominator is $(z-\zeta)^mq(z)$ with $q(\zeta)\ne0$, so $\class{ntn-Gst}{G}=\frac{1/q}{(z-\zeta)^m}$ is a pole of order $m$.)</li>
<li><em>Two circles.</em> Fix $0\lt r\lt1\lt R$. The residue theorem on $|z|=R$ counts all poles; on $|z|=r$ it counts only the pole at $0$. Subtracting, the residue at $0$ cancels:
\[ \frac1{2\pi i}\oint_{|z|=R}\class{ntn-Gst}{G}\,dz-\frac1{2\pi i}\oint_{|z|=r}\class{ntn-Gst}{G}\,dz=\sum_{\zeta^a=1\text{ or }\zeta^b=1}\class{ntn-res}{\operatorname{Res}}_\zeta \class{ntn-Gst}{G}. \]</li>
<li><em>The small circle gives $\class{ntn-cn}{c}(n)$.</em> On $|z|=r$, $\class{ntn-Gst}{G}=\sum_kc(k)z^{k-n-1}$ by @lem:the-generating-function. Since $|\class{ntn-cn}{c}(k)z^{k-n-1}|\le(k+1)r^{k-n-1}$ and $\sum_k(k+1)r^k\lt\infty$, the series converges uniformly on the circle (Weierstrass [M-test](apx:A21)) and may be integrated term by term. As $\frac1{2\pi i}\oint_{|z|=r}z^{k-n-1}dz$ is $1$ for $k=n$ and $0$ otherwise (step 3 of @thm:residue-theorem), the second integral is $\class{ntn-cn}{c}(n)$.</li>
<li><em>The big circle gives $0$.</em> On $|z|=R$: $|1-z^a|\ge R^a-1$, $|1-z^b|\ge R^b-1$, $|z^{-n-1}|=R^{-n-1}$. By the ML estimate,
\[ \Big|\frac1{2\pi i}\oint_{|z|=R}\class{ntn-Gst}{G}\,dz\Big|\le\frac{2\pi R}{2\pi}\cdot\frac{R^{-n-1}}{(R^a-1)(R^b-1)}=\frac{R^{-n}}{(R^a-1)(R^b-1)}\longrightarrow0\quad(R\to\infty). \]
The right side of step 2 does not depend on $R$, so letting $R\to\infty$ gives $0-\class{ntn-cn}{c}(n)=\sum\class{ntn-res}{\operatorname{Res}}_\zeta \class{ntn-Gst}{G}$. <span class="qed">∎</span></li>
</ol>
:::
