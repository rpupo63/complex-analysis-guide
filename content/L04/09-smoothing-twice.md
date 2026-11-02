---
id: t10
slide: Slide 10
title: 'Weyl''s lemma: smoothing twice'
toc: Smoothing twice
---
<p>Two facts drive the argument. (1) $\class{ntn-ud}{u_\delta}$ is harmonic (@prop:u-delta-is-harmonic). (2) Smoothing a harmonic function does nothing: $h\class{ntn-conv}{*}\class{ntn-chid}{\chi_{\delta'}}=h$ (@lem:averaging, using @thm:mean-value-property to get the mean value property).</p>

::: lemma {#lem:shrinking-twice name="shrinking twice"}
$\class{ntn-Omd}{\Omega_{\delta+\delta'}}\subset(\class{ntn-Omd}{\Omega_\delta})_{\delta'}$: if the closed disk of radius $\delta+\delta'$ about $z$ lies in $\Omega$, then the closed disk of radius $\delta'$ about $z$ lies in $\class{ntn-Omd}{\Omega_\delta}$.
:::
::: proof
Let $|w-z|\le\delta'$. Any $\zeta$ with $|\zeta-w|\le\delta$ has $|\zeta-z|\le\delta+\delta'$ by the triangle inequality, so it lies in $\Omega$. So the closed $\delta$-disk about $w$ lies in $\Omega$, i.e. $w\in\class{ntn-Omd}{\Omega_\delta}$.
:::

::: lemma {#lem:the-order-of-two-smoothings-does name="the order of two smoothings does not matter"}
On $\class{ntn-Omd}{\Omega_{\delta+\delta'}}$, $\ (u\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta})\class{ntn-conv}{*}\class{ntn-chid}{\chi_{\delta'}}=(u\class{ntn-conv}{*}\class{ntn-chid}{\chi_{\delta'}})\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}$.
:::
::: proof
Fix $z\in\class{ntn-Omd}{\Omega_{\delta+\delta'}}$. Writing out both convolutions,
\[ \big((u\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta})\class{ntn-conv}{*}\class{ntn-chid}{\chi_{\delta'}}\big)(z)=\iint\Big(\iint u(\xi)\,\class{ntn-chid}{\chi_\delta}(\zeta-\xi)\,dA(\xi)\Big)\class{ntn-chid}{\chi_{\delta'}}(z-\zeta)\,dA(\zeta). \]
Every $\xi$ that contributes is within $\delta+\delta'$ of $z$, so in $\Omega$. The integrand is absolutely integrable ($u$ is integrable on that bounded disk, the weights are bounded), so [Fubini's theorem](apx:A13) lets us integrate over $\zeta$ first:
\[ =\iint u(\xi)\Big(\iint\class{ntn-chid}{\chi_\delta}(\zeta-\xi)\,\class{ntn-chid}{\chi_{\delta'}}(z-\zeta)\,dA(\zeta)\Big)dA(\xi). \]
In the inner integral substitute $w=\zeta-\xi$ (a shift, which preserves area), and then $w'=(z-\xi)-w$ (a reflection and shift, also area-preserving):
\[ \iint\class{ntn-chid}{\chi_\delta}(w)\,\class{ntn-chid}{\chi_{\delta'}}(z-\xi-w)\,dA(w)=\iint\class{ntn-chid}{\chi_\delta}(z-\xi-w')\,\class{ntn-chid}{\chi_{\delta'}}(w')\,dA(w'). \]
The left form is the inner integral for the order "$\delta$ then $\delta'$", the right form for "$\delta'$ then $\delta$". So both orders equal $\iint u(\xi)\,K(z-\xi)\,dA(\xi)$ with the same combined weight $K$.
:::

::: proposition {#prop:all-the-u-delta-are-one name="all the $\class{ntn-ud}{u_\delta}$ are one function"}
For all $\delta,\delta'\gt0$, $\ \class{ntn-ud}{u_\delta}=\class{ntn-ud}{u_{\delta'}}$ on $\class{ntn-Omd}{\Omega_{\delta+\delta'}}$.
:::
::: proof
On $\class{ntn-Omd}{\Omega_{\delta+\delta'}}$:
\[ \class{ntn-ud}{u_\delta}\overset{(i)}=\class{ntn-ud}{u_\delta}\class{ntn-conv}{*}\class{ntn-chid}{\chi_{\delta'}}=(u\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta})\class{ntn-conv}{*}\class{ntn-chid}{\chi_{\delta'}}\overset{(ii)}=(u\class{ntn-conv}{*}\class{ntn-chid}{\chi_{\delta'}})\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}=\class{ntn-ud}{u_{\delta'}}\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}\overset{(iii)}=\class{ntn-ud}{u_{\delta'}}. \]
(i) $\class{ntn-ud}{u_\delta}$ is smooth and harmonic on the open set $\class{ntn-Omd}{\Omega_\delta}$ ([Props. #](@prop:u-delta-is-smooth), [#](@prop:u-delta-is-harmonic)), so it has the mean value property there (@thm:mean-value-property), and @lem:averaging, applied with $\class{ntn-Omd}{\Omega_\delta}$ in place of $\Omega$, gives $\class{ntn-ud}{u_\delta}\class{ntn-conv}{*}\class{ntn-chid}{\chi_{\delta'}}=\class{ntn-ud}{u_\delta}$ on $(\class{ntn-Omd}{\Omega_\delta})_{\delta'}$, which contains $\class{ntn-Omd}{\Omega_{\delta+\delta'}}$ by @lem:shrinking-twice. (ii) @lem:the-order-of-two-smoothings-does. (iii) The same as (i) with the roles of $\delta$ and $\delta'$ exchanged.
:::

::: definition {#def:the-function-v name="the function $v$"}
For $z\in\Omega$, choose any $\delta\gt0$ with $z\in\class{ntn-Omd}{\Omega_{2\delta}}$ and set $v(z):=\class{ntn-ud}{u_\delta}(z)$.
:::
<p>This is well defined. Such a $\delta$ exists because $\Omega$ is open. If $\delta$ and $\delta'$ both qualify, say $\delta\le\delta'$, then $z\in\class{ntn-Omd}{\Omega_{2\delta'}}\subset\class{ntn-Omd}{\Omega_{\delta+\delta'}}$ (a disk of radius $\delta+\delta'\le2\delta'$ fits inside one of radius $2\delta'$), so @prop:all-the-u-delta-are-one gives $\class{ntn-ud}{u_\delta}(z)=\class{ntn-ud}{u_{\delta'}}(z)$. This is the slide's "a single $v$ with $\class{ntn-ud}{u_\delta}=v$ at all points farther than $2\delta$ from $\class{ntn-dOm}{\partial\Omega}$".</p>

::: theorem {#thm:proof-of-weyls-lemma name="proof of Weyl's lemma"}
$v$ is smooth and harmonic on $\Omega$, and $u=v$ almost everywhere.
:::
::: proof
<em>Smooth and harmonic.</em> Fix $\delta$. On the open set $\class{ntn-Omd}{\Omega_{2\delta}}$, $v=\class{ntn-ud}{u_\delta}$ (by definition, using this $\delta$ for every point there), and $\class{ntn-ud}{u_\delta}$ is smooth and harmonic. Every point of $\Omega$ lies in some $\class{ntn-Omd}{\Omega_{2\delta}}$, so $v$ is smooth and harmonic near every point.<br>
<em>$v=u$ almost everywhere.</em> Let $K\subset\Omega$ be compact. Choose $\delta_0$ with $K\subset\class{ntn-Omd}{\Omega_{2\delta_0}}$ ([C.5](apx:C5)). For $\delta\le\delta_0$, $K\subset\class{ntn-Omd}{\Omega_{2\delta}}$ too, so $\class{ntn-ud}{u_\delta}=v$ on $K$. By @fact:smoothing, $\class{ntn-ud}{u_\delta}\to u$ in $L^2(K)$. But $\class{ntn-ud}{u_\delta}$ restricted to $K$ is the same function $v$ for every such $\delta$, so
\[ \norm{v-u}_{L^2(K)}=\lim_{\delta\to0}\norm{\class{ntn-ud}{u_\delta}-u}_{L^2(K)}=0. \]
A function with zero $L^2$ norm is zero almost everywhere, so $u=v$ almost everywhere on $K$. $\Omega$ is the union of the countably many compact sets
\[ K_j:=\{z\in\Omega:\ |z|\le j\ \text{and the closed disk of radius }1/j\text{ about }z\text{ lies in }\Omega\},\qquad j=1,2,\dots, \]
and a countable union of sets of measure zero has measure zero, so $u=v$ almost everywhere on $\Omega$.
:::
<p>From now on $u$ denotes $v$: we changed $u$ only on a set of area zero, which does not change it as an element of $L^2$ ([D.2](apx:D2)).</p>

::: corollary {#cor:the-lecture-3-limit-is-a name="the Lecture 3 limit is a classical harmonic function"}
Under @hyp:for-now, the limit $u$ of the finite element solutions $\class{ntn-Un}{U_n}$ is smooth in $\Omega$ and satisfies $\class{ntn-Delta}{\Delta} u=0$ at every point of $\Omega$.
:::
::: proof
@prop:the-limit-from-lecture-3 verifies the hypothesis of Weyl's lemma, and @thm:proof-of-weyls-lemma gives the conclusion.
:::
<p>This settles the first of the two "missing pieces" listed in @sec:s21. The second, that $u(z)\to g(p)$ as $z\to p\in\class{ntn-dOm}{\partial\Omega}$, is the subject of Lecture 5 (@thm:step-4-boundary-values).</p>
