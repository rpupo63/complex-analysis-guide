---
label: ex:the-blaschke-condition
source: Homework 2, Problem 2(c)
title: the Blaschke condition
placement: j6
order: 2
---
Let $f$ be holomorphic and bounded on $D(0,1)$, $f\not\equiv0$, with zeros $a_1,a_2,\dots$ (listed by multiplicity). Show $\sum_k(1-|a_k|)\lt\infty$.
<details class="sol"><summary>Hint</summary>
Assume $f(0)\ne0$. Apply Jensen on $|z|=r\lt1$, then let $r\to1$. Use $\log\frac1x\ge1-x$ for $0\lt x\le1$.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>Normalize.</em> If $f$ has a zero of order $k$ at $0$, replace $f$ by $f/z^k$: still holomorphic (@def:order-of-a-zero, or @lem:removable-singularities, the singularity at $0$ being removable) and bounded (bounded by $2^kM$ for $|z|\ge\frac12$, and continuous on $|z|\le\frac12$), and it drops only finitely many terms from the sum. So assume $f(0)\ne0$ and $|f|\le M$.</li>
<li><em>Jensen.</em> For $r\lt1$ with no zero on $|z|=r$ (all but countably many $r$: by @thm:identity-theorem-l10, only finitely many zeros lie in each $|z|\le r'\lt1$), @thm:jensens-formula gives
\[ \sum_{|a_k|\lt r}\log\frac r{|a_k|}=\frac1{2\pi}\int_0^{2\pi}\log|f(re^{i\theta})|\,d\theta-\log|f(0)|\le\log M-\log|f(0)|=:K. \]</li>
<li><em>Let $r\to1$.</em> Fix $n$. For $r\gt\max_{k\le n}|a_k|$, all terms are $\ge0$, so $\sum_{k\le n}\log\frac r{|a_k|}\le K$; letting $r\to1$, $\sum_{k\le n}\log\frac1{|a_k|}\le K$ for every $n$.</li>
<li>As $\log\frac1x\ge1-x$, $\sum_k(1-|a_k|)\le K\lt\infty$.</li>
</ol>
</details>
