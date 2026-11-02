---
id: h15
slide: Slide 16
title: Sampling at rate $T$
---

::: corollary {#cor:sampling-at-rate-t name="sampling at rate $T$"}
Let $T\gt0$, let $g$ be $C^2$ on $\R$ and vanish outside $[-\frac T2,\frac T2]$, and let $f(x):=\int g(\xi)e^{2\pi ix\xi}d\xi$. Then, the series converging absolutely,
\[ f(x)=\sum_{n\in\mathbb Z}f\Big(\frac nT\Big)\class{ntn-sinc}{\operatorname{sinc}}(Tx-n)\qquad(x\in\R). \]
:::
::: proof
Substituting $\xi=T\eta$,
\[ f(x/T)=\int g(\xi)e^{2\pi i(x/T)\xi}d\xi=\int Tg(T\eta)\,e^{2\pi ix\eta}\,d\eta. \]
The function $\eta\mapsto Tg(T\eta)$ is $C^2$ and vanishes outside $[-\frac12,\frac12]$ (as $|T\eta|\le\frac T2\iff|\eta|\le\frac12$). So @thm:whittaker-kotelnikov-shannon applies to $f_T(y):=f(y/T)$: $f_T(y)=\sum_nf_T(n)\class{ntn-sinc}{\operatorname{sinc}}(y-n)$. Take $y=Tx$: $f_T(Tx)=f(x)$ and $f_T(n)=f(n/T)$.
:::
<p>So $T$ samples per unit length determine a signal whose frequencies lie in $[-\frac T2,\frac T2]$: the sampling rate must be twice the largest frequency $\frac T2$. This rate is the <b>Nyquist rate</b>. (Audio CDs sample at 44.1 kHz to capture frequencies up to about 22 kHz, just above human hearing.)</p>
