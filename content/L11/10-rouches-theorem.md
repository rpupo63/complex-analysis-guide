---
id: m10
slide: Slide 11
title: Rouché's theorem
---
<p>The final slide returns to the argument principle (Lecture 7) and draws its most useful consequence: zeros are stable under small perturbations.</p>

::: theorem {#thm:rouche name=Rouché}
Let $f$, $g$ be holomorphic on an open set containing $\overline{\class{ntn-Dar}{D}(a,r)}$, and $C:=\partial \class{ntn-Dar}{D}(a,r)$. If $|f-g|\lt|f|$ on $C$, then $f$ and $g$ have equally many zeros in $\class{ntn-Dar}{D}(a,r)$, counted with multiplicity.
:::
<p>Picture: $g$ is $f$ plus a perturbation that is smaller than $f$ on the circle. A dog ($g$) on a leash shorter than its owner's ($f$) distance from a tree ($0$) circles the tree as often as its owner does ([winding numbers](apx:E17)).</p>
::: proof

<ol>
<li><em>Interpolate.</em> For $t\in[0,1]$ let $\class{ntn-ft}{f_t}:=f+t(g-f)$, so $f_0=f$ and $f_1=g$. On $C$, $|\class{ntn-ft}{f_t}|\ge|f|-t|g-f|\ge|f|-|g-f|\gt0$. So no $\class{ntn-ft}{f_t}$ vanishes on $C$.</li>
<li><em>Count.</em> By the argument principle (@thm:argument-principle, moved to the centre $a$; $\class{ntn-ft}{f_t}$ is holomorphic, so $P=0$),
\[ \class{ntn-Nt}{N}(t):=\frac1{2\pi i}\oint_C\frac{\class{ntn-ft}{f_t}'(z)}{\class{ntn-ft}{f_t}(z)}\,dz \]
is the number of zeros of $\class{ntn-ft}{f_t}$ in $\class{ntn-Dar}{D}(a,r)$: an integer.</li>
<li><em>$N$ is continuous.</em> The integrand $h(t,z):=\frac{f'(z)+t(g'(z)-f'(z))}{f(z)+t(g(z)-f(z))}$ is continuous on the [compact](apx:C5) set $[0,1]\times C$, as the denominator does not vanish there. So it is [uniformly continuous](apx:A16), and by the ML estimate
\[ |\class{ntn-Nt}{N}(t)-\class{ntn-Nt}{N}(s)|\le\frac{2\pi r}{2\pi}\max_{z\in C}|h(t,z)-h(s,z)|=r\max_{z\in C}|h(t,z)-h(s,z)|\longrightarrow0\quad(s\to t). \]</li>
<li><em>Integer-valued and continuous means constant.</em> If $\class{ntn-Nt}{N}(0)\ne \class{ntn-Nt}{N}(1)$, the [intermediate value theorem](apx:A24) would give a $t$ with $\class{ntn-Nt}{N}(t)$ equal to a non-integer between them. So $\class{ntn-Nt}{N}(0)=\class{ntn-Nt}{N}(1)$. <span class="qed">∎</span></li>
</ol>
:::
::: example {#eg:a-typical-use name="a typical use"}
How many zeros does $g(z)=z^5+3z+1$ have in $|z|\lt2$? Take $f(z)=z^5$. On $|z|=2$: $|g-f|=|3z+1|\le7\lt32=|f|$. So $g$, like $f$, has $5$ zeros in $|z|\lt2$, without solving anything. (Not from the slides; an illustration.)
:::
<p>Rouché's theorem gives a second proof of the fundamental theorem of algebra: for a polynomial of degree $d$ with leading term $f=cz^d$, the rest is smaller than $|f|$ on a large circle, so the polynomial has $d$ zeros inside.</p>
