---
id: h2
slide: Slide 3
title: A Fourier transform
---

::: definition {#def:fourier-transform name="Fourier transform"}
The <em>Fourier transform</em> of an integrable function $f$ on $\R$ (one with $\int|f|\lt\infty$) is
\[ \class{ntn-hat}{\hat f}(\xi):=\int_{-\infty}^\infty f(x)\,e^{-2\pi ix\xi}\,dx\qquad(\xi\in\R). \]
:::
<p>The integral converges absolutely because $|e^{-2\pi ix\xi}|=1$. $\class{ntn-hat}{\hat f}(\xi)$ measures how much of the frequency $\xi$ (oscillations $e^{2\pi ix\xi}$, $\xi$ per unit length) is present in $f$. Background and the inversion theorem are in [D.7](apx:D7).</p>

::: proposition {#prop:for}
For $f(x)=\dfrac1{1+x^2}$, $\ \class{ntn-hat}{\hat f}(\xi)=\pi e^{-2\pi|\xi|}$.
:::
::: proof

<ol>
<li><em>Which half-plane?</em> For $z=x+iy$, $|e^{-2\pi iz\xi}|=e^{\operatorname{Re}(-2\pi i(x+iy)\xi)}=e^{2\pi\xi y}$. If $\xi\ge0$ this is $\le1$ exactly when $y=\operatorname{Im}z\le0$. So close $[-R,R]$ by a semicircle in the <em>lower</em> half-plane, where the exponential is harmless.</li>
<li><em>Orientation.</em> Going along $[-R,R]$ left to right and back along the lower arc keeps the half-disk on the right: the loop is clockwise, so the residue theorem carries a factor $-2\pi i$. The only pole inside is $-i$.</li>
<li><em>The arc.</em> As in @sec:h1, the arc contributes at most $\frac{\pi R}{R^2-1}\cdot1\to0$.</li>
<li><em>The residue.</em> At $-i$, $\frac{e^{-2\pi iz\xi}}{(z+i)(z-i)}$ has a simple pole with residue $\frac{e^{-2\pi i(-i)\xi}}{-i-i}=\frac{e^{-2\pi\xi}}{-2i}$. So
\[ \class{ntn-hat}{\hat f}(\xi)=-2\pi i\class{ntn-res}{\operatorname{Res}}_{-i}\frac{e^{-2\pi iz\xi}}{(z+i)(z-i)}=-2\pi i\cdot\frac{e^{-2\pi\xi}}{-2i}=\pi e^{-2\pi\xi}. \]</li>
<li><em>$\xi\lt0$.</em> Now $|e^{-2\pi iz\xi}|\le1$ for $\operatorname{Im}z\ge0$: close in the upper half-plane, anticlockwise, around $i$, with residue $\frac{e^{2\pi\xi}}{2i}$, giving $2\pi i\cdot\frac{e^{2\pi\xi}}{2i}=\pi e^{2\pi\xi}=\pi e^{-2\pi|\xi|}$. <span class="qed">∎</span></li>
</ol>
:::
<p>The rule of thumb: the sign of $\xi$ decides the half-plane in which $e^{-2\pi iz\xi}$ decays, and the contour must be closed there.</p>
