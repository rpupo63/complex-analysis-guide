---
id: o8
slide: Slide 9
title: Remarks
---

::: remark {#rem:history name=history}
Riemann (1851) argued this way, taking the solution of the Dirichlet problem from [Dirichlet's principle](apx:E10): minimize the energy. Weierstrass (1870) showed that such a minimum need not be attained; Hilbert (1900) rescued the principle. Our solution of the Dirichlet problem by minimizing energy over finite element spaces (Lecture 3), then passing to limits for piecewise linear and then for continuous data (Lectures 4–5), is such a rescue, for unions of squares.
:::

::: remark {#rem:greens-function name="Green's function"}
$G:=-\log|f|=h-\log|z-z_0|$ is harmonic on $\Omega\setminus\{z_0\}$ and zero on $\partial\Omega$, with a logarithmic singularity at $z_0$. In equilibrium heat flow it is, up to a constant factor, the temperature due to a point source at $z_0$ with the boundary held at $0$. In Lecture 2's language it is the potential of a point charge at $z_0$ ([E.6](apx:E6)) inside a grounded conductor $\partial\Omega$. So the Riemann map is $|f|=e^{-G}$: the conformal map and the Green's function carry the same information.
:::

::: remark {#rem:the-general-theorem name="the general theorem"}
The Riemann mapping theorem for every simply connected open $\Omega\ne\mathbb C$ (@thm:riemann-mapping-theorem-stated) is due to Osgood (1900). The standard modern proof (Koebe, Fejér–Riesz) avoids the Dirichlet problem: it maximizes $|f'(z_0)|$ over injective maps into the disk, using normal families.
:::
