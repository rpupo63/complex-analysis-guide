---
id: h7
slide: Slide 8
title: The Paley–Wiener theorem
---
<p>The second half of the pattern of @sec:h4: vanishing outside an interval corresponds to $\class{ntn-hat}{\hat f}$ being entire with controlled growth.</p>

::: theorem {#thm:paley-wiener-a-simple-form name="Paley–Wiener, a simple form"}
Let $A\gt0$.<br>
(a) If $f$ is continuous and vanishes outside $[-A,A]$, then $\class{ntn-hat}{\hat f}(\zeta):=\int_{-A}^Af(x)e^{-2\pi ix\zeta}dx$ is an entire function of $\zeta$. If moreover $f$ is $C^2$ (on all of $\R$), then
\[ (1+|\zeta|^2)\,|\class{ntn-hat}{\hat f}(\zeta)|\le C\,e^{2\pi A|\operatorname{Im}\zeta|}\qquad\text{on }\mathbb C. \]
(b) Conversely, if $F$ is entire and $(1+|\zeta|^2)|F(\zeta)|\le C\,e^{2\pi A|\operatorname{Im}\zeta|}$ on $\mathbb C$, then $F=\class{ntn-hat}{\hat f}$ for a continuous $f$ vanishing outside $[-A,A]$.
:::
<p>Notation: $\class{ntn-n1}{\norm{f}_1}:=\int|f(x)|\,dx$. The constant in (a) can be taken as $C=\class{ntn-n1}{\norm{f}_1}+\class{ntn-n1}{\norm{f''}_1}$.</p>
::: proof {title="Proof of (a)."}

<ol>
<li><em>Entire.</em> The integral runs over the bounded interval $[-A,A]$, and $\zeta\mapsto f(x)e^{-2\pi ix\zeta}$ is entire with $\zeta$-derivative $-2\pi ix\,f(x)e^{-2\pi ix\zeta}$, continuous in $(x,\zeta)$. Differentiating under the integral sign ([A.4](apx:A4)) shows $\class{ntn-hat}{\hat f}$ has continuous partial derivatives satisfying Cauchy–Riemann, so it is entire.</li>
<li><em>Growth.</em> For $|x|\le A$, $|e^{-2\pi ix\zeta}|=e^{2\pi x\operatorname{Im}\zeta}\le e^{2\pi A|\operatorname{Im}\zeta|}$. So $|\class{ntn-hat}{\hat f}(\zeta)|\le\class{ntn-n1}{\norm{f}_1}e^{2\pi A|\operatorname{Im}\zeta|}$.</li>
<li><em>Decay from smoothness.</em> If $f$ is $C^2$, then $f$ and $f'$ are continuous and vanish outside $[-A,A]$, hence vanish at $\pm A$. Integrating by parts twice, the boundary terms vanish:
\[ \int_{-A}^Af''(x)e^{-2\pi ix\zeta}dx=2\pi i\zeta\int_{-A}^Af'(x)e^{-2\pi ix\zeta}dx=(2\pi i\zeta)^2\class{ntn-hat}{\hat f}(\zeta). \]
As in step 2, the left side is at most $\class{ntn-n1}{\norm{f''}_1}e^{2\pi A|\operatorname{Im}\zeta|}$, so $4\pi^2|\zeta|^2|\class{ntn-hat}{\hat f}(\zeta)|\le\class{ntn-n1}{\norm{f''}_1}e^{2\pi A|\operatorname{Im}\zeta|}$.</li>
<li><em>Add</em> steps 2 and 3: $(1+4\pi^2|\zeta|^2)|\class{ntn-hat}{\hat f}|\le(\class{ntn-n1}{\norm{f}_1}+\class{ntn-n1}{\norm{f''}_1})e^{2\pi A|\operatorname{Im}\zeta|}$, and $1+|\zeta|^2\le1+4\pi^2|\zeta|^2$. <span class="qed">∎</span></li>
</ol>
:::
