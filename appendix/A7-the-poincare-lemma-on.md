---
id: A7
title: The Poincaré lemma on a disk
status:
- derived
---
<div class="env"><span class="hd">Theorem.</span> Let $D$ be an open disk and $W=(W_1,W_2)$ a $C^1$ field on $D$ with $\class{ntn-divc}{\operatorname{curl}}W=\partial_xW_2-\partial_yW_1=0$. Then $W=\nabla\varphi$ for some $\varphi$, unique up to an additive constant.</div>
::: proof
Shift so the centre of $D$ is the origin. For $p=(x,y)\in D$, the segment from $0$ to $p$ lies in $D$; integrate $W$ along it:
\[ \varphi(x,y):=\int_0^1W(tx,ty)\cdot(x,y)\,dt=\int_0^1\big(x\,W_1(tx,ty)+y\,W_2(tx,ty)\big)\,dt. \]
Differentiate under the integral sign ([A.4](apx:A4)) in $x$, using the chain rule ($\partial_x[W_j(tx,ty)]=t\,(\partial_xW_j)(tx,ty)$):
\[ \varphi_x=\int_0^1\Big(W_1+t\,x\,\partial_xW_1+t\,y\,\partial_xW_2\Big)(tx,ty)\,dt. \]
Now use $\class{ntn-divc}{\operatorname{curl}}W=0$, i.e. $\partial_xW_2=\partial_yW_1$:
\[ \varphi_x=\int_0^1\Big(W_1+t\,(x\,\partial_xW_1+y\,\partial_yW_1)\Big)(tx,ty)\,dt=\int_0^1\frac{d}{dt}\Big[t\,W_1(tx,ty)\Big]\,dt=W_1(x,y), \]
since $\frac{d}{dt}[tW_1(tx,ty)]=W_1+t(x\partial_xW_1+y\partial_yW_1)$ by the product and chain rules, and the fundamental theorem of calculus gives $1\cdot W_1(x,y)-0$. The same computation gives $\varphi_y=W_2$.<br>
<em>Uniqueness:</em> if $\nabla\varphi_1=\nabla\varphi_2$, the difference has zero gradient on the connected set $D$, so it is constant (the argument of @thm:uniqueness, step 4).
:::
<p>The proof needs every segment from the centre to stay in the domain ("star-shaped"). On $\mathbb C\setminus\{0\}$ this fails, and so does the lemma (@prop:no-global-primitive-on-mathbb-c).</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Poincar%C3%A9_lemma" target="_blank" rel="noopener">Poincaré lemma</a> · <a href="https://en.wikipedia.org/wiki/Conservative_vector_field" target="_blank" rel="noopener">Conservative vector field</a></p>
