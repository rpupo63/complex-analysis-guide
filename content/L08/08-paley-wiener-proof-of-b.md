---
id: h8
slide: Slide 9
title: 'Paley–Wiener: proof of (b)'
---
::: proof {title="Proof of Theorem [#](=thm:paley-wiener-a-simple-form)(b)."}
Put $f(x):=\int_{-\infty}^\infty F(\xi)e^{2\pi ix\xi}d\xi$. On $\R$, $|F(\xi)|\le\frac{C}{1+\xi^2}$, so the integral converges absolutely and $f$ is continuous ([A.22](apx:A22)).
<figure>{{fig:h8-1}}<figcaption>Proof of [Theorem #(b)](@thm:paley-wiener-a-simple-form): the line of integration is pushed up to $\operatorname{Im}\zeta=t$, and then $t\to\infty$.</figcaption></figure>
<ol>
<li><em>$f(x)=0$ for $x\gt A$.</em> Fix such $x$ and $t\gt0$, and apply Cauchy's theorem (@prop:other-contours) to the entire function $F(\zeta)e^{2\pi ix\zeta}$ on the rectangle with corners $\pm R$, $\pm R+it$. For $0\le\operatorname{Im}\zeta\le t$,
\[ |F(\zeta)e^{2\pi ix\zeta}|\le\frac{Ce^{2\pi A\operatorname{Im}\zeta}}{1+|\zeta|^2}\,e^{-2\pi x\operatorname{Im}\zeta}=\frac{Ce^{-2\pi(x-A)\operatorname{Im}\zeta}}{1+|\zeta|^2}\le\frac{C}{1+|\zeta|^2}, \]
which is at most $\frac C{1+R^2}$ on the vertical sides. So they vanish as $R\to\infty$, and
\[ |f(x)|=\Big|\int_{-\infty}^\infty F(\xi+it)\,e^{2\pi ix(\xi+it)}\,d\xi\Big|\le Ce^{-2\pi(x-A)t}\int_{-\infty}^\infty\frac{d\xi}{1+\xi^2}=\pi C\,e^{-2\pi(x-A)t}, \]
using $|\xi+it|^2\ge\xi^2$.</li>
<li><em>Let $t\to\infty$.</em> As $x-A\gt0$, the bound tends to $0$: $f(x)=0$. For $x\lt-A$, shift down ($t\lt0$) instead.</li>
<li><em>$F=\class{ntn-hat}{\hat f}$.</em> On $\R$, $F$ and $f$ are continuous and integrable ($f$ vanishes outside $[-A,A]$), so Fourier inversion (@fact:fourier-inversion, second form) gives $\class{ntn-hat}{\hat f}=F$ on $\R$. By part (a), $\class{ntn-hat}{\hat f}$ is entire, so $F-\class{ntn-hat}{\hat f}$ is entire and vanishes on $\R$. Its zeros are not isolated, so $F-\class{ntn-hat}{\hat f}\equiv0$ (@thm:isolated-zeros). <span class="qed">∎</span></li>
</ol>
:::
<p>The trick in step 1 is the same as in [Theorem #(a)](@thm:strips-and-decay), run in reverse: the more room there is to push the line, the more decay one gets; here there is unlimited room, so $f$ is not just small but zero.</p>
