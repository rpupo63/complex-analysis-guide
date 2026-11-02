---
id: A3
title: Mean value theorem and a two-variable bound
status:
- cited
- derived
---
<div class="env"><span class="hd">Theorem (cited).</span> If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, there is $\xi\in(a,b)$ with $f(b)-f(a)=f'(\xi)(b-a)$.</div>
<div class="env"><span class="hd">Corollary (proved).</span> Let $F$ be continuously differentiable on a convex set $K\subset\R^2$ with $|\nabla F|\le M$ on $K$. Then $|F(P)-F(Q)|\le M\,|P-Q|$ for all $P,Q\in K$.</div>
::: proof
The segment from $Q$ to $P$ lies in $K$ by convexity. Put $f(t):=F(Q+t(P-Q))$ for $t\in[0,1]$. By the chain rule $f'(t)=\nabla F(Q+t(P-Q))\cdot(P-Q)$. The mean value theorem gives some $\tau$ with
\[ |F(P)-F(Q)|=|f(1)-f(0)|=|f'(\tau)|\le|\nabla F|\,|P-Q|\le M|P-Q|, \]
using the [vector inequality](apx:A12) $|a\cdot b|\le|a||b|$.
:::
<p>This is the first-order case of Taylor's theorem that the slide invokes. @lem:the-slides-taylors-theorem-on-each uses it with $K$ a grid square and $F=\partial_x\eta$ or $\partial_y\eta$.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Mean_value_theorem" target="_blank" rel="noopener">Mean value theorem</a> · <a href="https://en.wikipedia.org/wiki/Taylor%27s_theorem" target="_blank" rel="noopener">Taylor's theorem</a></p>
