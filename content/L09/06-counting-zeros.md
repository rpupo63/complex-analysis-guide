---
id: j6
slide: Slide 7
title: Counting zeros
---
<p>For $f$ holomorphic near $|z|\le R$, let $\class{ntn-Mr}{M}(R):=\max_{|z|=R}|f|$, and let $\class{ntn-nr}{n}(r)$ be the number of zeros of $f$ in $|z|\le r$, counted with multiplicity.</p>

::: lemma {#lem:maximum-modulus name="maximum modulus"}
If $f$ is holomorphic near $|z|\le R$, then $|f(w)|\le \class{ntn-Mr}{M}(R)$ for $|w|\le R$. In particular $\class{ntn-Mr}{M}(R')\le \class{ntn-Mr}{M}(R)$ for $R'\lt R$.
:::
::: proof
Fix $w$ and choose a real $\alpha$ with $e^{-i\alpha}f(w)=|f(w)|$. The function $u:=\operatorname{Re}(e^{-i\alpha}f)$ is harmonic (@cor:holomorphic-functions-are-smooth), so by the maximum principle (@cor:maximum-principle) on the disk,
\[ |f(w)|=u(w)\le\max_{|z|=R}u\le\max_{|z|=R}|e^{-i\alpha}f|=\class{ntn-Mr}{M}(R). \]
<span class="qed">∎</span>
:::
<p>The slide's "(maximum principle)" refers to this lemma.</p>

::: corollary {#cor:counting-zeros name="counting zeros"}
Let $f$ be holomorphic near $|z|\le R$, $f(0)\ne0$, and $0\lt r\lt R$. Then
\[ \class{ntn-nr}{n}(r)\le\frac{\log \class{ntn-Mr}{M}(R)-\log|f(0)|}{\log(R/r)}. \]
:::
::: proof

<ol>
<li><em>If $f\ne0$ on $|z|=R$.</em> In Jensen's formula, each of the $\class{ntn-nr}{n}(r)$ zeros with $|a_j|\le r$ contributes $\log\frac R{|a_j|}\ge\log\frac Rr$, and the others contribute $\gt0$. The left side is at most $\log \class{ntn-Mr}{M}(R)$, as $\log|f(Re^{i\theta})|\le\log \class{ntn-Mr}{M}(R)$. So $\class{ntn-nr}{n}(r)\log\frac Rr\le\log \class{ntn-Mr}{M}(R)-\log|f(0)|$.</li>
<li><em>Otherwise.</em> $f$ is holomorphic on a disk $|z|\lt R''$ with $R''\gt R$ ([C.5](apx:C5)(a)), which is connected, and $f\not\equiv0$ there as $f(0)\ne0$. So its zeros cannot accumulate (@thm:isolated-zeros), and only finitely many lie in the compact disk $|z|\le R$. Hence $f\ne0$ on $|z|=R'$ for all $R'$ close to $R$ except finitely many. For such $R'\in(r,R)$, step 1 and @lem:maximum-modulus give
\[ \class{ntn-nr}{n}(r)\le\frac{\log \class{ntn-Mr}{M}(R')-\log|f(0)|}{\log(R'/r)}\le\frac{\log \class{ntn-Mr}{M}(R)-\log|f(0)|}{\log(R'/r)}. \]
Let $R'\uparrow R$. <span class="qed">∎</span></li>
</ol>
:::
<p>So <b>a function that is not too big cannot have too many zeros</b>. A polynomial of degree $d$ is the model: $\log \class{ntn-Mr}{M}(R)\approx d\log R$, and taking $R$ huge recovers $\class{ntn-nr}{n}(r)\le d$.</p>
