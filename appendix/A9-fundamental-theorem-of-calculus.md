---
id: A9
title: Fundamental theorem of calculus, piecewise version
status:
- cited
- derived
---
<div class="env"><span class="hd">Theorem (cited).</span> If $f$ is continuously differentiable on $[a,b]$, then $f(b)-f(a)=\int_a^bf'(s)\,ds$.</div>
<div class="env"><span class="hd">Corollary (proved).</span> If $f$ is continuous on $[a,b]$ and continuously differentiable on each piece $[t_{k-1},t_k]$ of a partition $a=t_0\lt t_1\lt\dots\lt t_m=b$, then $f(b)-f(a)=\int_a^bf'(s)\,ds$, where $f'$ may be left undefined at the finitely many $t_k$.</div>
::: proof
Apply the theorem on each piece and add:
\[ \sum_{k=1}^m\int_{t_{k-1}}^{t_k}f'=\sum_{k=1}^m\big(f(t_k)-f(t_{k-1})\big)=f(t_m)-f(t_0). \]
The sum telescopes because $f$ is continuous, so each $f(t_k)$ is the same number from both sides. The values of $f'$ at finitely many points do not affect the integral.
:::
<p>Poincaré's inequality applies this to $s\mapsto v(s,y)$; @prop:and-weakly-write applies it to $x\mapsto \class{ntn-Un}{U_n}\psi$. Both are continuous, and smooth between grid lines.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus" target="_blank" rel="noopener">Fundamental theorem of calculus</a></p>
