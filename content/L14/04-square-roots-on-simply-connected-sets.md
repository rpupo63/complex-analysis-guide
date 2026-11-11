---
id: p4
slide: Reconstructed
title: Square roots on simply connected sets
---

::: fact {#fact:simply-connected-sets-satisfy-c name="simply connected sets satisfy (C)" status=cited}
If $\Omega$ is simply connected (@def:simply-connected), every harmonic function on $\Omega$ is the real part of a holomorphic function on $\Omega$.
:::
<p>Lecture 13 states this without proof (@sec:o2) and proves it for star-shaped sets (@lem:star-shaped-sets-satisfy-c). Its proof works whenever the integral of $u_x-iu_y$ does not depend on the path, and on a simply connected set that is the general form of Cauchy's theorem. This is the one result the lecture uses without proving it.</p>

::: corollary {#cor:logarithms-and-square-roots name="logarithms and square roots"}
Let $\Omega$ be simply connected and $h$ holomorphic and nonzero on $\Omega$. Then $h=e^G$ for some $G$ holomorphic on $\Omega$, and $k:=e^{G/2}$ satisfies $k^2=h$.
:::
::: proof
$\log|w|$ is harmonic on $\mathbb C\setminus\{0\}$ ([E.6](apx:E6)), so $\log|h|$ is harmonic on $\Omega$ (@thm:harmonic-composed-with-holomorphic). By @fact:simply-connected-sets-satisfy-c, $\log|h|=\operatorname{Re}G_0$ with $G_0$ holomorphic on $\Omega$. Then $he^{-G_0}$ is holomorphic with modulus $e^{\log|h|-\operatorname{Re}G_0}=1$. Its values lie on the unit circle, which contains no open set, so by the open mapping theorem (@thm:open-mapping) it is a constant $e^{i\theta}$. So $h=e^G$ with $G:=G_0+i\theta$.
:::

::: lemma {#lem:a-map-into-the-disk name="a map into the disk"}
Let $\Omega\ne\mathbb C$ be simply connected and $z_0\in\Omega$. There is $\Phi$ holomorphic on $\Omega$ with $|\Phi|\lt1$ and $\Phi'(z_0)\ne0$.
:::
::: proof

<ol>
<li><em>A square root.</em> Pick $a\notin\Omega$. By @cor:logarithms-and-square-roots there is $k$ holomorphic on $\Omega$ with $k(z)^2=z-a$. It is injective, since $k(z_1)=k(z_2)$ gives $z_1-a=z_2-a$, and it never takes the value $0$. Also $k'(z_0)=1/(2k(z_0))\ne0$.</li>
<li><em>$k$ misses a disk.</em> Let $b:=k(z_0)$. $k(\Omega)$ is open (@thm:open-mapping), so it contains a disk $D(b,\rho)$. If $\zeta=k(z_1)$ had $|\zeta+b|\lt\rho$, then $-\zeta\in D(b,\rho)$, so $-\zeta=k(z_2)$; squaring, $z_1-a=z_2-a$, so $z_1=z_2$ and $\zeta=-\zeta=0$, which is impossible. So $|k+b|\ge\rho$ on $\Omega$.</li>
<li><em>Into the disk.</em> $\Phi:=\rho/(k+b)$ is holomorphic with $|\Phi|\le1$, and $\Phi'(z_0)=-\rho\,k'(z_0)/(2b)^2\ne0$. $\Phi$ is not constant, so $\Phi(\Omega)$ is an open subset of the closed disk, hence of the open disk: $|\Phi|\lt1$. <span class="qed">∎</span></li>
</ol>
:::
<p>$\Omega\ne\mathbb C$ is used exactly here, through the point $a$. For $\Omega=\mathbb C$ there is no such $\Phi$: it would be a bounded nonconstant entire function, against Liouville (@cor:there-is-no-conformal-map).</p>
