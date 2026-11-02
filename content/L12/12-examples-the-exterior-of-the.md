---
id: n12
slide: Slide 13
title: 'Examples: the exterior of the disk'
---

::: proposition {#prop:joukowski-map name="Joukowski map"}
$J(z):=z+\dfrac1z$ is a conformal map of $\{|z|\gt1\}$ onto $\mathbb C\setminus[-2,2]$.
:::
::: proof

<ol>
<li><em>A quadratic.</em> For $z\ne0$, $J(z)=w\iff z^2-wz+1=0$. Its two roots $z_1,z_2$ (counted with multiplicity) have $z_1z_2=1$, the constant term. So either exactly one of them has modulus $\gt1$ (and the other $\lt1$), or both have modulus $1$.</li>
<li><em>Both on the unit circle exactly when $w\in[-2,2]$.</em> If $|z_1|=1$, then $z_2=1/z_1=\bar z_1$, so $w=z_1+z_2=z_1+\bar z_1=2\operatorname{Re}z_1\in[-2,2]$. Conversely $w=2\cos\theta$ has the roots $e^{\pm i\theta}$, both of modulus $1$.</li>
<li><em>Conclude.</em> For $w\notin[-2,2]$, exactly one root lies in $\{|z|\gt1\}$: $J$ takes $w$ exactly once there. For $w\in[-2,2]$, no root lies there. So $J$ is a bijection of $\{|z|\gt1\}$ onto $\mathbb C\setminus[-2,2]$, and it is holomorphic. <span class="qed">∎</span></li>
</ol>
:::
<p>Circles go to ellipses: $J(re^{i\theta})=\big(r+\tfrac1r\big)\cos\theta+i\big(r-\tfrac1r\big)\sin\theta$, an ellipse with semi-axes $r\pm\frac1r$ and foci at $\pm\sqrt{(r+\frac1r)^2-(r-\frac1r)^2}=\pm2$. Rays go to hyperbola branches with the same foci. As $r\downarrow1$ the ellipses flatten onto the slit $[-2,2]$.</p>
<figure>{{fig:n12-1}}<figcaption>The Joukowski map: images of the circles $|z|=1.25,1.6,2.2$ (brown ellipses) and of rays from $0$ (blue hyperbola branches). The slit $[-2,2]$ is the image of the unit circle.</figcaption></figure>
<p>A circle through $1$ that encloses $-1$ goes to an airfoil with a sharp trailing edge at $J(1)=2$, because $J'(1)=0$ there and the angle is doubled (@eg:z-2-doubles-angles-at-0). These are Joukowski's wing profiles: flows past a cylinder (@eg:f-z-z-1-z) are carried to flows past a wing.</p>
