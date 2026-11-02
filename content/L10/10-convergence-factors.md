---
id: k10
slide: Slide 11
title: Convergence factors
---
<p>Euler's product worked because the factors for $\pm n$ pair up as $1-\frac{z^2}{n^2}$, whose deviations from $1$ are summable. In general the naive product over the zeros diverges. For $a_k=k$: at $z=-1$, $\prod_{k\le N}(1+\frac1k)=\prod_{k\le N}\frac{k+1}k=N+1\to\infty$ (telescoping). The cure is to multiply each factor by an exponential, which has no zeros.</p>

::: definition {#def:weierstrass-factors name="Weierstrass factors"}

\[ \class{ntn-Ep}{E_0}(w):=1-w,\qquad \class{ntn-Ep}{E_p}(w):=(1-w)\exp\Big(w+\frac{w^2}2+\dots+\frac{w^p}p\Big)\quad(p\ge1). \]
Each $\class{ntn-Ep}{E_p}$ is entire, and its only zero is $w=1$, a simple one ($\exp$ never vanishes).
:::

::: lemma {#lem:convergence-factors name="convergence factors"}
For $p\ge0$ and $|w|\le\frac12$, $\ |1-\class{ntn-Ep}{E_p}(w)|\le4|w|^{p+1}$.
:::
::: proof

<ol>
<li><em>$1-w$ as an exponential.</em> For $|w|\lt1$ let $L(w):=-\sum_{k\ge1}w^k/k$. Then $L'(w)=-\sum_{k\ge1}w^{k-1}=-\frac1{1-w}$, so $\big((1-w)e^{-L}\big)'=e^{-L}\big(-1+(1-w)\frac{1}{1-w}\big)=0$; the function is constant on the disk, equal to $1$ at $w=0$. So $1-w=e^{L(w)}$.</li>
<li><em>$\class{ntn-Ep}{E_p}$ as an exponential.</em> Hence $\class{ntn-Ep}{E_p}(w)=e^{L(w)+w+\dots+w^p/p}=e^u$ with $u:=-\sum_{k\gt p}w^k/k$: the factor $\exp(w+\dots+w^p/p)$ cancels the first $p$ terms of $L$.</li>
<li><em>Estimate $u$.</em> For $|w|\le\frac12$: $|u|\le\sum_{k\gt p}|w|^k=\frac{|w|^{p+1}}{1-|w|}\le2|w|^{p+1}\le1$.</li>
<li><em>Estimate $e^u-1$.</em> For $|u|\le1$:
\[ |e^u-1|\le\sum_{j\ge1}\frac{|u|^j}{j!}\le|u|\sum_{j\ge1}\frac1{j!}=(e-1)|u|\le2|u|\le4|w|^{p+1}. \]
<span class="qed">∎</span></li>
</ol>
:::
<p>So $\class{ntn-Ep}{E_p}(w)$ is within $O(|w|^{p+1})$ of $1$ for small $w$, instead of $O(|w|)$ for $1-w$: the larger $p$, the faster the factors approach $1$.</p>
