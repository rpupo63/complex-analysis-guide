---
label: ex:zeros-at-the-integers-force-slow
source: Homework 2, Problem 2(a)
title: zeros at the integers force slow growth
placement: j6
order: 1
---
Let $f$ be entire with $f(n)=0$ for $n=1,2,3,\dots$ and $|f(z)|\le Ce^{c|z|}$ for all $z$, where $c\lt1$. Show $f\equiv0$.
<details class="sol"><summary>Hint</summary>
If $f\not\equiv0$, divide by a power of $z$ so that $f(0)\ne0$, and apply Jensen's formula (@thm:jensens-formula) on $|z|=R$ with $N\lt R\lt N+1$, $f\ne0$ on $|z|=R$. Show $N\log N-\log N!\ge N-1-\log N$ by comparing $\log N!$ with $\int_1^N\log t\,dt$.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>Normalize.</em> If $f\not\equiv0$, let $k$ be the order of its zero at $0$ (@def:order-of-a-zero; $k=0$ if $f(0)\ne0$) and write $f=z^kg$ with $g$ entire, $g(0)\ne0$ (@thm:isolated-zeros); $g$ still vanishes at $1,2,\dots$, and $|g(z)|\le Ce^{c|z|}$ for $|z|\ge1$.</li>
<li><em>Jensen.</em> For $N\lt R\lt N+1$ with $g\ne0$ on $|z|=R$ (all but finitely many such $R$: by @thm:identity-theorem-l10 there are only finitely many zeros in $|z|\le N+1$), Jensen's formula (@thm:jensens-formula) applies. Every zero in $|z|\lt R$ contributes a positive term $\log\frac R{|a_j|}$, so keeping only $1,\dots,N$, and bounding the mean of $\log|g|$ by its maximum (compare @cor:counting-zeros):
\[ \log|g(0)|+\sum_{n=1}^N\log\frac Rn\le\frac1{2\pi}\int_0^{2\pi}\log|g(Re^{i\theta})|\,d\theta\le\log C+cR\le\log C+c(N+1). \]</li>
<li><em>Stirling-type bound.</em> $\sum_{n\le N}\log\frac Rn\ge N\log N-\log N!$, and since $\log$ is increasing, $\log N!=\sum_{n=2}^N\log n\le\int_1^N\log t\,dt+\log N=N\log N-N+1+\log N$. So $\sum\ge N-1-\log N$.</li>
<li><em>Contradiction.</em> Combining, $(1-c)N\le\log C-\log|g(0)|+1+c+\log N$ for all large $N$. The left side grows linearly and the right side logarithmically, impossible as $c\lt1$. So $f\equiv0$.</li>
</ol>
<p>Remark: $\sin\pi z$ vanishes on $\mathbb Z$ and satisfies the bound with $c=\pi$; Carlson's theorem shows $c\lt\pi$ already forces $f\equiv0$. Jensen alone gives $c\lt1$.</p>
</details>
