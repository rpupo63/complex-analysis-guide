---
id: A1
title: Real differentiability and little-$o$
status:
- defined
- cited
---
<p>$o(|h|)$ ("little-$o$ of $|h|$") stands for any quantity $\epsilon(h)$ with $\epsilon(h)/|h|\to0$ as $h\to0$: an error that is small even compared with $|h|$.</p>
<p>A function $u:\R^2\to\R$ is <em>differentiable</em> at $(x_0,y_0)$ if
\[ u(x_0+h_1,\,y_0+h_2)=u(x_0,y_0)+h_1u_x+h_2u_y+o(|h|),\qquad|h|=\sqrt{h_1^2+h_2^2}, \]
that is, $u$ is well approximated near the point by a linear function (its tangent plane). A map $f=(u,v)$ is differentiable if both components are. Having both partial derivatives is <em>not</em> enough: $u=\frac{xy}{x^2+y^2}$ (with $u(0,0)=0$) has $u_x=u_y=0$ at the origin but is not even continuous there.</p>
<div class="env"><span class="hd">Theorem (cited).</span> If the partial derivatives exist near a point and are continuous at it (in particular if $u$ is $C^1$), then $u$ is differentiable there.</div>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Differentiable_function#Differentiability_in_higher_dimensions" target="_blank" rel="noopener">Differentiability in several variables</a> · <a href="https://en.wikipedia.org/wiki/Big_O_notation#Little-o_notation" target="_blank" rel="noopener">Little-o notation</a></p>
