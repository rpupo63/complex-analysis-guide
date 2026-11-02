---
id: h5
slide: Slide 6
title: Analyticity in a strip is exponential decay
---

::: fact {#fact:fourier-inversion name="Fourier inversion" status=cited}
If $f$ and $\class{ntn-hat}{\hat f}$ are continuous and integrable on $\R$, then $f(x)=\int\class{ntn-hat}{\hat f}(\xi)\,e^{2\pi ix\xi}\,d\xi$ for all $x\in\R$. Applied to $F$: if $F$ and $f(x):=\int F(\xi)e^{2\pi ix\xi}d\xi$ are continuous and integrable, then $\class{ntn-hat}{\hat f}=F$.
:::
<p>A standard theorem, used without proof; see [D.7](apx:D7). The second form follows from the first applied to $\xi\mapsto F(-\xi)$.</p>

::: theorem {#thm:strips-and-decay name="strips and decay"}
Let $f$ be continuous and integrable on $\R$, and $a\gt0$.<br>
(a) If $f$ extends holomorphically to the strip $|\operatorname{Im}z|\lt a$, with $|f(x+iy)|\le\dfrac{C}{1+x^2}$ for $|y|\lt a$, then $|\class{ntn-hat}{\hat f}(\xi)|\le\pi C\,e^{-2\pi a|\xi|}$.<br>
(b) Conversely, if $|\class{ntn-hat}{\hat f}(\xi)|\le C\,e^{-2\pi a|\xi|}$ for all $\xi\in\R$, then $f$ extends holomorphically to $|\operatorname{Im}z|\lt a$.
:::
<p>Check (a) on $\frac1{1+x^2}$: it is holomorphic for $|\operatorname{Im}z|\lt1$, and the theorem predicts decay at every rate $a\lt1$, consistent with $\pi e^{-2\pi|\xi|}$. (The bound $\frac{C}{1+x^2}$ holds only on narrower strips $|y|\le a'\lt1$, which is why $a\lt1$.)</p>
