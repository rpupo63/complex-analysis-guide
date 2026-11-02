---
id: f17
slide: Slide 18
title: The Hardy–Ramanujan theorem
---

::: theorem {#thm:hardy-and-ramanujan-1918 name="Hardy and Ramanujan, 1918"}

\[ \class{ntn-pn}{p}(n)\sim\frac1{4\sqrt3\,n}\,e^{\pi\sqrt{2n/3}}\qquad(n\to\infty). \]
:::
<p>Here $a_n\sim b_n$ means $a_n/b_n\to1$ ([A.20](apx:A20)). The proof occupies @sec:f17–@sec:f19 and is assembled at the end of @sec:f19. Numerically the ratio of the two sides is $1.145$ at $n=10$, $1.046$ at $n=100$ and $1.014$ at $n=1000$.</p>

::: definition {#def:the-radius name="the radius"}
As in the upper bound (@thm:upper-bound), take
\[ \class{ntn-tpar}{t}:=\frac\pi{\sqrt{6n}},\qquad\class{ntn-mu}{\mu}:=nt=\frac{\pi^2}{6\class{ntn-tpar}{t}}=\pi\sqrt{\frac n6},\qquad\text{so }2\class{ntn-mu}{\mu}=\pi\sqrt{\frac{2n}3}. \]
Let $n\ge4$; then $\sqrt2\,\class{ntn-tpar}{t}\le1$ (equivalent to $2\pi^2\le6n$, and $\pi^2/3\approx3.3$).
:::

::: lemma {#lem:the-exponent-on-the-major-arc name="the exponent on the major arc"}
On the major arc put $\theta=ts$ with $|s|\le1$. Then $\class{ntn-tau}{\tau}=\class{ntn-tpar}{t}(1-is)$, @lem:lemma-a applies, and
\[ \frac{\pi^2}{6\class{ntn-tau}{\tau}}+n\class{ntn-tau}{\tau}=2\class{ntn-mu}{\mu}-\class{ntn-mu}{\mu}\,\frac{s^2+is^3}{1+s^2}. \]
:::
::: proof
$\class{ntn-tau}{\tau}=\class{ntn-tpar}{t}-i\theta=\class{ntn-tpar}{t}(1-is)$. Its argument is $-\arctan s\in[-\frac\pi4,\frac\pi4]$ and $|\class{ntn-tau}{\tau}|=\class{ntn-tpar}{t}\sqrt{1+s^2}\le\sqrt2\,\class{ntn-tpar}{t}\le1$, so @lem:lemma-a applies. Using $\frac{\pi^2}{6\class{ntn-tpar}{t}}=\class{ntn-mu}{\mu}$ and $nt=\class{ntn-mu}{\mu}$,
\[ \frac{\pi^2}{6\class{ntn-tau}{\tau}}+n\class{ntn-tau}{\tau}=\frac{\class{ntn-mu}{\mu}}{1-is}+\class{ntn-mu}{\mu}(1-is). \]
Now $\frac1{1-is}=\frac{1+is}{1+s^2}$, so
\[ \frac1{1-is}+1-is=\frac{(1+is)+(1-is)(1+s^2)}{1+s^2}=\frac{2+s^2-is^3}{1+s^2}=2-\frac{s^2+is^3}{1+s^2}. \]
<span class="qed">∎</span>
:::
<p>At $s=0$ the exponent is $2\class{ntn-mu}{\mu}=\pi\sqrt{2n/3}$, exactly the exponent of the upper bound. Away from $s=0$ its real part drops like $-\class{ntn-mu}{\mu} s^2$: a Gaussian bump of width about $1/\sqrt{\class{ntn-mu}{\mu}}$ in $s$.</p>
