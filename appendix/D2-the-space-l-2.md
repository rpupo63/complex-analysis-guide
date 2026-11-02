---
id: D2
title: The space $L^2(\Omega)$ and Cauchy sequences
status:
- defined
---
<p>$L^2(\Omega)$ is the space of functions $f$ on $\Omega$ with $\norm{f}_{L^2}^2=\iint_\Omega|f|^2\,dA\lt\infty$. Functions that differ only on a zero-area set are treated as the same element. Distance is $\class{ntn-L2}{\norm{f-h}_{L^2}}$, and $f_n\to f$ in $L^2$ means $\class{ntn-L2}{\norm{f_n-f}_{L^2}}\to0$. Vector-valued functions such as gradients are handled componentwise.</p>
<p>In words: $u\in L^2(\Omega)$ says only that $u$ is <em>square-integrable</em>, that $|u|^2$ has a finite integral over $\Omega$. It says nothing about continuity or derivatives; $u$ may jump, and its values on a set of zero area are irrelevant. This is why Weyl's lemma (@thm:weyls-lemma) is surprising: from this weak information it concludes that $u$ is smooth. For a set $K\subset\Omega$, $L^2(K)$ is the same with the integral taken over $K$ only, so "$f_n\to f$ in $L^2(K)$" means $\iint_K|f_n-f|^2\,dA\to0$.</p>
<p>A sequence $(f_n)$ is <em>Cauchy</em> if for every $\delta\gt0$ there is $N$ with $\norm{f_n-f_k}\lt\delta$ for all $n,k\ge N$: its terms eventually become arbitrarily close to each other. A convergent sequence is always Cauchy. The converse is the content of [D.3](apx:D3).</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Lp_space" target="_blank" rel="noopener">$L^p$ space</a> · <a href="https://en.wikipedia.org/wiki/Cauchy_sequence" target="_blank" rel="noopener">Cauchy sequence</a></p>
