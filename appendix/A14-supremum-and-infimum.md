---
id: A14
title: Supremum and infimum
status:
- defined
---
<p>The <em>supremum</em> $\sup_\Omega h$ is the least upper bound of the values of $h$: $h\le\sup h$ everywhere, and no smaller number has that property. It exists (possibly $+\infty$) by the completeness of the real numbers ([A.15](apx:A15)). Unlike a maximum, it need not be attained: $\sup_{(0,1)}x=1$, but no point of $(0,1)$ has $x=1$. The <em>infimum</em> is the greatest lower bound. @thm:strong-maximum-principle assumes the supremum <em>is</em> attained at an interior point.</p>
<p>The <em>limit superior</em> $\limsup_{z\to p}F(z)$ is the largest value that $F$ keeps coming close to as $z$ approaches $p$: precisely, $\lim_{r\to0}\sup\{F(z):0\lt|z-p|\lt r\}$. It always exists (possibly infinite), even when $\lim F$ does not. For a nonnegative $F$, $\limsup_{z\to p}F(z)=0$ is the same as $\lim_{z\to p}F(z)=0$; @thm:step-4-boundary-values uses this with $F=|u-g(p)|$.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Infimum_and_supremum" target="_blank" rel="noopener">Infimum and supremum</a></p>
