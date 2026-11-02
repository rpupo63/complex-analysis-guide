---
id: C6
title: The distance function
status:
- defined
- derived
- cited
---
<p>For a nonempty closed set $A$, $\class{ntn-dist}{\operatorname{dist}}(z,A):=\min\{|z-a|:a\in A\}$, the distance from $z$ to the nearest point of $A$.</p>
<div class="env"><span class="hd">Proposition.</span> $\class{ntn-dist}{\operatorname{dist}}(\cdot,A)$ is 1-Lipschitz: $|\class{ntn-dist}{\operatorname{dist}}(z,A)-\class{ntn-dist}{\operatorname{dist}}(z',A)|\le|z-z'|$.</div>
::: proof
Let $a\in A$ be nearest to $z'$. Then
\[ \class{ntn-dist}{\operatorname{dist}}(z,A)\le|z-a|\le|z-z'|+|z'-a|=|z-z'|+\class{ntn-dist}{\operatorname{dist}}(z',A). \]
Swap $z$ and $z'$.
:::
<p>Near a straight piece of boundary, $\class{ntn-dist}{\operatorname{dist}}(z,\class{ntn-dOm}{\partial\Omega})$ is the distance to a line, a linear function whose gradient is a unit normal. In general $|\nabla\class{ntn-dist}{\operatorname{dist}}|=1$ almost everywhere off $A$ (cited). @eg:a-boundary-layer uses this to compute the energy of its boundary layer.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Distance_function" target="_blank" rel="noopener">Distance function</a> · <a href="https://en.wikipedia.org/wiki/Distance_set" target="_blank" rel="noopener">Distance to a set</a></p>
