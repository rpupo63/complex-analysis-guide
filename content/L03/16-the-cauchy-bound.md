---
id: s17
slide: Slide 17
title: The bound tends to zero
toc: The Cauchy bound
---

::: proposition {#prop:for-consequently-is-a-cauchy}
For $n\le k$, $\ \norm{\nabla(\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k})}_{L^2}^2\le2(\class{ntn-mn}{m_n}-\class{ntn-m}{m})+2(\class{ntn-mn}{m_k}-\class{ntn-m}{m})$. Consequently $(\nabla \class{ntn-Un}{U_n})$ is a [Cauchy sequence](apx:D2) in $L^2$: for every $\delta\gt0$ there is $N$ with $\class{ntn-L2}{\norm{\nabla(\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k})}}^2\lt\delta$ for all $n,k\ge N$.
:::
::: proof
$\class{ntn-Un}{U_n}\in \class{ntn-Vg}{V^g_{\eps_n}}\subset \class{ntn-Vg}{V^g_{\eps_k}}$ ([Lemma #(b)](@lem:nesting)) and $\class{ntn-Un}{U_k}\in \class{ntn-Vg}{V^g_{\eps_k}}$. Their average lies in $\class{ntn-Vg}{V^g_{\eps_k}}$ (@prop:v-g-eps-is-affine-not with $\lambda=\tfrac12$: "the boundary values average to $g$"). $\class{ntn-mn}{m_k}$ is the minimum of $E$ over that set, and $\class{ntn-mn}{m_k}\ge \class{ntn-m}{m}$ (@prop:so-decreases-to-a-limit), so $E\big(\tfrac12(\class{ntn-Un}{U_n}+\class{ntn-Un}{U_k})\big)\ge \class{ntn-mn}{m_k}\ge \class{ntn-m}{m}$. Substitute into @cor:x:
\[ \class{ntn-L2}{\norm{\nabla(\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k})}}^2\le2\class{ntn-mn}{m_n}+2\class{ntn-mn}{m_k}-4\class{ntn-m}{m}=2(\class{ntn-mn}{m_n}-\class{ntn-m}{m})+2(\class{ntn-mn}{m_k}-\class{ntn-m}{m}). \]
Given $\delta\gt0$, choose $N$ with $\class{ntn-mn}{m_j}-\class{ntn-m}{m}\lt\delta/4$ for all $j\ge N$, which is possible because $\class{ntn-mn}{m_j}\to \class{ntn-m}{m}$. For $n,k\ge N$ the right side is less than $\delta$.
:::
<p>This controls only gradients. A function can have a small gradient and still be large (add a constant). The next section closes that gap using the fact that $\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k}$ vanishes on the boundary.</p>
