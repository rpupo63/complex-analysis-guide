---
id: f16
slide: Slide 17
title: 'Lemma B: $P$ away from $z=1$'
---

::: lemma {#lem:lemma-b name="Lemma B"}
There is $\class{ntn-cLB}{c}\gt0$ such that, if $0\lt t\le1$, $r=e^{-t}$ and $t\le|\theta|\le\pi$, then
\[ |\class{ntn-Pz}{P}(re^{i\theta})|\le \class{ntn-Pz}{P}(r)\,e^{-\class{ntn-cLB}{c}/t}. \]
One can take $\class{ntn-cLB}{c}:=1-1/\class{ntn-lamB}{\lambda}\approx0.067$, with $\class{ntn-lamB}{\lambda}:=\sqrt{1+4/(e\pi^2)}$.
:::
::: proof
Let $z=re^{i\theta}$.
<ol>
<li><em>Compare term by term.</em> Since $|\class{ntn-Pz}{P}(z)|=|e^{\log \class{ntn-Pz}{P}(z)}|=e^{\operatorname{Re}\log \class{ntn-Pz}{P}(z)}$, @lem:log-p-as-a-series gives
\[ \log\frac{\class{ntn-Pz}{P}(r)}{|\class{ntn-Pz}{P}(z)|}=\sum_{m\ge1}\frac1m\Big(\frac{r^m}{1-r^m}-\operatorname{Re}\frac{z^m}{1-z^m}\Big). \]
Each term is $\ge0$: for $|w|\lt1$, $\operatorname{Re}\frac{w}{1-w}=\operatorname{Re}\sum_{j\ge1}w^j\le\sum_{j\ge1}|w|^j=\frac{|w|}{1-|w|}$; apply this with $w=z^m$, $|w|=r^m$.</li>
<li><em>Keep $m=1$.</em> Dropping the terms with $m\ge2$ only decreases the sum. Since $\frac r{1-r}=\frac1{1-r}-1$ and $\frac z{1-z}=\frac1{1-z}-1$,
\[ \log\frac{\class{ntn-Pz}{P}(r)}{|\class{ntn-Pz}{P}(z)|}\ge\frac r{1-r}-\operatorname{Re}\frac z{1-z}=\frac1{1-r}-\operatorname{Re}\frac1{1-z}\ge\frac1{1-r}-\frac1{|1-z|}. \]</li>
<li><em>$z$ stays away from $1$.</em> Expanding,
\[ |1-re^{i\theta}|^2=1-2r\cos\theta+r^2=(1-r)^2+2r(1-\cos\theta)=(1-r)^2+4r\sin^2\frac\theta2. \]
Now
\[ \sin\frac{|\theta|}2\ge\frac{|\theta|}\pi\ge\frac t\pi\ge\frac{1-r}\pi, \]
by concavity of $\sin$ on $[0,\frac\pi2]$ ($\sin x\ge\frac{2x}\pi$ there), then $|\theta|\ge t$, then $1-r=1-e^{-t}\le t$. As $t\le1$, $r\ge e^{-1}$, so
\[ |1-z|^2\ge(1-r)^2+\frac{4(1-r)^2}{e\pi^2}=\class{ntn-lamB}{\lambda}^2(1-r)^2,\qquad\class{ntn-lamB}{\lambda}=\sqrt{1+\tfrac4{e\pi^2}}\gt1. \]</li>
<li><em>Conclude.</em> So $\frac1{|1-z|}\le\frac1{\class{ntn-lamB}{\lambda}(1-r)}$, and step 2 gives
\[ \log\frac{\class{ntn-Pz}{P}(r)}{|\class{ntn-Pz}{P}(z)|}\ge\frac{1-1/\class{ntn-lamB}{\lambda}}{1-r}\ge\frac{\class{ntn-cLB}{c}}t, \]
using $1-r\le t$ once more. Exponentiate. <span class="qed">∎</span></li>
</ol>
:::
<p>Only the $m=1$ term was used: the pole of $\frac1{1-z}$ at $z=1$ alone makes $P$ smaller away from $1$ by the factor $e^{-\class{ntn-cLB}{c}/t}$. That factor is tiny compared with the polynomial factors in $t$ that appear on the major arc.</p>
