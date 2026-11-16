---
id: h10
slide: Slide 11
title: The sampling theorem
---

::: motivation
<p>@cor:if-is-continuous-and-time forbids a nonzero continuous signal from being limited both in time and in frequency. Band-limited functions remain an idealization of real signals. Within that idealization, the samples at the integers should rebuild the whole function.</p>
:::

::: theorem {#thm:whittaker-kotelnikov-shannon name="Whittaker, Kotelnikov, Shannon"}
Let $g$ be $C^2$ on $\R$ and vanish outside $[-\frac12,\frac12]$, and let $f(x):=\int g(\xi)e^{2\pi ix\xi}d\xi$. Then for every $x\in\R$, with absolutely convergent series,
\[ f(x)=\sum_{n\in\mathbb Z}f(n)\class{ntn-sinc}{\operatorname{sinc}}(x-n)=\sum_{n\in\mathbb Z}f(n)\,\frac{\sin\pi(x-n)}{\pi(x-n)}. \]
:::

::: plain
<p>If every frequency lies in an interval of length one, the function is the sum of its samples at the integers. Each sample is multiplied by a sinc function centred at that integer. The frequency content must be twice continuously differentiable. The series converges absolutely.</p>
:::
<figure>{{fig:h10-1}}<figcaption>The samples $f(n)$ (red), the terms $f(n)\class{ntn-sinc}{\operatorname{sinc}}(x-n)$ (grey), and their sum $f$ (blue).</figcaption></figure>
<p>So $f$ is band-limited ($\class{ntn-hat}{\hat f}=g$ vanishes outside $[-\frac12,\frac12]$, Step 1 below), and it is completely determined by its values at the integers. Each term $f(n)\class{ntn-sinc}{\operatorname{sinc}}(x-n)$ equals $f(n)$ at $x=n$ and $0$ at the other integers, so the series interpolates the samples. The proof (@sec:h12–@sec:h13) needs one more tool.</p>
