---
id: x11
slide: Slide 20
title: 'Streamlines: the level sets of $\operatorname{Im}f$'
toc: Streamlines
---
<p><b>Setup.</b> $f=\class{ntn-vphi}{\varphi}+i\class{ntn-spsi}{\psi}$ holomorphic, velocity $\class{ntn-Vfl}{V}=\nabla\class{ntn-vphi}{\varphi}=(\class{ntn-vphi}{\varphi}_x,\class{ntn-vphi}{\varphi}_y)$. By Cauchy–Riemann, $\nabla\class{ntn-spsi}{\psi}=(\class{ntn-spsi}{\psi}_x,\class{ntn-spsi}{\psi}_y)=(-\class{ntn-vphi}{\varphi}_y,\class{ntn-vphi}{\varphi}_x)$ is $\class{ntn-Vfl}{V}$ rotated by $90°$ anticlockwise.</p>

::: definition {#def:streamline name=streamline}
A <em>streamline</em> is the path of a fluid particle: a curve $\gamma(t)$ whose velocity is that of the fluid,
\[ \gamma'(t)=\class{ntn-Vfl}{V}(\gamma(t))=\nabla\class{ntn-vphi}{\varphi}(\gamma(t)). \]
:::

::: proposition {#prop:psi-is-conserved-along-streamlines name="$\class{ntn-spsi}{\psi}$ is conserved along streamlines"}
$\class{ntn-spsi}{\psi}$ does not change along a streamline. So a particle starting on $\{\class{ntn-spsi}{\psi}=c\}$ stays on $\{\class{ntn-spsi}{\psi}=c\}$: the level sets of $\operatorname{Im}f$ are the streamlines of the flow of $f'$.
:::
::: proof
By the chain rule,
\[ \frac{d}{dt}\class{ntn-spsi}{\psi}(\gamma(t))=\nabla\class{ntn-spsi}{\psi}\cdot\gamma'(t)=\nabla\class{ntn-spsi}{\psi}\cdot\nabla\class{ntn-vphi}{\varphi}=(-\class{ntn-vphi}{\varphi}_y,\class{ntn-vphi}{\varphi}_x)\cdot(\class{ntn-vphi}{\varphi}_x,\class{ntn-vphi}{\varphi}_y)=-\class{ntn-vphi}{\varphi}_y\class{ntn-vphi}{\varphi}_x+\class{ntn-vphi}{\varphi}_x\class{ntn-vphi}{\varphi}_y=0. \]
A function with zero derivative on an interval is constant ([mean value theorem](apx:A3)).
:::
<p>So $\class{ntn-spsi}{\psi}$ is a <em>conserved quantity</em> of the motion. Geometrically: $\nabla\class{ntn-spsi}{\psi}\perp \class{ntn-Vfl}{V}$, so the velocity is always tangent to the level curves of $\class{ntn-spsi}{\psi}$.</p>
