---
id: f18
slide: Slide 19
title: The major arc
---

::: proposition {#prop:the-major-arc name="the major arc"}
As $n\to\infty$,
\[ \frac1{2\pi}\int_{|\theta|\le \class{ntn-tpar}{t}}\class{ntn-Pz}{P}(e^{-\class{ntn-tau}{\tau}})\,e^{n\class{ntn-tau}{\tau}}\,d\theta=\frac {\class{ntn-tpar}{t}}{2\pi}\sqrt{\frac {\class{ntn-tpar}{t}}{2\pi}}\,e^{2\class{ntn-mu}{\mu}}\,\class{ntn-Imaj}{I},\qquad \class{ntn-Imaj}{I}=\sqrt{\frac\pi{\class{ntn-mu}{\mu}}}\,\big(1+o(1)\big). \]
:::
::: proof

<ol>
<li><em>Insert Lemma A.</em> By @cor:lemma-a-exponentiated and @lem:the-exponent-on-the-major-arc, on the major arc
\[ \class{ntn-Pz}{P}(e^{-\class{ntn-tau}{\tau}})\,e^{n\class{ntn-tau}{\tau}}=\sqrt{\frac{\class{ntn-tau}{\tau}}{2\pi}}\,e^{\pi^2/(6\class{ntn-tau}{\tau})+n\class{ntn-tau}{\tau}}\big(1+O(\class{ntn-tpar}{t})\big)=\sqrt{\frac{\class{ntn-tau}{\tau}}{2\pi}}\,e^{2\class{ntn-mu}{\mu}-\class{ntn-mu}{\mu}\frac{s^2+is^3}{1+s^2}}\big(1+O(\class{ntn-tpar}{t})\big), \]
where $O(|\class{ntn-tau}{\tau}|)=O(\class{ntn-tpar}{t})$ because $|\class{ntn-tau}{\tau}|\le\sqrt2\,\class{ntn-tpar}{t}$. Here $(1+O(\class{ntn-tpar}{t}))$ stands for a function of $s$ (and $n$) that differs from $1$ by at most $Ct$.</li>
<li><em>Change variables.</em> With $\theta=ts$, $d\theta=\class{ntn-tpar}{t}\,ds$, and $\sqrt{\class{ntn-tau}{\tau}}=\sqrt {\class{ntn-tpar}{t}}\,\sqrt{1-is}$ (both roots principal; $\class{ntn-tpar}{t}\gt0$ and $1-is$ lies in the right half-plane),
\[ \frac1{2\pi}\int_{|\theta|\le \class{ntn-tpar}{t}}\class{ntn-Pz}{P}(e^{-\class{ntn-tau}{\tau}})e^{n\class{ntn-tau}{\tau}}d\theta=\frac {\class{ntn-tpar}{t}}{2\pi}\sqrt{\frac {\class{ntn-tpar}{t}}{2\pi}}\,e^{2\class{ntn-mu}{\mu}}\class{ntn-Imaj}{I},\qquad \class{ntn-Imaj}{I}:=\int_{-1}^1\sqrt{1-is}\;e^{-\class{ntn-mu}{\mu}\frac{s^2+is^3}{1+s^2}}\big(1+O(\class{ntn-tpar}{t})\big)\,ds. \]</li>
<li><em>Rescale.</em> Put $s=u/\sqrt{\class{ntn-mu}{\mu}}$, so $ds=du/\sqrt{\class{ntn-mu}{\mu}}$, $\class{ntn-mu}{\mu} s^2=u^2$, $\class{ntn-mu}{\mu} s^3=u^3/\sqrt{\class{ntn-mu}{\mu}}$, $1+s^2=1+u^2/\class{ntn-mu}{\mu}$:
\[ \class{ntn-Imaj}{I}=\frac1{\sqrt{\class{ntn-mu}{\mu}}}\int_{-\sqrt{\class{ntn-mu}{\mu}}}^{\sqrt{\class{ntn-mu}{\mu}}}\sqrt{1-\frac{iu}{\sqrt{\class{ntn-mu}{\mu}}}}\;\exp\Big(-\frac{u^2+iu^3/\sqrt{\class{ntn-mu}{\mu}}}{1+u^2/\class{ntn-mu}{\mu}}\Big)\big(1+O(\class{ntn-tpar}{t})\big)\,du. \]</li>
<li><em>Dominate.</em> Extend the integrand by $0$ for $|u|\gt\sqrt{\class{ntn-mu}{\mu}}$. For $|s|\le1$: $|\sqrt{1-is}|=(1+s^2)^{1/4}\le2^{1/4}$; and $\operatorname{Re}\frac{s^2+is^3}{1+s^2}=\frac{s^2}{1+s^2}\ge\frac{s^2}2$, so the exponential has modulus at most $e^{-\class{ntn-mu}{\mu} s^2/2}=e^{-u^2/2}$. For large $n$ (small $\class{ntn-tpar}{t}$), $2^{1/4}|1+O(\class{ntn-tpar}{t})|\le2$. So the integrand is at most $2e^{-u^2/2}$, which is integrable over $\R$.</li>
<li><em>Pass to the limit.</em> As $n\to\infty$, $\class{ntn-mu}{\mu}\to\infty$ and $\class{ntn-tpar}{t}\to0$, so for each fixed $u$ the integrand tends to $1\cdot e^{-u^2}\cdot1$. By the [dominated convergence theorem](apx:A22),
\[ \int_{-\sqrt{\class{ntn-mu}{\mu}}}^{\sqrt{\class{ntn-mu}{\mu}}}(\cdots)\,du\longrightarrow\int_{-\infty}^\infty e^{-u^2}du=\sqrt\pi, \]
the Gaussian integral (proved in @sec:m9). So $\class{ntn-Imaj}{I}=\frac1{\sqrt{\class{ntn-mu}{\mu}}}(\sqrt\pi+o(1))=\sqrt{\pi/\class{ntn-mu}{\mu}}\,(1+o(1))$. <span class="qed">∎</span></li>
</ol>
:::
<p>The picture: on the scale $s\sim1/\sqrt{\class{ntn-mu}{\mu}}$ the integrand is a Gaussian, and the cubic term $is^3$ and the factor $\sqrt{1-is}$ become invisible. This is the <em>saddle point</em> idea: near its peak, an exponential integrand is approximately Gaussian.</p>
