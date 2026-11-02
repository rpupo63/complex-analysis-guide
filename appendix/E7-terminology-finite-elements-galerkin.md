---
id: E7
title: 'Terminology: finite elements, Galerkin, stiffness'
status:
- context
---
<ul>
<li><em>Finite element method</em>: approximate the solution by functions built from simple pieces on a mesh (here, bilinear pieces on squares), then impose the weak form on those functions.</li>
<li><em>Galerkin method</em>: impose a weak form using the same finite-dimensional space (up to boundary data) for trial and test functions. @def:discrete-problem is Galerkin with $\class{ntn-Vg}{V^g_\eps}$ and $\class{ntn-Vz}{V^0_\eps}$.</li>
<li><em>Stiffness matrix</em>: the matrix $A$ of @def:the-matrix-a. The name comes from structural mechanics, where the same construction relates forces to displacements. The per-square matrix $K$ of @lem:integrating-over-one-square is the <em>element stiffness matrix</em>, and summing over squares (@prop:summing-over-the-four-squares) is called <em>assembly</em>.</li>
<li><em>Bilinear interpolation</em>: filling in a square from its four corner values by the unique bilinear function (@lem:a-bilinear-function-is-fixed-by). $\class{ntn-Veps}{V_\eps}$ is exactly the set of such interpolants.</li>
</ul>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Finite_element_method" target="_blank" rel="noopener">Finite element method</a> · <a href="https://en.wikipedia.org/wiki/Galerkin_method" target="_blank" rel="noopener">Galerkin method</a> · <a href="https://en.wikipedia.org/wiki/Stiffness_matrix" target="_blank" rel="noopener">Stiffness matrix</a> · <a href="https://en.wikipedia.org/wiki/Bilinear_interpolation" target="_blank" rel="noopener">Bilinear interpolation</a></p>
