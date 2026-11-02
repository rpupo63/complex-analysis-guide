---
id: x14
slide: Slides 24–26
title: 'Example 3: $f''(z)=1/z$, a source'
toc: Source, vortex, $\log z$
---

::: example {#eg:f-z-1-z name="$f'(z)=1/z$" status=derived}

<b>The flow.</b> $f'=\frac1z=\frac{x-iy}{x^2+y^2}$, so $V=\frac{(x,y)}{r^2}$ with $r^2=x^2+y^2$: radially outward, speed $1/r$. A <b>source</b> at the origin.<br>
<b>A primitive</b> on a disk not containing $0$: choose a continuous branch of the angle $\theta$ and set $f(z)=\log z=\log r+i\theta$.<br>
<b>The streamlines.</b> $\{\theta=c\}$: rays from the origin.
:::
<figure><div class="fpanels"><div class="fpanel">{{fig:x14-1}}</div></div><figcaption>@eg:f-z-1-z: the source $f'=1/z$. Streamlines are rays; the flux out of the dashed circle is $2\pi$.</figcaption></figure>
::: proof {title=Check.}
$\frac1z=\frac{\bar z}{|z|^2}=\frac{x-iy}{r^2}$, so $\class{ntn-vphi}{\varphi}_x=x/r^2$ and $\class{ntn-vphi}{\varphi}_y=y/r^2$, and the speed is $\sqrt{x^2+y^2}/r^2=1/r$. On a disk not containing $0$ the angle can be chosen continuously ([branches of the logarithm](apx:E3)). $\nabla\log r=\nabla\tfrac12\log(x^2+y^2)=\frac{(x,y)}{r^2}=V$. The level sets of $\class{ntn-spsi}{\psi}=\theta$ are rays.
:::
<p>Compare Lecture 2: there the same $1/z$, scaled by $\frac1{2\pi}$, is the electric field of a unit point charge (@def:the-field-of-a-unit-charge). Here it is the velocity of a fluid source of strength $2\pi$.</p>

::: proposition {#prop:1-z-has-a-genuine-singularity name="$1/z$ has a genuine singularity at $0$"}
(a) The flux of the flow of $1/z$ out of any circle $|z|=\rho$ is $2\pi$. (b) $1/z$ has no holomorphic extension to a disk containing such a circle.
:::
::: proof
(a) Across $|z|=\rho$ the fluid moves outward at speed $1/\rho$, perpendicular to the circle, along a curve of length $2\pi\rho$: the flux is $\frac1\rho\cdot2\pi\rho=2\pi\ne0$. Fluid is being <em>created</em> at the origin.<br>
(b) Suppose $1/z$ had a holomorphic extension $g$ to a disk containing the circle (with $C^2$ parts, Standing @asm:from-now-on-holomorphic-functions). Then $g$ would have a primitive $f$ on that disk (@prop:velocity-potential-stream-function-primitive), and by @prop:the-flux-across-is-it the flux across the circle, a closed curve from $A$ back to $B=A$, would be $\operatorname{Im}f(B)-\operatorname{Im}f(A)=0$. But $g=1/z$ on the circle, so the flux is $2\pi$. So there is no such disk: the origin is a genuine singularity.
:::
<figure><div class="fpanels"><div class="fpanel">{{fig:x14-2}}</div></div><figcaption>The vortex $f'=-i/z$: circular streamlines, circulation $2\pi$ around the origin.</figcaption></figure>
<p>The <em>vortex</em> $f'=-i/z$ tells the same story with flux replaced by circulation: $-\frac iz=\frac{-y-ix}{r^2}$ gives $V=\frac{(-y,x)}{r^2}$, so the streamlines are circles around the origin, and the circulation around any of them is $\frac1\rho\cdot2\pi\rho=2\pi$.</p>

::: proposition {#prop:no-global-primitive-on-mathbb-c name="no global primitive on $\mathbb C\setminus\{0\}$"}
$1/z$ has no holomorphic primitive on $\mathbb C\setminus\{0\}$.
:::
::: proof
$\operatorname{Im}\log z=\theta$ increases by $2\pi$ once around the circle, so $\log z$ is not single-valued on $\mathbb C\setminus\{0\}$. Any other primitive would differ from a local branch of $\log z$ by a constant (the difference has derivative $0$, so it is constant on connected pieces), so it would have the same $2\pi$ jump. Equivalently, by @prop:the-flux-across-is-it, a primitive $f$ on $\mathbb C\setminus\{0\}$ would give flux $\operatorname{Im}f(A)-\operatorname{Im}f(A)=0$ around the unit circle, contradicting [Prop. #(a)](@prop:1-z-has-a-genuine-singularity).
:::
<p>This is why the Poincaré lemma (@fact:poincare-lemma-on-a-disk) was stated on a disk: on $\mathbb C\setminus\{0\}$, the curl-free field $(-v,u)$ for $V=(x,y)/r^2$ is not a gradient.</p>
