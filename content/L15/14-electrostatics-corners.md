---
id: q14
slide: Slide 17
title: 'Electrostatics: corners'
---

<p>The potential $u$ is harmonic outside the conductors and constant on each one, and the field is $E=-\nabla u$. Locally $u=\operatorname{Im}\Phi$ with $\Phi$ holomorphic (@lem:harmonic-conjugate-on-a-disk), and $|E|=|\Phi'|$, by the Cauchy–Riemann equations.</p>

::: proposition {#prop:the-field-near-a-corner name="the field near a corner"}
Let $F$ map $\mathbb H$ conformally onto the interior of $P$, and let $u$ be harmonic inside $P$, continuous up to $\partial P$, and constant on the two sides of $P$ at a vertex $w_k$ with angle $\alpha_k\pi$. Then for $w$ in $P$ near $w_k$,
\[ |E(w)|\approx c_1\,|w-w_k|^{1/\alpha_k-1}, \]
where $c_1\gt0$ unless the derivative $\Psi'(x_k)$ below vanishes.
:::
::: proof
$v:=u\circ F$ is harmonic on $\mathbb H$ (@thm:harmonic-composed-with-holomorphic) and equal to a constant $c$ on $\mathbb R$ near $x_k$. By @thm:harmonic-reflection and @lem:harmonic-conjugate-on-a-disk, $v-c=\operatorname{Im}\Psi$ near $x_k$, with $\Psi$ holomorphic and real on $\mathbb R$. In general $\Psi'(x_k)\ne0$. By step 2 of the proof of @thm:schwarz-christoffel, $F^{-1}(w)=h^{-1}\big((w-w_k)^{1/\alpha_k}\big)$ with $h'(x_k)\ne0$, so $|(F^{-1})'(w)|\approx c\,|w-w_k|^{1/\alpha_k-1}$. As $u-c=\operatorname{Im}(\Psi\circ F^{-1})$,
\[ |E(w)|=|\Psi'(F^{-1}(w))|\,|(F^{-1})'(w)|\approx c_1|w-w_k|^{1/\alpha_k-1}. \]
:::
<ul>
<li><b>Convex corner</b> ($\alpha_k\lt1$): $E\to0$. At a right angle, $|E|\approx c_1r$, with $r=|w-w_k|$.</li>
<li><b>Re-entrant corner</b> ($\alpha_k\gt1$): $E\to\infty$. At the edge of a thin plate ($\alpha_k=2$), $|E|\approx c_1r^{-1/2}$. Field and charge concentrate at sharp edges, and electric discharges start there.</li>
</ul>
<p>The case $\alpha_k=2$ is a slit, not a vertex of a polygon in the sense of @def:polygon, where $\alpha_k\lt2$. The same argument works there: $(F-w_k)^{1/2}$ is still a branch on the slit neighbourhood. The capacitor of @sec:q15 is such a case.</p>
