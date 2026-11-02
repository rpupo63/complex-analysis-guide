---
id: E8
title: Other averaging stencils
status:
- context
---
<p>A harmonic function equals its average over every circle inside its domain (@thm:mean-value-property, Lecture 4). @cor:each-interior-value-is-the-average is a discrete analogue: each nodal value is the average of its eight neighbours.</p>
<p>Different discretizations give different averaging rules. Finite differences, which replace $u_{xx}$ by $(u(x+\eps)-2u(x)+u(x-\eps))/\eps^2$, give the <em>five-point stencil</em>: each value is the average of its four edge neighbours. Bilinear finite elements give the nine-point rule of @prop:summing-over-the-four-squares.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Harmonic_function#The_mean_value_property" target="_blank" rel="noopener">Mean value property</a> · <a href="https://en.wikipedia.org/wiki/Five-point_stencil" target="_blank" rel="noopener">Five-point stencil</a> · <a href="https://en.wikipedia.org/wiki/Nine-point_stencil" target="_blank" rel="noopener">Nine-point stencil</a></p>
