---
id: x13
slide: Slides 22–23
title: 'Examples 1 and 2: uniform flow and a stagnation point'
toc: Uniform and corner flow
---

::: example {#eg:f-z-1 name="$f'(z)=1$" status=derived}

<b>The flow.</b> $f'=1=\class{ntn-vphi}{\varphi}_x-i\class{ntn-vphi}{\varphi}_y$: velocity field $V=(1,0)$. Every particle moves to the right at unit speed.<br>
<b>The primitive.</b> $f(z)=z=x+iy$, so $\class{ntn-vphi}{\varphi}=x$, $\class{ntn-spsi}{\psi}=y$.<br>
<b>The streamlines.</b> $\{\operatorname{Im}f=c\}=\{y=c\}$: horizontal lines.<br>
<b>The flux</b> across the vertical segment from $A=(0,0)$ to $B=(0,h)$ is $h$, and $\operatorname{Im}f(B)-\operatorname{Im}f(A)=h-0=h$.
:::
::: proof {title=Check.}
$f'=1$ means $\class{ntn-vphi}{\varphi}_x=1$, $\class{ntn-vphi}{\varphi}_y=0$. $\nabla\class{ntn-vphi}{\varphi}=\nabla x=(1,0)=V$. Travelling up the segment, $(dx,dy)=(0,ds)$, so $n=(1,0)$ and $V\cdot n=1$ along a segment of length $h$: flux $h$, matching @prop:the-flux-across-is-it.
:::

::: example {#eg:f-z-z name="$f'(z)=z$" status=derived}

<b>The flow.</b> $f'=x+iy=\class{ntn-vphi}{\varphi}_x-i\class{ntn-vphi}{\varphi}_y$, so the velocity at $(x,y)$ is $V=(x,-y)$: away from the $y$-axis horizontally, toward the $x$-axis vertically. At the origin the velocity is $0$: a <b>stagnation point</b>.<br>
<b>The primitive.</b> $f(z)=\frac12z^2=\frac12(x^2-y^2)+i\,xy$.<br>
<b>The streamlines.</b> $\{\operatorname{Im}f=c\}=\{xy=c\}$: hyperbolas with the axes as asymptotes. A particle comes in along the $y$-axis direction, turns, and leaves along the $x$-axis direction.
:::
<figure><div class="fpanels"><div class="fpanel">{{fig:x13-1}}</div></div><figcaption>@eg:f-z-z: streamlines $xy=c$ of the stagnation-point flow $V=(x,-y)$.</figcaption></figure>
::: proof {title=Check.}
Matching real and imaginary parts in $x+iy=\class{ntn-vphi}{\varphi}_x-i\class{ntn-vphi}{\varphi}_y$ gives $\class{ntn-vphi}{\varphi}_x=x$, $\class{ntn-vphi}{\varphi}_y=-y$. $z^2=(x+iy)^2=x^2-y^2+2ixy$, so $\class{ntn-vphi}{\varphi}=\frac12(x^2-y^2)$ and $\class{ntn-spsi}{\psi}=xy$, and $\nabla\class{ntn-vphi}{\varphi}=(x,-y)=V$. This is the stagnation-point field of @eg:which-flows-come-from-holomorphic-functions.
:::
