---
id: h14
slide: Slide 15
title: 'Why the band limit: aliasing'
---
<p>At every integer $n$, $e^{2\pi i(\xi+1)n}=e^{2\pi i\xi n}e^{2\pi in}=e^{2\pi i\xi n}$. <b>Frequencies $\xi$ and $\xi+1$ give the same samples.</b> So samples at the integers can only tell apart the frequencies in a band of width $1$, such as $[-\frac12,\frac12]$.</p>
::: example {#eg:aliasing name=aliasing}
$\cos(2\pi\cdot0.3\,x)$ and $\cos(2\pi\cdot0.7\,x)$ agree at every integer, as $0.7=1-0.3$:
\[ \cos(2\pi\cdot0.7n)=\cos(2\pi n-2\pi\cdot0.3n)=\cos(2\pi\cdot0.3n). \]

:::
<figure>{{fig:h14-1}}<figcaption>Frequencies $0.3$ (blue) and $0.7$ (red, thin): the same samples at the integers.</figcaption></figure>
<p>In signal processing this is <em>aliasing</em>: a frequency outside the band masquerades as one inside it. It is why the wheels of a car in a film can seem to turn backwards.</p>
