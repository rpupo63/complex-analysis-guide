---
id: E9
title: Random walks and harmonic measure
status:
- preview
---
<p>Start a random walk at an interior node $p$. At each step, move to one of the 8 neighbours with probability $\tfrac18$ each, and stop on reaching a boundary node. Let $h_q(p)$ be the probability that the walk stops at the boundary node $q$.</p>
<p>Conditioning on the first step gives $h_q(p)=\tfrac18\sum_{\text{nbrs}}h_q(\text{nbr})$, the equation of @cor:each-interior-value-is-the-average, with boundary data $e_q$. By uniqueness, $h_q(p)=\class{ntn-W}{W}_{pq}$, the weight of @prop:a-weighted-average-of-the-boundary. (This uses the fact that the walk reaches $B$ with probability 1, which is not proved here.) The continuum limit is Brownian motion, and the limiting weights form the <em>harmonic measure</em>. Lecture 3 announced this as the route to $u(x)\to g(p)$ at boundary points. Lecture 5 proves that fact a different way, with energy and a barrier (@thm:step-4-boundary-values), so the random walk is not needed.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Harmonic_measure" target="_blank" rel="noopener">Harmonic measure</a> · <a href="https://en.wikipedia.org/wiki/Random_walk" target="_blank" rel="noopener">Random walk</a></p>
