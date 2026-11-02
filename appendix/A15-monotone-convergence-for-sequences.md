---
id: A15
title: Monotone convergence for sequences
status:
- derived
---
<div class="env"><span class="hd">Theorem.</span> A non-increasing sequence of reals that is bounded below converges to its infimum.</div>
::: proof
The set $\{m_n\}$ is nonempty and bounded below, so it has a greatest lower bound $m$. This is the completeness axiom of the real numbers (cited). Given $\delta\gt0$, $m+\delta$ is not a lower bound, so $m_N\lt m+\delta$ for some $N$. For $n\ge N$, $m\le m_n\le m_N\lt m+\delta$. So $|m_n-m|\lt\delta$ for all $n\ge N$.
:::
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Monotone_convergence_theorem" target="_blank" rel="noopener">Monotone convergence theorem</a> · <a href="https://en.wikipedia.org/wiki/Least-upper-bound_property" target="_blank" rel="noopener">Least-upper-bound property</a></p>
