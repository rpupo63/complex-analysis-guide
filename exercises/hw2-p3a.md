---
label: ex:derangements
source: Homework 2, Problem 3(a)
title: derangements
placement: f11
order: 1
---
Let $D_n$ be the number of permutations of $\{1,\dots,n\}$ without fixed points ($D_0=1$). Choosing the set of fixed points gives $n!=\sum_k\binom nkD_{n-k}$. Deduce $\sum_nD_n\frac{z^n}{n!}=\frac{e^{-z}}{1-z}$ on $D(0,1)$. Show that $\frac{e^{-z}-e^{-1}}{1-z}$ extends to an entire function, and conclude $\big|\frac{D_n}{n!}-\frac1e\big|\le C_RR^{-n}$ for every $R\gt0$.
<details class="sol"><summary>Hint</summary>
Products of exponential generating functions multiply as $\sum a_n\frac{z^n}{n!}\cdot\sum b_n\frac{z^n}{n!}=\sum_n\big(\sum_k\binom nka_kb_{n-k}\big)\frac{z^n}{n!}$. For the entire function, write $e^{-z}-e^{-1}=e^{-1}(e^{1-z}-1)$. Finish with Cauchy's estimate (@cor:cauchys-estimate).
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>Generating function.</em> With $a_k=1$ (so $\sum a_k\frac{z^k}{k!}=e^z$) and $b_m=D_m$, the identity $n!=\sum_k\binom nkD_{n-k}$ says $e^z\cdot\sum_nD_n\frac{z^n}{n!}=\sum_nn!\frac{z^n}{n!}=\frac1{1-z}$ for $|z|\lt1$ (products of absolutely convergent series, [A.21](apx:A21)). Divide by $e^z$.</li>
<li><em>Entire.</em> $\frac{e^{-z}-e^{-1}}{1-z}=e^{-1}\,E(1-z)$ with $E(w):=\frac{e^w-1}w=\sum_{n\ge1}\frac{w^{n-1}}{n!}$ for $w\ne0$. The power series has infinite radius ([A.19](apx:A19)), so it defines an entire function. (Equivalently: $E$ is holomorphic on $w\ne0$ and bounded near $0$, so the singularity is removable, @lem:removable-singularities.) So $H(z):=\frac{e^{-z}}{1-z}-\frac{e^{-1}}{1-z}$ is entire.</li>
<li><em>Coefficients.</em> $\frac{e^{-1}}{1-z}=\sum_ne^{-1}z^n$ for $|z|\lt1$, so on $D(0,1)$ the power series of $H$ has $n$-th coefficient $\frac{D_n}{n!}-\frac1e$. These are the Taylor coefficients $H^{(n)}(0)/n!$ (@thm:cauchys-formula-for-derivatives), so they are the same on every circle $|z|=R$ (@thm:power-series). By Cauchy's estimate (@cor:cauchys-estimate) on $|z|=R$, the coefficient is at most $M_RR^{-n}$, $M_R:=\max_{|z|=R}|H|$.</li>
</ol>
<p>So $D_n/n!\to1/e$ faster than any geometric rate: the "probability that a random permutation has no fixed point" is $1/e$ to within $10^{-k}$ after very few terms. The single pole at $z=1$ gives the main term; there is no second singularity, hence no error term of geometric size.</p>
</details>
