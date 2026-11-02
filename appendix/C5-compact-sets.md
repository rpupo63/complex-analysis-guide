---
id: C5
title: Compact sets
status:
- defined
- cited
- derived
---
<p>A subset of $\R^2$ is <em>compact</em> if it is closed and bounded (for subsets of $\R^2$ this agrees with the general definition, by the Heine–Borel theorem, cited). Closed disks, $\overline\Omega$ for bounded $\Omega$, and $\class{ntn-dOm}{\partial\Omega}$ are compact. A <em>compact subset of $\Omega$</em> is a compact set contained in the open set $\Omega$; it stays a positive distance away from $\class{ntn-dOm}{\partial\Omega}$. On a compact set, a continuous function attains its maximum and minimum (extreme value theorem, cited).</p>
<div class="env"><span class="hd">Facts (proved).</span> Let $\Omega$ be open.
<ol type="a">
<li><em>Compact sets sit inside some $\class{ntn-Omd}{\Omega_\delta}$.</em> For compact $K\subset\Omega$ there is $\delta\gt0$ with $K\subset\class{ntn-Omd}{\Omega_\delta}$. Proof: $d(z):=$ distance from $z$ to the complement of $\Omega$ is continuous (it changes by at most $|z-z'|$ between $z$ and $z'$) and positive on $\Omega$ (which is open). On compact $K$ it attains a positive minimum $d_0$; any $\delta\lt d_0$ works.</li>
<li><em>$\class{ntn-Omd}{\Omega_\delta}$ is open.</em> If the closed $\delta$-disk about $z$ lies in $\Omega$, apply (a) to that disk: some slightly larger closed disk, of radius $\delta+\rho$, still lies in $\Omega$. Then every $w$ with $|w-z|\lt\rho$ has its closed $\delta$-disk inside it, so $w\in\class{ntn-Omd}{\Omega_\delta}$.</li>
<li><em>A nonempty bounded open set has a boundary point.</em> Take $P\in\Omega$ and move right: $T:=\sup\{t:P+(s,0)\in\Omega\text{ for all }0\le s\le t\}$ is finite because $\Omega$ is bounded. The point $P+(T,0)$ is a limit of points of $\Omega$, but is not in $\Omega$ (else, $\Omega$ being open, we could go further). So it lies on $\class{ntn-dOm}{\partial\Omega}$.</li>
<li>Every point of $\Omega$ lies in some $\class{ntn-Omd}{\Omega_\delta}$ (since $\Omega$ is open), so $\Omega=\bigcup_{\delta\gt0}\class{ntn-Omd}{\Omega_\delta}$.</li>
<li><em>Bolzano–Weierstrass (cited).</em> Every sequence in a compact set has a subsequence converging to a point of the set. Lectures 7, 9 and 10 use it to show that a holomorphic $f\not\equiv0$ has only finitely many zeros in a compact set: infinitely many would accumulate, contradicting @thm:isolated-zeros.</li>
</ol></div>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Compact_space" target="_blank" rel="noopener">Compact space</a> · <a href="https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem" target="_blank" rel="noopener">Heine–Borel theorem</a> · <a href="https://en.wikipedia.org/wiki/Extreme_value_theorem" target="_blank" rel="noopener">Extreme value theorem</a> · <a href="https://en.wikipedia.org/wiki/Bolzano%E2%80%93Weierstrass_theorem" target="_blank" rel="noopener">Bolzano–Weierstrass theorem</a></p>
