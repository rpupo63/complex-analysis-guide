---
id: s16
slide: Slide 16
title: The parallelogram law
toc: Parallelogram law
---

::: definition {#def:for-a-scalar-or-vector}
For a scalar- or vector-valued function $F$ on $\Omega$, $\norm{F}_{L^2}^2:=\iint_\Omega|F|^2\,dA$. So $\class{ntn-E}{E}(V)=\norm{\nabla V}_{L^2}^2$. (The space of such $F$ is [$L^2(\Omega)$](apx:D2).) <em>Convention:</em> from here on, $\class{ntn-L2}{\norm{F}}$ with no subscript always means $\class{ntn-L2}{\norm{F}_{L^2}}$. No other norm appears in the rest of the lecture.
:::

::: lemma {#lem:parallelogram-identity name="parallelogram identity"}
$\class{ntn-E}{E}(x-y)+\class{ntn-E}{E}(x+y)=2\class{ntn-E}{E}(x)+2\class{ntn-E}{E}(y)$, and $\class{ntn-E}{E}(\lambda x)=\lambda^2\class{ntn-E}{E}(x)$ ("the energy is quadratic").
:::
::: proof
By bilinearity and symmetry, $\class{ntn-E}{E}(x\pm y)=\class{ntn-E}{E}(x)\pm2\class{ntn-a}{a}(x,y)+\class{ntn-E}{E}(y)$. Adding the two, the cross terms cancel. Also $\class{ntn-E}{E}(\lambda x)=\class{ntn-a}{a}(\lambda x,\lambda x)=\lambda^2\class{ntn-a}{a}(x,x)$.
:::

::: corollary {#cor:x}

\[ \norm{\nabla(\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k})}_{L^2}^2=2\class{ntn-mn}{m_n}+2\class{ntn-mn}{m_k}-4E\big(\tfrac12(\class{ntn-Un}{U_n}+\class{ntn-Un}{U_k})\big). \]
:::
::: proof
Take $x=\class{ntn-Un}{U_n}$, $y=\class{ntn-Un}{U_k}$ in @lem:parallelogram-identity:
\[ \class{ntn-L2}{\norm{\nabla(\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k})}}^2=\class{ntn-E}{E}(\class{ntn-Un}{U_n}-\class{ntn-Un}{U_k})=2\class{ntn-E}{E}(\class{ntn-Un}{U_n})+2\class{ntn-E}{E}(\class{ntn-Un}{U_k})-\class{ntn-E}{E}(\class{ntn-Un}{U_n}+\class{ntn-Un}{U_k}). \]
$\class{ntn-E}{E}(\class{ntn-Un}{U_n})=\class{ntn-mn}{m_n}$ and $\class{ntn-E}{E}(\class{ntn-Un}{U_k})=\class{ntn-mn}{m_k}$ by @def:for-write-and-the-minimum, and, since the energy is quadratic,
\[ \class{ntn-E}{E}(\class{ntn-Un}{U_n}+\class{ntn-Un}{U_k})=E\big(2\cdot\tfrac12(\class{ntn-Un}{U_n}+\class{ntn-Un}{U_k})\big)=4E\big(\tfrac12(\class{ntn-Un}{U_n}+\class{ntn-Un}{U_k})\big). \]
:::
