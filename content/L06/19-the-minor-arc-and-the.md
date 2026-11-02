---
id: f19
slide: Slide 20
title: The minor arc, and the conclusion
---

::: proposition {#prop:the-minor-arc name="the minor arc"}

\[ \Big|\frac1{2\pi}\int_{\class{ntn-tpar}{t}\lt|\theta|\le\pi}\class{ntn-Pz}{P}(e^{-\class{ntn-tau}{\tau}})\,e^{n\class{ntn-tau}{\tau}}\,d\theta\Big|\le e^{2\class{ntn-mu}{\mu}}\,e^{-\class{ntn-cLB}{c}/\class{ntn-tpar}{t}}, \]
with $\class{ntn-cLB}{c}$ from @lem:lemma-b.
:::
::: proof
On the minor arc $|e^{n\class{ntn-tau}{\tau}}|=e^{nt}$, and by @lem:lemma-b (with $r=e^{-\class{ntn-tpar}{t}}$, valid as $\class{ntn-tpar}{t}\le1$) and @lem:on-the-real-axis, $|\class{ntn-Pz}{P}(e^{-\class{ntn-tau}{\tau}})|\le \class{ntn-Pz}{P}(e^{-\class{ntn-tpar}{t}})e^{-\class{ntn-cLB}{c}/\class{ntn-tpar}{t}}\le e^{\pi^2/(6\class{ntn-tpar}{t})}e^{-\class{ntn-cLB}{c}/\class{ntn-tpar}{t}}$. The arc has total length less than $2\pi$, so the integral divided by $2\pi$ is at most the maximum of the integrand, $e^{\pi^2/(6\class{ntn-tpar}{t})+nt}e^{-\class{ntn-cLB}{c}/\class{ntn-tpar}{t}}=e^{2\class{ntn-mu}{\mu}}e^{-\class{ntn-cLB}{c}/\class{ntn-tpar}{t}}$.
:::

::: proof {title="Proof of Theorem [#](=thm:hardy-and-ramanujan-1918)."}

<ol>
<li><em>Compare the arcs.</em> By @prop:the-major-arc the major arc is $\frac {\class{ntn-tpar}{t}}{2\pi}\sqrt{\frac {\class{ntn-tpar}{t}}{2\pi}}\sqrt{\frac\pi{\class{ntn-mu}{\mu}}}\,e^{2\class{ntn-mu}{\mu}}(1+o(1))$. Since $\class{ntn-mu}{\mu}=\pi^2/(6\class{ntn-tpar}{t})$, $\class{ntn-mu}{\mu}^{-1/2}$ is a constant times $\class{ntn-tpar}{t}^{1/2}$, so the major arc is of order $e^{2\class{ntn-mu}{\mu}}\class{ntn-tpar}{t}^{3/2}\cdot \class{ntn-tpar}{t}^{1/2}=e^{2\class{ntn-mu}{\mu}}\class{ntn-tpar}{t}^2$. The minor arc is at most $e^{2\class{ntn-mu}{\mu}}e^{-\class{ntn-cLB}{c}/\class{ntn-tpar}{t}}$, and $e^{-\class{ntn-cLB}{c}/\class{ntn-tpar}{t}}/\class{ntn-tpar}{t}^2\to0$ as $\class{ntn-tpar}{t}\to0$ (exponentials beat powers). So the minor arc is $o(\text{major arc})$.</li>
<li><em>Add.</em> By @prop:p-n-as-an-integral, $\class{ntn-pn}{p}(n)$ is the sum of the two arcs, so
\[ \class{ntn-pn}{p}(n)\sim\frac {\class{ntn-tpar}{t}}{2\pi}\sqrt{\frac {\class{ntn-tpar}{t}}{2\pi}}\sqrt{\frac\pi{\class{ntn-mu}{\mu}}}\,e^{2\class{ntn-mu}{\mu}}. \]</li>
<li><em>Simplify.</em> First $\class{ntn-mu}{\mu}=nt$: $\sqrt{\pi/\class{ntn-mu}{\mu}}=\sqrt\pi/(\sqrt n\sqrt {\class{ntn-tpar}{t}})$, so
\[ \frac {\class{ntn-tpar}{t}}{2\pi}\sqrt{\frac {\class{ntn-tpar}{t}}{2\pi}}\sqrt{\frac\pi{nt}}=\frac{\class{ntn-tpar}{t}\sqrt\pi}{(2\pi)^{3/2}\sqrt n}=\frac{\class{ntn-tpar}{t}}{2\sqrt2\,\pi\sqrt n}. \]
Then $\class{ntn-tpar}{t}=\pi/\sqrt{6n}$: this is $\frac{1}{2\sqrt2\sqrt6\,n}=\frac1{2\sqrt{12}\,n}=\frac1{4\sqrt3\,n}$. With $2\class{ntn-mu}{\mu}=\pi\sqrt{2n/3}$, the theorem follows. <span class="qed">∎</span></li>
</ol>
:::

::: remark {#rem:the-shape-of-the-argument name="the shape of the argument"}
Every step used Part II's basic tools: a coefficient is a contour integral (@thm:power-series); the circle is chosen to balance growth against decay (as in @cor:cauchys-estimate); the integral is dominated by the neighbourhood of the dominant singularity $z=1$; and the rest is shown to be negligible. Rademacher later turned this into an exact convergent series for $\class{ntn-pn}{p}(n)$, using all the roots of unity, not just $z=1$.
:::
