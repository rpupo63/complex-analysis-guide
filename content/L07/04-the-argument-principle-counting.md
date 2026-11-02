---
id: g4
slide: Slide 5
title: 'The argument principle: counting'
---
::: proof {title="Proof, part 2: counting."}

<ol>
<li><em>List the special points.</em> Let $\xi_1,\dots,\xi_q$ be the zeros and the poles of $f$ in $|z|\lt R$, with orders $m_1,\dots,m_q$. Take $\delta\gt0$ so small that the disks $|z-\xi_j|\lt2\delta$ are pairwise disjoint, lie in $|z|\lt R$, and contain no zero or pole other than $\xi_j$.</li>
<li><em>Where $f'/f$ is holomorphic.</em> $f'/f$ is holomorphic on the open set where $f$ is holomorphic and $\ne0$ (@cor:holomorphic-functions-are-smooth and the quotient rule). That set contains each punctured disk $0\lt|z-\xi_j|\lt2\delta$, and the closed region $A$ inside $C$ and outside the circles $|z-\xi_j|=\delta$: $A$ contains no zero or pole (those inside are the $\xi_j$, and $f\ne0$ on $C$).</li>
<li><em>Move the circle, then apply the lemma.</em> @lem:moving-the-circle, then @lem:logarithmic-derivative with $r=2\delta$ and $\epsilon=\delta$:
\[ \frac1{2\pi i}\oint_C\frac{f'}f\,dz=\sum_{j=1}^q\frac1{2\pi i}\oint_{|z-\xi_j|=\delta}\frac{f'}f\,dz=\sum_{\xi_j\text{ a zero}}m_j-\sum_{\xi_j\text{ a pole}}m_j=\class{ntn-ZP}{Z}-\class{ntn-ZP}{P}. \]</li>
</ol>
<span class="qed">∎</span>
:::
<p>In the language of the residue theorem: $f'/f$ has a simple pole at each zero and each pole of $f$, with residue $+m$ or $-m$ (step 4 and step 5 of @lem:logarithmic-derivative show $f'/f=\frac{\pm m}{z-a}+$ (bounded)), and no other singularities. The theorem is @thm:residue-theorem applied to $f'/f$.</p>
