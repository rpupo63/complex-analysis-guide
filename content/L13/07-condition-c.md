---
id: o7
slide: Slide 8
title: Condition (C)
---

::: proposition {#prop:c-is-necessary name="(C) is necessary"}
If $\Omega$ has a conformal map $f$ onto $D(0,1)$, then (C) holds. The annulus $\{1\lt|z|\lt2\}$ fails (C), so it has no conformal map onto the disk.
:::
::: proof
Let $u$ be harmonic on $\Omega$. Then $u\circ f^{-1}$ is harmonic on the disk (@thm:harmonic-composed-with-holomorphic), so $u\circ f^{-1}=\operatorname{Re}F$ with $F$ holomorphic on the disk (@lem:harmonic-conjugate-on-a-disk), and $u=\operatorname{Re}(F\circ f)$.<br>
On the annulus, $\log|z|$ is harmonic but not a real part: as in @rem:the-disk-matters, it would force $F'=\frac1z$, and then $\oint_{|z|=3/2}\frac{dz}z=\oint F'\,dz=0$, not $2\pi i$.
:::

::: lemma {#lem:star-shaped-sets-satisfy-c name="star-shaped sets satisfy (C)"}
If $\Omega$ is star-shaped about $c$ (the segment $[c,z]\subseteq\Omega$ for all $z\in\Omega$), then every harmonic $u$ on $\Omega$ is the real part of a holomorphic function.
:::
::: proof

<ol>
<li><em>A holomorphic candidate for $F'$.</em> Let $g:=u_x-iu_y$. Its real and imaginary parts $a=u_x$, $b=-u_y$ are $C^1$ and satisfy Cauchy–Riemann: $a_x=u_{xx}=-u_{yy}=b_y$ (harmonic), and $a_y=u_{xy}=u_{yx}=-b_x$ ([mixed partials](apx:A2)). So $g$ is holomorphic.</li>
<li><em>Integrate from the centre.</em> Let $F(z):=u(c)+\int_{[c,z]}g(\zeta)\,d\zeta$, along the segment (which lies in $\Omega$).</li>
<li><em>Moving the endpoint.</em> Let $D(z,r)\subseteq\Omega$ and $|k|\lt r$. The closed triangle with vertices $c$, $z$, $z+k$ lies in $\Omega$: each of its points lies on a segment from $c$ to a point of $[z,z+k]\subseteq D(z,r)\subseteq\Omega$, and such segments lie in $\Omega$ by star-shapedness. Cauchy's theorem on the triangle (@prop:other-contours) gives $\int_{[c,z+k]}g=\int_{[c,z]}g+\int_{[z,z+k]}g$, so
\[ F(z+k)-F(z)=\int_{[z,z+k]}g(\zeta)\,d\zeta=k\,g(z)+\int_{[z,z+k]}\big(g(\zeta)-g(z)\big)\,d\zeta=k\,g(z)+o(|k|), \]
the last integral being at most $|k|\max_{[z,z+k]}|g-g(z)|$ (ML estimate), which is $o(|k|)$ by continuity of $g$.</li>
<li><em>Compare gradients.</em> So $F$ is holomorphic with $F'=g=u_x-iu_y$. For any holomorphic $F=U+iV$, $F'=U_x+iV_x=U_x-iU_y$ (Cauchy–Riemann). So $U_x=u_x$ and $U_y=u_y$: $\nabla\operatorname{Re}F=\nabla u$. Then $\operatorname{Re}F-u$ has zero gradient on the connected set $\Omega$, so it is constant; at $c$ it is $\operatorname{Re}F(c)-u(c)=0$. So $u=\operatorname{Re}F$. <span class="qed">∎</span></li>
</ol>
:::
<p>This is @lem:harmonic-conjugate-on-a-disk with segments from $c$ in place of horizontal-then-vertical paths. The proof works whenever the integral of $g$ does not depend on the path, which is the real content of "simply connected": no holes for the integral to wind around.</p>
