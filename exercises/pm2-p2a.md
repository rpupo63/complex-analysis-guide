---
label: ex:polynomial-times-exponential
source: Practice midterm 2, Problem 2(a)
title: polynomial times exponential
placement: f5
order: 2
---
Let $f$ be entire with $|f(z)|\le(1+|z|)\,|e^z|$ for all $z$. Show that $f(z)=(a+bz)e^z$ for some $a,b\in\mathbb C$.
<details class="sol"><summary>Hint</summary>
Consider $g:=f\,e^{-z}$, and apply Cauchy's estimate to $g$.
</details>
<details class="sol"><summary>Solution</summary>
$g:=fe^{-z}$ is entire (a product of entire functions) with $|g|=|f|\,|e^z|^{-1}\le1+|z|$. Write $g=\sum b_nz^n$ (@thm:power-series; the $b_n=g^{(n)}(0)/n!$ do not depend on $R$, @thm:cauchys-formula-for-derivatives). Cauchy's estimate (@cor:cauchys-estimate) on $|z|=R$: $|b_n|\le(1+R)R^{-n}\to0$ as $R\to\infty$ for $n\ge2$. So $g(z)=a+bz$ and $f=(a+bz)e^z$. This is @rem:growth-bounds-the-same-proof with $k=1$.
</details>
