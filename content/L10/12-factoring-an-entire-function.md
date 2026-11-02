---
id: k12
slide: Slide 13
title: Factoring an entire function
---

::: corollary {#cor:weierstrass-factorization name="Weierstrass factorization"}
Every entire $f\not\equiv0$ can be written
\[ f(z)=z^m\,e^{h(z)}\prod_k\class{ntn-Ep}{E_k}\Big(\frac z{a_k}\Big), \]
with $h$ entire, $m\ge0$ the order of the zero of $f$ at $0$, and $a_k$ the zeros of $f$ other than $0$, each listed as often as its order.
:::
::: proof

<ol>
<li><em>The zeros are a legitimate list.</em> By the identity theorem, the zeros of $f\not\equiv0$ have no limit point in $\mathbb C$, so each disk $|z|\le R$ contains finitely many (else Bolzano–Weierstrass would give one). Each zero has finite order (otherwise $f\equiv0$ near it, hence on $\mathbb C$). So the $a_k$ are finitely many, or $|a_k|\to\infty$.</li>
<li><em>A function with the same zeros.</em> $Q(z):=z^m\prod_k\class{ntn-Ep}{E_k}(z/a_k)$ is entire (@thm:weierstrass, or a finite product) with the same zeros as $f$, with the same orders.</li>
<li><em>The quotient.</em> As in Step 1 of @sec:k7, $f/Q$ extends to an entire function without zeros: at a common zero $a$ of order $p$, $f=(z-a)^ph_1$ and $Q=(z-a)^ph_2$ with $h_1,h_2$ nonzero near $a$. By @lem:no-zeros, $f/Q=e^h$ with $h$ entire. <span class="qed">∎</span></li>
</ol>
:::
