---
id: f20
slide: Supplement
title: 'Worked example: making change'
toc: 'Worked example: making change'
---
<p>This worked example follows the course handout <em>Coin change via complex analysis</em>. It runs the stamp argument of @sec:f10 and @sec:f11 with four denominations instead of two. The new feature is that the denominations share factors, so the poles on the unit circle are no longer simple, and the periodic corrections grow with $n$.</p>

::: definition {#def:change-counts name="change counts"}
The number of ways to make change for $n$ dollars with $1$, $5$, $10$ and $20$ dollar bills is
\[ \class{ntn-chg}{a_n}:=\#\{(c_1,c_5,c_{10},c_{20})\in\mathbb Z_{\ge0}^4:\ c_1+5c_5+10c_{10}+20c_{20}=n\}. \]
Its generating function is $\class{ntn-Cchg}{C}(z):=\dfrac1{(1-z)(1-z^5)(1-z^{10})(1-z^{20})}$, and for a fixed $n\ge0$ we put $f_n(z):=\class{ntn-Cchg}{C}(z)\,z^{-n-1}$.
:::

::: lemma {#lem:the-change-generating-function name="the generating function for change"}
For $|z|\lt1$, $\class{ntn-Cchg}{C}(z)=\sum_{n\ge0}\class{ntn-chg}{a_n}z^n$. Moreover $1\le \class{ntn-chg}{a_n}\le(n+1)^3$.
:::
::: proof
As in @lem:the-generating-function: for $|z|\lt1$ each factor is a geometric series, $\frac1{1-z^d}=\sum_{k\ge0}z^{dk}$, converging absolutely. The product of the four absolutely convergent series is the absolutely convergent multiple series of products ([A.21](apx:A21)). Grouping its terms $z^{c_1+5c_5+10c_{10}+20c_{20}}$ by the value $n$ of the exponent gives $\class{ntn-chg}{a_n}z^n$. For the bounds: $(n,0,0,0)$ is one solution, and a solution is fixed by $c_5,c_{10},c_{20}\in\{0,1,\dots,n\}$, since then $c_1=n-5c_5-10c_{10}-20c_{20}$.
:::

::: proposition {#prop:change-by-residues name="making change by residues"}
For $n\ge0$,
\[ \class{ntn-chg}{a_n}=-\sum_{\omega^{20}=1}\class{ntn-res}{\operatorname{Res}}_\omega f_n. \]
:::
::: proof

<ol>
<li><em>The poles.</em> $f_n=\frac1{z^{n+1}(1-z)(1-z^5)(1-z^{10})(1-z^{20})}$ is a rational function with numerator $1$. Its poles are $0$ and the zeros of the four factors $1-z^d$. Each $d\in\{1,5,10,20\}$ divides $20$, so $z^d=1$ implies $z^{20}=1$: every pole other than $0$ is a twentieth root of unity, on $|z|=1$. Conversely every twentieth root of unity is a zero of $1-z^{20}$, hence a pole.</li>
<li><em>Two circles.</em> Fix $0\lt r\lt1\lt R$. As in step 2 of @prop:counting-by-residues, @thm:residue-theorem on the two circles and subtraction give
\[ \frac1{2\pi i}\oint_{|z|=R}f_n\,dz-\frac1{2\pi i}\oint_{|z|=r}f_n\,dz=\sum_{\omega^{20}=1}\class{ntn-res}{\operatorname{Res}}_\omega f_n. \]</li>
<li><em>The small circle gives $\class{ntn-chg}{a_n}$.</em> On $|z|=r$, $f_n=\sum_k \class{ntn-chg}{a_k}z^{k-n-1}$ by @lem:the-change-generating-function. Since $|\class{ntn-chg}{a_k}z^{k-n-1}|\le(k+1)^3r^{k-n-1}$ and $\sum_k(k+1)^3r^k\lt\infty$, the series converges uniformly on the circle ([M-test](apx:A21)) and may be integrated term by term. Only $k=n$ survives (step 3 of @thm:residue-theorem), so the second integral is $\class{ntn-chg}{a_n}$.</li>
<li><em>The big circle gives $0$.</em> Take $R\ge2$. On $|z|=R$, $|1-z^d|\ge R^d-1\ge R^d-\frac{R^d}2=\frac{R^d}2$, because $R^d\ge2$. Hence
\[ |f_n(z)|\le\frac{2^4}{R^{1+5+10+20}\,R^{n+1}}=\frac{16}{R^{n+37}}, \]
and the [ML estimate](apx:A25) bounds the first integral by $\frac{2\pi R}{2\pi}\cdot\frac{16}{R^{n+37}}=\frac{16}{R^{n+36}}\to0$ as $R\to\infty$. The right side of step 2 does not depend on $R$, so $0-\class{ntn-chg}{a_n}=\sum_{\omega^{20}=1}\class{ntn-res}{\operatorname{Res}}_\omega f_n$.</li>
</ol>
:::

::: lemma {#lem:the-pole-orders name="the pole orders"}
Let $\omega^{20}=1$, and let $q$ be the order of $\omega$: the least $q\ge1$ with $\omega^q=1$, a divisor of $20$. The pole of $f_n$ at $\omega$ has order
\[ m(\omega)=\#\{d\in\{1,5,10,20\}:\ q\mid d\}=\begin{cases}4,&q=1\ (\omega=1),\\3,&q=5,\\2,&q=2\text{ or }10,\\1,&q=4\text{ or }20.\end{cases} \]
:::
::: proof
$\omega^d=1$ exactly when $q\mid d$. For such $d$, $1-z^d$ has a simple zero at $\omega$: its derivative there is $-d\,\omega^{d-1}\ne0$. For the other $d$, $1-\omega^d\ne0$; and $\omega\ne0$. So the denominator of $f_n$ is $(z-\omega)^{m(\omega)}h(z)$ with $h$ a polynomial and $h(\omega)\ne0$, and $f_n=\frac{1/h}{(z-\omega)^{m(\omega)}}$ is a pole of order $m(\omega)$, as in step 1 of @prop:counting-by-residues. The table lists the divisors $q$ of $20$: for $q=5$ the multiples among $1,5,10,20$ are $5,10,20$; for $q=2$ and $q=10$ they are $10,20$; for $q=4$ and $q=20$ only $20$.
:::

::: theorem {#thm:growth-of-change-counts name="growth of change counts"}
For $n\ge0$,
\[ \class{ntn-chg}{a_n}=\frac{(n+18)(2n^2+72n+385)}{12000}+E_n,\qquad |E_n|\le K(n+1)^2, \]
for a constant $K$ independent of $n$. In particular $\class{ntn-chg}{a_n}=\frac{n^3}{6000}+O(n^2)$.
:::
::: proof

<ol>
<li><em>The shape of one residue.</em> Let $\omega$ be a pole of order $m=m(\omega)$ (@lem:the-pole-orders), and put $h_\omega(z):=(z-\omega)^m\class{ntn-Cchg}{C}(z)$, which is holomorphic near $\omega$ and does not depend on $n$. Then $f_n=\frac{g}{(z-\omega)^m}$ with $g(z)=z^{-n-1}h_\omega(z)$, and by @def:residue, $\class{ntn-res}{\operatorname{Res}}_\omega f_n=\frac{g^{(m-1)}(\omega)}{(m-1)!}$. By Leibniz's rule,
\[ g^{(m-1)}(\omega)=\sum_{j=0}^{m-1}\binom{m-1}j\,(-n-1)(-n-2)\cdots(-n-j)\,\omega^{-n-1-j}\,h_\omega^{(m-1-j)}(\omega). \]
Since $|\omega|=1$, the $j$-th term has modulus at most $\binom{m-1}j(n+j)^j\,|h_\omega^{(m-1-j)}(\omega)|$. So $|\class{ntn-res}{\operatorname{Res}}_\omega f_n|\le K_\omega(n+1)^{m-1}$ for a constant $K_\omega$.</li>
<li><em>The other nineteen poles.</em> For $\omega\ne1$, $m(\omega)\le3$ by @lem:the-pole-orders, so each residue is at most $K_\omega(n+1)^2$. Put $E_n:=-\sum_{\omega^{20}=1,\ \omega\ne1}\class{ntn-res}{\operatorname{Res}}_\omega f_n$ and $K:=\sum_{\omega\ne1}K_\omega$.</li>
<li><em>The pole at $1$.</em> With $Q_d(z):=1+z+\dots+z^{d-1}$, $1-z^d=(1-z)Q_d(z)$ (finite geometric sum), and $Q_1=1$. So
\[ (1-z)(1-z^5)(1-z^{10})(1-z^{20})=(z-1)^4\,Q_5Q_{10}Q_{20}, \]
the four signs $(-1)^4$ cancelling. Thus $f_n=\frac{g}{(z-1)^4}$ with $g=\frac{z^{-n-1}}{Q_5Q_{10}Q_{20}}$, $g(1)=\frac1{5\cdot10\cdot20}=\frac1{1000}$, and $\class{ntn-res}{\operatorname{Res}}_1f_n=\frac{g'''(1)}{6}$. In Leibniz's rule for $g'''(1)$ only the term with all three derivatives on $z^{-n-1}$ has degree $3$ in $n$; it is $(-n-1)(-n-2)(-n-3)\cdot\frac1{1000}$. So $-\class{ntn-res}{\operatorname{Res}}_1f_n=\frac{n^3}{6000}+O(n^2)$. The remaining terms use $Q_d(1)=d$, $Q_d'(1)=\frac{d(d-1)}2$, $Q_d''(1)=\frac{d(d-1)(d-2)}3$; collecting them (a routine computation, checked by computer algebra) gives exactly
\[ -\class{ntn-res}{\operatorname{Res}}_1f_n=\frac{(n+18)(2n^2+72n+385)}{12000}=\frac{n^3}{6000}+\frac{9n^2}{1000}+\frac{1681\,n}{12000}+\frac{231}{400}. \]</li>
<li><em>Conclusion.</em> By @prop:change-by-residues, $\class{ntn-chg}{a_n}=-\class{ntn-res}{\operatorname{Res}}_1f_n+E_n$. <span class="qed">∎</span></li>
</ol>
:::

<p>Each term of $E_n$ is $\omega^{-n}$ times a polynomial in $n$ of degree at most $m(\omega)-1$, and $\omega^{-n}$ depends only on $n$ modulo $20$. So $\class{ntn-chg}{a_n}$ is a cubic polynomial plus corrections that repeat with period $20$ in their phase but grow like $n^2$ in size: the primitive fifth roots of unity are poles of order $3$. Compare @thm:the-stamp-formula, where the denominations are coprime, every pole except $1$ is simple, and the corrections stay bounded.</p>

::: example {#eg:making-change-numbers name="the numbers" status=derived}
Counting directly (a short program) and comparing with the cubic $P(n):=\frac{(n+18)(2n^2+72n+385)}{12000}$ of @thm:growth-of-change-counts:
<div class="tbl"><table><thead><tr><th>$n$</th><th>$\class{ntn-chg}{a_n}$</th><th>$P(n)$</th><th>$E_n=\class{ntn-chg}{a_n}-P(n)$</th><th>$n^3/6000$</th></tr></thead>
<tbody>
<tr><td>10</td><td>4</td><td>3.05</td><td>0.95</td><td>0.17</td></tr>
<tr><td>20</td><td>10</td><td>8.31</td><td>1.69</td><td>1.33</td></tr>
<tr><td>50</td><td>56</td><td>50.92</td><td>5.09</td><td>20.83</td></tr>
<tr><td>100</td><td>286</td><td>271.25</td><td>14.75</td><td>166.67</td></tr>
<tr><td>200</td><td>1771</td><td>1721.93</td><td>49.07</td><td>1333.33</td></tr>
<tr><td>1000</td><td>176851</td><td>175807.33</td><td>1043.67</td><td>166666.67</td></tr>
</tbody></table></div>
For instance the $4$ ways for $n=10$ are $10\cdot1$, $5\cdot1+5$, $5+5$ and $10$.
:::
<p>The leading term alone is a poor guide for moderate $n$: at $n=100$ it gives $167$ against the true $286$. The full cubic is within $15$, and the error $E_n$ grows roughly like $n^2$, as step 2 of the proof predicts.</p>

::: theorem {#thm:polya-carlson name="Pólya–Carlson" status=cited}
Let $f(z)=\sum_{n\ge0}a_nz^n$ have integer coefficients $a_n$ and radius of convergence $1$. Then either $f$ is a rational function, or the unit circle is a natural boundary of $f$ (@def:natural-boundary, Lecture 11).
:::
::: remark {#rem:where-the-change-series-sits name="where the change series sits"}
$\class{ntn-Cchg}{C}$ has integer coefficients and radius of convergence $1$: the coefficients satisfy $1\le \class{ntn-chg}{a_n}\le(n+1)^3$ by @lem:the-change-generating-function, so $\class{ntn-chg}{a_n}^{1/n}\to1$. It is the rational alternative. A theorem of Fatou adds that then every pole is a root of unity, so that $f=P/(1-z^m)^q$ with $P$ a polynomial with integer coefficients. For $\class{ntn-Cchg}{C}$ one can take $m=20$, $q=4$:
\[ (1-z^{20})^4\,\class{ntn-Cchg}{C}(z)=\frac{(1-z^{20})^3}{(1-z)(1-z^5)(1-z^{10})} \]
is a polynomial, since each of $1-z$, $1-z^5$, $1-z^{10}$ divides $1-z^{20}$. The lacunary series of @prop:the-unit-circle-is-a (Lecture 11) is the other alternative. The handout proves the theorem with Hankel determinants of the $a_n$, written as Cauchy integrals over a contour that crosses the circle where $f$ continues, and the transfinite diameter of the inverted contour; that proof is not reproduced here.
:::
