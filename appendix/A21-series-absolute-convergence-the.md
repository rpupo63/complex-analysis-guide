---
id: A21
title: 'Series: absolute convergence, the M-test, double series'
status:
- cited
- derived
---
<div class="env"><span class="hd">Facts.</span>
<ol type="a">
<li><em>Absolute convergence.</em> If $\sum|a_n|\lt\infty$, then $\sum a_n$ converges, and any rearrangement or regrouping of its terms converges to the same sum (cited).</li>
<li><em>Weierstrass M-test.</em> If $|f_n|\le M_n$ on a set $S$ and $\sum M_n\lt\infty$, then $\sum f_n$ converges uniformly on $S$. Proof: the tails satisfy $|\sum_{n\gt N}f_n|\le\sum_{n\gt N}M_n\to0$, a bound independent of the point. In particular a uniformly convergent series of continuous functions on a curve may be integrated term by term: $|\int\sum_{n\gt N}f_n|\le\text{length}\cdot\sum_{n\gt N}M_n\to0$.</li>
<li><em>Double series.</em> If $\sum_{j,k}|a_{jk}|\lt\infty$ (summed in any order), then $\sum_j\sum_ka_{jk}=\sum_k\sum_ja_{jk}$, and the double series may be summed in any grouping (cited; Fubini's theorem for sums, compare [A.13](apx:A13)). In particular the product of two absolutely convergent series is $\big(\sum_ja_j\big)\big(\sum_kb_k\big)=\sum_{j,k}a_jb_k$.</li>
</ol></div>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Absolute_convergence" target="_blank" rel="noopener">Absolute convergence</a> · <a href="https://en.wikipedia.org/wiki/Weierstrass_M-test" target="_blank" rel="noopener">Weierstrass M-test</a> · <a href="https://en.wikipedia.org/wiki/Fubini%27s_theorem#For_infinite_sums" target="_blank" rel="noopener">Fubini for sums</a></p>
