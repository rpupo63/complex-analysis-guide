---
id: t4
slide: Slide 4
title: The strong maximum principle
toc: Strong maximum principle
---

::: theorem {#thm:strong-maximum-principle name="strong maximum principle"}
Let $\Omega$ be open and [connected](apx:C4), and let $h$ be $C^2$ and harmonic on $\Omega$. If $h(z_0)=\sup_\Omega h$ at some point $z_0\in\Omega$, then $h$ is constant on $\Omega$.
:::
::: proof
Put $M:=h(z_0)$, which is the [supremum](apx:A14) of $h$, so $h\le M$ everywhere on $\Omega$. Let $S:=\{z\in\Omega:h(z)=M\}$.
<ol>
<li><em>$S$ is not empty:</em> $z_0\in S$.</li>
<li><em>$S$ is [closed in $\Omega$](apx:C4).</em> If $z_k\in S$ and $z_k\to z\in\Omega$, then $h(z)=\lim h(z_k)=M$ by continuity, so $z\in S$.</li>
<li><em>$S$ is open.</em> Let $z_1\in S$. Since $\Omega$ is open, there is $r\gt0$ with the closed disk $|z-z_1|\le r$ inside $\Omega$. Fix $0\lt t\le r$. By @thm:mean-value-property with radius $t$,
\[ M=h(z_1)=\frac1{2\pi}\int_0^{2\pi}h(z_1+te^{i\theta})\,d\theta. \]
So $\varphi(\theta):=M-h(z_1+te^{i\theta})$ is continuous, nonnegative (because $h\le M$), and
\[ \int_0^{2\pi}\varphi(\theta)\,d\theta=2\pi M-2\pi M=0. \]
A continuous nonnegative function with zero integral is identically zero ([zero integral forces zero](apx:A11), interval version). This is the slide's argument: if $h\lt M$ at one point of $\class{ntn-Ct}{C_t}$, then $h\lt M$ on a whole arc around it, and the average would be less than $M$. So $h=M$ on the circle of radius $t$ about $z_1$. Every point $z$ with $0\lt|z-z_1|\lt r$ lies on such a circle (take $t=|z-z_1|$), and $z_1\in S$ already. So the open disk of radius $r$ about $z_1$ lies in $S$.</li>
<li><em>Conclude.</em> In a connected set, the only subsets that are both open and closed are the empty set and the whole set ([C.4](apx:C4)). $S$ is nonempty, open and closed in $\Omega$, so $S=\Omega$: $h\equiv M$. <span class="qed">∎</span></li>
</ol>
:::

::: remark {#rem:why-strong name="why \"strong\""}
The weak maximum principle ([E.12](apx:E12)) says the maximum over $\overline\Omega$ is reached <em>somewhere</em> on the boundary. The strong one says more: a harmonic function on a connected set cannot reach its maximum at an interior point at all, unless it is constant. Two things in the hypothesis matter. Connectedness: on two separate disks, $h=0$ on one and $h=1$ on the other is harmonic, reaches its supremum inside, and is not constant. And the supremum must be <em>attained</em> at a point of $\Omega$; the theorem says nothing if it is only approached at the boundary.
:::
