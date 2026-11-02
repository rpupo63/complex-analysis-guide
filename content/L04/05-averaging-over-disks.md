---
id: t6
slide: Slide 6
title: Averaging over disks
---

::: definition {#def:the-averaging-weight-chi name="the averaging weight $\class{ntn-chi}{\chi}$"}
Fix a function $\class{ntn-chi}{\chi}$ on the plane that is [smooth](apx:D1), $\class{ntn-chi}{\chi}\ge0$, <em>radial</em> ($\class{ntn-chi}{\chi}(\zeta)$ depends only on $|\zeta|$), zero outside the unit disk, and has $\iint\class{ntn-chi}{\chi}\,dA=1$. Such a $\class{ntn-chi}{\chi}$ exists; see [mollifiers](apx:D5) for an explicit one.
:::

::: definition {#def:rescaled-weight name="rescaled weight"}
For $\delta\gt0$, $\ \class{ntn-chid}{\chi_\delta}(\zeta):=\delta^{-2}\class{ntn-chi}{\chi}(\zeta/\delta)$.
:::

::: lemma {#lem:is-smooth-radial-zero-outside}
$\class{ntn-chid}{\chi_\delta}$ is smooth, $\ge0$, radial, zero outside the disk of radius $\delta$, and $\iint\class{ntn-chid}{\chi_\delta}\,dA=1$.
:::
::: proof
Smoothness, sign and radial symmetry pass from $\class{ntn-chi}{\chi}$ to $\class{ntn-chid}{\chi_\delta}$ directly. If $|\zeta|\ge\delta$ then $|\zeta/\delta|\ge1$, so $\class{ntn-chi}{\chi}(\zeta/\delta)=0$. For the integral, substitute $\zeta=\delta w$, which scales areas by $\delta^2$, so $dA(\zeta)=\delta^2\,dA(w)$ ([change of variables](apx:A8)):
\[ \iint\delta^{-2}\class{ntn-chi}{\chi}(\zeta/\delta)\,dA(\zeta)=\iint\delta^{-2}\class{ntn-chi}{\chi}(w)\,\delta^2\,dA(w)=\iint\class{ntn-chi}{\chi}\,dA=1. \]
The factor $\delta^{-2}$ is there exactly to cancel the area scaling: shrinking the support to radius $\delta$ while keeping total weight $1$ forces the weight to be taller.
:::

::: definition {#def:the-shrunken-domain-and-convolution name="the shrunken domain and convolution"}
$\class{ntn-Omd}{\Omega_\delta}$ is the set of $z\in\Omega$ whose closed disk of radius $\delta$ lies in $\Omega$. For a function $v$ on $\Omega$ and $z\in\class{ntn-Omd}{\Omega_\delta}$, the <em>convolution</em> is
\[ (v\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta})(z):=\iint v(\zeta)\,\class{ntn-chid}{\chi_\delta}(z-\zeta)\,dA(\zeta). \]
The weight $\class{ntn-chid}{\chi_\delta}(z-\zeta)$ is zero unless $|z-\zeta|\lt\delta$, so only values of $v$ on the disk of radius $\delta$ about $z$ enter, and that disk lies in $\Omega$. The weights are $\ge0$ and total $1$, so $v\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}$ is a <em>weighted average of $v$ over that disk</em>.
:::
<p>Two facts about $\class{ntn-Omd}{\Omega_\delta}$ are used below ([compact sets](apx:C5)): it is open, and every compact $K\subset\Omega$ lies inside $\class{ntn-Omd}{\Omega_\delta}$ once $\delta$ is small enough. Also, every point of $\Omega$ belongs to some $\class{ntn-Omd}{\Omega_\delta}$, because $\Omega$ is open.</p>

::: lemma {#lem:averaging name=averaging}
Let $v$ be continuous on $\Omega$ and have the mean value property (@def:the-mean-value-property). Then $v\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}=v$ on $\class{ntn-Omd}{\Omega_\delta}$.
:::
::: proof

<ol>
<li><em>Write the weight radially.</em> Since $\class{ntn-chid}{\chi_\delta}$ is radial, $\class{ntn-chid}{\chi_\delta}(\zeta)=k(|\zeta|)$ for a one-variable function $k$ with $\class{ntn-kt}{k}(t)=0$ for $t\ge\delta$. In [polar coordinates](apx:A8), $dA=t\,dt\,d\theta$, so the normalization of @lem:is-smooth-radial-zero-outside reads
\[ 1=\iint\class{ntn-chid}{\chi_\delta}\,dA=\int_0^\delta\!\!\int_0^{2\pi}\class{ntn-kt}{k}(t)\,t\,d\theta\,dt=\int_0^\delta \class{ntn-kt}{k}(t)\,2\pi t\,dt. \]</li>
<li><em>Polar coordinates about $z$.</em> Fix $z\in\class{ntn-Omd}{\Omega_\delta}$ and write $\zeta=z+te^{i\theta}$. Then $|z-\zeta|=t$, so $\class{ntn-chid}{\chi_\delta}(z-\zeta)=\class{ntn-kt}{k}(t)$, and
\[ (v\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta})(z)=\int_0^\delta \class{ntn-kt}{k}(t)\Big(\int_0^{2\pi}v(z+te^{i\theta})\,d\theta\Big)\,t\,dt. \]
Splitting the double integral into an inner $\theta$-integral and an outer $t$-integral is [Fubini's theorem](apx:A13); the integrand is continuous on a closed disk.</li>
<li><em>Use the mean value property, circle by circle.</em> For each $t\le\delta$, the closed disk of radius $t$ about $z$ lies inside the closed disk of radius $\delta$, which lies in $\Omega$. So $\int_0^{2\pi}v(z+te^{i\theta})\,d\theta=2\pi v(z)$, and
\[ (v\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta})(z)=\int_0^\delta \class{ntn-kt}{k}(t)\,2\pi v(z)\,t\,dt=v(z)\int_0^\delta \class{ntn-kt}{k}(t)\,2\pi t\,dt=v(z). \]</li>
</ol>
In words: the disk average is an average of circle averages, and each circle average is $v(z)$.
:::
