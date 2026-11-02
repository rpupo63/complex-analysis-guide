---
id: s6
slide: Slide 6
title: Nodal values and the space $\class{ntn-Veps}{V_\eps}$
toc: Nodal values and $V_\eps$
---

::: lemma {#lem:key-property name="key property"}
$\class{ntn-phi}{\varphi_{ij}}(x_k,y_l)=1$ if $(k,l)=(i,j)$, and $0$ at every other node.
:::
::: proof
$(x_k-x_i)/\eps = k-i$ and $(y_l-y_j)/\eps=l-j$ are integers, so $\class{ntn-phi}{\varphi_{ij}}(x_k,y_l)=\class{ntn-Lam}{\Lambda}(k-i)\,\class{ntn-Lam}{\Lambda}(l-j)$. By @lem:the-tent this is $1\cdot1$ when both integers are $0$, and $0$ when either is nonzero.
:::

::: corollary {#cor:the-coefficients-are-the-nodal-values name="the coefficients are the nodal values"}
If $U=\sum_{ij}c_{ij}\class{ntn-phi}{\varphi_{ij}}$ (summed over nodes), then $U(x_k,y_l)=c_{kl}$. In particular the hats are [linearly independent](apx:B2).
:::
::: proof
$U(x_k,y_l)=\sum_{ij}c_{ij}\class{ntn-phi}{\varphi_{ij}}(x_k,y_l)=c_{kl}$, since only the term with $(i,j)=(k,l)$ survives. If $U\equiv0$, evaluating at each node gives every $c_{kl}=0$.
:::

::: definition {#def:the-set-of-functions-restricted}
$\class{ntn-Veps}{V_\eps} := \operatorname{span}\{\class{ntn-phi}{\varphi_{ij}} : (x_i,y_j)\text{ a node}\}$, the set of functions $U=\sum c_{ij}\class{ntn-phi}{\varphi_{ij}}$ restricted to $\overline\Omega$. ([Span](apx:B2).)
:::

::: definition {#def:bilinear name=bilinear}
A function on a square is <em>bilinear</em> if it has the form $a+bx+cy+dxy$ there. In local coordinates $s=(x-x_i)/\eps$, $t=(y-y_j)/\eps\in[0,1]$ this is the same as the form $\alpha+\beta s+\gamma t+\delta st$, since substituting $x=x_i+\eps s$, $y=y_j+\eps t$ into one form gives the other.
:::

::: lemma {#lem:the-four-hats-on-one-square name="the four hats on one square"}
On the square $Q=[x_i,x_{i+1}]\times[y_j,y_{j+1}]$ with local coordinates $s,t\in[0,1]$, only the hats of the four corners are not identically zero, and
\[ \class{ntn-phi}{\varphi_{ij}}=(1-s)(1-t),\quad \class{ntn-phi}{\varphi_{i+1,j}}=s(1-t),\quad \class{ntn-phi}{\varphi_{i+1,j+1}}=st,\quad \class{ntn-phi}{\varphi_{i,j+1}}=(1-s)t. \]
Each is bilinear on $Q$.
:::
::: proof
For $x\in[x_i,x_{i+1}]$ we have $(x-x_i)/\eps=s\in[0,1]$, so $\class{ntn-Lam}{\Lambda}(s)=1-s$. Also $(x-x_{i+1})/\eps=s-1\in[-1,0]$, so $\class{ntn-Lam}{\Lambda}(s-1)=1-(1-s)=s$. The same holds in $y$; multiply. The hat of any other node has $|x-x_k|\ge\eps$ or $|y-y_l|\ge\eps$ throughout $Q$, so it vanishes on $Q$. Expanding, for example $(1-s)(1-t)=1-s-t+st$, shows each hat is bilinear.
:::

::: lemma {#lem:a-bilinear-function-is-fixed-by name="a bilinear function is fixed by its corner values"}
Given four numbers $p_{00},p_{10},p_{01},p_{11}$, there is exactly one bilinear $p(s,t)=\alpha+\beta s+\gamma t+\delta st$ with $p(0,0)=p_{00}$, $p(1,0)=p_{10}$, $p(0,1)=p_{01}$, $p(1,1)=p_{11}$.
:::
::: proof
The conditions read $\alpha=p_{00}$, $\alpha+\beta=p_{10}$, $\alpha+\gamma=p_{01}$, $\alpha+\beta+\gamma+\delta=p_{11}$. Solving in that order gives the unique answer
\[ \alpha=p_{00},\quad \beta=p_{10}-p_{00},\quad \gamma=p_{01}-p_{00},\quad \delta=p_{11}-p_{10}-p_{01}+p_{00}. \]
<span class="qed">∎</span>
:::

::: proposition {#prop:the-slides-description-of-v-eps name="the slide's description of $\class{ntn-Veps}{V_\eps}$"}
$\class{ntn-Veps}{V_\eps}$ is exactly the set of functions that are continuous on $\overline\Omega$ and bilinear on each grid square of $\Omega$.
:::
::: proof
(⊆) Each $\class{ntn-phi}{\varphi_{ij}}$ is continuous (@prop:the-hat) and bilinear on each square (@lem:the-four-hats-on-one-square, or identically $0$). Sums and multiples of continuous, squarewise-bilinear functions are again continuous and squarewise bilinear.<br>
(⊇) Let $f$ be continuous and squarewise bilinear. Put $U:=\sum_{ij}f(x_i,y_j)\class{ntn-phi}{\varphi_{ij}}\in \class{ntn-Veps}{V_\eps}$. On any square, $f$ and $U$ are both bilinear and agree at the four corners (@cor:the-coefficients-are-the-nodal-values), so they agree on the whole square (@lem:a-bilinear-function-is-fixed-by). The squares cover $\overline\Omega$, so $f=U$.
:::

::: proposition {#prop:linear-along-grid-lines-not-on name="linear along grid lines, not on squares"}
A bilinear function is linear (affine) along every horizontal and vertical segment of its square, in particular along every grid edge. It is not linear on the square when $\delta\ne0$.
:::
::: proof
Fix $t$. Then $\alpha+\beta s+\gamma t+\delta st=(\alpha+\gamma t)+(\beta+\delta t)s$, which is affine in $s$. The same argument works with $s$ fixed. Along the diagonal $s=t$ the function is $\alpha+(\beta+\gamma)s+\delta s^2$, which is not affine when $\delta\ne0$; this is the "$xy$ term" of the slide.
:::
<p>This is also why continuity across a shared edge comes for free: the functions on the two sides are both linear on that edge and have the same endpoint values.</p>
