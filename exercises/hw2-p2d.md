---
label: ex:blaschke-products
source: Homework 2, Problem 2(d) (optional)
title: Blaschke products
placement: k5
order: 1
---
Let $0\lt|a_k|\lt1$ with $\sum_k(1-|a_k|)\lt\infty$. Show that $B(z):=\prod_k\frac{|a_k|}{a_k}\cdot\frac{a_k-z}{1-\bar a_kz}$ converges uniformly on each $\overline{D(0,r)}$, $r\lt1$, to a holomorphic function on $D(0,1)$ with $|B|\le1$, whose zeros are exactly the $a_k$.
<details class="sol"><summary>Hint</summary>
For $|z|\le r$, the factor differs from $1$ by at most $(1-|a_k|)\frac{1+r}{1-r}$. Then use @lem:products.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>The factor minus one.</em> With $b_k(z):=\frac{|a_k|}{a_k}\cdot\frac{a_k-z}{1-\bar a_kz}$,
\[ b_k(z)-1=\frac{|a_k|(a_k-z)-a_k(1-\bar a_kz)}{a_k(1-\bar a_kz)}=\frac{-(1-|a_k|)\,(a_k+|a_k|z)}{a_k(1-\bar a_kz)}. \]
For $|z|\le r$: $|a_k+|a_k|z|\le|a_k|(1+r)$ and $|1-\bar a_kz|\ge1-r$, so $|b_k-1|\le(1-|a_k|)\frac{1+r}{1-r}$.</li>
<li><em>Products.</em> These bounds are summable, so @lem:products (with $U=D(0,1)$ and $u_k=b_k-1$) gives uniform convergence on each $\overline{D(0,r)}$ to a holomorphic $B$ whose zeros are those of the factors: $b_k$ vanishes only at $a_k$, simply.</li>
<li><em>$|B|\le1$.</em> Each factor is $\frac{|a_k|}{a_k}\varphi_{a_k}$, a rotation of the automorphism of @def:automorphism-varphi-a, so it maps the disk into itself (@lem:is-an-automorphism-of-with, Lecture 12). Directly, each factor has modulus $\lt1$ on the disk: $|1-\bar az|^2-|a-z|^2=(1-|a|^2)(1-|z|^2)\gt0$ for $|a|,|z|\lt1$ (expand both sides). So partial products have modulus $\lt1$, hence their limit satisfies $|B|\le1$.</li>
</ol>
<p>With the previous exercise: the zero sets of bounded holomorphic functions on the disk are exactly the sequences with $\sum(1-|a_k|)\lt\infty$.</p>
</details>
