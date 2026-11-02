---
id: m3
slide: Slide 4
title: Euler's integral
---

::: proposition {#prop:the-gamma-function name="the Gamma function"}
For $\operatorname{Re}z\gt0$, the integral
\[ \Gamma(z):=\int_0^\infty t^{z-1}e^{-t}\,dt\qquad\big(t^{z-1}:=e^{(z-1)\log t}\big) \]
converges absolutely, $\Gamma$ is holomorphic, and $\Gamma(z+1)=z\Gamma(z)$. So $\Gamma(n+1)=n!$ for integers $n\ge0$.
:::
::: proof
Let $0\lt a\le\operatorname{Re}z\le b$.
<ol>
<li><em>Domination.</em> $|t^{z-1}|=|e^{(z-1)\log t}|=e^{(\operatorname{Re}z-1)\log t}=t^{\operatorname{Re}z-1}$. On $(0,1]$, $\log t\le0$, so this is at most $t^{a-1}$; on $[1,\infty)$ it is at most $t^{b-1}$. Since $\int_0^1t^{a-1}dt=\frac1a$ and $\int_1^\infty t^{b-1}e^{-t}dt\lt\infty$, the integral converges absolutely.</li>
<li><em>Truncations are entire.</em> $I_N(z):=\int_{1/N}^Nt^{z-1}e^{-t}dt$ is entire: the interval is compact and $\partial_zt^{z-1}=(\log t)\,t^{z-1}$ is continuous, so differentiation under the integral sign ([A.4](apx:A4)) applies.</li>
<li><em>Uniform convergence on strips.</em>
\[ |\Gamma(z)-I_N(z)|\le\int_0^{1/N}t^{a-1}dt+\int_N^\infty t^{b-1}e^{-t}dt=\frac{N^{-a}}a+\int_N^\infty t^{b-1}e^{-t}dt\longrightarrow0, \]
uniformly in the strip $a\le\operatorname{Re}z\le b$.</li>
<li><em>Holomorphic.</em> Each closed disk in $\{\operatorname{Re}z\gt0\}$ lies in such a strip, so $\Gamma$ is holomorphic by @thm:uniform-limits.</li>
<li><em>Functional equation.</em> Integrating by parts on $[\epsilon,N]$, with $\frac{d}{dt}t^z=zt^{z-1}$,
\[ \int_\epsilon^Nt^ze^{-t}dt=\big[-t^ze^{-t}\big]_\epsilon^N+z\int_\epsilon^Nt^{z-1}e^{-t}dt. \]
As $\epsilon\to0^+$ and $N\to\infty$, the boundary terms vanish ($|t^z|=t^{\operatorname{Re}z}\to0$ at $0$, and $t^{\operatorname{Re}z}e^{-t}\to0$ at $\infty$), giving $\Gamma(z+1)=z\Gamma(z)$.</li>
<li><em>Factorials.</em> $\Gamma(1)=\int_0^\infty e^{-t}dt=1$, and by induction $\Gamma(n+1)=n\Gamma(n)=n!$. <span class="qed">∎</span></li>
</ol>
:::
<p>So $\Gamma$ interpolates the factorials: $\Gamma(n+1)=n!$. The integral diverges at $t=0$ when $\operatorname{Re}z\le0$; the next section continues $\Gamma$ there using the functional equation instead.</p>
