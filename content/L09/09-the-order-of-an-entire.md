---
id: j9
slide: Slide 10
title: The order of an entire function
---
<p>An <em>entire</em> function is one that is holomorphic on all of $\mathbb C$. By @thm:power-series, its Taylor series at $0$ converges everywhere.</p>

::: definition {#def:order name=order}
For $f$ entire, let $\class{ntn-Mr}{M}(r):=\max_{|z|=r}|f(z)|$. If $\class{ntn-Mr}{M}(r)\le e^{r^\lambda}$ for all large $r$, for some $\lambda\gt0$, then $f$ has <em>finite order</em>; its <em>order</em> $\class{ntn-rhoo}{\rho}$ is the infimum of such $\lambda$.
:::
<p>The order measures growth on a doubly exponential scale: $\class{ntn-rhoo}{\rho}=\limsup_{r\to\infty}\frac{\log\log \class{ntn-Mr}{M}(r)}{\log r}$ for non-constant $f$ (then $\class{ntn-Mr}{M}(r)\to\infty$, so $\log\log \class{ntn-Mr}{M}(r)$ is defined for large $r$). A constant has order $0$.</p>
<div class="tbl"><table>
<thead><tr><th>$f$</th><th>Order</th><th>Why</th><th>Zeros</th></tr></thead>
<tbody>
<tr><td>polynomial</td><td>$0$</td><td>$\class{ntn-Mr}{M}(r)\le Cr^d\le e^{r^\lambda}$ for large $r$, for every $\lambda\gt0$</td><td>finitely many</td></tr>
<tr><td>$e^{az+b}$, $a\ne0$</td><td>$1$</td><td>$\class{ntn-Mr}{M}(r)=e^{|a|r+\operatorname{Re}b}$</td><td>none</td></tr>
<tr><td>$\sin\pi z$</td><td>$1$</td><td>$\sinh\pi r\le \class{ntn-Mr}{M}(r)\le e^{\pi r}$ (by @sec:j7, step 2)</td><td>$\mathbb Z$: about $2r$ in $|z|\le r$</td></tr>
<tr><td>$\cos\sqrt z=\sum_k\frac{(-z)^k}{(2k)!}$</td><td>$\frac12$</td><td>$|\cos w|\le e^{|w|}$ gives $\class{ntn-Mr}{M}(r)\le e^{\sqrt r}$; at $z=-r$ it is $\cosh\sqrt r$</td><td>$\pi^2(n-\frac12)^2$, $n\ge1$: about $\sqrt r/\pi$ in $|z|\le r$</td></tr>
<tr><td>$e^{z^2}$</td><td>$2$</td><td>$\class{ntn-Mr}{M}(r)=e^{r^2}$</td><td>none</td></tr>
</tbody></table></div>
<p>The power series defines $\cos\sqrt z$ without choosing a square root: it is $\cos w$ for either root $w$ of $z$, since $\cos$ is even. Its zeros are the $z=w^2$ with $\cos w=0$, i.e. $w=\pi(n-\frac12)$. The table suggests that order controls the number of zeros: order $1$, about $r$ zeros; order $\frac12$, about $\sqrt r$. The next theorem proves one direction.</p>
