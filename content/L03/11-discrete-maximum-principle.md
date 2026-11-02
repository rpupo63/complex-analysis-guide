---
id: s12
slide: Slide 12
title: The discrete maximum principle
toc: Discrete maximum principle
---

::: lemma {#lem:an-average-equal-to-the-maximum name="an average equal to the maximum"}
If $c_{kl}=\frac18\sum_{\text{nbrs}}c_{ij}$ and every neighbour satisfies $c_{ij}\le M=c_{kl}$, then every neighbour has $c_{ij}=M$.
:::
::: proof
$\sum_{\text{nbrs}}(M-c_{ij})=8M-8c_{kl}=0$. A sum of nonnegative terms that equals zero has every term equal to zero.
:::

::: lemma {#lem:bilinear-extrema-are-at-corners name="bilinear extrema are at corners"}
A bilinear function on a closed square attains its maximum and minimum at corners.
:::
::: proof
Let $(s,t)$ be any point of the square. For fixed $t$, $p$ is affine in $s$ (@prop:linear-along-grid-lines-not-on), and an affine function on $[0,1]$ is at most its larger endpoint value, so $p(s,t)\le\max\big(p(0,t),p(1,t)\big)$. Each of $p(0,t)$ and $p(1,t)$ is affine in $t$, so it is at most the larger of its values at $t=0$ and $t=1$. Hence $p(s,t)$ is at most the largest corner value. The minimum is handled the same way.
:::

::: theorem {#thm:discrete-maximum-principle name="discrete maximum principle"}
$\class{ntn-Ue}{U_\eps}$ attains its maximum and minimum over $\overline\Omega$ at boundary nodes. Consequently
\[ \min_{q\in \class{ntn-B}{B}}g(x_q,y_q)\ \le\ \class{ntn-Ue}{U_\eps}(x,y)\ \le\ \max_{q\in \class{ntn-B}{B}}g(x_q,y_q)\qquad\text{for all }(x,y)\in\overline\Omega. \]
:::
::: proof
Let $M$ be the largest nodal value, which exists because there are finitely many nodes.
<ol>
<li><em>$M$ is attained at a boundary node.</em> Suppose $M$ is attained at an interior node $P_0$. By @cor:each-interior-value-is-the-average and @lem:an-average-equal-to-the-maximum, all 8 neighbours of $P_0$ have value $M$, in particular $P_1=P_0+(\eps,0)$. If $P_1$ is interior, repeat to get $P_2=P_1+(\eps,0)$ with value $M$, and so on. $\Omega$ is bounded, so this cannot continue forever, and some $P_m$ is not interior. $P_m$ is a node (a neighbour of an interior node is a corner of one of its four squares), so it is a boundary node with value $M$. This is the slide's "propagates the value to the boundary".</li>
<li><em>Between the nodes.</em> On each square $\class{ntn-Ue}{U_\eps}$ is bilinear, so by @lem:bilinear-extrema-are-at-corners $\class{ntn-Ue}{U_\eps}(x,y)$ is at most its largest corner value, which is at most $M$.</li>
<li>Hence $\class{ntn-Ue}{U_\eps}\le M=g(\text{some boundary node})\le\max_{\class{ntn-B}{B}}g$.</li>
<li><em>Minimum.</em> The equations are linear, so $-\class{ntn-Ue}{U_\eps}$ is the discrete solution for data $-g$. Steps 1–3 give $-\class{ntn-Ue}{U_\eps}\le\max_{\class{ntn-B}{B}}(-g)=-\min_{\class{ntn-B}{B}}g$. <span class="qed">∎</span></li>
</ol>
:::
<p>Boundary nodes lie on $\class{ntn-dOm}{\partial\Omega}$ (@lem:nodes-and-the-boundary), so in particular $\min_{\class{ntn-dOm}{\partial\Omega}}g\le \class{ntn-Ue}{U_\eps}\le\max_{\class{ntn-dOm}{\partial\Omega}}g$.</p>
