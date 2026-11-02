---
id: h13
slide: Slide 14
title: 'The sampling theorem: end of proof'
---
::: proof {title="Step 3: the interpolation formula."}
Let $x\in\R$. Multiply Step 2 by $e^{2\pi ix\xi}$ and integrate over $[-\frac12,\frac12]$ (Step 2 fails at most at the two endpoints, which do not affect the integral). The series $\sum_nf(n)e^{-2\pi in\xi}$ converges uniformly in $\xi$, since its terms are bounded by $|f(n)|$ and $\sum|f(n)|\lt\infty$ (Step 1 and the [M-test](apx:A21)), so it may be integrated term by term. By @lem:the-box, $\int_{-1/2}^{1/2}e^{2\pi it\xi}d\xi=\class{ntn-sinc}{\operatorname{sinc}}t$. Therefore
\[ f(x)=\int_{-1/2}^{1/2}g(\xi)e^{2\pi ix\xi}d\xi=\sum_nf(n)\int_{-1/2}^{1/2}e^{2\pi i(x-n)\xi}d\xi=\sum_nf(n)\class{ntn-sinc}{\operatorname{sinc}}(x-n). \]
The series converges absolutely because $|\class{ntn-sinc}{\operatorname{sinc}}|\le1$ and $\sum|f(n)|\lt\infty$.
:::
::: remark {#rem:the-proof-in-one-line name="the proof in one line"}
$f$ and $g$ are a Fourier pair. Sampling $f$ at the integers turns $g$ into its periodic version $\sum_mg(\xi+m)$ (Poisson). If $g$ lives in a window of width $1$, the periodic version shows $g$ unchanged on the window, so the samples determine $g$, and hence $f$.
:::
