---
id: s14
slide: Slide 14
title: The discrete solution minimizes the energy
toc: Energy minimization
---
<p>Up to now the argument assumed a solution of the continuous problem exists. From here on, the discrete problem is used to produce one.</p>

::: definition {#def:energy name=energy}
$\class{ntn-E}{E}(V):=\class{ntn-a}{a}(V,V)=\iint_\Omega|\nabla V|^2\,dA$.
:::

::: lemma {#lem:among-all-is-the-unique}
Among all $V\in \class{ntn-Vg}{V^g_\eps}$, $\class{ntn-Ue}{U_\eps}$ is the unique minimizer of $E$.
:::
::: proof
Let $V\in \class{ntn-Vg}{V^g_\eps}$ and put $w:=V-\class{ntn-Ue}{U_\eps}$, which lies in $\class{ntn-Vz}{V^0_\eps}$ by @prop:v-g-eps-is-affine-not. By bilinearity and symmetry (@prop:properties-of-a),
\[ \class{ntn-E}{E}(V)=\class{ntn-a}{a}(\class{ntn-Ue}{U_\eps}+w,\class{ntn-Ue}{U_\eps}+w)=\class{ntn-a}{a}(\class{ntn-Ue}{U_\eps},\class{ntn-Ue}{U_\eps})+\class{ntn-a}{a}(\class{ntn-Ue}{U_\eps},w)+\class{ntn-a}{a}(w,\class{ntn-Ue}{U_\eps})+\class{ntn-a}{a}(w,w)=\class{ntn-E}{E}(\class{ntn-Ue}{U_\eps})+2\class{ntn-a}{a}(\class{ntn-Ue}{U_\eps},w)+\class{ntn-E}{E}(w). \]
The discrete equations (@def:discrete-problem) give $\class{ntn-a}{a}(\class{ntn-Ue}{U_\eps},w)=0$, since $w\in \class{ntn-Vz}{V^0_\eps}$. So $\class{ntn-E}{E}(V)=\class{ntn-E}{E}(\class{ntn-Ue}{U_\eps})+\class{ntn-E}{E}(w)\ge \class{ntn-E}{E}(\class{ntn-Ue}{U_\eps})$. If equality holds, then $\class{ntn-E}{E}(w)=0$. Writing $w=\sum d_{kl}\class{ntn-phi}{\varphi_{kl}}$ over interior nodes, @lem:the-quadratic-form-is-the-energy gives $d^{\mathsf T}\class{ntn-AII}{A_{II}}d=0$, and positive definiteness (@thm:a-ii-is-positive-definite) forces $d=0$, so $w=0$ and $V=\class{ntn-Ue}{U_\eps}$.
:::
<p>The continuous version of this lemma is known as [Dirichlet's principle](apx:E10).</p>
