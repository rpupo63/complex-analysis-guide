---
id: E19
title: The circle method, and where Lemma A comes from
status:
- context
---
<p>@sec:f14–@sec:f19 is the simplest instance of the <em>circle method</em> of Hardy and Ramanujan (1918), later developed by Hardy–Littlewood for Waring's problem and by Vinogradov. Its ingredients: a generating function, Cauchy's coefficient formula on a circle close to the radius of convergence, a <em>major arc</em> near the dominant singularity where the function has an explicit approximation, and <em>minor arcs</em> where it is shown to be small.</p>
<p><b>@lem:lemma-a, outline.</b> Write $\log P(e^{-\tau})=\sum_{k\ge1}\phi(k\tau)$ with $\phi(u):=-\log(1-e^{-u})$. For small $\tau$ the sum is a Riemann sum with step $\tau$:
\[ \sum_{k\ge1}\phi(k\tau)\approx\frac1\tau\int_0^\infty\phi(u)\,du+\text{correction}=\frac{\pi^2}{6\tau}+\dots, \]
since
\[ \int_0^\infty-\log(1-e^{-u})\,du=\sum_m\frac1m\int_0^\infty e^{-mu}du=\sum\frac1{m^2}=\frac{\pi^2}6. \]
The correction comes from the singularity of $\phi(u)\approx-\log u$ at $u=0$; the Euler–Maclaurin formula, together with Stirling's formula ([A.23](apx:A23)) for $\sum\log k$, produces the term $\frac12\log\frac\tau{2\pi}$. A cleaner route is the modular transformation of Dedekind's eta function, which gives the formula with an exponentially small error.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Partition_function_(number_theory)" target="_blank" rel="noopener">Partition function</a> · <a href="https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_circle_method" target="_blank" rel="noopener">Circle method</a> · <a href="https://en.wikipedia.org/wiki/Euler%E2%80%93Maclaurin_formula" target="_blank" rel="noopener">Euler–Maclaurin formula</a> · <a href="https://en.wikipedia.org/wiki/Dedekind_eta_function" target="_blank" rel="noopener">Dedekind eta function</a></p>
