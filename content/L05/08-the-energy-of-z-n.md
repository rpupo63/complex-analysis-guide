---
id: v9
slide: Slide 9
title: 'Proof of the lemma: the energy of $\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}$ vanishes'
toc: The energy of $z_n^+$ vanishes
---

::: proposition {#prop:step-1-z-n-lives-inside name="Step 1: $\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}$ lives inside $\Omega$"}
Properties (a)–(e) of @prop:properties-of-f apply to $f=\class{ntn-zn}{z_n}$.
:::
::: proof
<em>Uses $\class{ntn-Un}{U_n}=g\le \class{ntn-vc}{v}$ on $\class{ntn-dOm}{\partial\Omega}$.</em> On $\class{ntn-dOm}{\partial\Omega}$, $\class{ntn-Un}{U_n}=g$ (fact 1 of @sec:v4) and $\class{ntn-vc}{v}\ge g$, so $\class{ntn-zn}{z_n}=g-\class{ntn-sig}{\sigma}-\class{ntn-vc}{v}\le-\class{ntn-sig}{\sigma}$. Also $\class{ntn-zn}{z_n}$ is continuous on $\overline\Omega$ ($\class{ntn-Un}{U_n}$ and $\class{ntn-vc}{v}$ are), and inside $\Omega$ it is smooth on each closed square of the level-$n$ grid ($\class{ntn-Un}{U_n}$ is bilinear there and $\class{ntn-vc}{v}$ is smooth, being harmonic). These are the hypotheses of @sec:v8.
:::

::: proposition {#prop:step-2-its-energy-tends-to name="Step 2: its energy tends to zero"}
$\class{ntn-L2}{\norm{\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}\le\class{ntn-L2}{\norm{\nabla(\class{ntn-Un}{U_n}-u)}}\to0$, and $\class{ntn-L2}{\norm{\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}\to0$.
:::
::: proof
<em>Uses $u$ harmonic and $\nabla \class{ntn-Un}{U_n}\to\nabla u$.</em>
<ol>
<li>By [Prop. #(c)](@prop:properties-of-f), $|\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}|^2=\nabla \class{ntn-zn}{z_n}\cdot\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}$ almost everywhere.</li>
<li>Split $\class{ntn-zn}{z_n}=(\class{ntn-zn}{z_n}-\class{ntn-zf}{z})+\class{ntn-zf}{z}$, where $\class{ntn-zn}{z_n}-\class{ntn-zf}{z}=\class{ntn-Un}{U_n}-u$ (the $-\class{ntn-sig}{\sigma}-\class{ntn-vc}{v}$ cancels):
\[ \iint_\Omega|\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}|^2\,dA=\iint_\Omega\nabla(\class{ntn-Un}{U_n}-u)\cdot\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}\,dA+\underbrace{\iint_\Omega\nabla \class{ntn-zf}{z}\cdot\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}\,dA}_{=\,0}. \]</li>
<li>The last integral is $0$ by [Prop. #(d)](@prop:properties-of-f): $\class{ntn-zf}{z}=u-\class{ntn-sig}{\sigma}-\class{ntn-vc}{v}$ is smooth and harmonic in $\Omega$, since $u$ and $\class{ntn-vc}{v}$ are harmonic, $\class{ntn-sig}{\sigma}$ is a constant, and $\class{ntn-Delta}{\Delta}$ is linear.</li>
<li>By [Cauchy–Schwarz](apx:A12), the first integral is at most $\class{ntn-L2}{\norm{\nabla(\class{ntn-Un}{U_n}-u)}}\,\class{ntn-L2}{\norm{\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}$. So
\[ \class{ntn-L2}{\norm{\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}^2\le\class{ntn-L2}{\norm{\nabla(\class{ntn-Un}{U_n}-u)}}\,\class{ntn-L2}{\norm{\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}. \]
If $\class{ntn-L2}{\norm{\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}=0$ the claim is trivial; otherwise divide by it: $\class{ntn-L2}{\norm{\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}\le\class{ntn-L2}{\norm{\nabla(\class{ntn-Un}{U_n}-u)}}$, which tends to $0$ by fact 2 of @sec:v4.</li>
<li>By [Prop. #(e)](@prop:properties-of-f), $\class{ntn-L2}{\norm{\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}\le \class{ntn-L}{L}\class{ntn-L2}{\norm{\nabla \class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}\to0$. <span class="qed">∎</span></li>
</ol>
:::
<p>The point of Step 2: the energy of $\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}$ is controlled by how far $\nabla \class{ntn-Un}{U_n}$ is from $\nabla u$. This is exactly where gradient convergence enters, the ingredient @eg:a-boundary-layer lacked.</p>
