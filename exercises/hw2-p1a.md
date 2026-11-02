---
label: ex:one-solution-in-the-disk
source: Homework 2, Problem 1(a); Practice midterm 1, Problem 3
title: one solution in the disk
placement: m10
order: 1
---
Let $\lambda\gt1$. Show that $z\,e^{\lambda-z}=1$ has exactly one solution in $D(0,1)$, and that this solution is real and lies in $(0,1)$.
<details class="sol"><summary>Hint</summary>
Compare $z\,e^{\lambda-z}-1$ with $z\,e^{\lambda-z}$ on $|z|=1$ using @thm:rouche. For "real", use the intermediate value theorem on $[0,1]$.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>Rouché.</em> Let $f(z):=z\,e^{\lambda-z}$ and $g:=f-1$, both entire. On $|z|=1$, $|f(z)|=|z|\,|e^{\lambda-z}|=e^{\lambda-\operatorname{Re}z}\ge e^{\lambda-1}\gt1=|f-g|$, as $\operatorname{Re}z\le1$ and $\lambda\gt1$. By @thm:rouche, $g$ has as many zeros in $D(0,1)$ as $f$, counted with multiplicity. $f$ has exactly one: $e^{\lambda-z}\ne0$, so its only zero is at $0$, of order $1$ (@def:zero-of-order-m).</li>
<li><em>It is real.</em> $\phi(x):=x\,e^{\lambda-x}-1$ is continuous on $[0,1]$ with $\phi(0)=-1\lt0$ and $\phi(1)=e^{\lambda-1}-1\gt0$, so it vanishes at some $x_0\in(0,1)$ by the intermediate value theorem ([A.24](apx:A24)). That is a solution in $D(0,1)$, and by step 1 there is only one, so it is $x_0$.</li>
</ol>
</details>
