---
id: x15
slide: Slides 27–28
title: 'Example 4: flow past a cylinder'
toc: Flow past a cylinder
---

::: example {#eg:f-z-z-1-z name="$f(z)=z+1/z$" status=derived}
This time start from the primitive. $f(z)=z+1/z$ is holomorphic on $\mathbb C\setminus\{0\}$, and
\[ \operatorname{Im}f=y-\frac{y}{x^2+y^2}=y\Big(1-\frac1{r^2}\Big). \]
The streamlines are the curves $y\,(1-1/r^2)=c$.
<br>– $c=0$ gives the unit circle $r=1$ (together with the $x$-axis). So <b>the unit circle is a streamline</b>: no fluid crosses it. The flow does not notice whether the disk is full of fluid or a solid cylinder.
<br>– For large $r$, $\operatorname{Im}f\approx y$: far away, the uniform flow of @eg:f-z-1.
:::
<figure><div class="fpanels"><div class="fpanel">{{fig:x15-1}}</div></div><figcaption>@eg:f-z-z-1-z: flow past a cylinder, $f=z+1/z$. Streamlines bunch up above and below the disk, where the speed is $2$.</figcaption></figure>
::: proof {title=Check.}
$\frac1z=\frac{x-iy}{r^2}$ has imaginary part $-y/r^2$, so $\operatorname{Im}f=y-y/r^2$. It is zero when $y=0$ or $r=1$. As $r\to\infty$, $y/r^2\to0$ relative to $y$.
:::

::: proposition {#prop:where-is-the-fluid-fast name="where is the fluid fast?"}
The velocity is $\overline{f'(z)}$, with $f'(z)=1-\frac1{z^2}$; the speed is $|f'(z)|$. On the circle $z=e^{i\theta}$, $\ |f'|=|1-e^{-2i\theta}|=2|\sin\theta|$.
<br>– It vanishes at $z=\pm1$: <b>stagnation points</b> at the front and back of the cylinder. The fluid comes to rest there and splits to go around.
<br>– At the top, $z=i$: $f'(i)=1-1/i^2=2$, and likewise at the bottom. The fluid moves at <b>twice</b> the far-field speed there.
:::
::: proof
Velocity and speed: @prop:so-is-the-flow-associated. On the circle, $z^2=e^{2i\theta}$, so $\frac1{z^2}=e^{-2i\theta}$ and
\[ |1-e^{-2i\theta}|=|e^{-i\theta}|\,|e^{i\theta}-e^{-i\theta}|=1\cdot|2i\sin\theta|=2|\sin\theta|, \]
using $e^{i\theta}-e^{-i\theta}=2i\sin\theta$. This is $0$ at $\theta=0,\pi$ ($z=\pm1$) and $2$ at $\theta=\pm\pi/2$ ($z=\pm i$). Directly, $i^2=-1$ gives $f'(i)=1+1=2$.
:::
<p>Look at the picture: above and below the cylinder the streamlines are squeezed together. That is the flux proposition at work (@prop:the-flux-across-is-it): the same amount of fluid has to pass through a narrower channel, so it speeds up.</p>
