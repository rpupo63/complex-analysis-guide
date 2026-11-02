---
id: t5
slide: Slide 5
title: The maximum principle, and uniqueness
toc: Maximum principle and uniqueness
---
<p>Here $C^2(\Omega)\cap C(\overline\Omega)$ means: twice continuously differentiable inside $\Omega$, and continuous up to and including the boundary ([function classes](apx:D1)).</p>

::: corollary {#cor:maximum-principle name="maximum principle"}
Let $\Omega$ be bounded and open, and $h\in C^2(\Omega)\cap C(\overline\Omega)$ harmonic. Then $\max_{\overline\Omega}h=\max_{\class{ntn-dOm}{\partial\Omega}}h$ and $\min_{\overline\Omega}h=\min_{\class{ntn-dOm}{\partial\Omega}}h$.
:::
::: proof

<ol>
<li><em>The maximum exists.</em> $\overline\Omega$ is closed and bounded, hence [compact](apx:C5), and $h$ is continuous on it. By the extreme value theorem it attains its maximum $M$ at some $z_0\in\overline\Omega$. The boundary $\class{ntn-dOm}{\partial\Omega}$ is also compact and nonempty ([compact sets](apx:C5), part (c)), so $\max_{\class{ntn-dOm}{\partial\Omega}}h$ exists, and it is at most $M$ because $\class{ntn-dOm}{\partial\Omega}\subset\overline\Omega$. It remains to find a boundary point where $h=M$.</li>
<li><em>If $z_0\in\class{ntn-dOm}{\partial\Omega}$</em>, we are done.</li>
<li><em>If $z_0\in\Omega$</em>, let $\Omega'$ be the [connected component](apx:C4) of $\Omega$ containing $z_0$. It is open and connected, $h$ is harmonic on it, and $h(z_0)=M\ge\sup_{\Omega'}h$. By @thm:strong-maximum-principle, $h\equiv M$ on $\Omega'$.</li>
<li><em>Carry the value to the boundary.</em> $\Omega'$ is bounded and nonempty, so it has a boundary point $p$ ([compact sets](apx:C5), part (c)). Since $h$ is continuous on $\overline\Omega$ and $p$ is a limit of points of $\Omega'$ where $h=M$, also $h(p)=M$.</li>
<li><em>$p$ lies on $\class{ntn-dOm}{\partial\Omega}$.</em> $p$ is in the closure of $\Omega'$, hence of $\Omega$. Suppose $p\in\Omega$. Then a small disk $D$ about $p$ lies in $\Omega$. That disk is connected and, since $p$ is a boundary point of $\Omega'$, it meets $\Omega'$. So $\Omega'\cup D$ is connected, and by maximality of the component, $D\subset\Omega'$; then $p\in\Omega'$, which is impossible for a boundary point of the open set $\Omega'$. So $p\notin\Omega$, i.e. $p\in\overline\Omega\setminus\Omega=\class{ntn-dOm}{\partial\Omega}$. This is the slide's "$\class{ntn-dOm}{\partial\Omega}'$ is a nonempty part of $\class{ntn-dOm}{\partial\Omega}$".</li>
<li>So $\max_{\class{ntn-dOm}{\partial\Omega}}h\ge h(p)=M$, and the maximum statement holds.</li>
<li><em>Minimum.</em> $-h$ is also harmonic and in the same class. Its maximum statement reads $\max_{\overline\Omega}(-h)=\max_{\class{ntn-dOm}{\partial\Omega}}(-h)$, which is $-\min_{\overline\Omega}h=-\min_{\class{ntn-dOm}{\partial\Omega}}h$. <span class="qed">∎</span></li>
</ol>
:::

::: corollary {#cor:stability name=stability}
If $h_1,h_2\in C^2(\Omega)\cap C(\overline\Omega)$ are harmonic on a bounded open $\Omega$, then
\[ \max_{\overline\Omega}|h_1-h_2|=\max_{\class{ntn-dOm}{\partial\Omega}}|h_1-h_2|. \]
In particular, if $h_1=h_2$ on $\class{ntn-dOm}{\partial\Omega}$ then $h_1=h_2$ on $\Omega$.
:::
::: proof
Put $w:=h_1-h_2$. The Laplacian is linear, so $\class{ntn-Delta}{\Delta} w=\class{ntn-Delta}{\Delta} h_1-\class{ntn-Delta}{\Delta} h_2=0$, and $w$ is in the same class. For any $z\in\overline\Omega$, @cor:maximum-principle gives
\[ w(z)\le\max_{\class{ntn-dOm}{\partial\Omega}}w\le\max_{\class{ntn-dOm}{\partial\Omega}}|w|,\qquad -w(z)\le\max_{\overline\Omega}(-w)=\max_{\class{ntn-dOm}{\partial\Omega}}(-w)\le\max_{\class{ntn-dOm}{\partial\Omega}}|w|. \]
So $|w(z)|\le\max_{\class{ntn-dOm}{\partial\Omega}}|w|$ for every $z$, i.e. $\max_{\overline\Omega}|w|\le\max_{\class{ntn-dOm}{\partial\Omega}}|w|$. The reverse inequality holds because $\class{ntn-dOm}{\partial\Omega}\subset\overline\Omega$. If $h_1=h_2$ on $\class{ntn-dOm}{\partial\Omega}$, the right side is $0$, so $w\equiv0$.
:::
<p>"Stability" means: boundary data that are close (within $\delta$ everywhere on $\class{ntn-dOm}{\partial\Omega}$) give solutions that are close (within $\delta$ everywhere in $\Omega$). The uniqueness half reproves @thm:uniqueness of Lecture 2, which used energy and needed $h_1,h_2\in C^2(\overline\Omega)$; here continuity up to the boundary is enough. @cor:uniqueness-again was its discrete version.</p>
