---
id: o4
slide: Slide 5
title: 'Existence: the construction'
---
::: proof {title="Proof of existence in Theorem [#](=thm:riemann-mapping-theorem)."}
Fix $z_0\in\Omega$.
<ol>
<li><em>Solve a Dirichlet problem.</em> $\log|z-z_0|$ is continuous on $\partial\Omega$ (as $z_0\notin\partial\Omega$). By (D) there is $h$ harmonic on $\Omega$, continuous on $\overline\Omega$, with $h(z)=\log|z-z_0|$ on $\partial\Omega$.</li>
<li><em>Complete it to a holomorphic function.</em> By (C), $h=\operatorname{Re}H$ with $H$ holomorphic on $\Omega$. Replacing $H$ by $H-i\operatorname{Im}H(z_0)$ (which does not change the real part) makes $H(z_0)=h(z_0)$ real.</li>
<li><em>Define the map.</em>
\[ f(z):=(z-z_0)\,e^{-H(z)}. \]</li>
<li><em>Property 1: one simple zero, positive derivative.</em> $f$ is holomorphic on $\Omega$. As $e^{-H}$ never vanishes, its only zero is $z_0$, and it is simple, with $f'(z_0)=e^{-H(z_0)}=e^{-h(z_0)}\gt0$.</li>
<li><em>Property 2: $|f|\to1$ at the boundary.</em> $\log|f(z)|=\log|z-z_0|-h(z)$. This function is continuous on $\overline\Omega$ minus a small disk about $z_0$ (a compact set) and equals $0$ on $\partial\Omega$. By uniform continuity ([A.16](apx:A16)), it is within any given $\epsilon$ of $0$ at all points close enough to $\partial\Omega$. So $|f(z)|\to1$ as $z\to\partial\Omega$.</li>
<li><em>Conclude.</em> By the counting proposition (@prop:counting), $f$ takes every value $w\in D(0,1)$ exactly $d$ times, where $d=1$ is its number of zeros (property 1), and takes no other values. So $f$ is a bijection of $\Omega$ onto $D(0,1)$: a conformal map, with $f(z_0)=0$, $f'(z_0)\gt0$. <span class="qed">∎</span></li>
</ol>
:::
<p>Only two properties of $f$ were used: exactly one zero, and $|f|\to1$ at the boundary. Everything else (injectivity, surjectivity) comes from counting.</p>
