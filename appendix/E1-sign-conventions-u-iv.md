---
id: E1
title: 'Sign conventions: $u+iv$ versus $u-iv$'
status:
- context
---
<p>The lectures attach a vector field to a complex function in two ways, and it is easy to mix them up.</p>
<div class="tbl"><table>
<thead><tr><th>Convention</th><th>Where</th><th>Cauchy–Riemann reads</th></tr></thead>
<tbody>
<tr><td>$f=u+iv$, $f\leftrightarrow(u,v)$ as a map $\R^2\to\R^2$</td><td>@def:complex-functions-as-maps-of-the, @thm:cauchy-riemann</td><td>$u_x=v_y$, $u_y=-v_x$</td></tr>
<tr><td>$f=u-iv$, $(u,v)$ a velocity or electric field</td><td>@sec:x6, @sec:x10, Lecture 2</td><td>$\operatorname{div}(u,v)=0$, $\operatorname{curl}(u,v)=0$</td></tr>
</tbody></table></div>
<p>The second is the first applied to the pair $(u,-v)$ (@prop:cauchy-riemann-in-the-language-of). In flow language: if $f=\class{ntn-vphi}{\varphi}+i\class{ntn-spsi}{\psi}$ is the complex potential, the velocity field is $V=\overline{f'}$ (@prop:so-is-the-flow-associated), and $f'=u-iv$ with $(u,v)=V$. Lecture 2's $f$ is Lecture 1's complex velocity $f'$, not its complex potential: both lectures attach $\frac1z$ to the radial field $(x,y)/r^2$ (@eg:f-z-1-z, @def:the-field-of-a-unit-charge).</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Potential_flow#Analysis_for_two-dimensional_flow" target="_blank" rel="noopener">Two-dimensional potential flow</a> · <a href="https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations" target="_blank" rel="noopener">Cauchy–Riemann equations</a></p>
