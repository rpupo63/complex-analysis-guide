---
id: t11
slide: Slide 11
title: The converse of the mean value property
toc: Converse of the mean value property
---

::: theorem {#thm:converse-of-the-mean-value-property name="converse of the mean value property"}
A continuous function $v$ on $\Omega$ with the mean value property is smooth and harmonic.
:::
::: proof
<em>$v$ is smooth.</em> By @lem:averaging, $v=v\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}$ on $\class{ntn-Omd}{\Omega_\delta}$. In
\[ (v\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta})(z)=\iint v(\zeta)\,\class{ntn-chid}{\chi_\delta}(z-\zeta)\,dA(\zeta) \]
the variable $z$ appears only inside $\class{ntn-chid}{\chi_\delta}$. As in @prop:u-delta-is-smooth, differentiate under the integral sign: every derivative falls on $\class{ntn-chid}{\chi_\delta}$, which is smooth, and $v$ only needs to be continuous (so integrable on disks). So $v$ is smooth on $\class{ntn-Omd}{\Omega_\delta}$. Every point of $\Omega$ lies in some $\class{ntn-Omd}{\Omega_\delta}$, so $v$ is smooth on $\Omega$.<br>
<em>$v$ is harmonic.</em> Fix $z_0$ and let $\class{ntn-Mt}{M}(t)$ be the average of $v$ over the circle of radius $t$ about $z_0$, for $t$ small enough that the closed disk lies in $\Omega$. Steps 1–4 of @thm:mean-value-property used only that $h$ is $C^2$, not that it is harmonic, until the last equality. Since $v$ is now smooth, they give
\[ \class{ntn-Mt}{M}'(t)=\frac1{2\pi t}\iint_{\class{ntn-Dt}{D_t}}\class{ntn-Delta}{\Delta} v\,dA. \]
The mean value property says $\class{ntn-Mt}{M}(t)=v(z_0)$ for every such $t$, so $M$ is constant and $\class{ntn-Mt}{M}'(t)=0$. Hence $\iint_{\class{ntn-Dt}{D_t}}\class{ntn-Delta}{\Delta} v\,dA=0$ for every small $t$. Divide by the area $\pi t^2$:
\[ 0=\frac1{\pi t^2}\iint_{\class{ntn-Dt}{D_t}}\class{ntn-Delta}{\Delta} v\,dA,\qquad \Big|\frac1{\pi t^2}\iint_{\class{ntn-Dt}{D_t}}\class{ntn-Delta}{\Delta} v\,dA-\class{ntn-Delta}{\Delta} v(z_0)\Big|\le\max_{\class{ntn-Dt}{\overline{D_t}}}|\class{ntn-Delta}{\Delta} v-\class{ntn-Delta}{\Delta} v(z_0)|. \]
$\class{ntn-Delta}{\Delta} v$ is continuous, so the right side tends to $0$ as $t\to0$, and the disk averages (all zero) tend to $\class{ntn-Delta}{\Delta} v(z_0)$. So $\class{ntn-Delta}{\Delta} v(z_0)=0$.
:::
<p>Together with @thm:mean-value-property: <b>a continuous function is harmonic if and only if it has the mean value property.</b> The right side of this equivalence mentions no derivatives.</p>
