---
id: n8
slide: Slide 9
title: Local injectivity
---

::: corollary {#cor:local-injectivity name="local injectivity"}
Let $f$ be holomorphic near $z_0$, and not constant near $z_0$. Then $f$ is injective on some disk about $z_0$ if and only if $f'(z_0)\ne0$.
:::
::: proof
Apply @thm:local-behaviour with $w_0:=f(z_0)$ and $m$ the order of the zero of $f-w_0$ at $z_0$. Note that $m=1$ exactly when $a_1=f'(z_0)\ne0$.
<ul>
<li><em>(⇐) $f'(z_0)\ne0$, so $m=1$.</em> Each $w\in D(w_0,\delta)$ is taken exactly once on $D(z_0,r)$. So $f$ is injective on $D(z_0,r)\cap f^{-1}(D(w_0,\delta))$: if $f(z_1)=f(z_2)=w$ for two points there, then $w\in D(w_0,\delta)$ is taken twice in $D(z_0,r)$ unless $z_1=z_2$. That set is open (an intersection of open sets) and contains $z_0$, so it contains a disk about $z_0$.</li>
<li><em>(⇒) If $f'(z_0)=0$ then $m\ge2$.</em> $f'$ is not identically zero near $z_0$ ($f$ is not constant), so its zeros are isolated (@thm:isolated-zeros): take $r$ so small that also $f'\ne0$ on $0\lt|z-z_0|\lt r$. For $w\in D(w_0,\delta)$ with $w\ne w_0$, the $m$ zeros of $f-w$ in $D(z_0,r)$ are not at $z_0$ (where $f=w_0\ne w$), so the derivative $f'$ is nonzero there and each zero is simple. So $f=w$ at $m\ge2$ distinct points of $D(z_0,r)$. As $r$ can be taken arbitrarily small, $f$ is injective on no disk about $z_0$. <span class="qed">∎</span></li>
</ul>
:::
<p>Example: $z^2$ at $0$ has derivative $0$, and indeed it takes each nearby $w\ne0$ twice, at $\pm\sqrt w$.</p>
