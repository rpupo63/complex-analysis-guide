---
id: k7
slide: Slide 8
title: Euler's sine product
---

::: theorem {#thm:euler name=Euler}
For every $z\in\mathbb C$,
\[ \sin\pi z=\class{ntn-Ps}{P}(z):=\pi z\prod_{n\ge1}\Big(1-\frac{z^2}{n^2}\Big). \]
:::
<p>Euler's heuristic: $\sin\pi z$ vanishes exactly at the integers, like a "polynomial of infinite degree", so it should factor over its zeros. The proof below makes this honest in three steps.</p>
::: proof {title="Step 1: $f:=\sin\pi z/\class{ntn-Ps}{P}$ is entire and zero-free, so $f=e^G$."}

<ol>
<li><em>$\class{ntn-Ps}{P}$ is entire, with simple zeros exactly at the integers.</em> On $|z|\le R$, $|z^2/n^2|\le R^2/n^2$, which is summable over $n$. So the product lemma (@lem:products, with $u_n=-z^2/n^2$) makes $\class{ntn-Ps}{P}$ entire. Its zeros: $\pi z$ vanishes (simply) at $0$, and $1-\frac{z^2}{n^2}=(1-\frac zn)(1+\frac zn)$ vanishes simply at $\pm n$; by the lemma, the zeros of $\class{ntn-Ps}{P}$ are exactly these, each simple.</li>
<li><em>So is $\sin\pi z$.</em> $\sin\pi z=0$ iff $e^{2\pi iz}=1$ iff $z\in\mathbb Z$. At $m\in\mathbb Z$ the derivative $\pi\cos\pi m=\pm\pi\ne0$, so the zero is simple.</li>
<li><em>The quotient.</em> Off $\mathbb Z$, $f$ is holomorphic and nonzero. At $m\in\mathbb Z$, both are $(z-m)$ times a function holomorphic and nonzero at $m$, so $f$ is a quotient of two such functions: bounded near $m$, hence holomorphic there by @lem:removable-singularities, and nonzero at $m$. So $f$ is entire with no zeros, and $f=e^G$ by @lem:no-zeros.</li>
<li><em>$f$ is even, and $f(0)=1$.</em> $\sin\pi z$ and $\class{ntn-Ps}{P}$ are both odd, so their quotient is even. As $z\to0$, $\frac{\sin\pi z}{\pi z}\to1$ and $\frac{\class{ntn-Ps}{P}(z)}{\pi z}=\prod_n(1-\frac{z^2}{n^2})\to1$ (the product is continuous, with value $1$ at $0$). So $f(0)=1$. <span class="qed">∎</span></li>
</ol>
:::
