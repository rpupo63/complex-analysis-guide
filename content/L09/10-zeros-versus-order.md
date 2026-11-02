---
id: j10
slide: Slide 11
title: Zeros versus order
---

::: theorem {#thm:zeros-versus-order name="zeros versus order"}
Let $f$ be entire of finite order $\class{ntn-rhoo}{\rho}$, with $f(0)\ne0$ and zeros $a_1,a_2,\dots$ (repeated by multiplicity). Then:<br>
(1) for every $\epsilon\gt0$, $\class{ntn-nr}{n}(r)=O(r^{\class{ntn-rhoo}{\rho}+\epsilon})$ as $r\to\infty$;<br>
(2) for every $\sigma\gt\class{ntn-rhoo}{\rho}$, $\sum_k|a_k|^{-\sigma}\lt\infty$.
:::
::: proof

<ol>
<li><em>(1).</em> By definition of the order, $\class{ntn-Mr}{M}(2r)\le e^{(2r)^{\class{ntn-rhoo}{\rho}+\epsilon}}$ for large $r$. @cor:counting-zeros with $R=2r$ (so $\log\frac Rr=\log2$) gives
\[ \class{ntn-nr}{n}(r)\le\frac{(2r)^{\class{ntn-rhoo}{\rho}+\epsilon}-\log|f(0)|}{\log2}=O(r^{\class{ntn-rhoo}{\rho}+\epsilon}). \]</li>
<li><em>(2), dyadic shells.</em> Let $\epsilon:=(\sigma-\class{ntn-rhoo}{\rho})/2\gt0$. By (1) there is $C$ with $\class{ntn-nr}{n}(r)\le Cr^{\class{ntn-rhoo}{\rho}+\epsilon}$ for all $r\ge1$ (for small $r$ enlarge $C$). The zeros with $2^j\lt|a_k|\le2^{j+1}$ number at most $\class{ntn-nr}{n}(2^{j+1})\le C2^{\class{ntn-rhoo}{\rho}+\epsilon}\,2^{j(\class{ntn-rhoo}{\rho}+\epsilon)}$, and each contributes $|a_k|^{-\sigma}\lt2^{-j\sigma}$. Since $\class{ntn-rhoo}{\rho}+\epsilon-\sigma=-\epsilon$,
\[ \sum_{|a_k|\gt1}|a_k|^{-\sigma}\le C2^{\class{ntn-rhoo}{\rho}+\epsilon}\sum_{j\ge0}2^{j(\class{ntn-rhoo}{\rho}+\epsilon)}2^{-j\sigma}=C2^{\class{ntn-rhoo}{\rho}+\epsilon}\sum_{j\ge0}2^{-j\epsilon}\lt\infty. \]
Only finitely many $a_k$ have $|a_k|\le1$ (zeros cannot accumulate). <span class="qed">∎</span></li>
</ol>
:::
::: remark {#rem:sigma-rho-can-fail name="$\sigma=\class{ntn-rhoo}{\rho}$ can fail"}
$\frac{\sin\pi z}{\pi z}$ has order $1$ and zeros $\pm1,\pm2,\dots$, and $\sum_{n\ge1}\frac2n=\infty$. So (2) is sharp.
:::
<p>@thm:zeros-versus-order(2) is exactly what is needed to build a convergent product with prescribed zeros (Hadamard's theorem, @thm:hadamard). Lecture 10 develops infinite products.</p>
