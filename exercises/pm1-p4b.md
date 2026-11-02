---
label: ex:a-double-zero-at-the-origin
source: Practice midterm 1, Problem 4(b)
title: a double zero at the origin
placement: n14
order: 1
---
Let $f:D(0,1)\to D(0,1)$ be holomorphic with $f(0)=f'(0)=0$. Let $g(z):=f(z)/z$ for $z\ne0$, $g(0):=0$. (i) Show $g$ is holomorphic on $D(0,1)$. (ii) Show $g$ maps $D(0,1)$ into $D(0,1)$. (iii) Apply the Schwarz lemma to $g$ to conclude $|f(z)|\le|z|^2$.
<details class="sol"><summary>Hint</summary>
(i) @lem:removable-singularities. (ii) The Schwarz lemma for $f$ gives $|g|\le1$; rule out $|g|=1$ at an interior point using $g(0)=0$ and @rem:maximum-modulus-again.
</details>
<details class="sol"><summary>Solution</summary>
<ol type="i">
<li>$\frac{f(z)}z=\frac{f(z)-f(0)}z\to f'(0)=0$ as $z\to0$: bounded near $0$, so removable (@lem:removable-singularities), with value $0$.</li>
<li>By the Schwarz lemma for $f$ (@thm:schwarz-lemma), $|f(z)|\le|z|$, so $|g|\le1$. If $|g(z_0)|=1$ for some $z_0$, then $|g|$ has an interior maximum, so $g$ is constant (@rem:maximum-modulus-again), contradicting $g(0)=0$. So $|g|\lt1$.</li>
<li>$g$ maps the disk into itself with $g(0)=0$, so $|g(z)|\le|z|$ by the Schwarz lemma (@thm:schwarz-lemma), i.e. $|f(z)|\le|z|^2$.</li>
</ol>
</details>
