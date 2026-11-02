---
id: n4
slide: Slide 5
title: The Cayley map
---

::: proposition {#prop:cayley-map name="Cayley map"}
$C(z):=\dfrac{z-i}{z+i}$ is a bijection of $\mathbb H$ onto $D(0,1)$, with inverse $C^{-1}(w)=i\,\dfrac{1+w}{1-w}$. Both are holomorphic.
:::
::: proof

<ol>
<li><em>$C$ maps $\mathbb H$ into the disk.</em> $|C(z)|\lt1\iff|z-i|\lt|z+i|$: $z$ is closer to $i$ than to $-i$. With $z=x+iy$,
\[ |z-i|^2-|z+i|^2=\big(x^2+(y-1)^2\big)-\big(x^2+(y+1)^2\big)=-4y, \]
so this holds exactly when $y\gt0$.</li>
<li><em>Solve for $z$.</em> For $w\ne1$,
\[ \frac{z-i}{z+i}=w\iff z-i=wz+wi\iff z(1-w)=i(1+w)\iff z=i\,\frac{1+w}{1-w}. \]</li>
<li><em>Onto.</em> For $|w|\lt1$, this $z$ satisfies $C(z)=w$, so $|C(z)|\lt1$ and, by step 1, $z\in\mathbb H$. So each $w\in D(0,1)$ has exactly one preimage in $\mathbb H$.</li>
<li><em>Holomorphic.</em> Both are rational functions; their only poles, $z=-i$ and $w=1$, lie outside $\mathbb H$ and outside $D(0,1)$. <span class="qed">∎</span></li>
</ol>
:::
<p>The real line goes to the unit circle: for real $x$, $|x-i|=|x+i|$. And $C(i)=0$, $C(0)=-1$, $C(\infty)=1$.</p>
