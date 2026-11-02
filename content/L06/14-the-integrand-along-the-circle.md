---
id: f14
slide: Slide 15
title: The integrand along the circle
---

::: proposition {#prop:p-n-as-an-integral name="$\class{ntn-pn}{p}(n)$ as an integral"}
Let $t\gt0$ and $\class{ntn-tau}{\tau}:=t-i\theta$. Then
\[ \class{ntn-pn}{p}(n)=\frac1{2\pi}\int_{-\pi}^{\pi}\class{ntn-Pz}{P}(e^{-\class{ntn-tau}{\tau}})\,e^{n\class{ntn-tau}{\tau}}\,d\theta. \]
:::
::: proof
As $\theta$ runs over $[-\pi,\pi]$, $z=e^{-\class{ntn-tau}{\tau}}=e^{-t}e^{i\theta}$ runs once around the circle $|z|=e^{-t}\lt1$. Put $z$ into $\class{ntn-Pz}{P}(z)=\sum_mp(m)z^m$ and multiply by $e^{n\class{ntn-tau}{\tau}}$:
\[ \class{ntn-Pz}{P}(e^{-\class{ntn-tau}{\tau}})\,e^{n\class{ntn-tau}{\tau}}=\sum_mp(m)\,e^{(n-m)\class{ntn-tau}{\tau}}=\sum_mp(m)\,e^{(n-m)t}\,e^{i(m-n)\theta}. \]
The terms are bounded by $\class{ntn-pn}{p}(m)e^{(n-m)t}$, which is summable (@prop:eulers-product at $r=e^{-t}$), so the series converges uniformly in $\theta$ (M-test) and may be integrated term by term. As $\int_{-\pi}^\pi e^{i(m-n)\theta}d\theta$ is $2\pi$ if $m=n$ and $0$ otherwise, only $m=n$ survives, giving $2\pi \class{ntn-pn}{p}(n)$.
:::
<p>This is Cauchy's coefficient formula of @thm:power-series, $\class{ntn-pn}{p}(n)=\frac1{2\pi i}\oint_{|z|=e^{-t}}\class{ntn-Pz}{P}(z)z^{-n-1}dz$, written with $z=e^{-t+i\theta}$, $dz=iz\,d\theta$ and $z^{-n}=e^{n\class{ntn-tau}{\tau}}$.</p>
<p>The integrand has modulus $e^{nt}|\class{ntn-Pz}{P}(e^{-t+i\theta})|$. Since $|\class{ntn-Pz}{P}(z)|\le\sum \class{ntn-pn}{p}(m)|z|^m=\class{ntn-Pz}{P}(|z|)$, with equality at $\theta=0$, it is largest at $\theta=0$, and in fact sharply peaked there.</p>
<figure>{{fig:f14-1}}<figcaption>Blue: $\log|\class{ntn-Pz}{P}(e^{-t+i\theta})|$ for $n=1000$, $t=\pi/\sqrt{6n}$. Red dashed: the formula of @lem:lemma-a, which uses only the pole at $z=1$. The peaks at other roots of unity are much lower.</figcaption></figure>
<p>The plan (the [circle method](apx:E19) of Hardy and Ramanujan) splits the circle in two:</p>
<ul>
<li><b>Major arc</b> $|\theta|\le t$: near $z=1$, where @lem:lemma-a gives a precise formula for $P$.</li>
<li><b>Minor arc</b> $t\lt|\theta|\le\pi$: away from $z=1$, where @lem:lemma-b shows $P$ is much smaller.</li>
</ul>
