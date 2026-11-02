---
id: v12
slide: Slide 12
title: Squeezing $u$ at $p$
---

::: definition {#def:the-squeezing-functions name="the squeezing functions"}
Fix $\class{ntn-rho}{\rho}\le\class{ntn-epsn}{\eps_0}/2$ and $d\le\class{ntn-rho}{\rho}/2$. Let
\[ \class{ntn-osc}{\operatorname{osc}_\rho}:=\max\{|g(q)-g(p)|:q\in\class{ntn-dOm}{\partial\Omega},\ |q-p|\le\class{ntn-rho}{\rho}\} \]
(the <em>oscillation</em> of $g$ within $\class{ntn-rho}{\rho}$ of $p$), and put
\[ \class{ntn-vpm}{v_\pm}:=g(p)\pm\big(\class{ntn-osc}{\operatorname{osc}_\rho}+\class{ntn-kk}{k}\,\class{ntn-wd}{w_d}\big),\qquad \class{ntn-kk}{k}:=\frac{2\max|g|}{\log(\class{ntn-rho}{\rho}/\class{ntn-dd}{d})}. \]
:::
<p>The maximum defining $\class{ntn-osc}{\operatorname{osc}_\rho}$ exists because it is taken over a compact set ($\class{ntn-dOm}{\partial\Omega}$ intersected with a closed disk) of values of a continuous function. Since $\class{ntn-rho}{\rho}/d\ge2$, $\log(\class{ntn-rho}{\rho}/\class{ntn-dd}{d})\ge\log2\gt0$, so $\class{ntn-kk}{k}$ is a well-defined nonnegative number. Also $d\le\class{ntn-rho}{\rho}/2\le\class{ntn-epsn}{\eps_0}/4$, as @def:the-barrier requires.</p>

::: lemma {#lem:boundary-comparison name="boundary comparison"}
$\class{ntn-vpm}{v_-}\le g\le \class{ntn-vpm}{v_+}$ on $\class{ntn-dOm}{\partial\Omega}$, and $\class{ntn-vpm}{v_\pm}$ are continuous on $\overline\Omega$ and harmonic in $\Omega$.
:::
::: proof
$\class{ntn-vpm}{v_\pm}$ is a constant plus a constant multiple of $\class{ntn-wd}{w_d}$, which is smooth on $\overline\Omega$ and harmonic in $\Omega$ ([Lemma #(i)](@lem:properties-of-the-barrier)). Let $q\in\class{ntn-dOm}{\partial\Omega}$.
<ul>
<li><em>Within $\class{ntn-rho}{\rho}$ of $p$</em> ($|q-p|\le\class{ntn-rho}{\rho}$): $\class{ntn-kk}{k}\,\class{ntn-wd}{w_d}(q)\ge0$ by @lem:properties-of-the-barrier(ii), so
\[ \class{ntn-vpm}{v_+}(q)\ge g(p)+\class{ntn-osc}{\operatorname{osc}_\rho}\ge g(p)+|g(q)-g(p)|\ge g(q). \]</li>
<li><em>Farther than $\class{ntn-rho}{\rho}$ from $p$</em>: $|q-p|\gt\class{ntn-rho}{\rho}\ge2\class{ntn-dd}{d}$, so @lem:properties-of-the-barrier(iv) gives $\class{ntn-wd}{w_d}(q)\ge\log(|q-p|/\class{ntn-dd}{d})\ge\log(\class{ntn-rho}{\rho}/\class{ntn-dd}{d})$, hence $\class{ntn-kk}{k}\,\class{ntn-wd}{w_d}(q)\ge2\max|g|$. Since $\class{ntn-osc}{\operatorname{osc}_\rho}\ge0$ and $g(p)\ge-\max|g|$,
\[ \class{ntn-vpm}{v_+}(q)\ge g(p)+2\max|g|\ge\max|g|\ge g(q). \]</li>
</ul>
So $\class{ntn-vpm}{v_+}\ge g$ on $\class{ntn-dOm}{\partial\Omega}$. The same two cases, with all signs reversed, give $\class{ntn-vpm}{v_-}\le g$.
:::

::: theorem {#thm:step-4-boundary-values name="step 4: boundary values"}
For every $p\in\class{ntn-dOm}{\partial\Omega}$, $u(z)\to g(p)$ as $z\to p$ with $z\in\Omega$.
:::
::: proof

<ol>
<li><em>Squeeze.</em> By @lem:boundary-comparison and the comparison lemma (@lem:comparison, both halves), $\class{ntn-vpm}{v_-}\le u\le \class{ntn-vpm}{v_+}$ in $\Omega$. Subtracting $g(p)$:
\[ |u(z)-g(p)|\le\class{ntn-osc}{\operatorname{osc}_\rho}+\class{ntn-kk}{k}\,\class{ntn-wd}{w_d}(z)\qquad\text{for all }z\in\Omega. \]</li>
<li><em>Let $z\to p$.</em> $\class{ntn-wd}{w_d}$ is continuous at $p$ with $\class{ntn-wd}{w_d}(p)=\log2$, so taking the [limit superior](apx:A14),
\[ \limsup_{z\to p}|u(z)-g(p)|\le\class{ntn-osc}{\operatorname{osc}_\rho}+\class{ntn-kk}{k}\log2=\class{ntn-osc}{\operatorname{osc}_\rho}+\frac{2\max|g|\log2}{\log(\class{ntn-rho}{\rho}/\class{ntn-dd}{d})}. \]</li>
<li><em>Remove $\class{ntn-dd}{d}$ and $\class{ntn-rho}{\rho}$.</em> The left side involves neither $\class{ntn-dd}{d}$ nor $\class{ntn-rho}{\rho}$, so the inequality holds for every admissible choice. Let $d\to0$ with $\class{ntn-rho}{\rho}$ fixed: $\log(\class{ntn-rho}{\rho}/\class{ntn-dd}{d})\to\infty$, so the second term vanishes, and $\limsup|u(z)-g(p)|\le\class{ntn-osc}{\operatorname{osc}_\rho}$. Then let $\class{ntn-rho}{\rho}\to0$: $\class{ntn-osc}{\operatorname{osc}_\rho}\to0$ by continuity of $g$ at $p$.</li>
<li>So $\limsup_{z\to p}|u(z)-g(p)|=0$, which means $u(z)\to g(p)$. <span class="qed">∎</span></li>
</ol>
:::
<p>The two parameters do different jobs. $\class{ntn-rho}{\rho}$ controls how much $g$ itself varies near $p$; $\class{ntn-dd}{d}$ controls how sharply the barrier rises away from $p$, and sending $d\to0$ makes the barrier's cost at $p$ (the term $\class{ntn-kk}{k}\log2$) negligible.</p>
