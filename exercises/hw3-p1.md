---
label: ex:integral-of-one-plus-x-to-the-n
source: Homework 3, Problem 1
title: integral of $1/(1+x^n)$
placement: h16
order: 4
---
For an integer $n\ge2$, integrate $1/(1+z^n)$ over the boundary of the sector $\{|z|\le R,\ 0\le\arg z\le 2\pi/n\}$ with $R\gt1$, and let $R\to\infty$, to show that
\[ \int_0^\infty\frac{dx}{1+x^n}=\frac{\pi/n}{\sin(\pi/n)}. \]
<details class="sol"><summary>Hint</summary>
On the ray $\arg z=2\pi/n$, $z^n=t^n$ with $t=|z|$. The case $n=3$ is @ex:a-sector.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>The pole inside the sector.</em> The solutions of $z^n=-1$ are $\alpha_k=e^{i(2k+1)\pi/n}$ for $k=0,\dots,n-1$. The open sector is $0\lt\arg z\lt 2\pi/n$, and $(2k+1)\pi/n$ lies there only when $2k+1=1$, so only $\alpha:=e^{i\pi/n}$. For $R\gt1$ this point is in the interior. It is a simple pole: $B(z)=1+z^n$ satisfies $B(\alpha)=0$ and $B'(\alpha)=n\alpha^{n-1}\ne0$. By @prop:simple-poles-of-a-quotient the residue is $1/(n\alpha^{n-1})=\alpha/(n\alpha^n)=-\alpha/n$.</li>
<li><em>The contour.</em> Let $\omega:=e^{2\pi i/n}$, and let $\Gamma_R$ be the boundary of the sector, sector on the left: $[0,R]$, the arc $|z|=R$ from $R$ to $R\omega$, then back to $0$. By @prop:other-contours,
\[ \oint_{\Gamma_R}\frac{dz}{1+z^n}=2\pi i\Big(-\frac\alpha n\Big). \]</li>
<li><em>The rays.</em> The outward ray contributes $\int_0^R dx/(1+x^n)$. On the return ray $z=t\omega$, with $t$ running from $R$ down to $0$, so $dz=\omega\,dt$ and $z^n=t^n\omega^n=t^n$. That side contributes $-\omega\int_0^R dt/(1+t^n)$. Together the rays contribute $(1-\omega)\int_0^R dx/(1+x^n)$.</li>
<li><em>The arc vanishes.</em> Its length is $2\pi R/n$, and $|1+z^n|\ge R^n-1$. By the [ML estimate](apx:A25) the integral over the arc is at most $\frac{2\pi R/n}{R^n-1}\to0$ as $R\to\infty$, since $n\ge2$.</li>
<li><em>The limit.</em> Write $I_R$ for the integral up to $R$. Then $(1-\omega)I_R$ tends to $-2\pi i\alpha/n$. The integrand is positive, so $I_R$ tends to the [improper integral](apx:A22) $I=\int_0^\infty dx/(1+x^n)$, and $(1-\omega)I=-2\pi i\alpha/n$. Now $\omega=\alpha^2$, so
\[ 1-\omega=1-\alpha^2=-\alpha\big(\alpha-\alpha^{-1}\big)=-\alpha\big(e^{i\pi/n}-e^{-i\pi/n}\big)=-2i\alpha\sin(\pi/n). \]
Therefore
\[ I=\frac{-2\pi i\alpha/n}{-2i\alpha\sin(\pi/n)}=\frac{\pi/n}{\sin(\pi/n)}. \]</li>
</ol>
</details>
