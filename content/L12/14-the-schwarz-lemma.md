---
id: n14
slide: Slide 15
title: The Schwarz lemma
---
<p>The maps $e^{i\theta}\varphi_a$ turn out to be all the automorphisms of the disk. The tool for proving this:</p>

::: theorem {#thm:schwarz-lemma name="Schwarz lemma"}
Let $f$ be holomorphic on $D(0,1)$, with $|f|\lt1$ and $f(0)=0$. Then $|f(z)|\le|z|$ for $z\in D(0,1)$, and $|f'(0)|\le1$. If $|f(z_0)|=|z_0|$ for some $z_0\ne0$, or $|f'(0)|=1$, then $f(z)=cz$ with $|c|=1$: a rotation.
:::
::: proof

<ol>
<li><em>Divide by $z$.</em> As $f(0)=0$, $\frac{f(z)}z=\frac{f(z)-f(0)}{z}\to f'(0)$ as $z\to0$, so $g(z):=f(z)/z$ is bounded near $0$ and extends holomorphically to $D(0,1)$ with $g(0)=f'(0)$ (@lem:removable-singularities).</li>
<li><em>Bound on circles.</em> On $|z|=r\lt1$, $|g|=|f|/r\lt1/r$. By maximum modulus (@lem:maximum-modulus) on the closed disk of radius $r$, $|g|\le1/r$ on $D(0,r)$.</li>
<li><em>Let $r\to1$.</em> For fixed $z$, the bound holds for every $r\in(|z|,1)$, so $|g(z)|\le1$. That is, $|f(z)|\le|z|$, and $|f'(0)|=|g(0)|\le1$.</li>
<li><em>Equality.</em> If $|f(z_0)|=|z_0|$ with $z_0\ne0$, or $|f'(0)|=1$, then $|g|$ reaches its maximum value $1$ at an interior point ($z_0$, or $0$). By @rem:maximum-modulus-again, $g$ is a constant $c$, $|c|=1$, and $f(z)=cz$. <span class="qed">∎</span></li>
</ol>
:::
<p>The idea: a self-map of the disk that fixes $0$ cannot push any point outwards. All three practice midterms use this, usually after composing with $\varphi_a$ or the Cayley map to move a given point to $0$.</p>
