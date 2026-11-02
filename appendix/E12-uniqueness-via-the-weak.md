---
id: E12
title: Uniqueness via the weak maximum principle
status:
- derived
---
<div class="env"><span class="hd">Theorem (weak maximum principle).</span> Let $\Omega$ be bounded and open, and let $u$ be twice continuously differentiable in $\Omega$, continuous on $\overline\Omega$, with $\class{ntn-Delta}{\Delta} u=0$. Then $\max_{\overline\Omega}u=\max_{\class{ntn-dOm}{\partial\Omega}}u$.</div>
::: proof
Fix $\delta\gt0$ and put $v:=u+\delta(x^2+y^2)$. Then $\class{ntn-Delta}{\Delta} v=\class{ntn-Delta}{\Delta} u+4\delta=4\delta\gt0$. $v$ is continuous on the compact set $\overline\Omega$, so it attains a maximum there ([extreme value theorem](apx:C2)). Suppose the maximum is at an interior point $P$. Then $x\mapsto v(x,P_y)$ has a local maximum at $P_x$, so its second derivative there is $\le0$; likewise in $y$. So $\class{ntn-Delta}{\Delta} v(P)\le0$, a contradiction. The maximum of $v$ is therefore on $\class{ntn-dOm}{\partial\Omega}$. With $R$ such that $x^2+y^2\le R^2$ on $\overline\Omega$,
\[ u\le v\le\max_{\class{ntn-dOm}{\partial\Omega}}v\le\max_{\class{ntn-dOm}{\partial\Omega}}u+\delta R^2. \]
Let $\delta\to0$.
:::
<div class="env"><span class="hd">Corollary (uniqueness).</span> The Dirichlet problem has at most one solution.</div>
::: proof
If $u_1,u_2$ both solve it, $w=u_1-u_2$ is harmonic with $w=0$ on $\class{ntn-dOm}{\partial\Omega}$. The theorem gives $w\le0$, and applied to $-w$ it gives $w\ge0$.
:::
<p>This is a third proof of uniqueness, alongside the energy method of Lecture 2 (@thm:uniqueness) and the strong maximum principle of Lecture 4 (@cor:stability). @thm:discrete-maximum-principle is the discrete counterpart, proved by the averaging property rather than second derivatives. Lecture 4 reproves this result the same way, through the mean value property: @thm:strong-maximum-principle and @cor:maximum-principle, [#](@cor:stability).</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Maximum_principle" target="_blank" rel="noopener">Maximum principle</a> · <a href="https://en.wikipedia.org/wiki/Dirichlet_problem" target="_blank" rel="noopener">Dirichlet problem</a></p>
