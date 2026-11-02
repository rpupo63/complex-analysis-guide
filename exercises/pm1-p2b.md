---
label: ex:prescribed-values-at-1-n
source: Practice midterm 1, Problem 2(b)
title: prescribed values at $1/n$
placement: k2
order: 1
---
Is there an entire function $f$ with $f(\frac1n)=\frac1{n^2}$ for all integers $n\ge1$, and $f(2)=2$?
<details class="sol"><summary>Hint</summary>
Which entire function takes the values $\frac1{n^2}$ at $\frac1n$? Use the identity theorem (@thm:identity-theorem-l10).
</details>
<details class="sol"><summary>Solution</summary>
No. $f$ and $z^2$ are entire and agree at the points $\frac1n\to0\in\mathbb C$, so $f=z^2$ on the connected ([C.4](apx:C4)) set $\mathbb C$ by the identity theorem, @thm:identity-theorem-l10 (the limit point $0$ lies in $\mathbb C$, and $\frac1n\ne0$). Then $f(2)=4\ne2$.
</details>
