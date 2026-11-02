---
label: ex:moving-the-zero-to-the-centre
source: Practice midterm 3, Problem 4(b)
title: moving the zero to the centre
placement: n14
order: 3
---
Let $f:D(0,1)\to D(0,1)$ be holomorphic with $f(\frac12)=0$. Let $\varphi(z):=\frac{\frac12-z}{1-\frac12z}$, an automorphism of $D(0,1)$, and $g:=f\circ\varphi$. (i) Show $g$ maps $D(0,1)$ into $D(0,1)$ and $g(0)=0$. (ii) Show $f(0)=g(\frac12)$, and conclude $|f(0)|\le\frac12$. (iii) Find an $f$ with $f(\frac12)=0$ and $|f(0)|=\frac12$.
<details class="sol"><summary>Hint</summary>
$\varphi=\varphi_{1/2}$ of @lem:is-an-automorphism-of-with: it swaps $0$ and $\frac12$.
</details>
<details class="sol"><summary>Solution</summary>
<ol type="i">
<li>$\varphi=\varphi_{1/2}$ in the notation of @def:automorphism-varphi-a, an automorphism of the disk (@lem:is-an-automorphism-of-with), so $g=f\circ\varphi$ maps the disk into itself, and $g(0)=f(\varphi(0))=f(\frac12)=0$.</li>
<li>$\varphi(\frac12)=0$ (@lem:is-an-automorphism-of-with), so $g(\frac12)=f(\varphi(\frac12))=f(0)$. Schwarz lemma (@thm:schwarz-lemma) for $g$: $|f(0)|=|g(\frac12)|\le\frac12$.</li>
<li>$f=\varphi$ itself: it maps the disk into itself (@lem:is-an-automorphism-of-with), $f(\frac12)=0$ and $f(0)=\frac12$. (So does any $e^{i\theta}\varphi$.)</li>
</ol>
</details>
