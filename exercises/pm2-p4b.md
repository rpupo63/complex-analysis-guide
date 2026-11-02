---
label: ex:schwarz-on-the-half-plane
source: Practice midterm 2, Problem 4(b)
title: Schwarz on the half-plane
placement: n14
order: 2
---
Let $\mathbb H:=\{z:\operatorname{Im}z\gt0\}$ and let $f:\mathbb H\to\mathbb H$ be holomorphic with $f(i)=i$. Let $C(z)=\frac{z-i}{z+i}$, a conformal map of $\mathbb H$ onto $D(0,1)$, and $g:=C\circ f\circ C^{-1}$. (i) Show $g$ maps $D(0,1)$ into $D(0,1)$, $g(0)=0$, and deduce $|g'(0)|\le1$. (ii) Show $g'(0)=f'(i)$. (iii) Conclude $|f'(i)|\le1$, and check equality for $f(z)=-1/z$.
<details class="sol"><summary>Hint</summary>
(ii) Chain rule, with $(C^{-1})'(0)=1/C'(i)$ (@thm:inverse).
</details>
<details class="sol"><summary>Solution</summary>
<ol type="i">
<li>$C^{-1}$ maps the disk to $\mathbb H$, $f$ maps $\mathbb H$ to $\mathbb H$, and $C$ maps $\mathbb H$ to the disk (@prop:cayley-map). $g$ is holomorphic as a composition. $g(0)=C(f(C^{-1}(0)))=C(f(i))=C(i)=0$. Schwarz lemma (@thm:schwarz-lemma): $|g'(0)|\le1$.</li>
<li>Chain rule: $g'(0)=C'(f(i))\,f'(i)\,(C^{-1})'(0)=C'(i)\,f'(i)\,\frac1{C'(i)}=f'(i)$, using $C^{-1}(0)=i$ and $(C^{-1})'(0)=1/C'(i)$ from the inverse theorem (@thm:inverse). (Explicitly $C'(z)=\frac{2i}{(z+i)^2}$, so $C'(i)=\frac1{2i}$.)</li>
<li>$|f'(i)|=|g'(0)|\le1$. For $f(z)=-\frac1z$: if $z=re^{i\theta}$ with $0\lt\theta\lt\pi$, then $-\frac1z=\frac1re^{i(\pi-\theta)}\in\mathbb H$; $f(i)=-\frac1i=i$; and $f'(z)=\frac1{z^2}$, so $f'(i)=-1$, $|f'(i)|=1$.</li>
</ol>
</details>
