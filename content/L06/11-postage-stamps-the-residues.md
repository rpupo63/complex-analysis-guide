---
id: f11
slide: Slide 12
title: 'Postage stamps: the residues'
---

::: lemma {#lem:the-simple-poles name="the simple poles"}
If $\zeta^a=1\ne\zeta$, then $\zeta^b\ne1$, $\zeta$ is a simple pole of $\class{ntn-Gst}{G}$, and
\[ -\class{ntn-res}{\operatorname{Res}}_\zeta \class{ntn-Gst}{G}=\frac{\zeta^{-n}}{a(1-\zeta^b)}. \]
Symmetrically, $-\class{ntn-res}{\operatorname{Res}}_\zeta \class{ntn-Gst}{G}=\frac{\zeta^{-n}}{b(1-\zeta^a)}$ if $\zeta^b=1\ne\zeta$. The only common root of $z^a=1$ and $z^b=1$ is $1$.
:::
::: proof
Since $a,b$ are coprime, [Bézout's identity](apx:B5) gives integers $x,y$ with $xa+yb=1$. If $\zeta^a=\zeta^b=1$, then $\zeta=\zeta^{xa+yb}=(\zeta^a)^x(\zeta^b)^y=1$. So $\zeta^a=1\ne\zeta$ forces $\zeta^b\ne1$.<br>
Apply @prop:simple-poles-of-a-quotient with $A:=\frac{z^{-n-1}}{1-z^b}$ (holomorphic near $\zeta$, as $\zeta^b\ne1$ and $\zeta\ne0$; and $A(\zeta)\ne0$) and $B:=1-z^a$, which has $B(\zeta)=0$ and $B'(\zeta)=-a\zeta^{a-1}=-a\zeta^a/\zeta=-a/\zeta\ne0$. So
\[ \class{ntn-res}{\operatorname{Res}}_\zeta \class{ntn-Gst}{G}=\frac{A(\zeta)}{B'(\zeta)}=\frac{\zeta^{-n-1}}{1-\zeta^b}\cdot\Big(-\frac\zeta a\Big)=-\frac{\zeta^{-n}}{a(1-\zeta^b)}. \]
<span class="qed">∎</span>
:::

::: lemma {#lem:the-double-pole-at-1 name="the double pole at $1$"}
$\class{ntn-Gst}{G}$ has a pole of order $2$ at $1$, and
\[ -\class{ntn-res}{\operatorname{Res}}_1\class{ntn-Gst}{G}=\frac1{ab}\Big(n+1+\frac{a-1}2+\frac{b-1}2\Big). \]
:::
::: proof
Let $\class{ntn-Qa}{Q_a}(z):=1+z+\dots+z^{a-1}$, so that $1-z^a=(1-z)\class{ntn-Qa}{Q_a}(z)$ (finite geometric sum). Then $(1-z^a)(1-z^b)=(z-1)^2\class{ntn-Qa}{Q_a}\class{ntn-Qa}{Q_b}$, and $\class{ntn-Gst}{G}=\frac{g}{(z-1)^2}$ with $g:=\frac{z^{-n-1}}{\class{ntn-Qa}{Q_a}\class{ntn-Qa}{Q_b}}$. As $\class{ntn-Qa}{Q_a}(1)=a\ne0$ and $\class{ntn-Qa}{Q_b}(1)=b$, $g$ is holomorphic near $1$ with $g(1)=\frac1{ab}\ne0$: a pole of order $2$, and $\class{ntn-res}{\operatorname{Res}}_1\class{ntn-Gst}{G}=g'(1)$ by @def:residue. By the product rule, where $g\ne0$,
\[ \frac{g'}{g}=-\frac{n+1}z-\frac{\class{ntn-Qa}{Q_a}'}{\class{ntn-Qa}{Q_a}}-\frac{\class{ntn-Qa}{Q_b}'}{\class{ntn-Qa}{Q_b}}. \]
At $z=1$: $\class{ntn-Qa}{Q_a}'(1)=0+1+\dots+(a-1)=\frac{a(a-1)}2$, so $\frac{\class{ntn-Qa}{Q_a}'(1)}{\class{ntn-Qa}{Q_a}(1)}=\frac{a-1}2$, and likewise for $b$. Hence
\[ -\class{ntn-res}{\operatorname{Res}}_1\class{ntn-Gst}{G}=-g(1)\cdot\frac{g'(1)}{g(1)}=\frac1{ab}\Big(n+1+\frac{a-1}2+\frac{b-1}2\Big). \]
<span class="qed">∎</span>
:::

::: theorem {#thm:the-stamp-formula name="the stamp formula"}
For every $n\ge0$,
\[ \class{ntn-cn}{c}(n)=\frac n{ab}+\frac1{2a}+\frac1{2b}+\frac1a\sum_{\zeta^a=1\ne\zeta}\frac{\zeta^{-n}}{1-\zeta^b}+\frac1b\sum_{\zeta^b=1\ne\zeta}\frac{\zeta^{-n}}{1-\zeta^a}. \]
:::
::: proof
@prop:counting-by-residues with [Lemmas #](@lem:the-simple-poles) and [#](@lem:the-double-pole-at-1), using $\frac1{ab}\big(1+\frac{a-1}2+\frac{b-1}2\big)=\frac{a+b}{2ab}=\frac1{2a}+\frac1{2b}$.
:::
<p>So $\class{ntn-cn}{c}(n)$ is a linear function $\frac n{ab}+\frac1{2a}+\frac1{2b}$ plus two periodic corrections: $\zeta^{-n}$ depends only on $n$ modulo $a$ (or $b$). The double pole gives the growth, the simple poles the wobble.</p>

::: example {#eg:3-and-5-stamps name="3¢ and 5¢ stamps"}
Take $a=3$, $b=5$. The two sums have period $15$ in $n$, so $\class{ntn-cn}{c}(n+15)=\class{ntn-cn}{c}(n)+\frac{15}{15}=\class{ntn-cn}{c}(n)+1$. Listing directly,
<div class="tbl"><table><thead><tr><th>$n$</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr></thead>
<tbody><tr><th>$\class{ntn-cn}{c}(n)$</th><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></tbody></table></div>
(for instance $8=3+5$, $11=6+5$, $14=9+5$). Since $\class{ntn-cn}{c}(n+15)=\class{ntn-cn}{c}(n)+1\ge1$, every $n\ge0$ except $1,2,4,7$ can be paid.
:::
<p>The largest amount that cannot be paid, $7=3\cdot5-3-5$, is an instance of Sylvester's formula $ab-a-b$ for the "Frobenius number".</p>
