---
id: m7
slide: Slide 8
title: '$1/\Gamma$ is entire: Gauss''s limit'
---
::: proof {title="Part 3: $\Gamma R=1$ on $\class{ntn-Wset}{W}$."}
$\Gamma R$ is holomorphic on the connected set $\class{ntn-Wset}{W}$, so by uniqueness (@prop:gluing-and-uniqueness(2)) it suffices to show $\Gamma(x)\class{ntn-Rg}{R}(x)=1$ for real $x\gt0$. Fix $x\gt0$ and let
\[ \class{ntn-gN}{g_N}:=\int_0^Nt^{x-1}\Big(1-\frac tN\Big)^Ndt. \]
<ol>
<li><em>$\class{ntn-gN}{g_N}\to\Gamma(x)$.</em> Write $\class{ntn-gN}{g_N}=\int_0^\infty\mathbf 1_{[0,N]}(t)\,t^{x-1}(1-\frac tN)^Ndt$. Since $\log(1-u)\le-u$, $0\le(1-\frac tN)^N=e^{N\log(1-t/N)}\le e^{-t}$ on $[0,N]$; so the integrand is dominated by $t^{x-1}e^{-t}$, which is integrable. For fixed $t$, $N\log(1-\frac tN)\to-t$, so the integrand tends to $t^{x-1}e^{-t}$. By [dominated convergence](apx:A22), $\class{ntn-gN}{g_N}\to\Gamma(x)$.</li>
<li><em>$\class{ntn-gN}{g_N}$ is explicit.</em> Substitute $t=Ns$: $\class{ntn-gN}{g_N}=N^x\int_0^1s^{x-1}(1-s)^Nds$. For $y\gt0$ and $k\ge1$, integration by parts (the boundary term $\big[\frac{s^y}y(1-s)^k\big]_0^1$ vanishes) gives
\[ \int_0^1s^{y-1}(1-s)^kds=\frac ky\int_0^1s^y(1-s)^{k-1}ds. \]
Applying this $N$ times, with $y=x,x+1,\dots,x+N-1$ and $k=N,N-1,\dots,1$:
\[ \class{ntn-gN}{g_N}=N^x\cdot\frac{N!}{x(x+1)\cdots(x+N-1)}\int_0^1s^{x+N-1}ds=\frac{N^x\,N!}{x(x+1)\cdots(x+N)}. \]</li>
<li><em>$1/\class{ntn-gN}{g_N}$ is a partial product of $R$.</em>
\[ N^{-x}=e^{-x\log N}=e^{x \class{ntn-aN}{a_N}}e^{-x\sum_{n\le N}1/n}=e^{x\class{ntn-aN}{a_N}}\prod_{n\le N}e^{-x/n}. \]
And
\[ \frac{x(x+1)\cdots(x+N)}{N!}=x\prod_{n\le N}\frac{n+x}n=x\prod_{n\le N}(1+\frac xn). \]
So
\[ \frac1{\class{ntn-gN}{g_N}}=x\,e^{x\class{ntn-aN}{a_N}}\prod_{n\le N}\Big(1+\frac xn\Big)e^{-x/n}\longrightarrow x\,e^{\class{ntn-gam}{\gamma} x}\prod_{n\ge1}\Big(1+\frac xn\Big)e^{-x/n}=\class{ntn-Rg}{R}(x). \]</li>
<li>Hence $\Gamma(x)\class{ntn-Rg}{R}(x)=\lim \class{ntn-gN}{g_N}\cdot\lim\frac1{\class{ntn-gN}{g_N}}=1$. <span class="qed">∎</span></li>
</ol>
Finally, $\Gamma R=1$ on $\class{ntn-Wset}{W}$ shows $\Gamma(z)\ne0$ there, and $1/\Gamma=R$ on $\class{ntn-Wset}{W}$; $R$ is the entire extension (with value $0$ at the poles of $\Gamma$).
:::
::: corollary {#cor:gausss-limit name="Gauss's limit"}
For $x\gt0$, $\displaystyle\Gamma(x)=\lim_{N\to\infty}\frac{N^x\,N!}{x(x+1)\cdots(x+N)}$.
:::
<p>This is step 2 combined with step 1. The same limit holds for complex $z\in \class{ntn-Wset}{W}$: the algebra of step 3 works verbatim for complex $z$ (with $N^{z}:=e^{z\log N}$), so the reciprocals of the right side are the partial products of $\class{ntn-Rg}{R}(z)$, which converge to $\class{ntn-Rg}{R}(z)=1/\Gamma(z)\ne0$.</p>
