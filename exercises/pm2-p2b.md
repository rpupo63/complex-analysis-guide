---
label: ex:zeros-at-1-n-or-at
source: Practice midterm 2, Problem 2(b)
title: zeros at $1/n$ or at $n$
placement: k2
order: 2
---
Is there an entire function $f\not\equiv0$ with $f(\frac1n)=0$ for all integers $n\ge1$? Is there one with $f(n)=0$ for all integers $n\ge1$?
<details class="sol"><summary>Hint</summary>
Where do the zeros accumulate in each case?
</details>
<details class="sol"><summary>Solution</summary>
First: no. The zeros $\frac1n$ accumulate at $0\in\mathbb C$, so $f\equiv0$ by the identity theorem, @thm:identity-theorem-l10 (with $g=0$; compare @cor:isolated-zeros). Second: yes, for example $\sin\pi z$. The zeros $1,2,3,\dots$ have no limit point in $\mathbb C$, so the identity theorem says nothing. (Any sequence $|a_k|\to\infty$ is the zero set of an entire function: @thm:weierstrass.)
</details>
