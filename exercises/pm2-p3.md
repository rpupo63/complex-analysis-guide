---
label: ex:counting-solutions-with-rouche
source: Practice midterm 2, Problem 3
title: counting solutions with Rouché
placement: m10
order: 5
---
Let $n\ge1$ and $|a|\gt e$. Show that $e^z=az^n$ has exactly $n$ solutions in $D(0,1)$, counted with multiplicity.
<details class="sol"><summary>Hint</summary>
Which of $az^n$ and $e^z$ is bigger on $|z|=1$?
</details>
<details class="sol"><summary>Solution</summary>
On $|z|=1$: $|az^n|=|a|\gt e\ge e^{\operatorname{Re}z}=|e^z|$. Take $f=az^n$ and $g=az^n-e^z$ in @thm:rouche: $|f-g|=|e^z|\lt|f|$, so $g$ has as many zeros in $D(0,1)$ as $az^n$, namely $n$ (a zero of order $n$ at $0$, @def:zero-of-order-m). The zeros of $g$ are exactly the solutions of $e^z=az^n$.
</details>
