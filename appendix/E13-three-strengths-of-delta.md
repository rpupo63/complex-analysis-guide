---
id: E13
title: Three strengths of "$\class{ntn-Delta}{\Delta} u=0$" and distributions
status:
- context
---
<p>The two lectures meet the equation in three forms, each moving more derivatives off $u$ onto a test function $\eta$:</p>
<div class="tbl"><table>
<thead><tr><th>Form</th><th>Statement</th><th>Needs of $u$</th></tr></thead>
<tbody>
<tr><td>Classical (@def:dirichlet-problem)</td><td>$\class{ntn-Delta}{\Delta} u=0$ at every point</td><td>two derivatives</td></tr>
<tr><td>Weak (@def:weak-form-of-the-dirichlet-problem)</td><td>$\iint\nabla u\cdot\nabla\eta=0$</td><td>one (weak) derivative</td></tr>
<tr><td>Very weak (@thm:weyls-lemma)</td><td>$\iint u\,\class{ntn-Delta}{\Delta}\eta=0$</td><td>none: $u\in L^2$</td></tr>
</tbody></table></div>
<p>The last form treats $u$ as a <em>distribution</em>: an object known only through its integrals against test functions. Each form implies the next when $u$ is smooth enough (integration by parts). Weyl's lemma goes the other way, all the way back: for the Laplacian, the weakest form already forces the strongest. This is the simplest case of <em>elliptic regularity</em>.</p>
<p>The <em>Dirac delta</em> $\delta_0$ of Lecture 2 is the basic example of a distribution that is not a function: it is known only through $\eta\mapsto\eta(0)$. "$\operatorname{div}E_0=\delta_0$" (@def:meaning-of-operatorname-div-e-0) means $-\iint E_0\cdot\nabla\eta\,dA=\eta(0)$ for every test function $\eta$: the divergence moved onto $\eta$, exactly as in the weak forms above. @def:meaning-of-operatorname-div-e-0 states the same thing with fluxes through curves instead of test functions.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Distribution_(mathematics)" target="_blank" rel="noopener">Distributions</a> · <a href="https://en.wikipedia.org/wiki/Weyl%27s_lemma_(Laplace_equation)" target="_blank" rel="noopener">Weyl's lemma</a> · <a href="https://en.wikipedia.org/wiki/Elliptic_regularity" target="_blank" rel="noopener">Elliptic regularity</a></p>
