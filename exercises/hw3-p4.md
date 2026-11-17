---
label: ex:entire-functions-of-square-root-growth
source: Homework 3, Problem 4
title: entire functions of square-root growth
placement: f5
order: 3
---
Find all entire functions $f$ such that $|f(z)|\le e^x(1+|z|)^{1/2}$ for all $z=x+iy\in\mathbb C$.
<details class="sol"><summary>Hint</summary>
The function $g(z)=f(z)\,e^{-z}$ is entire and satisfies $|g(z)|\le(1+|z|)^{1/2}$. Use Cauchy's estimates to show that $g$ is constant.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>The auxiliary function.</em> $e^{-z}$ is entire, so $g(z):=f(z)\,e^{-z}$ is entire. $|e^{-z}|=e^{-x}$, hence $|g(z)|\le(1+|z|)^{1/2}$.</li>
<li><em>Kill the higher coefficients.</em> By @thm:power-series, $g(z)=\sum_{n\ge0}a_nz^n$ on $\mathbb C$. On the circle $|z|=R$, $|g|\le(1+R)^{1/2}$. Cauchy's estimate (@cor:cauchys-estimate) gives $|a_n|\le(1+R)^{1/2}R^{-n}$. For $n\ge1$, the right side tends to $0$ as $R\to\infty$, so $a_n=0$. Thus $g$ is constant, say $g(z)=c$, and $f(z)=ce^z$.</li>
<li><em>Which constants.</em> $|f(0)|=|c|\le(1+0)^{1/2}=1$. Conversely, if $|c|\le1$, then $|ce^z|=|c|e^x\le e^x\le e^x(1+|z|)^{1/2}$. So the functions are exactly $f(z)=ce^z$ with $|c|\le1$.</li>
</ol>
</details>
