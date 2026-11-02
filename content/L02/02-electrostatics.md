---
id: w2
slide: Slides 4–5
title: 'A second interpretation: electrostatics'
toc: Electrostatics
---

::: definition {#def:electric-field name="electric field"}
Think of $(u,v)$ as an <em>electric field</em> $\class{ntn-Ef}{E}$ confined to two dimensions: the cross-section of the field of long charged wires perpendicular to the plane. A test charge $q$ placed at $(x,y)$ feels the force
\[ q\,\class{ntn-Ef}{E}(x,y)=q\,\big(u(x,y),v(x,y)\big), \]
so $\class{ntn-Ef}{E}$ is the force per unit charge. (For fluids, $(u,v)$ was the velocity of the particle at $(x,y)$.)
:::

::: hypothesis {#hyp:the-laws-of-electrostatics name="the laws of electrostatics"}
In units where $\varepsilon_0=1$,
\[ \class{ntn-divc}{\operatorname{div}}\class{ntn-Ef}{E}=\class{ntn-rhoc}{\rho},\qquad\class{ntn-divc}{\operatorname{curl}}\class{ntn-Ef}{E}=0, \]
where $\class{ntn-rhoc}{\rho}$ is the <em>charge density</em>. With the electrostatic voltage (potential) $\class{ntn-Phi}{\Phi}$, the sign convention is $\class{ntn-Ef}{E}=-\nabla\class{ntn-Phi}{\Phi}$.
:::
<p>These are physical laws (Gauss's law and the static case of Faraday's law; see [Maxwell's equations](apx:E4)), not theorems. Here $\varepsilon_0$ is the permittivity of free space, unrelated to the grid size $\class{ntn-epsn}{\eps_0}$ of Lecture 3.</p>

::: proposition {#prop:no-charge-means-holomorphic name="no charge means holomorphic"}
In a disk with no charge ($\class{ntn-rhoc}{\rho}=0$) and $\class{ntn-Ef}{E}=(u,v)$ of class $C^1$, $\class{ntn-divc}{\operatorname{div}}\class{ntn-Ef}{E}=0$ and $\class{ntn-divc}{\operatorname{curl}}\class{ntn-Ef}{E}=0$, so $f=u-iv$ is holomorphic. Here $f$ represents the electric field itself.
:::
::: proof
Put $\class{ntn-rhoc}{\rho}=0$ in @hyp:the-laws-of-electrostatics: these are exactly condition (2) of @thm:three-descriptions-from-lecture-1, which gives (1).
:::

::: remark {#rem:the-potential-and-where-lectures-3 name="the potential, and where Lectures 3–5 come in"}
If $\class{ntn-Ef}{E}=-\nabla\class{ntn-Phi}{\Phi}$ with $\class{ntn-Phi}{\Phi}$ of class $C^2$, then $\class{ntn-divc}{\operatorname{curl}}\class{ntn-Ef}{E}=-(\class{ntn-Phi}{\Phi}_{yx}-\class{ntn-Phi}{\Phi}_{xy})=0$ automatically ([mixed partials commute](apx:A2)), and $\class{ntn-divc}{\operatorname{div}}\class{ntn-Ef}{E}=-(\class{ntn-Phi}{\Phi}_{xx}+\class{ntn-Phi}{\Phi}_{yy})=-\class{ntn-Delta}{\Delta}\class{ntn-Phi}{\Phi}$. So the law $\class{ntn-divc}{\operatorname{div}}\class{ntn-Ef}{E}=\class{ntn-rhoc}{\rho}$ becomes $-\class{ntn-Delta}{\Delta}\class{ntn-Phi}{\Phi}=\class{ntn-rhoc}{\rho}$, and in a charge-free region the voltage is harmonic (@def:harmonic): $\class{ntn-Delta}{\Delta}\class{ntn-Phi}{\Phi}=0$. Prescribing the voltage on the boundary of a region, as on the plates of a capacitor, and asking for the voltage inside is the Dirichlet problem of Lectures 3–5.
:::
