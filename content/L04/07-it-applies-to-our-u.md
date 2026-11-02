---
id: t8
slide: Slide 8
title: Weyl's lemma applies to our $u$
toc: It applies to our $u$
---

::: proposition {#prop:the-limit-from-lecture-3}
The limit $u$ from Lecture 3 satisfies $\iint_\Omega u\,\class{ntn-Delta}{\Delta}\eta\,dA=0$ for every test function $\eta$.
:::
::: proof

<ol>
<li><em>What Lecture 3 proved.</em> $\class{ntn-Un}{U_n}\to u$ and $\nabla \class{ntn-Un}{U_n}\to(p,q)=\nabla u$ in $L^2$ (@prop:three-limits). A test function $\eta$ is smooth on $\overline\Omega$ (extended by zero near the boundary) and vanishes on $\class{ntn-dOm}{\partial\Omega}$, so @thm:smooth-test-functions applies to it:
\[ \class{ntn-a}{a}(u,\eta)=\iint(p\,\partial_x\eta+q\,\partial_y\eta)\,dA=0. \]</li>
<li><em>Integrate by parts, for each $n$.</em> We show $\iint\nabla \class{ntn-Un}{U_n}\cdot\nabla\eta\,dA=-\iint \class{ntn-Un}{U_n}\,\class{ntn-Delta}{\Delta}\eta\,dA$. On each closed grid square $Q$, $\class{ntn-Un}{U_n}$ is bilinear, so $F:=\class{ntn-Un}{U_n}\nabla\eta$ is $C^1$ there, and by the product rule $\nabla\cdot F=\nabla \class{ntn-Un}{U_n}\cdot\nabla\eta+\class{ntn-Un}{U_n}\,\class{ntn-Delta}{\Delta}\eta$. The [divergence theorem](apx:A6) on $Q$ gives
\[ \iint_Q\big(\nabla \class{ntn-Un}{U_n}\cdot\nabla\eta+\class{ntn-Un}{U_n}\,\class{ntn-Delta}{\Delta}\eta\big)\,dA=\oint_{\partial Q}\class{ntn-Un}{U_n}\,\nabla\eta\cdot n\,ds. \]
Add over all squares of $\Omega$. An edge shared by two squares appears twice, with the same integrand $\class{ntn-Un}{U_n}\nabla\eta$ (since $\class{ntn-Un}{U_n}$ is continuous) and opposite outward normals, so the two contributions cancel. An edge on $\class{ntn-dOm}{\partial\Omega}$ contributes nothing, because $\nabla\eta=0$ there ($\eta$ vanishes near $\class{ntn-dOm}{\partial\Omega}$). The squares cover $\Omega$ up to edges of zero area. So the left sides add to $0$, which is the claim. This is the same bookkeeping as Step 4 of @prop:the-slides-computation.</li>
<li><em>Let $n\to\infty$.</em> By [Cauchy–Schwarz](apx:A12), exactly as in @prop:and-weakly-write,
\[ \Big|\iint(\nabla \class{ntn-Un}{U_n}-\nabla u)\cdot\nabla\eta\Big|\le\norm{\nabla \class{ntn-Un}{U_n}-\nabla u}\,\norm{\nabla\eta}\to0,\qquad \Big|\iint(\class{ntn-Un}{U_n}-u)\,\class{ntn-Delta}{\Delta}\eta\Big|\le\norm{\class{ntn-Un}{U_n}-u}\,\norm{\class{ntn-Delta}{\Delta}\eta}\to0. \]
So the left side of Step 2 tends to $\iint(p\,\partial_x\eta+q\,\partial_y\eta)=0$, and the right side tends to $-\iint u\,\class{ntn-Delta}{\Delta}\eta$. Equal sequences have equal limits: $\iint u\,\class{ntn-Delta}{\Delta}\eta=0$. <span class="qed">∎</span></li>
</ol>
:::
<p>So the hypothesis of Weyl's lemma holds for our $u$. Note the route: Lecture 3 gave "one derivative on $u$, one on $\eta$" in the limit; Step 2 moves the last derivative onto $\eta$ before taking the limit, while $\class{ntn-Un}{U_n}$ is still a concrete piecewise-bilinear function.</p>
