---
id: w5
slide: Slides 10–11
title: Gauss's theorem
---
<p>Suppose the charge consists of $k$ <b>point charges</b> $q_1,\dots,q_k$ at the points $z_1,\dots,z_k$: $\class{ntn-rhoc}{\rho}=\sum_jq_j\,\class{ntn-dlt}{\delta_{z_j}}$, so that $\class{ntn-divc}{\operatorname{div}}\class{ntn-Ef}{E}=\sum_jq_j\,\class{ntn-dlt}{\delta_{z_j}}$ and $\class{ntn-divc}{\operatorname{curl}}\class{ntn-Ef}{E}=0$. By @rem:consequence-the-singularity-is-the-charge this means precisely
\[ \class{ntn-Ef}{E}=H+\sum_{j=1}^kq_j\,\class{ntn-E0}{E_0}(\cdot-z_j), \]
where $H$ is a $C^1$ field with $\class{ntn-divc}{\operatorname{div}}H=\class{ntn-divc}{\operatorname{curl}}H=0$ on a region containing $\overline D$ (the field of the charges outside), and $\class{ntn-E0}{E_0}(\cdot-z_j)$ is the unit-charge field moved to $z_j$.</p>

::: theorem {#thm:gausss-theorem name="Gauss's theorem"}
Let $\gamma$ be a [positively oriented simple closed curve](apx:C3) bounding a region $D$, not passing through any $z_j$. Then
\[ \oint_\gamma \class{ntn-Ef}{E}\cdot n\,ds=\sum_{z_j\in D}q_j\qquad\text{and}\qquad\oint_\gamma \class{ntn-Ef}{E}\cdot t\,ds=0. \]
:::
::: proof
The slide's one-line proof is
\[ \oint_\gamma \class{ntn-Ef}{E}\cdot n\,ds=\iint_D\class{ntn-divc}{\operatorname{div}}\class{ntn-Ef}{E}\,dA=\iint_D\sum_jq_j\,\class{ntn-dlt}{\delta_{z_j}}\,dA=\sum_{z_j\in D}q_j,\qquad\oint_\gamma \class{ntn-Ef}{E}\cdot t\,ds=\iint_D\class{ntn-divc}{\operatorname{curl}}\class{ntn-Ef}{E}\,dA=0. \]
The middle steps integrate a delta, so here is the same computation term by term, using only results proved above. Both integrals are linear in $\class{ntn-Ef}{E}$.
<ul>
<li>For $H$: the [divergence theorem and Green's theorem](apx:A6) give flux $\iint_D\class{ntn-divc}{\operatorname{div}}H=0$ and circulation $\iint_D\class{ntn-divc}{\operatorname{curl}}H=0$.</li>
<li>For $q_j\class{ntn-E0}{E_0}(\cdot-z_j)$: @thm:the-claim, moved to $z_j$, gives flux $q_j$ if $z_j\in D$ and $0$ if $z_j\notin\overline D$ (the case $z_j\in\gamma$ is excluded), and circulation $0$ in both cases.</li>
</ul>
Adding up gives $\sum_{z_j\in D}q_j$ and $0$.
:::
<p>The shape of $\gamma$ does not matter, only which charges it encloses.</p>
