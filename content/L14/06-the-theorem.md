---
id: p6
slide: Reconstructed
title: The theorem
---

::: theorem {#thm:riemann-mapping-theorem-general name="Riemann mapping theorem, general form"}
Let $\Omega\ne\mathbb C$ be a nonempty simply connected open set, and $z_0\in\Omega$. There is exactly one conformal map $f$ of $\Omega$ onto $D(0,1)$ with $f(z_0)=0$ and $f'(z_0)\gt0$.
:::
<p>Uniqueness is @prop:uniqueness. This is @thm:riemann-mapping-theorem-stated, now proved, apart from @fact:simply-connected-sets-satisfy-c.</p>
::: proof {title="Proof of existence."}

<ol>
<li><em>Riemann maps of grid regions.</em> Let $V_n$ be as in @lem:exhaustion-by-grid-regions. Each $V_n$ is bounded and connected, satisfies (D) by @thm:the-dirichlet-problem-on-a-union and (C) by @fact:simply-connected-sets-satisfy-c. By @thm:riemann-mapping-theorem it has a conformal map $f_n$ onto $D(0,1)$ with $f_n(z_0)=0$ and $f_n'(z_0)\gt0$.</li>
<li><em>The derivatives decrease.</em> $f_n^{-1}$ maps $D(0,1)$ onto $V_n\subseteq V_{n+1}$ (@thm:inverse), so $f_{n+1}\circ f_n^{-1}$ maps $D(0,1)$ into itself and $0$ to $0$. By the Schwarz lemma (@thm:schwarz-lemma), its derivative at $0$, which is $f_{n+1}'(z_0)/f_n'(z_0)$, is at most $1$.</li>
<li><em>…but stay away from $0$.</em> Let $\Phi$ be as in @lem:a-map-into-the-disk and $p:=\Phi(z_0)$. Then $\psi:=\varphi_p\circ\Phi\circ f_n^{-1}$ maps $D(0,1)$ into itself with $\psi(0)=\varphi_p(p)=0$ (@lem:is-an-automorphism-of-with). Since $\varphi_p'(z)=\frac{|p|^2-1}{(1-\bar pz)^2}$, $\varphi_p'(p)=-\frac1{1-|p|^2}$, and the Schwarz lemma gives
\[ |\psi'(0)|=\frac{|\Phi'(z_0)|}{(1-|p|^2)\,f_n'(z_0)}\le1,\qquad\text{so}\qquad f_n'(z_0)\ge\frac{|\Phi'(z_0)|}{1-|p|^2}\gt0. \]
So $f_n'(z_0)$ decreases to a limit $L\gt0$.</li>
<li><em>A limit map.</em> $|f_n|\lt1$, so by Montel (@thm:montel) a subsequence converges uniformly on compact subsets of $\Omega$ to a holomorphic $f$, with $f(z_0)=0$ and $f'(z_0)=L\gt0$. So $f$ is not constant, and by Hurwitz (@thm:hurwitz) it is injective. $|f|\le1$, and $f(\Omega)$ is open (@thm:open-mapping), so $f(\Omega)\subseteq D(0,1)$. It remains to show that $f$ is onto.</li>
<li><em>Onto: the square-root trick.</em> Suppose $w\in D(0,1)$ is not a value of $f$. Then $h:=\varphi_w\circ f$ is injective, maps $\Omega$ into $D(0,1)$, and has no zero. By @cor:logarithms-and-square-roots, $h=k^2$ with $k$ holomorphic; $k$ is injective (as $h$ is) and $|k|\lt1$. Let $s:=k(z_0)$, so $s^2=h(z_0)=\varphi_w(0)=w$, and put $F:=\varphi_s\circ k$: injective, into $D(0,1)$, with $F(z_0)=0$. Since $\varphi_w$ and $\varphi_s$ are their own inverses,
\[ f=\varphi_w(k^2)=\varphi_w\big(\varphi_s(F)^2\big)=Q\circ F,\qquad Q(\zeta):=\varphi_w\big(\varphi_s(\zeta)^2\big). \]
$Q$ maps $D(0,1)$ into itself with $Q(0)=\varphi_w(s^2)=0$, and it is not injective: for $0\lt|t|\lt1$ the distinct points $\varphi_s(t)$, $\varphi_s(-t)$ have the same image. So $Q$ is not a rotation, and the Schwarz lemma gives $|Q'(0)|\lt1$. By the chain rule $L=f'(z_0)=Q'(0)F'(z_0)$, so
\[ |F'(z_0)|=\frac L{|Q'(0)|}\gt L. \]
But $F\circ f_n^{-1}$ maps $D(0,1)$ into itself and $0$ to $0$, so by the Schwarz lemma $|F'(z_0)|\le f_n'(z_0)$ for every $n$, and in the limit $|F'(z_0)|\le L$. This contradiction shows $f(\Omega)=D(0,1)$. <span class="qed">∎</span></li>
</ol>
:::

::: remark {#rem:the-whole-sequence-converges name="the whole sequence converges"}
Not just a subsequence: $f_n\to f$ uniformly on compact subsets of $\Omega$. Otherwise some compact $K$, some $\varepsilon\gt0$ and a subsequence would have $\max_K|f_n-f|\ge\varepsilon$. Applying steps 4 and 5 to that subsequence gives a further subsequence converging to a conformal map of $\Omega$ onto the disk with the same normalization, which is $f$ by @prop:uniqueness: a contradiction. So the Riemann map is the limit of the Riemann maps of the grid regions, as Lecture 15's first slide says: the proof constructs the map.
:::
