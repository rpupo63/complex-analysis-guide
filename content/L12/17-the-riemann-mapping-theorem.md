---
id: n17
slide: Slide 18
title: The Riemann mapping theorem
---

::: definition {#def:simply-connected name="simply connected"}
An open set $U\subseteq\mathbb C$ is <em>simply connected</em> if it is [connected](apx:C4) and each connected component of $\mathbb C\setminus U$ is unbounded. (This is equivalent to the usual definition, "every closed curve in $U$ can be shrunk to a point within $U$".) Examples: disks, half-planes, strips, $\mathbb C\setminus(-\infty,0]$. Not simply connected: the annulus $\{1\lt|z|\lt2\}$, whose complement has the bounded component $\{|z|\le1\}$.
:::

::: theorem {#thm:riemann-mapping-theorem-stated name="Riemann mapping theorem; stated" status=cited}
Let $U\ne\mathbb C$ be a nonempty, simply connected open set, and $z_0\in U$. There is exactly one conformal map $f$ of $U$ onto $D(0,1)$ with $f(z_0)=0$ and $f'(z_0)\gt0$.
:::
<p>Lecture 13 proves the existence for regions made of grid squares, and Lecture 14 for all (@thm:riemann-mapping-theorem-general). Three comments from the slide:</p>
<ul>
<li><b>$U\ne\mathbb C$ is needed,</b> by @cor:there-is-no-conformal-map.</li>
<li><b>Uniqueness</b> (proved here, @prop:uniqueness).</li>
<li><b>Boundary behaviour.</b> If $\partial U$ is a Jordan curve (a closed curve without self-intersections), $f$ extends to a homeomorphism of $\overline U$ onto $\overline{D(0,1)}$ (Carathéodory's theorem, cited). So the Dirichlet problem on $U$ becomes one on the disk: $h\mapsto h\circ f$, by @cor:transporting-harmonic-functions.</li>
</ul>

::: proposition {#prop:uniqueness name=uniqueness}
Two conformal maps $f,g$ of $U$ onto $D(0,1)$ with $f(z_0)=g(z_0)=0$ and $f'(z_0),g'(z_0)\gt0$ are equal.
:::
::: proof
$g\circ f^{-1}$ is an automorphism of the disk (@thm:inverse) fixing $0$. By @thm:automorphisms-of-the-disk it is $e^{i\theta}\varphi_a$, and $e^{i\theta}\varphi_a(0)=e^{i\theta}a=0$ forces $a=0$; as $\varphi_0(w)=-w$, $g\circ f^{-1}(w)=cw$ with $|c|=1$. So $g=cf$, and $g'(z_0)=cf'(z_0)$ with both derivatives positive: $c\gt0$, so $c=1$.
:::
