---
id: E18
title: The Basel sum $\sum1/n^2=\pi^2/6$
status:
- derived
---
<p>@lem:on-the-real-axis uses this; it follows from Euler's product, proved later (@thm:euler). There is no circularity: Lecture 10 does not use Lecture 6's partition estimates.</p>
::: proof
On $|z|\lt1$, $\frac{\sin\pi z}{\pi z}=\prod_{n\ge1}\big(1-\frac{z^2}{n^2}\big)$, and the partial products $Q_N$ converge uniformly on $|z|\le\frac12$ (@lem:products). The $z^2$-coefficient of a holomorphic function near $|z|\le\frac12$ is $\frac1{2\pi i}\oint_{|z|=1/2}(\cdot)\,z^{-3}dz$ (@thm:power-series), which passes to uniform limits. The $z^2$-coefficient of $Q_N$ is $-\sum_{n\le N}\frac1{n^2}$ (expand the finite product), and that of $\frac{\sin\pi z}{\pi z}=1-\frac{\pi^2z^2}6+\dots$ is $-\frac{\pi^2}6$. So $\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}6$.
:::
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Basel_problem" target="_blank" rel="noopener">Basel problem</a></p>
