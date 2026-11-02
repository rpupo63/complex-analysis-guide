---
id: k9
slide: Slide 10
title: The partial products
---
<figure>{{fig:k9-1}}<figcaption>$\class{ntn-PN}{P_N}(x)=\pi x\prod_{n\le N}(1-x^2/n^2)$ for $N=1,3,10$, and $\sin\pi x$ (thick), on $[-3.6,3.6]$.</figcaption></figure>
<ul>
<li><b>No polynomial is the sine.</b> $\class{ntn-PN}{P_N}(x):=\pi x\prod_{n\le N}(1-x^2/n^2)$ is a polynomial of degree $2N+1$, so $|\class{ntn-PN}{P_N}(x)|\to\infty$ as $|x|\to\infty$, while $|\sin\pi x|\le1$. The partial products follow the sine only on a bounded window, which grows with $N$.</li>
<li><b>The convergence is slow.</b> For fixed $x\notin\mathbb Z$, as $N\to\infty$,
\[ \frac{\class{ntn-PN}{P_N}(x)}{\sin\pi x}=\prod_{n\gt N}\Big(1-\frac{x^2}{n^2}\Big)^{-1}=\exp\Big(\sum_{n\gt N}-\log\Big(1-\frac{x^2}{n^2}\Big)\Big)=e^{x^2/N+O(N^{-2})}, \]
since $-\log(1-t)=t+O(t^2)$ and $\sum_{n\gt N}\frac1{n^2}=\frac1N+O(\frac1{N^2})$ (compare with $\int_N^\infty dt/t^2$). So the relative error is about $x^2/N$: halving it costs doubling $N$. At $x=1.5$, $N=10$ the ratio is $1.24$ (the leading term predicts $e^{0.225}\approx1.25$).</li>
</ul>
