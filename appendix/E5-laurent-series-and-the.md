---
id: E5
title: Laurent series and the residue theorem
status:
- cited
---
<div class="env"><span class="hd">Theorem (Laurent).</span> If $f$ is holomorphic on a punctured disk $0\lt|z-z_0|\lt R$, then $f(z)=\sum_{m=-\infty}^{\infty}c_m(z-z_0)^m$ there, converging uniformly on every smaller closed annulus. The terms with $m\lt0$ form the <em>principal part</em>; $c_{-1}$ is the residue.</div>
<p>In Lecture 2's notation, $a_m=c_{-m}$ for $m\ge1$, and the terms with $m\ge0$ are the "part holomorphic near $z_0$". Uniform convergence on the circle is what justifies integrating term by term in @prop:the-contour-integral-sees-only-the. The <em>residue theorem</em> says $\oint_\gamma f\,dz=2\pi i\sum\class{ntn-res}{\operatorname{Res}}$ over the singularities enclosed by $\gamma$; @cor:the-residue-theorem-point-charge-form is the case of simple charges, and @thm:residue-theorem proves it for poles of any order, where the principal part is finite (@prop:principal-part). Laurent series are needed only for <em>essential</em> singularities, where infinitely many negative powers occur, such as $e^{1/z}=\sum_{m\ge0}z^{-m}/m!$ at $0$; the residue theorem holds there too, with $c_{-1}$ as the residue.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Laurent_series" target="_blank" rel="noopener">Laurent series</a> · <a href="https://en.wikipedia.org/wiki/Residue_theorem" target="_blank" rel="noopener">Residue theorem</a> · <a href="https://en.wikipedia.org/wiki/Multipole_expansion" target="_blank" rel="noopener">Multipole expansion</a></p>
