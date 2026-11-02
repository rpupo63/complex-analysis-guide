---
id: j4
slide: Slide 5
title: The mean of $\log|Re^{i\theta}-a|$
---

::: lemma {#lem:the-mean-of-a-logarithmic-potential name="the mean of a logarithmic potential"}
For $R\gt0$ and $|a|\ne R$,
\[ \frac1{2\pi}\int_0^{2\pi}\log|Re^{i\theta}-a|\,d\theta=\log\max(R,|a|). \]
:::
::: proof
By the mean value property for harmonic functions, @thm:mean-value-property.
<ol>
<li><em>$|a|\gt R$ (charge outside).</em> $z\mapsto\log|z-a|$ is harmonic away from $a$ ([E.6](apx:E6)), in particular near $|z|\le R$. So its mean over the circle $|z|=R$ is its value at the centre: $\log|0-a|=\log|a|$.</li>
<li><em>$|a|\lt R$ (charge inside).</em> Factor out $R$:
\[ |Re^{i\theta}-a|=|e^{i\theta}|\,|R-ae^{-i\theta}|=|\overline{R-ae^{-i\theta}}|=|R-\bar ae^{i\theta}|=R\,\Big|1-\frac{\bar a}Re^{i\theta}\Big|. \]
So the mean is $\log R$ plus the mean over $|w|=1$ of $h(w):=\log|1-\frac{\bar a}{R}w|$. If $a=0$, $h\equiv0$. Otherwise $h(w)=\log\frac{|a|}R+\log|w-\frac R{\bar a}|$ is harmonic away from $\frac R{\bar a}$, which lies outside $|w|\le1$ since $|\frac R{\bar a}|\gt1$. So $h$ is harmonic near $|w|\le1$, and its mean over $|w|=1$ is $h(0)=\log1=0$. The total is $\log R$. <span class="qed">∎</span></li>
</ol>
:::
<p>Physically: the average of a point charge's potential over a circle is the potential at the centre if the charge is outside, and as if the charge sat on the circle ($\log R$) if it is inside. This is Newton's shell theorem in two dimensions.</p>
