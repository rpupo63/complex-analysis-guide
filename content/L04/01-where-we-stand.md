---
id: t2
slide: Slide 2
title: Where we stand
---
<p>Lecture 3 worked under @hyp:for-now: $\Omega$ is a finite union of squares of the coarsest grid, and $g$ is linear on each boundary edge of that grid. $\class{ntn-Un}{U_n}$ is the finite element solution on the grid of side $\class{ntn-epsn}{\eps_n}=2^{-n}\class{ntn-epsn}{\eps_0}$. @thm:existence-of-a-weak-solution proved two things:</p>
<ul>
<li>$\class{ntn-Un}{U_n}\to u$ and $\nabla \class{ntn-Un}{U_n}\to\nabla u$ in $L^2(\Omega)$ (@prop:three-limits and @prop:and-weakly-write);</li>
<li>$\class{ntn-a}{a}(u,\eta)=0$ for every smooth $\eta$ vanishing on $\class{ntn-dOm}{\partial\Omega}$ (@thm:smooth-test-functions).</li>
</ul>
<p>So $u$ is a <em>weak</em> solution. Its gradient exists only as a weak derivative, and the equation holds only after integrating against test functions. The goal of this lecture is to show that $u$ is in fact a classical solution in the interior: $u$ is [smooth](apx:D1) and $\class{ntn-Delta}{\Delta} u=0$ at every point of $\Omega$ (@cor:the-lecture-3-limit-is-a). The road goes through the mean value property, which describes harmonic functions without mentioning derivatives.</p>
