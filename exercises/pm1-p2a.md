---
label: ex:a-growth-bound-forces-zero
source: Practice midterm 1, Problem 2(a)
title: a growth bound forces zero
placement: f5
order: 1
---
Let $f$ be entire with $|f(z)|\le|z|^{5/2}$ for all $z\in\mathbb C$. Show that $f\equiv0$.
<details class="sol"><summary>Hint</summary>
Write $f=\sum a_nz^n$ and use Cauchy's estimate (@cor:cauchys-estimate) on $|z|=R$: once with $R\to\infty$, once with $R\to0$. (Compare @rem:growth-bounds-the-same-proof.)
</details>
<details class="sol"><summary>Solution</summary>
$f$ is entire, so $f=\sum a_nz^n$ on all of $\mathbb C$, with $a_n=f^{(n)}(0)/n!$ independent of the circle used ([Theorems #](@thm:power-series) and [#](@thm:cauchys-formula-for-derivatives)). By Cauchy's estimate (@cor:cauchys-estimate) on $|z|=R$, with $M=\max_{|z|=R}|f|\le R^{5/2}$, $|a_n|\le R^{5/2}R^{-n}=R^{5/2-n}$ for every $R\gt0$. For $n\ge3$ the exponent is negative: let $R\to\infty$, so $a_n=0$. For $n\le2$ it is positive: let $R\to0$, so $a_n=0$. Hence $f\equiv0$. (In words: the bound makes $f$ grow too slowly at $\infty$ for degree $\ge3$, and vanish too fast at $0$ for degree $\le2$.)
</details>
