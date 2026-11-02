---
id: w10
slide: Slide 21
title: 'In practice: how does one compute the solution?'
toc: Computing the solution
---
<p>We know the boundary values determine the harmonic function. But given the boundary values, how do we <em>find</em> it?
\[ \class{ntn-Delta}{\Delta} u=0\ \text{ in }\Omega,\qquad u=g\ \text{ on }\class{ntn-dOm}{\partial\Omega}. \]
The standard tool is the <b>finite element method</b>, in three steps: rewrite the problem in <b>weak form</b>; choose a finite-dimensional space of functions built on a grid; solve the resulting linear system. That is Lecture 3 (Part II, starting at @sec:s2), and at the end of it there is a concrete, finite-dimensional picture of <em>why</em> the boundary values determine everything (@sec:s12–@sec:s13).</p>
