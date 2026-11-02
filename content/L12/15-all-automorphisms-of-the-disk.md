---
id: n15
slide: Slide 16
title: All automorphisms of the disk
---

::: theorem {#thm:automorphisms-of-the-disk name="automorphisms of the disk"}
The automorphisms of $D(0,1)$ are exactly the maps $z\mapsto e^{i\theta}\varphi_a(z)$, with $\theta\in\R$ and $|a|\lt1$.
:::
::: proof

<ol>
<li><em>These are automorphisms:</em> by @lem:is-an-automorphism-of-with, followed by the rotation $w\mapsto e^{i\theta}w$.</li>
<li><em>Move the problem to $0$.</em> Let $\varphi$ be an automorphism and $a:=\varphi^{-1}(0)$. Then $\psi:=\varphi\circ\varphi_a$ is an automorphism with $\psi(0)=\varphi(a)=0$, and so is $\psi^{-1}$ (holomorphic by @thm:inverse), also fixing $0$.</li>
<li><em>Schwarz both ways.</em> @thm:schwarz-lemma for $\psi$ and for $\psi^{-1}$ gives
\[ |\psi(z)|\le|z|\qquad\text{and}\qquad|z|=|\psi^{-1}(\psi(z))|\le|\psi(z)|. \]
So $|\psi(z)|=|z|$ for every $z$, and by the equality case $\psi(z)=e^{i\theta}z$.</li>
<li><em>Undo the move.</em> As $\varphi_a\circ\varphi_a=\mathrm{id}$, $\varphi=\psi\circ\varphi_a=e^{i\theta}\varphi_a$. <span class="qed">∎</span></li>
</ol>
:::
