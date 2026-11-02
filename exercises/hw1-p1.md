---
label: ex:a-holomorphic-flow
source: Homework 1, Problem 1
title: a holomorphic flow
placement: x16
order: 1
---
Consider the complex potential $F(z)=\frac{z^3}3$, with velocity field $V=\overline{F'(z)}$ (@prop:so-is-the-flow-associated).
<ol>
<li>Write $V=(u,v)$ explicitly in terms of $x$ and $y$.</li>
<li>Verify directly that $V$ is divergence-free and curl-free.</li>
<li>Find an equation for the streamlines, and sketch the streamline $\operatorname{Im}F=0$ with several nearby streamlines. Indicate the direction of the flow.</li>
<li>Find every stagnation point and express the speed $|V|$ in terms of $|z|$.</li>
<li>Let $C$ be the vertical segment from $A=(0,-1)$ to $B=(0,1)$, oriented upward. Compute the flux across $C$ both directly and from $\operatorname{Im}F(B)-\operatorname{Im}F(A)$.</li>
</ol>
<details class="sol"><summary>Hint</summary>
<ul>
<li>If $F'=a+ib$, then $V=(a,-b)$.</li>
<li>Expand $(x+iy)^2$ and $(x+iy)^3$ before taking real and imaginary parts.</li>
<li>Streamlines are the level curves $\operatorname{Im}F=c$ (@prop:psi-is-conserved-along-streamlines).</li>
<li>On an oriented curve, the convention is $n\,ds=(dy,-dx)$ (@sec:x12).</li>
<li>Your two flux calculations should agree in sign as well as size (@prop:the-flux-across-is-it).</li>
</ul>
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li>$F'(z)=z^2=(x^2-y^2)+2ixy$, so by @prop:so-is-the-flow-associated (velocity $=\overline{F'}$, with $F$ the complex potential of @def:complex-potential-and-complex-velocity) $V=\overline{F'}=(x^2-y^2,\,-2xy)$.</li>
<li>$\operatorname{div}V=\partial_x(x^2-y^2)+\partial_y(-2xy)=2x-2x=0$ and $\operatorname{curl}V=\partial_x(-2xy)-\partial_y(x^2-y^2)=-2y+2y=0$ (@def:divergence-and-curl). This is no accident: it is @prop:cauchy-riemann-in-the-language-of applied to the holomorphic $F'$, and by @prop:incompressible-and-irrotational the flow is incompressible and irrotational.</li>
<li>$F=\frac13(x+iy)^3=\frac13\big(x^3-3xy^2\big)+\frac i3\big(3x^2y-y^3\big)$, so, as streamlines are the level sets of $\operatorname{Im}F$ (@def:streamline, @prop:psi-is-conserved-along-streamlines), they are
\[ \operatorname{Im}F=x^2y-\tfrac13y^3=y\big(x^2-\tfrac13y^2\big)=c. \]
For $c=0$: $y=0$ or $y=\pm\sqrt3\,x$, three lines through $0$ at angles $0°,60°,120°$. They cut the plane into six sectors, and the other streamlines are hyperbola-like curves in each sector, asymptotic to the two bounding lines. Direction: on the real axis $V=(x^2,0)$ points right, so the flow comes in along the negative real axis and leaves along the positive one; the pattern repeats with three-fold symmetry (a "monkey saddle" flow, compare the corner flow of @eg:f-z-z).</li>
<li>$V=0\iff z^2=0\iff z=0$: the only stagnation point is the origin (compare the stagnation points of @prop:where-is-the-fluid-fast). Speed $|V|=|F'(z)|=|z|^2$, since the speed is $|F'|$ (@prop:so-is-the-flow-associated).</li>
<li><em>Directly:</em> with the convention $n\,ds=(dy,-dx)$ of @sec:x12, on $C$ we have $x=0$, $dx=0$, so $n\,ds=(dy,0)$ and $V\cdot n\,ds=(x^2-y^2)\,dy=-y^2\,dy$. Flux $=\int_{-1}^1-y^2\,dy=-\frac23$.<br>
<em>From the stream function</em> (@prop:the-flux-across-is-it: flux $=\operatorname{Im}F(B)-\operatorname{Im}F(A)$): $\operatorname{Im}F(0,1)=1\cdot(0-\frac13)=-\frac13$ and $\operatorname{Im}F(0,-1)=(-1)(0-\frac13)=\frac13$, so the flux is $-\frac13-\frac13=-\frac23$. ✓ (Negative: the fluid crosses $C$ from right to left, against $n$, which points right for an upward curve.)</li>
</ol>
</details>
