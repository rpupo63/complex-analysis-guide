---
id: t3
slide: Slide 3
title: The mean value property
---
<p>The lecture writes points of the plane as complex numbers, $z=x+iy$. This is only notation: no complex arithmetic beyond $e^{i\theta}=\cos\theta+i\sin\theta$ is used. See [complex notation for the plane](apx:C1).</p>

::: definition {#def:circles-disks-circle-averages name="circles, disks, circle averages"}
Fix a centre $z_0$. For $t\gt0$:
<ul>
<li>$\class{ntn-Ct}{C_t}$ is the circle of radius $t$:
\[ \class{ntn-Ct}{C_t}:=\{z:|z-z_0|=t\}=\{z_0+te^{i\theta}:0\le\theta\le2\pi\}; \]</li>
<li>$\class{ntn-Dt}{D_t}:=\{z:|z-z_0|\lt t\}$ is the open disk inside it, and $\class{ntn-Dt}{\overline{D_t}}=\{|z-z_0|\le t\}$ the closed disk;</li>
<li>for a continuous $h$, $\ \class{ntn-Mt}{M}(t):=\dfrac1{2\pi}\displaystyle\int_0^{2\pi}h(z_0+te^{i\theta})\,d\theta$ is the <em>average of $h$ over $\class{ntn-Ct}{C_t}$</em>.</li>
</ul>
The average is taken with respect to the angle; since arc length on $\class{ntn-Ct}{C_t}$ is $ds=t\,d\theta$ ([polar coordinates](apx:A8)), it equals $\frac{1}{2\pi t}\oint_{\class{ntn-Ct}{C_t}}h\,ds$, total over length.
:::

::: theorem {#thm:mean-value-property name="mean value property"}
Let $h$ be $C^2$ and harmonic on an open set $\Omega$, and let the closed disk $|z-z_0|\le r$ lie in $\Omega$. Then
\[ h(z_0)=\frac1{2\pi}\int_0^{2\pi}h(z_0+re^{i\theta})\,d\theta. \]
:::
::: proof
Let $\class{ntn-Mt}{M}(t)$ be the average of $h$ over $\class{ntn-Ct}{C_t}$ for $0\lt t\le r$ (@def:circles-disks-circle-averages). We show $M$ is constant and tends to $h(z_0)$.
<ol>
<li><em>Differentiate under the integral.</em> The function $(t,\theta)\mapsto h(z_0+te^{i\theta})$ has a continuous $t$-derivative on the rectangle $[0,r]\times[0,2\pi]$, because $h$ is $C^2$ on an open set containing the closed disk. So [differentiation under the integral sign](apx:A4) applies:
\[ \class{ntn-Mt}{M}'(t)=\frac1{2\pi}\int_0^{2\pi}\partial_t\big[h(z_0+te^{i\theta})\big]\,d\theta. \]</li>
<li><em>Chain rule.</em> In coordinates, $z_0+te^{i\theta}=(x_0+t\cos\theta,\ y_0+t\sin\theta)$. Its $t$-derivative is the unit vector $e^{i\theta}=(\cos\theta,\sin\theta)$, so
\[ \partial_t\big[h(z_0+te^{i\theta})\big]=h_x\cos\theta+h_y\sin\theta=\nabla h\cdot e^{i\theta}. \]
At the point $z_0+te^{i\theta}$ of $\class{ntn-Ct}{C_t}$, the vector $e^{i\theta}$ points straight away from the centre: it is the outward unit normal $n$ to $\class{ntn-Ct}{C_t}$. So the integrand is $\nabla h\cdot n$, the outward normal derivative.</li>
<li><em>Change $d\theta$ to arc length.</em> On $\class{ntn-Ct}{C_t}$, $ds=t\,d\theta$, so $d\theta=ds/t$:
\[ \class{ntn-Mt}{M}'(t)=\frac1{2\pi}\int_0^{2\pi}\nabla h\cdot n\,d\theta=\frac1{2\pi t}\oint_{\class{ntn-Ct}{C_t}}\nabla h\cdot n\,ds. \]</li>
<li><em>Divergence theorem.</em> Apply the [divergence theorem](apx:A6) on $\class{ntn-Dt}{D_t}$ to $F=\nabla h$, which is $C^1$ on $\class{ntn-Dt}{\overline{D_t}}\subset\Omega$. Since $\nabla\cdot\nabla h=\class{ntn-Delta}{\Delta} h$,
\[ \oint_{\class{ntn-Ct}{C_t}}\nabla h\cdot n\,ds=\iint_{\class{ntn-Dt}{D_t}}\class{ntn-Delta}{\Delta} h\,dA=0, \]
because $h$ is harmonic. So $\class{ntn-Mt}{M}'(t)=0$ for $0\lt t\le r$.</li>
<li><em>$M$ is constant.</em> A function with zero derivative on an interval is constant there, by the [mean value theorem](apx:A3). So $\class{ntn-Mt}{M}(t)=M(r)$ for all $0\lt t\le r$.</li>
<li><em>Let $t\to0$.</em> Since every $\theta$-average of a constant is that constant,
\[ |\class{ntn-Mt}{M}(t)-h(z_0)|=\Big|\frac1{2\pi}\int_0^{2\pi}\big(h(z_0+te^{i\theta})-h(z_0)\big)d\theta\Big|\le\max_{\theta}\big|h(z_0+te^{i\theta})-h(z_0)\big|. \]
Given any tolerance, continuity of $h$ at $z_0$ makes the right side smaller than it once $t$ is small. So $\class{ntn-Mt}{M}(t)\to h(z_0)$.</li>
<li>A constant function that tends to $h(z_0)$ equals $h(z_0)$. In particular $M(r)=h(z_0)$. <span class="qed">∎</span></li>
</ol>
:::

::: definition {#def:the-mean-value-property name="the mean value property"}
A continuous function $v$ on an open set $\Omega$ <em>has the mean value property</em> if, for every $z$ and every $r\gt0$ with the closed disk $|\zeta-z|\le r$ inside $\Omega$, $v(z)$ equals the average of $v$ over the circle of radius $r$ about $z$.
:::
<p>@thm:mean-value-property says: every $C^2$ harmonic function has the mean value property. @thm:converse-of-the-mean-value-property will prove the converse, so the two descriptions are equivalent. @cor:each-interior-value-is-the-average in Lecture 3 was the discrete version: each nodal value is the average of its eight neighbours.</p>
