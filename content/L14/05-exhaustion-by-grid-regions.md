---
id: p5
slide: Reconstructed
title: Exhaustion by grid regions
---

::: lemma {#lem:exhaustion-by-grid-regions name="exhaustion by grid regions"}
Let $\Omega$ be simply connected and $z_0\in\Omega$. There are open sets $V_1\subseteq V_2\subseteq\dots$ such that
<ol type="a">
<li>each $V_n$ is bounded, simply connected, and the interior of a finite union of closed grid squares;</li>
<li>$z_0\in V_n\subseteq\Omega$;</li>
<li>every compact subset of $\Omega$ lies in some $V_n$; in particular $\bigcup_nV_n=\Omega$.</li>
</ol>
:::
::: proof

<ol>
<li><em>Squares inside $\Omega$.</em> For $n\ge1$ let $S_n$ be the union of the closed squares of side $2^{-n}$ with corners in $2^{-n}\mathbb Z^2$ that lie in $\Omega\cap D(z_0,n)$; there are finitely many. Each such square is the union of four squares of the next size, which lie in $\Omega\cap D(z_0,n+1)$, so $S_n\subseteq S_{n+1}$. When $z_0$ is in the interior of $S_n$ (true for large $n$, by step 4 with $K=\{z_0\}$), let $U_n$ be the [component](apx:C4) of that interior containing $z_0$. Drop the first few $n$ and renumber.</li>
<li><em>Fill the holes.</em> $U_n$ is bounded, so $\mathbb C\setminus U_n$ has exactly one unbounded component $E_n$: it contains the connected set $\{|z|\gt R\}$ for $R$ large. Put $V_n:=\mathbb C\setminus E_n$, that is, $U_n$ together with the bounded components of $\mathbb C\setminus U_n$ (its "holes"). Components of a closed set are closed, so $V_n$ is open. $V_n$ is connected (each hole is attached to $U_n$ along its boundary), and $\mathbb C\setminus V_n=E_n$ is connected and unbounded: $V_n$ is simply connected (@def:simply-connected). Its boundary lies in $\partial U_n$, on grid lines, so each open grid square lies entirely in $V_n$ or entirely outside it, and the bounded set $V_n$ is the interior of the union of the finitely many closed squares inside it. An edge between a square of $U_n$ and a square of a hole belongs to the hole, so $V_n$ has no slits.</li>
<li><em>$V_n\subseteq\Omega$, and the $V_n$ increase.</em> Let $p\notin\Omega$. Its component $F$ in $\mathbb C\setminus\Omega$ is unbounded, because $\Omega$ is simply connected, and connected, and it misses $U_n\subseteq\Omega$. So $F\subseteq E_n$, and $p\notin V_n$. Next, $U_n\subseteq U_{n+1}$, so $E_{n+1}$ is a connected unbounded subset of $\mathbb C\setminus U_n$, hence $E_{n+1}\subseteq E_n$ and $V_n\subseteq V_{n+1}$.</li>
<li><em>Compact sets are eventually inside.</em> Let $K\subseteq\Omega$ be compact. Cover $K$ by finitely many closed disks in $\Omega$, and join each centre to $z_0$ by a path in $\Omega$ ([C.4](apx:C4)). The union $K'$ of these disks and paths is compact, connected, and contains $K$ and $z_0$. It has a positive distance $\delta$ from $\mathbb C\setminus\Omega$ ([C.5](apx:C5)). Take $n$ with $\sqrt2\,2^{-n}\lt\delta$ and $K'\subseteq D(z_0,n-1)$. Every closed grid square of side $2^{-n}$ that meets $K'$ has diameter less than $\delta$, so it lies in $\Omega\cap D(z_0,n)$, that is, in $S_n$. Each point of $K'$ is interior to the union of the (up to four) squares that contain it, all of which meet $K'$. So $K'$ lies in the interior of $S_n$, and, being connected and containing $z_0$, in $U_n\subseteq V_n$. <span class="qed">∎</span></li>
</ol>
:::
<p>Step 3 is where simple connectivity enters. Without it the filled region could swallow a hole of $\Omega$: for the annulus $\{1\lt|z|\lt2\}$, $U_n$ is a ring of squares and $V_n$ contains the unit disk.</p>
