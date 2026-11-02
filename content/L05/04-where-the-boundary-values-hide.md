---
id: v5
slide: Slide 5
title: Where the boundary values hide
---
<p><b>We know</b> $\class{ntn-Un}{U_n}=g$ on $\class{ntn-dOm}{\partial\Omega}$ for every $n$, and $\class{ntn-Un}{U_n}\to u$ in $L^2$ with $u$ harmonic. <b>We want</b> $u=g$ on $\class{ntn-dOm}{\partial\Omega}$. This does not follow, and no argument using only these facts can prove it. Here is a counterexample.</p>

::: example {#eg:a-boundary-layer name="a boundary layer"}
Take $g\equiv0$ and, for $\eps\gt0$,
\[ \class{ntn-Uex}{U_\eps}(z):=\min\Big(1,\ \frac{\class{ntn-dist}{\operatorname{dist}}(z,\class{ntn-dOm}{\partial\Omega})}{\eps}\Big), \]
where $\class{ntn-dist}{\operatorname{dist}}(z,\class{ntn-dOm}{\partial\Omega})$ is the [distance](apx:C6) from $z$ to the boundary. (This $\class{ntn-Uex}{U_\eps}$ is unrelated to the discrete solution of @def:the-discrete-solution.)
:::

<figure>
{{fig:v5-1}}
<figcaption>$\class{ntn-Uex}{U_\eps}$ climbs from $0$ to $1$ across a layer of width $\eps$ along the boundary, then stays at $1$.</figcaption>
</figure>

::: proposition {#prop:what-the-example-does name="what the example does"}
(a) $\class{ntn-Uex}{U_\eps}=0$ on $\class{ntn-dOm}{\partial\Omega}$. (b) $\class{ntn-Uex}{U_\eps}\to1$ in $L^2(\Omega)$ as $\eps\to0$. (c) The limit $1$ is harmonic, with the wrong boundary values. (d) $\iint|\nabla \class{ntn-Uex}{U_\eps}|^2\,dA\approx|\class{ntn-dOm}{\partial\Omega}|/\eps\to\infty$, where $|\class{ntn-dOm}{\partial\Omega}|$ is the length of the boundary.
:::
::: proof
(a) On $\class{ntn-dOm}{\partial\Omega}$ the distance is $0$.<br>
(b) $\class{ntn-Uex}{U_\eps}=1$ wherever $\class{ntn-dist}{\operatorname{dist}}(z,\class{ntn-dOm}{\partial\Omega})\ge\eps$. So $\class{ntn-Uex}{U_\eps}\ne1$ only on the layer $T_\eps:=\{z\in\Omega:\class{ntn-dist}{\operatorname{dist}}(z,\class{ntn-dOm}{\partial\Omega})\lt\eps\}$, where $0\le \class{ntn-Uex}{U_\eps}\le1$. Hence $\norm{\class{ntn-Uex}{U_\eps}-1}^2\le\operatorname{area}(T_\eps)$. $\class{ntn-dOm}{\partial\Omega}$ consists of finitely many segments of total length $|\class{ntn-dOm}{\partial\Omega}|$, and the points within $\eps$ of a segment of length $\ell$ form a "stadium" of area $2\eps\ell+\pi\eps^2$. So $\operatorname{area}(T_\eps)\le2\eps|\class{ntn-dOm}{\partial\Omega}|+N\pi\eps^2\to0$, with $N$ the number of segments.<br>
(c) The constant $1$ has $\class{ntn-Delta}{\Delta}1=0$, but it equals $1$, not $g=0$, on $\class{ntn-dOm}{\partial\Omega}$.<br>
(d) In the layer, $\class{ntn-Uex}{U_\eps}=\class{ntn-dist}{\operatorname{dist}}/\eps$, and the distance function has gradient of length $1$ almost everywhere ([C.6](apx:C6)). So $|\nabla \class{ntn-Uex}{U_\eps}|=1/\eps$ on the layer and $0$ outside it, and $\iint|\nabla \class{ntn-Uex}{U_\eps}|^2=\operatorname{area}(T_\eps)/\eps^2$. For small $\eps$ the layer is a strip of width $\eps$ along a boundary of length $|\class{ntn-dOm}{\partial\Omega}|$, of area about $\eps|\class{ntn-dOm}{\partial\Omega}|$, giving about $|\class{ntn-dOm}{\partial\Omega}|/\eps$.
:::

::: remark {#rem:the-moral name="the moral"}
The example satisfies "$U=g$ on $\class{ntn-dOm}{\partial\Omega}$, $U\to u$ in $L^2$, $u$ harmonic", yet $u\ne g$ on the boundary. So those facts alone cannot prove step 4. The difference with our $\class{ntn-Un}{U_n}$ is energy: the example's energy blows up, while ours stays bounded ($\class{ntn-E}{E}(\class{ntn-Un}{U_n})=m_n\le m_0$, @prop:so-decreases-to-a-limit) and $\nabla \class{ntn-Un}{U_n}$ converges in $L^2$ (fact 2 of @sec:v4). Any proof of step 4 must use the gradient convergence.
<p style="text-align:center"><b>$L^2$ limits forget the boundary values. Energy limits remember them.</b></p>
:::
