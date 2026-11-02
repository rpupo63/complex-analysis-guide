---
id: g3
slide: Slide 4
title: The argument principle
---

::: theorem {#thm:argument-principle name="argument principle"}
Let $f$ be holomorphic near $\{|z|\le R\}\setminus\{\zeta_1,\dots,\zeta_p\}$, with poles at $\zeta_1,\dots,\zeta_p\in\{|z|\lt R\}$, and $f\ne0$ on $C:=\{|z|=R\}$. Let $\class{ntn-ZP}{Z}$ and $\class{ntn-ZP}{P}$ be the numbers of zeros and of poles of $f$ in $|z|\lt R$, counted with multiplicity (each zero or pole counted as often as its order). Then
\[ \frac1{2\pi i}\oint_C\frac{f'(z)}{f(z)}\,dz=\class{ntn-ZP}{Z}-\class{ntn-ZP}{P}. \]
:::
<p>The name: along $C$, $\frac{f'}{f}dz$ is the change in a logarithm of $f(z)$, whose imaginary part is the argument. So the integral is the number of times $f(z)$ winds around $0$ as $z$ goes once around $C$; see [winding numbers](apx:E17).</p>

::: proof {title="Proof, part 1: $\class{ntn-ZP}{Z}$ is finite."}

<ol>
<li>$\Omega:=\{|z|\lt R\}\setminus\{\zeta_1,\dots,\zeta_p\}$ is open, and [connected](apx:C4) (any two of its points can be joined by a path in the disk that detours around the finitely many $\zeta_j$).</li>
<li>$f\not\equiv0$ on $\Omega$: $f$ is continuous and nonzero on $C$, so it is nonzero at points of $\Omega$ close to $C$.</li>
<li>By the isolated zeros theorem (@thm:isolated-zeros) each zero of $f$ in $\Omega$ is isolated, and its Taylor coefficients are not all $0$ (step 1 of that proof), so it has a finite order. Otherwise $f\equiv0$ near it.</li>
<li>Suppose there were infinitely many distinct zeros $z_k$. They lie in the compact disk $|z|\le R$, so a subsequence converges to some $w$ with $|w|\le R$ (Bolzano–Weierstrass, [C.5](apx:C5)). Then:
<ul>
<li>$w$ is not a pole: near a pole, $|f|=|g|/|z-\zeta|^m\to\infty$, but $f(z_k)=0$;</li>
<li>so $f$ is continuous at $w$, and $f(w)=\lim f(z_k)=0$; in particular $w\notin C$;</li>
<li>so $w\in\Omega$ is a zero that is a limit of other zeros, i.e. not isolated. This contradicts step 3.</li>
</ul></li>
</ol>
So there are finitely many zeros, each of finite order, and $\class{ntn-ZP}{Z}$ is a finite number.
:::
