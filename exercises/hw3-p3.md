---
label: ex:zeros-lie-in-one-plus-m
source: Homework 3, Problem 3
title: zeros lie in $|z|\lt 1+M$
placement: f4
order: 1
---
Let $p(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_1z+a_0$ and $M=\max_k|a_k|$. Prove that every zero of $p$ lies in the disk $|z|\lt 1+M$.
<details class="sol"><summary>Hint</summary>
Suppose $|z|\ge 1+M$, and compare $|z|^n$ with $|a_{n-1}z^{n-1}+\cdots+a_0|$ using a geometric series.
</details>
<details class="sol"><summary>Solution</summary>
<p>Let $|z|\ge 1+M$, and write $p(z)=z^n+s(z)$ with $s(z)=a_{n-1}z^{n-1}+\cdots+a_0$. Then $|s(z)|\le M\sum_{j=0}^{n-1}|z|^j$.</p>
<ol>
<li><em>The zero polynomial in the lower terms.</em> If $M=0$, then $s=0$ and $|z|^n\ge1\gt0$, so $p(z)\ne0$.</li>
<li><em>The geometric sum.</em> If $M\gt0$, then $|z|\ge 1+M\gt1$. The sum is the finite geometric series from the proof of @thm:power-series: $\sum_{j=0}^{n-1}|z|^j=(|z|^n-1)/(|z|-1)$. Since $|z|-1\ge M$,
\[ |s(z)|\le M\cdot\frac{|z|^n-1}{|z|-1}\le |z|^n-1\lt|z|^n. \]
So $|s(z)|\lt|z^n|$, and $p(z)\ne0$.</li>
</ol>
<p>Every zero therefore satisfies $|z|\lt 1+M$.</p>
</details>
