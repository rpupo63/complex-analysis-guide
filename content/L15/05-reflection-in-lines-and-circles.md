---
id: q5
slide: Slide 6
title: Reflection in lines and circles
---

::: corollary {#cor:reflection-in-a-line name="reflection in a line"}
In @set:a-symmetric-open-set, let $f$ be holomorphic on $\Omega^+$, continuous on $\Omega^+\cup I$, with $f(I)$ contained in the line $L=\{a+e^{i\theta}t:t\in\mathbb R\}$. Then $f$ extends to a holomorphic $F$ on $\Omega$ with
\[ F(\bar z)=a+e^{2i\theta}\,\overline{F(z)-a}, \]
the mirror image of $F(z)$ in $L$.
:::
::: proof
$e^{-i\theta}(f-a)$ is real on $I$. Extend it by @thm:schwarz-reflection to $E$ with $E(\bar z)=\overline{E(z)}$, and put $F:=a+e^{i\theta}E$. Then $F(\bar z)=a+e^{i\theta}\,\overline{e^{-i\theta}(F(z)-a)}=a+e^{2i\theta}\,\overline{F(z)-a}$.
:::

::: corollary {#cor:reflection-in-a-circle name="reflection in a circle"}
In @set:a-symmetric-open-set, let $f$ be holomorphic on $\Omega^+$, continuous on $\Omega^+\cup I$, with $f(I)$ contained in the circle $|w-a|=r$. Then $f$ extends to a function $F$ on $\Omega$, holomorphic except for poles in $\Omega^-$, with
\[ F(\bar z)=a+\frac{r^2}{\overline{F(z)-a}}, \]
the mirror image of $F(z)$ in the circle. The poles are the points $\bar z$ with $f(z)=a$.
:::
::: proof
The Cayley map satisfies $C(\bar w)=\dfrac{\bar w-i}{\bar w+i}=1/\overline{C(w)}$, and $C^{-1}(w)=i\frac{1+w}{1-w}$ maps the unit circle minus $1$ into $\mathbb R$ (@prop:cayley-map). Let $x\in I$.
<ul>
<li>If $f(x)\ne a+r$, then $f\ne a+r$ on $D^+\cup(D\cap\mathbb R)$ for a small disk $D$ about $x$, by continuity. There $E:=C^{-1}\big((f-a)/r\big)$ is holomorphic on $D^+$, continuous up to $D\cap\mathbb R$, and real on $D\cap\mathbb R$. Extend $E$ by @thm:schwarz-reflection and put $F:=a+r\,C(E)$, which equals $f$ on $D^+$. Then
\[ F(\bar z)=a+r\,C\big(\overline{E(z)}\big)=a+\frac{r}{\overline{C(E(z))}}=a+\frac{r^2}{\overline{F(z)-a}}. \]</li>
<li>If $f(x)=a+r$, do the same with $C^{-1}\big((a-f)/r\big)$, which is defined near $x$, since $(a-f(x))/r=-1$.</li>
</ul>
The local extensions agree where they overlap, since each is given on $\Omega^-$ by the displayed formula. $F$ has a pole exactly where $F(z)=a$ for $z\in\Omega^+$, at $\bar z$.
:::

::: example {#eg:the-cayley-map-by-reflection name="the Cayley map"}
$C$ maps $\mathbb R$ into the unit circle, and $C(\bar z)=\dfrac{\bar z-i}{\bar z+i}=1/\overline{C(z)}$: its pole $-i$ is the mirror image of its zero $i$.
:::

::: corollary {#cor:zero-on-a-segment name="zero on a segment"}
If $f$ is holomorphic on $\mathbb H$, continuous on $\mathbb H\cup(a,b)$, and $0$ on $(a,b)$, then $f=0$.
:::
::: proof
Take $\Omega:=\mathbb H\cup(a,b)\cup\{\bar z:z\in\mathbb H\}$, which is open, symmetric and connected. By @thm:schwarz-reflection, $f$ extends to $F$ holomorphic on $\Omega$, and $F=0$ on $(a,b)$. By the identity theorem (@thm:identity-theorem-l10), $F=0$.
:::
