---
id: s3
slide: Slide 3
title: The plan in three steps
toc: The plan
---
<p>Uniqueness does not say what the solution is, or that there is one. The [finite element method](apx:E7) turns the differential equation into a finite linear system in three steps.</p>
<ol>
  <li><b>Weak form</b> (@sec:s4). Replace "$\class{ntn-Delta}{\Delta} u = 0$ at every point" by "an integral identity holds against every test function". This uses only first derivatives of $u$, so it makes sense for functions with corners.</li>
  <li><b>Choose where to look</b> (@sec:s5–@sec:s7). Replace $u$ by a function built from finitely many pieces, determined by its values at grid nodes. Replace "$u=g$ on $\class{ntn-dOm}{\partial\Omega}$" by "$U=g$ at the boundary nodes".</li>
  <li><b>Solve</b> (@sec:s8–@sec:s10). The weak form restricted to these functions is an $n\times n$ linear system, and it has exactly one solution.</li>
</ol>
<p>The slide promises two further outcomes. @sec:s11–@sec:s13 read the system as "each value is the average of its neighbours", which gives a discrete maximum principle and a concrete sense in which boundary values determine the solution. @sec:s14–@sec:s21 let the grid size tend to zero and prove that the discrete solutions converge to a function satisfying the weak form, under the grid [assumptions #](@hyp:fix-and-grid-lines-with) and [#](@hyp:for-now).</p>
