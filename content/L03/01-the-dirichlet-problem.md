---
id: s2
slide: Slide 2
title: The Dirichlet problem
---
<p>Slide 1 is the title slide.</p>

::: setting {#set:the-slide-leaves-this-implicit kind="Standing setting"}
The slide leaves this implicit. $\Omega\subset\R^2$ is a [bounded open set](apx:C2) with [boundary](apx:C2) $\class{ntn-dOm}{\partial\Omega}$, and $g:\class{ntn-dOm}{\partial\Omega}\to\R$ is a given continuous function, the <em>boundary data</em>.
:::

::: definition {#def:dirichlet-problem name="Dirichlet problem"}
Given $g$, find a harmonic function $u$, twice differentiable in $\Omega$ and continuous on $\overline\Omega$, such that
\[ \class{ntn-Delta}{\Delta} u = 0 \ \text{in } \Omega, \qquad u = g \ \text{on } \class{ntn-dOm}{\partial\Omega}. \]
Here $\class{ntn-Delta}{\Delta}$ is the Laplacian, and "harmonic" means $\class{ntn-Delta}{\Delta} u=0$ (@def:harmonic, Lecture 2). The regularity clause ("twice differentiable in $\Omega$, continuous on $\overline\Omega$") is not on the slide. It makes precise what "$\class{ntn-Delta}{\Delta} u=0$ in $\Omega$" and "$u=g$ on $\class{ntn-dOm}{\partial\Omega}$" require.
:::

<p>The slide recalls that the previous lecture proved uniqueness: the problem has at most one solution. That is @thm:uniqueness (Lecture 2, by the energy method, for solutions $C^2$ up to the boundary). Lecture 4 proves it again under weaker assumptions (@cor:stability), and [E.12](apx:E12) gives a third proof. This lecture works toward the other half, that a solution exists, and it does so constructively. The construction is a numerical method you could run on a computer.</p>
