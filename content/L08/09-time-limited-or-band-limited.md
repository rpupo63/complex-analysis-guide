---
id: h9
slide: Slide 10
title: Time-limited or band-limited, not both
---

::: definition {#def:a-function-on-is-time}
A function $f$ on $\R$ is <em>time-limited</em> if it vanishes outside a bounded interval, and <em>band-limited</em> if $\class{ntn-hat}{\hat f}$ does.
:::

::: motivation
<p>Entire transforms of time-limited continuous functions are the content of @thm:paley-wiener-a-simple-form. Band-limiting also asks the transform to vanish outside a bounded interval. A nonzero continuous signal should be unable to meet both restrictions.</p>
:::

::: corollary {#cor:if-is-continuous-and-time}
If $f$ is continuous and time-limited, and $\class{ntn-hat}{\hat f}$ vanishes on an interval of positive length, then $f\equiv0$. In particular, a continuous $f\not\equiv0$ is not both time-limited and band-limited.
:::
::: proof
By Paley–Wiener (a), $\class{ntn-hat}{\hat f}$ is entire. Every point of the interval is a limit of other zeros, so the zeros are not isolated and $\class{ntn-hat}{\hat f}\equiv0$ (@thm:isolated-zeros). Then $f$ and $\class{ntn-hat}{\hat f}=0$ are continuous and integrable, and Fourier inversion gives $f=\int0\cdot e^{2\pi ix\xi}d\xi=0$. For the second statement: if $f$ is band-limited, $\class{ntn-hat}{\hat f}$ vanishes outside a bounded interval, in particular on an interval of positive length.
:::

::: plain
<p>A continuous time-limited function whose transform vanishes on some interval must be identically zero. A nonzero continuous function cannot be both time-limited and band-limited. A signal cannot be confined both in time and in frequency.</p>
:::
<p>This is a form of the uncertainty principle: a signal cannot be confined both in time and in frequency. It is the identity theorem in disguise. Every real signal is time-limited, so "band-limited" in the next sections is always an idealization.</p>
