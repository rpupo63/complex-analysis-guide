---
label: ex:holomorphic-on-the-disk-but-not
source: Practice midterm 3, Problem 2(b)
title: holomorphic on the disk but not entire
placement: k2
order: 3
---
Is there a holomorphic $f:D(0,1)\to\mathbb C$ with $f(\frac1n)=\frac1{n+1}$ for all integers $n\ge2$? Is there an entire one?
<details class="sol"><summary>Hint</summary>
Write $\frac1{n+1}$ as a function of $\frac1n$. For the entire question, where would that function have to be singular?
</details>
<details class="sol"><summary>Solution</summary>
<ul>
<li><em>On the disk: yes.</em> $\frac1{n+1}=\frac{1/n}{1+1/n}$, so $f(z)=\frac z{1+z}$ works; its only pole, $-1$, is outside $D(0,1)$. (It is the only one, by @thm:identity-theorem-l10 on the connected set $D(0,1)$.)</li>
<li><em>Entire: no.</em> If $F$ were entire with these values, then $F$ and $\frac z{1+z}$ are holomorphic on the connected ([C.4](apx:C4)) open set $\mathbb C\setminus\{-1\}$ and agree at the points $\frac1n\to0$, so $F=\frac z{1+z}$ on all of $\mathbb C\setminus\{-1\}$ by the identity theorem (@thm:identity-theorem-l10). But $\frac z{1+z}\to\infty$ as $z\to-1$, while $F$ is continuous at $-1$. Contradiction.</li>
</ul>
</details>
