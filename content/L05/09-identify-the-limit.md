---
id: v10
slide: Slide 10
title: 'Proof of the lemma: identify the limit'
toc: Identify the limit
---

::: proposition {#prop:step-3-z-n-to-z name="Step 3: $\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}\to \class{ntn-zf}{z}^{\class{ntn-pos}{+}}$ in $L^2$"}
$\class{ntn-L2}{\norm{\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}-\class{ntn-zf}{z}^{\class{ntn-pos}{+}}}}\le\class{ntn-L2}{\norm{\class{ntn-Un}{U_n}-u}}\to0$, and consequently $\class{ntn-zf}{z}^{\class{ntn-pos}{+}}=0$ almost everywhere in $\Omega$.
:::
::: proof
<em>Uses $\class{ntn-Un}{U_n}\to u$ in $L^2$.</em> By [Prop. #(b)](@prop:properties-of-f), at every point of $\Omega$,
\[ |\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}-\class{ntn-zf}{z}^{\class{ntn-pos}{+}}|\le|\class{ntn-zn}{z_n}-\class{ntn-zf}{z}|=|\class{ntn-Un}{U_n}-u|. \]
Square and integrate: $\class{ntn-L2}{\norm{\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}-\class{ntn-zf}{z}^{\class{ntn-pos}{+}}}}\le\class{ntn-L2}{\norm{\class{ntn-Un}{U_n}-u}}\to0$. So $\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}\to \class{ntn-zf}{z}^{\class{ntn-pos}{+}}$ in $L^2$, while $\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}\to0$ by @prop:step-2-its-energy-tends-to. Limits in $L^2$ are unique:
\[ \class{ntn-L2}{\norm{\class{ntn-zf}{z}^{\class{ntn-pos}{+}}}}\le\class{ntn-L2}{\norm{\class{ntn-zf}{z}^{\class{ntn-pos}{+}}-\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}+\class{ntn-L2}{\norm{\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}}}\to0, \]
so $\class{ntn-L2}{\norm{\class{ntn-zf}{z}^{\class{ntn-pos}{+}}}}=0$, and $\class{ntn-zf}{z}^{\class{ntn-pos}{+}}=0$ [almost everywhere](apx:A11).
:::

::: proposition {#prop:step-4-almost-everywhere-to-everywhere name="Step 4: almost everywhere to everywhere"}
$\class{ntn-zf}{z}\le0$ at every point of $\Omega$, that is, $u\le \class{ntn-vc}{v}+\class{ntn-sig}{\sigma}$.
:::
::: proof
$\class{ntn-zf}{z}=u-\class{ntn-sig}{\sigma}-\class{ntn-vc}{v}$ is continuous in $\Omega$. If $\class{ntn-zf}{z}\gt0$ at some point, continuity gives a disk around it on which $\class{ntn-zf}{z}\gt0$, so $\class{ntn-zf}{z}^{\class{ntn-pos}{+}}\gt0$ on a set of positive area. That contradicts @prop:step-3-z-n-to-z. So $\class{ntn-zf}{z}\le0$ everywhere.
:::

::: proof {title="Proof of Lemma [#](=lem:comparison)."}
Let $\class{ntn-vc}{v}\ge g$ on $\class{ntn-dOm}{\partial\Omega}$. For each $\class{ntn-sig}{\sigma}\gt0$, [Props. #](@prop:step-1-z-n-lives-inside)–[#](=prop:step-4-almost-everywhere-to-everywhere) give $u\le \class{ntn-vc}{v}+\class{ntn-sig}{\sigma}$ in $\Omega$. Let $\class{ntn-sig}{\sigma}\downarrow0$: $u\le \class{ntn-vc}{v}$.<br>
For the mirror statement, suppose $\class{ntn-vc}{v}\le g$ on $\class{ntn-dOm}{\partial\Omega}$ and take $\class{ntn-zn}{z_n}:=\class{ntn-vc}{v}-\class{ntn-sig}{\sigma}-\class{ntn-Un}{U_n}$ and $\class{ntn-zf}{z}:=\class{ntn-vc}{v}-\class{ntn-sig}{\sigma}-u$. On $\class{ntn-dOm}{\partial\Omega}$, $\class{ntn-zn}{z_n}=\class{ntn-vc}{v}-\class{ntn-sig}{\sigma}-g\le-\class{ntn-sig}{\sigma}$; $\class{ntn-zf}{z}$ is harmonic; and $\class{ntn-zn}{z_n}-\class{ntn-zf}{z}=u-\class{ntn-Un}{U_n}$. The same four steps apply word for word and give $\class{ntn-vc}{v}\le u+\class{ntn-sig}{\sigma}$, hence $\class{ntn-vc}{v}\le u$.
:::

::: remark {#rem:each-hypothesis-has-one-job name="each hypothesis has one job"}

<div class="tbl"><table>
<thead><tr><th>Hypothesis</th><th>Used for</th><th>Where</th></tr></thead>
<tbody>
<tr><td>Boundary inequality $\class{ntn-Un}{U_n}=g\le \class{ntn-vc}{v}$</td><td>$\class{ntn-zn}{z_n}^{\class{ntn-pos}{+}}$ lives inside $\Omega$</td><td>@prop:step-1-z-n-lives-inside</td></tr>
<tr><td>Gradient convergence $\nabla \class{ntn-Un}{U_n}\to\nabla u$</td><td>its energy vanishes</td><td>@prop:step-2-its-energy-tends-to</td></tr>
<tr><td>$L^2$ convergence $\class{ntn-Un}{U_n}\to u$</td><td>its limit is $\class{ntn-zf}{z}^{\class{ntn-pos}{+}}$</td><td>@prop:step-3-z-n-to-z</td></tr>
<tr><td>Harmonicity of $u$</td><td>no cross term</td><td>@prop:step-2-its-energy-tends-to, step 3</td></tr>
</tbody></table></div>
:::
