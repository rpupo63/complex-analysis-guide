---
id: E16
title: A proof of Poisson summation by residues
status:
- derived
---
<p>The slides refer @thm:poisson-summation to a homework problem. Here is a complete proof with the tools of Lectures 6 and 8. Let $F$ be holomorphic on $|\operatorname{Im}z|\lt a$ with $|F(x+iy)|\le\frac C{1+x^2}$ there, and fix $0\lt b\lt a$.</p>
::: proof

<ol>
<li><em>A kernel with residue $\frac1{2\pi i}$ at each integer.</em> Let $k(z):=\frac1{e^{2\pi iz}-1}$. Its poles are the zeros of $e^{2\pi iz}-1$, the integers, all simple, and $\class{ntn-res}{\operatorname{Res}}_nk=\frac1{2\pi ie^{2\pi in}}=\frac1{2\pi i}$ by @prop:simple-poles-of-a-quotient with $A=1$, $B=e^{2\pi iz}-1$. ($B$ is not a polynomial, but the proof still works: by @thm:power-series, $B(n)=0$ gives $B=(z-n)B_1$ with $B_1$ holomorphic.)</li>
<li><em>Rectangle.</em> Let $Q_N$ be the rectangle with vertical sides $\operatorname{Re}z=\pm(N+\frac12)$ and horizontal sides $\operatorname{Im}z=\pm b$, anticlockwise. It encloses the integers $|n|\le N$, so by @prop:other-contours
\[ \oint_{Q_N}F(z)k(z)\,dz=2\pi i\sum_{|n|\le N}\frac{F(n)}{2\pi i}=\sum_{|n|\le N}F(n). \]</li>
<li><em>Vertical sides.</em> On $\operatorname{Re}z=\pm(N+\frac12)$, $e^{2\pi iz}=-e^{-2\pi y}$ is negative, so $|e^{2\pi iz}-1|=1+e^{-2\pi y}\ge1$ and $|k|\le1$. With $|F|\le\frac C{1+N^2}$ and height $2b$, these sides are $O(N^{-2})$.</li>
<li><em>Bottom side</em> ($\operatorname{Im}z=-b$, left to right). There $|e^{2\pi iz}|=e^{2\pi b}\gt1$, so $k(z)=\frac{e^{-2\pi iz}}{1-e^{-2\pi iz}}=\sum_{m\ge1}e^{-2\pi imz}$, uniformly convergent on the line (ratio $e^{-2\pi b}$). Integrating term by term over the whole line (the bound $\frac{C}{1+x^2}\sum_me^{-2\pi bm}$ is integrable),
\[ \int_{\operatorname{Im}z=-b}F(z)k(z)\,dz=\sum_{m\ge1}\int_{-\infty}^\infty F(x-ib)e^{-2\pi im(x-ib)}dx=\sum_{m\ge1}\class{ntn-hat}{\hat F}(m), \]
the last step being the line shift of [Theorem #(a)](@thm:strips-and-decay), step 1.</li>
<li><em>Top side</em> ($\operatorname{Im}z=b$, traversed right to left). There $|e^{2\pi iz}|=e^{-2\pi b}\lt1$, so $k(z)=-\frac1{1-e^{2\pi iz}}=-\sum_{m\ge0}e^{2\pi imz}$. The minus sign cancels against the reversed direction, so this side contributes
\[ \sum_{m\ge0}\int_{-\infty}^\infty F(x+ib)\,e^{2\pi im(x+ib)}\,dx=\sum_{m\ge0}\class{ntn-hat}{\hat F}(-m), \]
shifting the line back to $\R$ as before ($|e^{2\pi imz}|\le1$ for $\operatorname{Im}z\ge0$).</li>
<li><em>Let $N\to\infty$.</em> The truncated horizontal integrals converge to the full ones (the integrands are dominated by integrable functions), and the vertical sides vanish. So
\[ \sum_nF(n)=\sum_{m\ge1}\class{ntn-hat}{\hat F}(m)+\sum_{m\ge0}\class{ntn-hat}{\hat F}(-m)=\sum_{m\in\mathbb Z}\class{ntn-hat}{\hat F}(m). \]
<span class="qed">∎</span></li>
</ol>
:::
<p>The usual real-variable proof expands the periodic function $\sum_nF(x+n)$ in a Fourier series and evaluates at $x=0$.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Poisson_summation_formula" target="_blank" rel="noopener">Poisson summation formula</a></p>
