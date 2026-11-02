---
id: v11
slide: Slide 11
title: 'The barrier: a point charge outside $\Omega$'
toc: The barrier
---

::: lemma {#lem:an-empty-coarse-square-at-p name="an empty coarse square at $p$"}
Fix $p\in\class{ntn-dOm}{\partial\Omega}$. Some closed square $\class{ntn-Ssq}{S}$ of the coarsest grid contains $p$ and is not a square of $\Omega$. Its interior misses $\overline\Omega$, and it contains a closed square $\class{ntn-Qp}{Q_p}$ of side $\class{ntn-epsn}{\eps_0}/2$ with a corner at $p$.
:::
::: proof
The closed coarse squares containing $p$ (one, two or four of them, depending on whether $p$ is inside a square, on an edge, or at a node) together cover a disk around $p$. If all of them were squares of $\Omega$, that disk would lie in their union, and $p$ would be in the interior of $\overline\Omega$, which is $\Omega$ (@hyp:fix-and-grid-lines-with). But $p\in\class{ntn-dOm}{\partial\Omega}$ and $\Omega$ is open, so $p\notin\Omega$. So one of them, $\class{ntn-Ssq}{S}$, is not a square of $\Omega$.<br>
Distinct grid squares overlap only along edges, so no closed square of $\Omega$ meets the interior of $\class{ntn-Ssq}{S}$; since $\overline\Omega$ is the union of those squares, $\overline\Omega$ misses the interior of $\class{ntn-Ssq}{S}$.<br>
Finally, $p\in \class{ntn-Ssq}{S}$ is within $\class{ntn-epsn}{\eps_0}/2$ of the centre of $\class{ntn-Ssq}{S}$ in each coordinate, so the square of side $\class{ntn-epsn}{\eps_0}/2$ with corner $p$ that extends towards the centre of $\class{ntn-Ssq}{S}$ lies inside $\class{ntn-Ssq}{S}$. Call it $\class{ntn-Qp}{Q_p}$.
:::

::: definition {#def:the-barrier name="the barrier"}
Let $\class{ntn-yp}{y}$ be the point on the diagonal of $\class{ntn-Qp}{Q_p}$ through $p$ at distance $d\le\class{ntn-epsn}{\eps_0}/4$ from $p$, and
\[ \class{ntn-wd}{w_d}(z):=\log\frac{|z-\class{ntn-yp}{y}|}{\class{ntn-dd}{d}/2}. \]
This is the [potential of a point charge](apx:E6) at $\class{ntn-yp}{y}$ (Lecture 2, @rem:consequence-the-singularity-is-the-charge). Here $z$ is again a point of the plane, and $\class{ntn-yp}{y}$ is a point, not a coordinate.
:::

<figure>
{{fig:v11-1}}
<figcaption>The charge sits at $\class{ntn-yp}{y}$, just outside $\Omega$ in the empty square $\class{ntn-Qp}{Q_p}$. Inside the small circle (radius $\class{ntn-dd}{d}/2$) $\class{ntn-wd}{w_d}\lt0$, but that circle misses $\overline\Omega$. Dashed: level curves of $\class{ntn-wd}{w_d}$.</figcaption>
</figure>

::: lemma {#lem:properties-of-the-barrier name="properties of the barrier"}

(i) $\class{ntn-wd}{w_d}$ is harmonic in $\Omega$ and smooth on $\overline\Omega$, since $\class{ntn-yp}{y}\notin\overline\Omega$.<br>
(ii) $\class{ntn-wd}{w_d}\ge0$ on $\overline\Omega$.<br>
(iii) $\class{ntn-wd}{w_d}(p)=\log2$.<br>
(iv) $\class{ntn-wd}{w_d}(z)\ge\log(|z-p|/\class{ntn-dd}{d})$ whenever $|z-p|\ge2\class{ntn-dd}{d}$.
:::
::: proof
Write $\class{ntn-yp}{y}=p+\frac{\class{ntn-dd}{d}}{\sqrt2}(\pm1,\pm1)$, with signs pointing into $\class{ntn-Qp}{Q_p}$.
<ol type="i">
<li>$\log|z-\class{ntn-yp}{y}|$ is harmonic away from $\class{ntn-yp}{y}$ ([E.6](apx:E6)), and $\class{ntn-wd}{w_d}$ differs from it by the constant $-\log(\class{ntn-dd}{d}/2)$. The point $\class{ntn-yp}{y}$ is at distance $\class{ntn-dd}{d}/\sqrt2\gt0$ from the two sides of $\class{ntn-Qp}{Q_p}$ through $p$, and at distance at least $\class{ntn-epsn}{\eps_0}/2-\class{ntn-dd}{d}/\sqrt2\ge\class{ntn-epsn}{\eps_0}/2-\class{ntn-epsn}{\eps_0}/(4\sqrt2)\gt0$ from the other two, so $\class{ntn-yp}{y}$ is in the interior of $\class{ntn-Qp}{Q_p}\subset \class{ntn-Ssq}{S}$, which misses $\overline\Omega$ (@lem:an-empty-coarse-square-at-p). So $\class{ntn-wd}{w_d}$ is smooth on a neighbourhood of $\overline\Omega$.</li>
<li>$\class{ntn-wd}{w_d}\lt0$ exactly when $|z-\class{ntn-yp}{y}|\lt \class{ntn-dd}{d}/2$. The disk of radius $\class{ntn-dd}{d}/2$ about $\class{ntn-yp}{y}$ lies inside $\class{ntn-Qp}{Q_p}$: its radius $\class{ntn-dd}{d}/2$ is less than $\class{ntn-dd}{d}/\sqrt2$, the distance to the near sides, and less than $\class{ntn-epsn}{\eps_0}/2-\class{ntn-dd}{d}/\sqrt2\approx0.32\,\class{ntn-epsn}{\eps_0}$, the distance to the far sides (since $\class{ntn-dd}{d}/2\le\class{ntn-epsn}{\eps_0}/8$). So that disk misses $\overline\Omega$, and $\class{ntn-wd}{w_d}\ge0$ on $\overline\Omega$.</li>
<li>$|p-\class{ntn-yp}{y}|=\class{ntn-dd}{d}$, so $\class{ntn-wd}{w_d}(p)=\log\frac{\class{ntn-dd}{d}}{\class{ntn-dd}{d}/2}=\log2$.</li>
<li>If $|z-p|\ge2\class{ntn-dd}{d}$ then $d\le\frac12|z-p|$, and by the triangle inequality
\[ |z-\class{ntn-yp}{y}|\ge|z-p|-|p-\class{ntn-yp}{y}|=|z-p|-d\ge\tfrac12|z-p|. \] Since $\log$ is increasing, $\class{ntn-wd}{w_d}(z)\ge\log\frac{|z-p|/2}{\class{ntn-dd}{d}/2}=\log\frac{|z-p|}{\class{ntn-dd}{d}}$. <span class="qed">∎</span></li>
</ol>
:::
<p>So the barrier is small at $p$ (exactly $\log2$) and large everywhere else as $d\to0$: at a fixed distance $r$ from $p$ it is at least $\log(r/\class{ntn-dd}{d})\to\infty$. Placing the charge <em>outside</em> $\Omega$ is what keeps $\class{ntn-wd}{w_d}$ harmonic and nonnegative on all of $\overline\Omega$; this is possible because every boundary point of a union of squares has an empty square next to it.</p>
