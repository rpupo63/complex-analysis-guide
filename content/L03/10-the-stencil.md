---
id: s11
slide: Slide 11
title: 'What the equations say: the stencil'
toc: The stencil
---

::: lemma {#lem:only-neighbours-interact name="only neighbours interact"}
$\class{ntn-A}{A_{kl,ij}}=0$ unless the nodes $(i,j)$ and $(k,l)$ are corners of a common square, that is, $|i-k|\le1$ and $|j-l|\le1$.
:::
::: proof
On any open square only the four corner hats are nonzero (@lem:the-four-hats-on-one-square). If no square has both nodes as corners, then on every open square one of the two gradients is zero, so the integrand is zero except on grid lines, which have [zero area](apx:A11).
:::

::: lemma {#lem:integrating-over-one-square name="integrating over one square"}
On one square $Q$, label its corners $1=(0,0)$, $2=(1,0)$, $3=(1,1)$, $4=(0,1)$ in local coordinates, with hats $\class{ntn-Na}{N_1},\dots,\class{ntn-Na}{N_4}$ as in @lem:the-four-hats-on-one-square. Then $\class{ntn-K}{K_{ab}}:=\iint_Q\nabla \class{ntn-Na}{N_a}\cdot\nabla \class{ntn-Na}{N_b}\,dA$ does not depend on $\eps$, and
\[ \class{ntn-K}{K_{aa}}=\tfrac23,\qquad \class{ntn-K}{K_{ab}}=-\tfrac16\ \text{(edge-adjacent corners, e.g. 1,2)},\qquad \class{ntn-K}{K_{ab}}=-\tfrac13\ \text{(opposite corners, e.g. 1,3)}. \]
:::
::: proof
Substitute $x=x_i+\eps s$, $y=y_j+\eps t$. Then $\partial_x=\frac1\eps\partial_s$, $\partial_y=\frac1\eps\partial_t$ and $dA=\eps^2\,ds\,dt$, so
\[ \class{ntn-K}{K_{ab}}=\int_0^1\!\!\int_0^1\frac1{\eps^2}\big(\partial_s\class{ntn-Na}{N_a}\,\partial_s\class{ntn-Na}{N_b}+\partial_t\class{ntn-Na}{N_a}\,\partial_t\class{ntn-Na}{N_b}\big)\,\eps^2\,ds\,dt, \]
and $\eps$ cancels. The partial derivatives are:
\[ \begin{array}{c|cc} & \partial_s & \partial_t\\\hline \class{ntn-Na}{N_1}=(1-s)(1-t) & -(1-t) & -(1-s)\\ \class{ntn-Na}{N_2}=s(1-t) & 1-t & -s\\ \class{ntn-Na}{N_3}=st & t & s\\ \class{ntn-Na}{N_4}=(1-s)t & -t & 1-s\end{array} \]
The one-dimensional integrals needed are $\int_0^1(1-t)^2dt=\int_0^1t^2dt=\tfrac13$ and $\int_0^1t(1-t)\,dt=\tfrac12-\tfrac13=\tfrac16$. An integrand depending only on $t$ integrates over $s\in[0,1]$ to itself, so
\[ \begin{aligned} \class{ntn-K}{K_{11}}&=\iint\big[(1-t)^2+(1-s)^2\big]=\tfrac13+\tfrac13=\tfrac23,\\ \class{ntn-K}{K_{12}}&=\iint\big[-(1-t)^2+(1-s)s\big]=-\tfrac13+\tfrac16=-\tfrac16,\\ \class{ntn-K}{K_{13}}&=\iint\big[-(1-t)t-(1-s)s\big]=-\tfrac16-\tfrac16=-\tfrac13. \end{aligned} \]
Rotating the square by $90°$ permutes the corners and preserves the integrals. So every diagonal entry equals $\class{ntn-K}{K_{11}}$, every edge-adjacent pair equals $\class{ntn-K}{K_{12}}$, and every opposite pair equals $\class{ntn-K}{K_{13}}$. As a check, each row sums to $\tfrac23-\tfrac16-\tfrac13-\tfrac16=0$. This must happen, because $\class{ntn-Na}{N_1}+\class{ntn-Na}{N_2}+\class{ntn-Na}{N_3}+\class{ntn-Na}{N_4}\equiv1$ has zero gradient.
:::

::: proposition {#prop:summing-over-the-four-squares name="summing over the four squares"}
Let $(k,l)$ be an interior node. Then
\[ \class{ntn-A}{A_{kl,kl}}=\tfrac83,\qquad \class{ntn-A}{A_{kl,ij}}=-\tfrac13\ \text{for each of the 8 neighbours }(i,j),\qquad \class{ntn-A}{A_{kl,ij}}=0\ \text{otherwise}. \]
:::
::: proof
Since $(k,l)$ is interior, $\class{ntn-phi}{\varphi_{kl}}$ is supported on four squares, all in $\Omega$. So $\class{ntn-A}{A_{kl,ij}}$ is the sum of the element entries over these four squares.
<ul>
<li><em>Diagonal:</em> $(k,l)$ is a corner of all four squares, giving $4\cdot\tfrac23=\tfrac83$.</li>
<li><em>Edge neighbour</em>, e.g. $(k+1,l)$: the edge joining the two nodes is shared by two of the four squares, and in each the nodes are edge-adjacent corners. This gives $2\cdot(-\tfrac16)=-\tfrac13$.</li>
<li><em>Diagonal neighbour</em>, e.g. $(k+1,l+1)$: exactly one square has both as corners, as opposite corners. This gives $1\cdot(-\tfrac13)=-\tfrac13$.</li>
<li><em>All other nodes:</em> @lem:only-neighbours-interact. <span class="qed">∎</span></li>
</ul>
:::

<figure>
<div class="stencil" role="img" aria-label="Stencil: minus 1 in all eight neighbour positions, 8 in the centre, times one third.">
  <div>−1</div><div>−1</div><div>−1</div>
  <div>−1</div><div class="c">8</div><div>−1</div>
  <div>−1</div><div>−1</div><div>−1</div>
</div>
<figcaption>Row $(k,l)$ of $A$ laid out on the grid, times $\tfrac13$. Row sum: $\tfrac83-8\cdot\tfrac13=0$.</figcaption>
</figure>

::: corollary {#cor:each-interior-value-is-the-average name="each interior value is the average of its eight neighbours"}
For every interior node,
\[ c_{kl}=\frac18\sum_{\substack{(i,j)\text{ one of the}\\\text{8 neighbours of }(k,l)}}c_{ij}. \]
:::
::: proof
With @prop:summing-over-the-four-squares, the equation of @prop:the-equations reads $\tfrac83c_{kl}-\tfrac13\sum_{\text{nbrs}}c_{ij}=0$. Multiply by $\tfrac38$. Neighbours that are boundary nodes enter with their known values $c_{ij}=g(x_i,y_j)$.
:::
<p>This is a discrete analogue of the mean value property of harmonic functions, @thm:mean-value-property in Lecture 4. Other discretizations give [other averaging rules](apx:E8).</p>
