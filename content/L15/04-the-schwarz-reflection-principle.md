---
id: q4
slide: Slide 5
title: The Schwarz reflection principle
---

::: theorem {#thm:schwarz-reflection name="Schwarz reflection principle"}
In @set:a-symmetric-open-set, let $f$ be holomorphic on $\Omega^+$, continuous on $\Omega^+\cup I$, and real on $I$. Define $F:=f$ on $\Omega^+\cup I$ and $F(z):=\overline{f(\bar z)}$ on $\Omega^-$. Then $F$ is holomorphic on $\Omega$, and $F(\bar z)=\overline{F(z)}$.
:::
::: proof

<ol>
<li><em>On $\Omega^-$.</em> $F$ is holomorphic there: its difference quotients at $z$ are the conjugates of those of $f$ at $\bar z$.</li>
<li><em>A holomorphic $G$ near a point of $I$.</em> Let $x\in I$. By @thm:harmonic-reflection, $\operatorname{Im}f$ extends to a function $V$ harmonic on $\Omega$, with $V(\bar z)=-V(z)$. Let $D\subseteq\Omega$ be a disk about $x$. By @lem:harmonic-conjugate-on-a-disk, $V=\operatorname{Re}H$ with $H$ holomorphic on $D$; then $G:=iH$ is holomorphic on $D$ with $\operatorname{Im}G=V$.</li>
<li><em>$f=G$ on the upper half $D^+$.</em> $\operatorname{Im}(f-G)=0$ on $D^+$, so $f-G$ takes values in $\mathbb R$, which is not open. $D^+$ is connected, so by the open mapping theorem (@thm:open-mapping) $f-G$ is a real constant. Adding it to $G$ does not change $\operatorname{Im}G$. Now $f=G$ on $D^+$.</li>
<li><em>$G$ is symmetric.</em> $K(z):=\overline{G(\bar z)}-G(z)$ is holomorphic on $D$ (step 1 again), with imaginary part $-V(\bar z)-V(z)=0$. So $K$ is a real constant (@thm:open-mapping), and $K(x)=\overline{G(x)}-G(x)=-2iV(x)=0$. Hence $G(\bar z)=\overline{G(z)}$.</li>
<li><em>$F=G$ on $D$.</em> On $D^-$, $F(z)=\overline{f(\bar z)}=\overline{G(\bar z)}=G(z)$. On $D\cap\mathbb R$, $F=f=G$ by continuity of $f$ and $G$ from $D^+$. So $F$ is holomorphic near $x$. <span class="qed">∎</span></li>
</ol>
:::
