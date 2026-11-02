---
label: ex:zeros-of-partial-sums-of-the
source: Homework 2, Problem 1(d)–(e)
title: zeros of partial sums of the exponential
placement: m10
order: 4
---
Let $s_N(z):=\sum_{n=0}^N\frac{z^n}{n!}$. (d) Show that for every $R\gt0$ there is $N_0$ such that $s_N$ has no zeros in $D(0,R)$ for $N\ge N_0$. (e) (Optional) Plot the zeros of $s_N(Nz)$ for $N=20,50,100$; they approach the Szegő curve $|z\,e^{1-z}|=1$, $|z|\le1$. Warning: the roots of $s_N$ are very sensitive to rounding. Double precision (e.g. <code>numpy.roots</code>) already gives spurious zeros for $N=50$; use about 30 significant digits for $N=100$ (e.g. <code>mpmath</code>). The convergence to the curve is slowest near $z=1$.
<details class="sol"><summary>Hint</summary>
(d) $s_N\to e^z$ uniformly on compact sets, and $e^z$ has no zeros. You don't need Rouché: compare $|s_N|$ with $|e^z|$ directly. (e) Use <code>mpmath.polyroots</code> with <code>mp.dps = 30</code>.
</details>
<details class="sol"><summary>Solution</summary>
(d) The power series of $e^z$ converges uniformly on $\overline{D(0,R)}$ ([A.19](apx:A19)), so $\max_{|z|\le R}|s_N-e^z|\to0$. Let $\mu:=\min_{|z|\le R}|e^z|=e^{-R}\gt0$, and take $N_0$ with $|s_N-e^z|\lt\mu$ on the disk for $N\ge N_0$. Then $|s_N(z)|\ge|e^z|-|s_N(z)-e^z|\gt0$ there. (This is Hurwitz's theorem, @ex:hurwitzs-theorem, in a quantitative form; the same comparison is the hypothesis of Rouché, @thm:rouche, with $e^z$ having no zeros.)<br>
(e) A script:
<pre>from mpmath import mp, polyroots, factorial, exp
mp.dps = 30
N = 50
coeffs = [N**n/factorial(n) for n in range(N, -1, -1)]   # s_N(Nz), highest power first
roots = polyroots(coeffs, maxsteps=200, extraprec=200)</pre>
Plot the roots with the curve $|z|e^{1-\operatorname{Re}z}=1$ in $|z|\le1$. Why that curve: by Stirling, $s_N(Nz)\approx e^{Nz}$ inside it and $\approx\frac{(Nz)^N}{N!}\approx\frac{(ze)^N}{\sqrt{2\pi N}}$ outside; zeros sit where the two sizes balance, $|e^{z}|=|ze|$, i.e. $|z\,e^{1-z}|=1$.
</details>
