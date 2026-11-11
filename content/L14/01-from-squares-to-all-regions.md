---
id: p1
slide: Reconstructed
title: From squares to all simply connected regions
---

<p>Lecture 13 proved that a bounded connected open set satisfying (D) and (C) has a Riemann map (@thm:riemann-mapping-theorem). Interiors of finite unions of grid squares satisfy (D) (@thm:the-dirichlet-problem-on-a-union). The general statement, @thm:riemann-mapping-theorem-stated, was only stated.</p>
<p><b>The plan.</b> Fill a simply connected $\Omega\ne\mathbb C$ with grid regions $V_1\subseteq V_2\subseteq\dots$ (@sec:p5). Each $V_n$ has a Riemann map $f_n$ at $z_0$. Then:</p>
<ol>
<li>the $f_n$ have a convergent subsequence: Montel's theorem (@sec:p2);</li>
<li>the limit $f$ is injective, because each $f_n$ is: Hurwitz's theorem (@sec:p3);</li>
<li>$f$ is onto the disk: otherwise a square-root trick (Koebe) and the Schwarz lemma give a map with a larger derivative at $z_0$ than every $f_n$, which is impossible (@sec:p6).</li>
</ol>
<p>So the Riemann map of $\Omega$ is a limit of Riemann maps of grid regions, each of them built from a solution of the Dirichlet problem (Lecture 13).</p>
