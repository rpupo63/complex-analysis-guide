---
id: E11
title: A sharper Poincaré constant
status:
- derived
---
<p>In step 3 of @thm:poincares-inequality, keep the factor $x$ instead of replacing it by $\class{ntn-L}{L}$:
\[ \int_0^{\class{ntn-L}{L}}|v(x,y)|^2dx\le\int_0^Lx\,dx\cdot\int_0^{\class{ntn-L}{L}}|\partial_xv|^2ds=\frac{\class{ntn-L}{L}^2}2\int_0^{\class{ntn-L}{L}}|\partial_xv|^2ds. \]
This gives $\norm{v}\le\frac{\class{ntn-L}{L}}{\sqrt2}\norm{\nabla v}$. The best constant for a strip of width $\class{ntn-L}{L}$ is $\class{ntn-L}{L}/\pi$, from the first eigenvalue of $-d^2/dx^2$ on $(0,\class{ntn-L}{L})$ with zero boundary values. For the existence proof any constant independent of $n,k$ is enough.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Poincar%C3%A9_inequality" target="_blank" rel="noopener">Poincaré inequality</a> · <a href="https://en.wikipedia.org/wiki/Wirtinger%27s_inequality_for_functions" target="_blank" rel="noopener">Wirtinger's inequality</a></p>
