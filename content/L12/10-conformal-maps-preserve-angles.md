---
id: n10
slide: Slide 11
title: Conformal maps preserve angles
---

::: proposition {#prop:angles name=angles}
Let $f$ be holomorphic near $z_0$ with $f'(z_0)\ne0$, and let $\gamma_1,\gamma_2$ be $C^1$ curves with $\gamma_j(0)=z_0$ and $\gamma_j'(0)\ne0$. Then
\[ (f\circ\gamma_j)'(0)=f'(z_0)\,\gamma_j'(0). \]
So both tangent vectors are multiplied by the same complex number $f'(z_0)$: rotated by $\arg f'(z_0)$ and scaled by $|f'(z_0)|$. The image curves meet at the same angle as $\gamma_1$ and $\gamma_2$, and with the same orientation.
:::
::: proof
By complex differentiability,
\[ f(\gamma_j(t))-f(z_0)=f'(z_0)\big(\gamma_j(t)-z_0\big)+o(|\gamma_j(t)-z_0|). \]
Divide by $t$ and let $t\to0$: $\frac{\gamma_j(t)-z_0}t\to\gamma_j'(0)$, and the error term divided by $t$ tends to $0$ because $|\gamma_j(t)-z_0|/|t|$ stays bounded. The angle between the images is $\arg\frac{(f\circ\gamma_2)'(0)}{(f\circ\gamma_1)'(0)}=\arg\frac{\gamma_2'(0)}{\gamma_1'(0)}$, the same as before.
:::
<p>This is where the word "conformal" (same form) comes from: tiny shapes are rotated and scaled, not distorted. Lecture 1's flows illustrate it: streamlines and equipotentials meet at right angles because both are images of the horizontal and vertical lines under a conformal map.</p>

::: example {#eg:z-2-doubles-angles-at-0 name="$z^2$ doubles angles at $0$"}
At a zero of $f'$ angles are not preserved: $z^2$ sends the ray $\arg z=\alpha$ to the ray $\arg z=2\alpha$, so it maps the quadrant $\{\operatorname{Re}z\gt0,\operatorname{Im}z\gt0\}$ onto $\mathbb H$. Away from $0$ angles are preserved: with $z^2=(x^2-y^2)+2ixy$, the line $\operatorname{Re}z=a$ goes to the parabola $u=a^2-\frac{v^2}{4a^2}$ and the line $\operatorname{Im}z=b$ to $u=\frac{v^2}{4b^2}-b^2$, and these parabolas still meet at right angles.
:::
<figure>{{fig:n10-1}}<figcaption>Under $z^2$ the lines $\operatorname{Re}z=a$ (brown) and $\operatorname{Im}z=b$ (blue) of the quadrant become parabolas in $\mathbb H$, still meeting at right angles.</figcaption></figure>
