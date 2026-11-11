---
id: q3
slide: Slide 4
title: Reflection for harmonic functions
---

::: setting {#set:a-symmetric-open-set name="a symmetric open set"}
$\Omega$ is open and symmetric about $\mathbb R$: $z\in\Omega\iff\bar z\in\Omega$. Write
\[ \Omega^\pm:=\Omega\cap\{\pm\operatorname{Im}z\gt0\},\qquad I:=\Omega\cap\mathbb R. \]
:::

::: theorem {#thm:harmonic-reflection name="reflection principle, harmonic form: the method of images"}
Let $v$ be harmonic on $\Omega^+$, continuous on $\Omega^+\cup I$, and $0$ on $I$. Define $V:=v$ on $\Omega^+\cup I$ and $V(z):=-v(\bar z)$ on $\Omega^-$. Then $V$ is harmonic on $\Omega$.
:::
::: proof

<ol>
<li><em>Away from $I$.</em> On $\Omega^+$, $V=v$. On $\Omega^-$, $z\mapsto\bar z$ preserves the Laplacian, so $V$ is harmonic there. $V$ is continuous on $\Omega$: as $z\in\Omega^-$ tends to $x\in I$, $V(z)=-v(\bar z)\to-v(x)=0=V(x)$. And $V$ is odd: $V(\bar z)=-V(z)$.</li>
<li><em>A square about a point of $I$.</em> Let $x\in I$, and let $Q\subseteq\Omega$ be a closed square centred at $x$ with sides parallel to the axes. $Q$ is a grid square, so by @thm:the-dirichlet-problem-on-a-union there is $w$ harmonic on the interior of $Q$, continuous on $Q$, with $w=V$ on $\partial Q$.</li>
<li><em>$w$ is odd.</em> $Q$ is symmetric about $\mathbb R$. The function $-w(\bar z)$ is harmonic inside $Q$, and on $\partial Q$ it equals $-V(\bar z)=V(z)$. By the uniqueness in @thm:the-dirichlet-problem-on-a-union, $-w(\bar z)=w(z)$. In particular $w=0$ on $Q\cap\mathbb R$.</li>
<li><em>$w=v$ on the upper half.</em> On the open upper half $Q^+$ of $Q$, $w-v$ is harmonic and continuous up to the boundary. On the boundary it is $0$: on the three sides in $\partial Q$, $w=V=v$, and on $Q\cap\mathbb R$, $w=0=v$. By the maximum principle (@cor:maximum-principle), applied to $\pm(w-v)$, $w=v$ on $Q^+$.</li>
<li><em>Conclusion.</em> On the lower half, $w(z)=-w(\bar z)=-v(\bar z)=V(z)$. So $V=w$ inside $Q$, and $V$ is harmonic near $x$. <span class="qed">∎</span></li>
</ol>
:::
<p>The slide writes "$w$ harmonic on $Q$"; this means on the interior of $Q$.</p>
