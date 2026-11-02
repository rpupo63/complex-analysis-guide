---
id: x9
slide: Slides 17–18
title: Derivatives of holomorphic functions
toc: Derivatives are holomorphic
---
<p>The derivative of a holomorphic function is holomorphic. This is a deeper theorem in general, but easy under slightly stronger regularity.</p>

::: proposition {#prop:let-be-holomorphic-with-then}
Let $f=\class{ntn-vphi}{\varphi}+i\class{ntn-spsi}{\psi}$ be holomorphic with $\class{ntn-vphi}{\varphi},\class{ntn-spsi}{\psi}\in C^2$. Then $f'=\class{ntn-vphi}{\varphi}_x+i\class{ntn-spsi}{\psi}_x$ is holomorphic, with $C^1$ parts.
:::
::: proof
By @thm:cauchy-riemann, $f'=\class{ntn-vphi}{\varphi}_x+i\class{ntn-spsi}{\psi}_x$, and $\class{ntn-vphi}{\varphi}_x,\class{ntn-spsi}{\psi}_x$ are $C^1$. Differentiate the Cauchy–Riemann equations $\class{ntn-vphi}{\varphi}_x=\class{ntn-spsi}{\psi}_y$, $\class{ntn-vphi}{\varphi}_y=-\class{ntn-spsi}{\psi}_x$ of $f$, using [equality of mixed partials](apx:A2):
\[ (\class{ntn-vphi}{\varphi}_x)_x=(\class{ntn-spsi}{\psi}_y)_x=(\class{ntn-spsi}{\psi}_x)_y,\qquad(\class{ntn-vphi}{\varphi}_x)_y=(\class{ntn-vphi}{\varphi}_y)_x=(-\class{ntn-spsi}{\psi}_x)_x=-(\class{ntn-spsi}{\psi}_x)_x. \]
These are the Cauchy–Riemann equations for $\class{ntn-vphi}{\varphi}_x+i\class{ntn-spsi}{\psi}_x$ (real part $\class{ntn-vphi}{\varphi}_x$, imaginary part $\class{ntn-spsi}{\psi}_x$), and $C^1$ parts are differentiable, so @thm:cauchy-riemann applies.
:::

::: assumption {#asm:from-now-on-holomorphic-functions kind="Standing assumption" short="Standing assumption"}
From now on, holomorphic functions have $C^2$ (in practice, smooth) real and imaginary parts. That this is automatic is a theorem for later in the course: @cor:holomorphic-functions-are-smooth proves it, assuming only $C^1$ parts (@conv:holomorphic-near-k).
:::
