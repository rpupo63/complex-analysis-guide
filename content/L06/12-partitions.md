---
id: f12
slide: Slide 13
title: Partitions
---

::: definition {#def:partitions name=partitions}
A <em>partition</em> of $n$ writes $n$ as a sum of positive integers, order ignored, and $\class{ntn-pn}{p}(n)$ is the number of them. For example
\[ 4=3+1=2+2=2+1+1=1+1+1+1, \]
so $\class{ntn-pn}{p}(4)=5$; and $\class{ntn-pn}{p}(0):=1$. Equivalently, $\class{ntn-pn}{p}(n)$ counts the ways to pay $n$ with stamps of values $1,2,3,\dots$ (a partition is fixed by how many parts equal $k$, for each $k$). Its generating function is $\class{ntn-Pz}{P}(z):=\sum_{n\ge0}\class{ntn-pn}{p}(n)z^n$.
:::

::: proposition {#prop:eulers-product name="Euler's product"}
For $|z|\lt1$ the series $\class{ntn-Pz}{P}(z)$ converges, and
\[ \class{ntn-Pz}{P}(z)=\prod_{k\ge1}\frac1{1-z^k}. \]
:::
::: proof

<ol>
<li><em>Finite products.</em> As for two stamp values (@lem:the-generating-function), multiplying the geometric series $\frac1{1-z^k}=\sum_{j\ge0}z^{jk}$ for $k=1,\dots,K$ gives $\prod_{k\le K}\frac1{1-z^k}=\sum_n\class{ntn-pK}{p_K}(n)z^n$, where $\class{ntn-pK}{p_K}(n)$ counts partitions of $n$ with all parts $\le K$ (choose the number $j_k$ of parts equal to $k$; then $n=\sum_kkj_k$). Clearly $\class{ntn-pK}{p_K}(n)\le \class{ntn-pn}{p}(n)$, with equality when $K\ge n$.</li>
<li><em>$\class{ntn-Pz}{P}(r)$ converges for $0\le r\lt1$.</em> The terms are $\ge0$, and the partial sums are bounded:
\[ \sum_{n\le K}\class{ntn-pn}{p}(n)r^n=\sum_{n\le K}\class{ntn-pK}{p_K}(n)r^n\le\prod_{k\le K}\frac1{1-r^k}=\exp\Big(\sum_{k\le K}-\log(1-r^k)\Big)\le\exp\Big(\sum_{k\ge1}\frac{r^k}{1-r}\Big)=e^{r/(1-r)^2}, \]
using $-\log(1-x)\le\frac{x}{1-x}$ for $0\le x\lt1$ (compare the series $\sum x^m/m$ with $\sum x^m$) and $1-r^k\ge1-r$. A bounded increasing sequence converges ([A.15](apx:A15)). So $\class{ntn-Pz}{P}(z)$ converges absolutely for $|z|\lt1$.</li>
<li><em>The product converges to $P$.</em> For $|z|=r\lt1$,
\[ \Big|\class{ntn-Pz}{P}(z)-\prod_{k\le K}\frac1{1-z^k}\Big|=\Big|\sum_{n\gt K}\big(\class{ntn-pn}{p}(n)-\class{ntn-pK}{p_K}(n)\big)z^n\Big|\le\sum_{n\gt K}\class{ntn-pn}{p}(n)r^n\longrightarrow0\quad(K\to\infty), \]
the tail of the convergent series of step 2. <span class="qed">∎</span></li>
</ol>
:::
<p>The slide justifies convergence by "$\sum_k|z|^k\lt\infty$": that is the hypothesis of the product lemma, @lem:products, with $u_k=\frac{z^k}{1-z^k}$. The proof above avoids that lemma, which comes later.</p>
<figure>{{fig:f12-1}}<figcaption>Each factor $1/(1-z^k)$ has poles at the $k$-th roots of unity, so $P$ has poles on a dense subset of the unit circle (dots, larger for small $k$). Cauchy's formula is applied on a circle $|z|=r\lt1$ (blue) just inside.</figcaption></figure>
<p>Values: $\class{ntn-pn}{p}(10)=42$, $\class{ntn-pn}{p}(100)=190\,569\,292$, $\class{ntn-pn}{p}(200)=3\,972\,999\,029\,388$. The rest of the lecture explains this growth.</p>
