---
id: j7
slide: Slide 8
title: 'A check: $\sin\pi z$'
---
<p>Test Jensen's formula on $f(z):=\dfrac{\sin\pi z}{\pi z}$ (with $f(0):=1$; it is entire, by its power series), with $R:=K+\frac12$ for an integer $K\ge1$. Then $f(0)=1$, and the zeros in $|z|\lt R$ are $\pm1,\dots,\pm K$, all simple. (The radius is a half-integer so that no zero lies on the circle.)</p>

::: proposition {#prop:both-sides-of-jensen-for-sin name="both sides of Jensen for $\sin\pi z/\pi z$"}
As $R\to\infty$, both sides of Jensen's formula equal $2R-\log(2\pi R)+O(1/R)$.
:::
::: proof

<ol>
<li><em>The zeros.</em>
\[ \sum_{0\lt|n|\lt R}\log\frac R{|n|}=2(K\log R-\log K!). \]
[Stirling's formula](apx:A23) gives $\log K!=K\log K-K+\frac12\log(2\pi K)+O(\frac1K)$, and
\[ K\log R-K\log K=K\log(1+\frac1{2K})=\frac12+O(\frac1K). \]
So
\[ 2(K\log R-\log K!)=2K+1-\log(2\pi K)+O(\tfrac1K)=2R-\log(2\pi R)+O(\tfrac1R), \]
using $2K+1=2R$ and $\log(2\pi R)-\log(2\pi K)=\log\frac RK=O(\frac1R)$.</li>
<li><em>The circle: a formula for $|\sin|$.</em> For $z=x+iy$,
\[ \sin\pi z=\sin\pi x\cosh\pi y+i\cos\pi x\sinh\pi y, \]
so
\[ |\sin\pi z|^2=\sin^2\pi x\cosh^2\pi y+\cos^2\pi x\sinh^2\pi y=\sin^2\pi x+\sinh^2\pi y. \]
</li>
<li><em>The circle: $\log|f|$.</em> On $|z|=R$ we claim
\[ \log|f(z)|=\pi|y|-\log(2\pi R)+O(e^{-2\pi|y|}) \]
with an absolute constant. Since $\log|f|=\log|\sin\pi z|-\log(\pi R)$, this says $\log|\sin\pi z|=\pi|y|-\log2+O(e^{-2\pi|y|})$. For $|y|\ge1$: $\sinh^2\pi y\le|\sin\pi z|^2\le\cosh^2\pi y$, and both $\log\sinh\pi|y|$ and $\log\cosh\pi y$ equal $\pi|y|-\log2+O(e^{-2\pi|y|})$. For $|y|\lt1$ (and $R\ge3$): $x^2=R^2-y^2$ puts $|x|$ within $1/R$ of $R=K+\frac12$, so $|\sin\pi x|\ge\cos(\pi/R)\ge\frac12$, and $\log|\sin\pi z|$ lies between $\log\frac12$ and $\log\cosh\pi$: bounded, as is $\pi|y|-\log2$. A bounded difference is $O(e^{-2\pi|y|})$ when $|y|\lt1$.</li>
<li><em>Average over the circle.</em> With $y=R\sin\theta$:
\[ \frac1{2\pi}\int_0^{2\pi}\pi R|\sin\theta|\,d\theta=\frac{\pi R}{2\pi}\cdot4=2R. \]
For the error,
\[ \int_0^{2\pi}e^{-2\pi R|\sin\theta|}d\theta=4\int_0^{\pi/2}e^{-2\pi R\sin\theta}d\theta\le4\int_0^{\pi/2}e^{-4R\theta}d\theta\le\frac1R, \]
using $\sin\theta\ge\frac{2\theta}\pi$. So the mean of $\log|f|$ is $2R-\log(2\pi R)+O(\frac1R)$. <span class="qed">∎</span></li>
</ol>
:::
<div class="tbl"><table>
<thead><tr><th>$R$</th><th>$\frac1{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta$</th><th>$\sum_{0\lt|n|\lt R}\log\frac R{|n|}$</th><th>$2R-\log(2\pi R)$</th></tr></thead>
<tbody>
<tr><td>10.5</td><td>16.8187</td><td>16.8187</td><td>16.8107</td></tr>
<tr><td>100.5</td><td>194.5528</td><td>194.5528</td><td>194.5520</td></tr>
</tbody></table></div>
<p>The first two columns agree to all digits shown, as Jensen's formula says they must. The third column, the common asymptotic value, is off by $O(1/R)$.</p>
