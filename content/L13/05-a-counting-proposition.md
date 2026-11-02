---
id: o5
slide: Slide 6
title: A counting proposition
---

::: proposition {#prop:counting name=counting}
Let $\Omega$ be a bounded connected open set, $f$ holomorphic and not constant on $\Omega$, with $|f(z)|\to1$ as $z\to\partial\Omega$. Then $f(\Omega)\subseteq D(0,1)$, and $f$ takes every $w\in D(0,1)$ exactly $d\ge1$ times, where $d$ is the number of zeros of $f$ (with multiplicity).
:::
::: proof

<ol>
<li><em>$|f|\lt1$.</em> Extend $|f|$ by $1$ on $\partial\Omega$: by hypothesis this is continuous on the compact set $\overline\Omega$, so it attains a maximum. If $|f(z_1)|\ge1$ for some $z_1\in\Omega$, the maximum is $\ge1$ and is attained at a point of $\Omega$ (at $z_1$ if it equals $1$; at an interior point anyway if it exceeds $1$, as boundary values are $1$). That contradicts @rem:maximum-modulus-again. So $|f|\lt1$ on $\Omega$.</li>
<li><em>A compact set holding all small values.</em> Fix $\rho\lt1$ and let $K_\rho:=\{z\in\overline\Omega:|f(z)|\le\rho\}$ (with $|f|=1$ on $\partial\Omega$). It is closed and bounded, hence compact, and it misses $\partial\Omega$; so it lies in $\Omega$ at a positive distance $\eta$ from $\partial\Omega$ ([C.5](apx:C5)).</li>
<li><em>A polygon around it.</em> Take a grid of side $\eps$ with $\eps\sqrt2\lt\eta$, and let $R$ be the union of the closed grid squares that meet $K_\rho$. Each such square lies within $\eps\sqrt2$ of $K_\rho$, so $R\subset\Omega$. Every point of $K_\rho$ lies in the interior of $R$ (all the closed squares containing it meet $K_\rho$). So on the boundary $\Gamma:=\partial R$, which is made of grid segments, $|f|\gt\rho$.</li>
<li><em>Count by the argument principle.</em> For $|w|\lt\rho$, every solution of $f(z)=w$ in $\Omega$ has $|f(z)|\lt\rho$, so it lies in $K_\rho$, inside $R$; there are finitely many (isolated zeros in a compact set). The argument principle, proved as for circles but on the region $R$ (with @prop:other-contours in place of @thm:residue-theorem), gives the number of solutions as
\[ N(w)=\frac1{2\pi i}\oint_\Gamma\frac{f'(z)}{f(z)-w}\,dz. \]</li>
<li><em>$N$ is constant.</em> On $\Gamma$, $|f-w|\ge\min_\Gamma|f|-\rho=:\mu\gt0$ for all $|w|\lt\rho$ ($\min_\Gamma|f|\gt\rho$, by compactness of $\Gamma$). So
\[ |N(w)-N(w')|\le\frac{\operatorname{length}(\Gamma)}{2\pi}\max_\Gamma|f'|\cdot\frac{|w-w'|}{\mu^2}, \]
using $\frac1{f-w}-\frac1{f-w'}=\frac{w-w'}{(f-w)(f-w')}$. $N$ is continuous and integer-valued on the connected disk $D(0,\rho)$, hence constant ([A.24](apx:A24), along segments from $0$): $N(w)=N(0)=d$.</li>
<li><em>All values, and $d\ge1$.</em> Every $w\in D(0,1)$ lies in some $D(0,\rho)$, so it is taken exactly $d$ times. And $d\ge1$: $f(\Omega)$ is a nonempty subset of $D(0,1)$, so some $w$ is taken at least once. <span class="qed">∎</span></li>
</ol>
:::
<p>The idea in one line: the number of solutions of $f=w$ cannot change as $w$ moves, because no solution can escape through the boundary, where $|f|$ is close to $1$.</p>
