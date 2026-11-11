---
id: q13
slide: Slide 16
title: A doubly periodic function
---

::: definition {#def:sn name="Jacobi's $\operatorname{sn}$"}
$\operatorname{sn}:=F^{-1}$, with $F$ and $R$ as in @eg:rectangles. It maps $R$ conformally onto $\mathbb H$ (@thm:inverse), continuously up to $\partial R$; it is real on $\partial R$ except for a pole at $iK'=F(\infty)$.
:::

::: proposition {#prop:sn-is-doubly-periodic name="$\operatorname{sn}$ is doubly periodic"}
$\operatorname{sn}$ extends to $\mathbb C$, holomorphic except for poles, with
\[ \operatorname{sn}(w+4K)=\operatorname{sn}(w)=\operatorname{sn}(w+2iK'). \]
:::
::: proof

<ol>
<li><em>Reflection in a side.</em> Across $[-K,K]$, @thm:schwarz-reflection gives $\operatorname{sn}(\bar w)=\overline{\operatorname{sn}(w)}$. Across $\operatorname{Re}w=K$, apply it to $z\mapsto\operatorname{sn}(K+iz)$, which is defined for $\operatorname{Im}z\gt0$ and real on $\mathbb R$: $\operatorname{sn}(2K-\bar w)=\overline{\operatorname{sn}(w)}$. The side $\operatorname{Re}w=-K$ is the same. The top side $\operatorname{Im}w=K'$ contains the pole $iK'$, so reflect $1/\operatorname{sn}$ there instead (it is real and continuous on that side, and $0$ at $iK'$), or use @cor:reflection-in-a-circle; the result is $\operatorname{sn}(\bar w+2iK')=\overline{\operatorname{sn}(w)}$. Each reflection extends $\operatorname{sn}$ to the neighbouring rectangle, with values in $-\mathbb H$.</li>
<li><em>Continue.</em> Reflecting again and again extends $\operatorname{sn}$ to every rectangle of the grid with corners $\pm K+2mK+i nK'$, with values in $\mathbb H$ and $-\mathbb H$ in a checkerboard pattern. Around each corner the four reflections close up, because the angles are right angles. Each reflection preserves "holomorphic except for poles", so $\operatorname{sn}$ extends to $\mathbb C$ in this sense.</li>
<li><em>Periods.</em> Two reflections in parallel lines make a translation: in $\operatorname{Re}w=-K$ ($w\mapsto-2K-\bar w$) then in $\operatorname{Re}w=K$ ($w\mapsto2K-\bar w$) give $w\mapsto w+4K$; in $\operatorname{Im}w=0$ then in $\operatorname{Im}w=K'$ give $w\mapsto w+2iK'$. Each reflection conjugates the value, so two of them leave it unchanged. <span class="qed">∎</span></li>
</ol>
:::
<p><b>Poles are unavoidable.</b> A doubly periodic entire function is bounded, since it takes all its values on one closed period rectangle, which is [compact](apx:C5). So by @thm:liouville it is constant.</p>

::: remark {#rem:correction-sn-top-side name="correction to the slide"}
The slide says $\operatorname{sn}$ "is real on $\partial R$" and reflects in every side with the same theorem. On the top side $\operatorname{sn}$ has a pole at $iK'$, so @thm:schwarz-reflection does not apply to $\operatorname{sn}$ there. Step 1 reflects $1/\operatorname{sn}$ instead. The conclusion is unchanged.
:::
