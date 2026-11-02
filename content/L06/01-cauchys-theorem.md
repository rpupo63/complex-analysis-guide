---
id: f1
slide: Slide 2
title: Cauchy's theorem
---
<p>Part I proved Cauchy's theorem in the language of electrostatics (@cor:cauchys-theorem): a charge-free field has zero contour integral. Part II restates it for regions bounded by circles, with a short self-contained proof, and builds the whole theory on it. First, a convention fixes what "holomorphic" will mean from now on.</p>

::: convention {#conv:holomorphic-near-k name="holomorphic near $K$"}
"$f$ is holomorphic near $K$" means: $f$ is holomorphic (@def:holomorphic), with $C^1$ real and imaginary parts, on some [open](apx:C2) set containing $K$.
:::
<p>The $C^1$ requirement is what Green's theorem needs. It is weaker than Standing @asm:from-now-on-holomorphic-functions ($C^2$ parts), and @cor:holomorphic-functions-are-smooth shows that it already makes $f$ infinitely differentiable. For why the requirement can be dropped altogether, see [Goursat's theorem](apx:E2). "Near $K$" lets us work on a closed set $K$, such as a closed disk, without worrying about what happens exactly on its edge.</p>

::: theorem {#thm:cauchys-theorem name="Cauchy's theorem"}
Let $D$ be a closed region bounded by finitely many circles, and let $f$ be holomorphic near $D$. Then
\[ \oint_{\partial D}f\,dz=0, \]
where $\partial D$ is oriented with $D$ on its left.
:::
<p>"Bounded by finitely many circles" covers a closed disk, a closed annulus, and a disk with several round holes. With $D$ on the left, the outer circle runs anticlockwise and each inner circle clockwise ([orientation](apx:C3)).</p>
::: proof
Write $f=u+iv$ and $dz=dx+i\,dy$ (the contour integral of @def:contour-integral). Multiplying out,
\[ f\,dz=(u+iv)(dx+i\,dy)=(u\,dx-v\,dy)+i\,(v\,dx+u\,dy). \]
[Green's theorem](apx:A6) says $\oint_{\partial D}P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dA$ for $C^1$ functions $P,Q$ on a neighbourhood of $D$, including regions with holes. Apply it twice:
<ul>
<li>real part, $P=u$, $Q=-v$: $\ \oint(u\,dx-v\,dy)=\iint_D(-v_x-u_y)\,dA$;</li>
<li>imaginary part, $P=v$, $Q=u$: $\ \oint(v\,dx+u\,dy)=\iint_D(u_x-v_y)\,dA$.</li>
</ul>
By the Cauchy–Riemann equations (@thm:cauchy-riemann), $u_x=v_y$ and $u_y=-v_x$, so both integrands vanish identically:
\[ \oint_{\partial D}f\,dz=\iint_D(-v_x-u_y)\,dA+i\iint_D(u_x-v_y)\,dA=0+i\cdot0=0. \]
<span class="qed">∎</span>
:::
<p>Compare Lecture 2: there $f=u-iv$ was attached to a field $(u,v)$ ([sign conventions](apx:E1)), and the two integrals were the circulation and the flux. Here the same two integrals are killed directly by Cauchy–Riemann.</p>
