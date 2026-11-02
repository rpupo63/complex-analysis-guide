---
id: D4
title: 'Test functions: three versions'
status:
- defined
---
<p>A function $w:\overline\Omega\to\R$ is <em>piecewise continuously differentiable</em> if $\overline\Omega$ can be cut by finitely many line segments into pieces, and on each piece $w$ extends to a continuously differentiable function. It is an <em>admissible test function</em> if, in addition, it is continuous on $\overline\Omega$ and $w=0$ on $\class{ntn-dOm}{\partial\Omega}$.</p>
<p>This is the precise meaning this guide gives to the slide's "any function $w$ vanishing on $\class{ntn-dOm}{\partial\Omega}$". It is broad enough to include hat functions (cut along grid lines) and smooth functions (no cuts). Its gradient exists off the cuts, which have [zero area](apx:A11), so $a(u,w)$ is defined.</p>
<p>The lectures use three classes of test function, each fitted to what it is tested against:</p>
<div class="tbl"><table>
<thead><tr><th>Name</th><th>Where</th><th>Smoothness</th><th>At the boundary</th></tr></thead>
<tbody>
<tr><td>admissible $w$</td><td>weak form, @def:weak-form-of-the-dirichlet-problem</td><td>continuous, piecewise $C^1$</td><td>$=0$ on $\class{ntn-dOm}{\partial\Omega}$</td></tr>
<tr><td>$\psi$</td><td>weak derivative, @def:weak-derivative</td><td>$C^1$</td><td>$=0$ near $\class{ntn-dOm}{\partial\Omega}$</td></tr>
<tr><td>$\eta$</td><td>Weyl's lemma, @def:test-function-lecture-4</td><td>smooth</td><td>$=0$ near $\class{ntn-dOm}{\partial\Omega}$</td></tr>
</tbody></table></div>
<p>The weak form only moves one derivative and tests a function ($u$) whose boundary values are known, so vanishing on $\class{ntn-dOm}{\partial\Omega}$ is enough. The other two test an $L^2$ function with no boundary values at all, so they must vanish on a whole band ([C.7](apx:C7)). Weyl's lemma moves two derivatives, so it asks for smoothness.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Weak_formulation" target="_blank" rel="noopener">Weak formulation</a> · <a href="https://en.wikipedia.org/wiki/Piecewise#Continuity_and_differentiability_of_piecewise-defined_functions" target="_blank" rel="noopener">Piecewise functions</a></p>
