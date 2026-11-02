---
label: ex:one-real-zero
source: Practice midterm 3, Problem 3
title: one real zero
placement: m10
order: 6
---
Show that $p(z)=z^4+6z+3$ has exactly one zero in $D(0,1)$, counted with multiplicity, and that this zero is real.
<details class="sol"><summary>Hint</summary>
Compare $p$ with $6z$ on $|z|=1$. For "real": coefficients are real, so non-real zeros come in conjugate pairs.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>Rouché.</em> On $|z|=1$, $|p-6z|=|z^4+3|\le4\lt6=|6z|$. By @thm:rouche (with $f=6z$, $g=p$), $p$ has as many zeros in $D(0,1)$ as $6z$: exactly one.</li>
<li><em>Real.</em> $p(-1)=1-6+3=-2\lt0$ and $p(0)=3\gt0$, so $p$ has a real zero in $(-1,0)\subset D(0,1)$ (intermediate value theorem, [A.24](apx:A24)). It is the only one. (Alternatively: $p$ has real coefficients, so $\overline{p(z)}=p(\bar z)$; a non-real zero $z_0$ in the disk would bring $\bar z_0\ne z_0$, giving two.)</li>
</ol>
</details>
