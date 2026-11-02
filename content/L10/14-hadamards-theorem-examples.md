---
id: k14
slide: Slide 15
title: 'Hadamard''s theorem: examples'
---

::: example {#eg:the-sine-again name="the sine again"}
$\sin\pi z$ has order $1$ (table of @sec:j9), so $p=1$. List its nonzero zeros as $1,-1,2,-2,\dots$ and pair consecutive factors (grouping factors of a convergent product does not change its limit, as it only selects a subsequence of partial products):
\[ \class{ntn-Ep}{E_1}\Big(\frac zn\Big)\class{ntn-Ep}{E_1}\Big(-\frac zn\Big)=\Big(1-\frac zn\Big)e^{z/n}\Big(1+\frac zn\Big)e^{-z/n}=1-\frac{z^2}{n^2}. \]
So $\sin\pi z=z\,e^{a+bz}\prod_{n\ge1}(1-\frac{z^2}{n^2})$. Here $e^{a+bz}$ is even, as a quotient of odd functions, so $b=0$; and letting $z\to0$, $e^a=\lim\frac{\sin\pi z}z=\pi$. This is Euler's product again (@thm:euler).
:::

::: example {#eg:cos-sqrt-z name="$\cos\sqrt z$"}
$\cos\sqrt z:=\sum_{n\ge0}\frac{(-z)^n}{(2n)!}$ has order $\frac12$ (@sec:j9), so $p=0$ and $h$ is a constant. Its zeros $\pi^2(n-\frac12)^2$, $n\ge1$, are simple (the derivative, $-\frac{\sin w}{2w}$ at $w=\sqrt z$, is nonzero there), and $\cos\sqrt0=1$ fixes $e^h=1$. So, with $\class{ntn-Ep}{E_0}(w)=1-w$,
\[ \cos\sqrt z=\prod_{n\ge1}\Big(1-\frac{z}{\pi^2(n-\frac12)^2}\Big). \]
Replacing $z$ by $z^2$ gives the companion of Euler's product: $\cos z=\prod_{n\ge1}\big(1-\frac{4z^2}{\pi^2(2n-1)^2}\big)$.
:::
