---
id: g2
slide: Slide 3
title: 'The logarithmic derivative: proof'
---
::: proof {title="Proof of Lemma [#](=lem:logarithmic-derivative)."}

<ol>
<li><em>Rewrite as an average.</em> Let $\class{ntn-Gld}{G}(z):=(z-a)\,f'(z)/f(z)$. With $z=a+\epsilon e^{i\theta}$, $dz=i\epsilon e^{i\theta}d\theta=i(z-a)\,d\theta$, so
\[ \class{ntn-Ieps}{I}(\epsilon):=\frac1{2\pi i}\oint_{|z-a|=\epsilon}\frac{f'(z)}{f(z)}\,dz=\frac1{2\pi i}\int_0^{2\pi}\frac{f'(z)}{f(z)}\,i(z-a)\,d\theta=\frac1{2\pi}\int_0^{2\pi}\class{ntn-Gld}{G}(a+\epsilon e^{i\theta})\,d\theta. \]</li>
<li><em>$\class{ntn-Ieps}{I}(\epsilon)$ is constant.</em> $f'$ is holomorphic where $f$ is (@cor:holomorphic-functions-are-smooth), so $f'/f$ is holomorphic on $0\lt|z-a|\lt r$, where $f\ne0$. For $0\lt\epsilon_1\lt\epsilon_2\lt r$, @lem:moving-the-circle with $C:|z-a|=\epsilon_2$ and the single inner circle $|z-a|=\epsilon_1$ gives $\class{ntn-Ieps}{I}(\epsilon_1)=\class{ntn-Ieps}{I}(\epsilon_2)$.</li>
<li><em>Reduce to a limit.</em> Writing $\pm m=\frac1{2\pi}\int_0^{2\pi}(\pm m)\,d\theta$,
\[ |\class{ntn-Ieps}{I}(\epsilon)\mp m|=\Big|\frac1{2\pi}\int_0^{2\pi}\big(\class{ntn-Gld}{G}(a+\epsilon e^{i\theta})\mp m\big)\,d\theta\Big|\le\max_\theta|\class{ntn-Gld}{G}(a+\epsilon e^{i\theta})\mp m|. \]
So if $\class{ntn-Gld}{G}(z)\to\pm m$ as $z\to a$, then $\class{ntn-Ieps}{I}(\epsilon)\to\pm m$ as $\epsilon\to0$; and since $I$ is constant, $\class{ntn-Ieps}{I}(\epsilon)=\pm m$ for every $\epsilon$. It remains to show $\class{ntn-Gld}{G}(z)\to\pm m$.</li>
<li><em>At a zero.</em> The Taylor coefficients of $f'$ at $a$ are those of $f$ shifted: the $k$-th one is $\frac{(f')^{(k)}(a)}{k!}=\frac{f^{(k+1)}(a)}{k!}=(k+1)\,a_{k+1}$ (@thm:cauchys-formula-for-derivatives). It is $0$ for $k\lt m-1$ and $m\,a_m$ for $k=m-1$. The Taylor remainder (@cor:taylor-remainder), for $f$ with $N=m+1$ and for $f'$ with $N=m$, gives, as $z\to a$,
\[ f(z)=(z-a)^m\big(a_m+O(|z-a|)\big),\qquad f'(z)=(z-a)^{m-1}\big(m\,a_m+O(|z-a|)\big). \]
So
\[ \class{ntn-Gld}{G}(z)=\frac{(z-a)\,(z-a)^{m-1}(m\,a_m+O(|z-a|))}{(z-a)^m(a_m+O(|z-a|))}=\frac{m\,a_m+O(|z-a|)}{a_m+O(|z-a|)}\longrightarrow m, \]
since $a_m\ne0$.</li>
<li><em>At a pole.</em> Near $a$, $g\ne0$ (it is continuous with $g(a)\ne0$). From $f=g\,(z-a)^{-m}$, the product rule gives $f'=g'(z-a)^{-m}-m\,g\,(z-a)^{-m-1}$, so
\[ \frac{f'}f=\frac{g'}g-\frac m{z-a},\qquad \class{ntn-Gld}{G}(z)=(z-a)\frac{g'(z)}{g(z)}-m\longrightarrow-m, \]
because $g'/g$ is continuous, hence bounded, near $a$. <span class="qed">∎</span></li>
</ol>
:::
