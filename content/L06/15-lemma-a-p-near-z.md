---
id: f15
slide: Slide 16
title: 'Lemma A: $P$ near $z=1$'
---

::: lemma {#lem:lemma-a name="Lemma A" status=cited}
For $|\arg\class{ntn-tau}{\tau}|\le\pi/4$ and $0\lt|\class{ntn-tau}{\tau}|\le1$, with principal logarithms and an absolute $O$-constant,
\[ \log \class{ntn-Pz}{P}(e^{-\class{ntn-tau}{\tau}})=\frac{\pi^2}{6\class{ntn-tau}{\tau}}+\frac12\log\frac{\class{ntn-tau}{\tau}}{2\pi}+O(|\class{ntn-tau}{\tau}|). \]
:::
<p>The slide omits the proof ("compare $\sum_{k\ge1}-\log(1-e^{-k\class{ntn-tau}{\tau}})$ with an integral, using Stirling's formula"); an outline is in [E.19](apx:E19). The condition $|\arg\class{ntn-tau}{\tau}|\le\pi/4$ forces $\operatorname{Re}\class{ntn-tau}{\tau}\gt0$, so $|e^{-\class{ntn-tau}{\tau}}|\lt1$ and $\log \class{ntn-Pz}{P}(e^{-\class{ntn-tau}{\tau}})$ is defined by @lem:log-p-as-a-series. "Absolute $O$-constant" means one constant $C$ works for all such $\class{ntn-tau}{\tau}$ ([A.20](apx:A20)). As a check, for real $\class{ntn-tau}{\tau}=t$ the main term is the $\frac{\pi^2}{6t}$ of @lem:on-the-real-axis.</p>

::: corollary {#cor:lemma-a-exponentiated name="Lemma A, exponentiated"}
In the same range,
\[ \class{ntn-Pz}{P}(e^{-\class{ntn-tau}{\tau}})=\sqrt{\frac{\class{ntn-tau}{\tau}}{2\pi}}\;e^{\pi^2/(6\class{ntn-tau}{\tau})}\big(1+O(|\class{ntn-tau}{\tau}|)\big), \]
with the principal square root.
:::
::: proof
Exponentiate @lem:lemma-a: $e^{\frac12\log(\class{ntn-tau}{\tau}/2\pi)}$ is the principal root $\sqrt{\class{ntn-tau}{\tau}/2\pi}$ ([C.8](apx:C8)). For the error, if $|w|\le C|\class{ntn-tau}{\tau}|\le C$ then $|e^w-1|=\big|\sum_{j\ge1}w^j/j!\big|\le|w|e^{|w|}\le Ce^C|\class{ntn-tau}{\tau}|$, so $e^{O(|\class{ntn-tau}{\tau}|)}=1+O(|\class{ntn-tau}{\tau}|)$ for $|\class{ntn-tau}{\tau}|\le1$.
:::
<p>So near $z=1$, $P$ is huge, about $e^{\pi^2/(6\class{ntn-tau}{\tau})}$, and the formula comes from the pole structure at $z=1$ alone: every factor $\frac1{1-z^k}$ has a pole there. In the figure of @sec:f14, the dashed curve is this formula.</p>
