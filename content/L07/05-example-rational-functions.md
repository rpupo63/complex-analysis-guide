---
id: g5
slide: Slide 6
title: 'Example: rational functions'
---

::: example {#eg:rational-functions name="rational functions" status=derived}
Let $f(z)=\lambda\prod_j(z-a_j)^{m_j}\big/\prod_k(z-b_k)^{n_k}$, with $\lambda\ne0$, the $a_j,b_k$ distinct, and none of them on $|z|=R$. Then
\[ \frac1{2\pi i}\oint_{|z|=R}\frac{f'(z)}{f(z)}\,dz=\sum_{|a_j|\lt R}m_j-\sum_{|b_k|\lt R}n_k, \]
and this is $\class{ntn-ZP}{Z}-\class{ntn-ZP}{P}$, as @thm:argument-principle predicts.
:::
::: proof

<ol>
<li><em>Logarithmic derivative of a product.</em> By the product rule, $(gh)'/(gh)=g'/g+h'/h$, and similarly for quotients with a minus sign; also $\frac{((z-a)^m)'}{(z-a)^m}=\frac m{z-a}$. So
\[ \frac{f'(z)}{f(z)}=\sum_j\frac{m_j}{z-a_j}-\sum_k\frac{n_k}{z-b_k}. \]</li>
<li><em>Integrate each term.</em> For $|a|\ne R$:
\[ \frac1{2\pi i}\oint_{|z|=R}\frac{dz}{z-a}=\begin{cases}1,&|a|\lt R,\\0,&|a|\gt R.\end{cases} \]
The first case is @thm:cauchys-integral-formula with $f\equiv1$ and $w=a$; the second is @thm:cauchys-theorem, since $\tfrac1{z-a}$ is holomorphic near $|z|\le R$.</li>
<li><em>Identify $\class{ntn-ZP}{Z}-\class{ntn-ZP}{P}$.</em> Near $a_j$, $f=(z-a_j)^{m_j}h$ with $h$ holomorphic and $h(a_j)\ne0$ (the other factors do not vanish at $a_j$). By Leibniz's rule for the $k$-th derivative of a product, $f^{(k)}(a_j)=\sum_i\binom ki\big((z-a_j)^{m_j}\big)^{(i)}h^{(k-i)}\big|_{a_j}$, and $\big((z-a_j)^{m_j}\big)^{(i)}$ vanishes at $a_j$ unless $i=m_j$. So $f^{(k)}(a_j)=0$ for $k\lt m_j$ and $f^{(m_j)}(a_j)=m_j!\,h(a_j)\ne0$: a zero of order $m_j$. Near $b_k$, $f=g/(z-b_k)^{n_k}$ with $g(b_k)\ne0$: a pole of order $n_k$. There are no other zeros or poles. <span class="qed">∎</span></li>
</ol>
:::
<p>For rational functions the argument principle is therefore just bookkeeping. Its power is that it holds for every $f$ that is holomorphic apart from poles (a <em>meromorphic</em> function), whose zeros usually cannot be listed in advance. Rouché's theorem (@thm:rouche) is the main application in the course.</p>
