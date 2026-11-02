---
id: A20
title: 'Asymptotic notation: $O$, $o$, $\sim$'
status:
- defined
---
<p>Let $F$ and $G\ge0$ be functions of a variable tending to a limit (such as $w\to z_0$, or $n\to\infty$).</p>
<ul>
<li>$F=O(G)$ ("big-$O$"): $|F|\le CG$ for some constant $C$, for all values close enough to the limit. An <em>absolute</em> constant is one that does not depend on any other parameter in sight. Inside a formula, $O(G)$ stands for some quantity of this size: $f(w)=a_m(w-z_0)^m+O(|w-z_0|^{m+1})$ means the difference is at most $C|w-z_0|^{m+1}$.</li>
<li>$F=o(G)$ ("little-$o$"): $F/G\to0$; for instance $o(1)$ is a quantity tending to $0$. ([A.1](apx:A1) uses $o(|h|)$ in the same sense.)</li>
<li>$F\sim G$ ("asymptotic to"): $F/G\to1$. Equivalently $F=G(1+o(1))$.</li>
</ul>
<p>Rules used freely: $O(G)+O(G)=O(G)$; $O(G_1)O(G_2)=O(G_1G_2)$; if $|w|\le C$ then $e^{O(|w|)}=1+O(|w|)$; and $\frac{a+O(\epsilon)}{b+O(\epsilon)}\to\frac ab$ when $b\ne0$ and $\epsilon\to0$.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Big_O_notation" target="_blank" rel="noopener">Big O notation</a> · <a href="https://en.wikipedia.org/wiki/Asymptotic_analysis" target="_blank" rel="noopener">Asymptotic analysis</a></p>
