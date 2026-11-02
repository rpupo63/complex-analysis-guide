---
id: k2
slide: Slide 3
title: 'The identity theorem: proof'
---
::: proof {title="Proof, Step 2: $h\equiv0$ on $U$."}
Let $S:=\{z\in U:h\equiv0\text{ on some disk }\class{ntn-Dar}{D}(z,r)\subset U\}$.
<ul>
<li>$x\in S$, by Step 1 ($U$ is open, so some disk $\class{ntn-Dar}{D}(x,r)$ lies in $U$).</li>
<li>$S$ is open: if $h\equiv0$ on $\class{ntn-Dar}{D}(z,r)$, every $w\in \class{ntn-Dar}{D}(z,r)$ has the disk $\class{ntn-Dar}{D}(w,r-|w-z|)\subset \class{ntn-Dar}{D}(z,r)$ on which $h\equiv0$, so $\class{ntn-Dar}{D}(z,r)\subset S$.</li>
<li>$S$ is closed in $U$: let $z\in U$ be a limit of points $z_n\in S\setminus\{z\}$. Then $h(z_n)=0$, so $z$ is a limit of zeros $z_n\ne z$, and Step 1 (with $z$ in place of $x$) gives $h\equiv0$ on a disk $\class{ntn-Dar}{D}(z,r)\subset U$: $z\in S$.</li>
</ul>
As $U$ is connected, the nonempty, open and closed set $S$ is all of $U$.
:::
::: example {#eg:for-all-here-and-are}
$\sin2z=2\sin z\cos z$ for all $z\in\mathbb C$. Here $\sin z:=\frac{e^{iz}-e^{-iz}}{2i}$ and $\cos z:=\frac{e^{iz}+e^{-iz}}2$ are entire (power series with infinite radius, [A.19](apx:A19)). Both sides are entire, and they agree on $\R$, which contains a sequence such as $\frac1n\to0$. @thm:identity-theorem-l10 does the rest.
:::
<p>This is how every real identity between entire functions (addition formulas, $\sin^2+\cos^2=1$, and so on) passes to $\mathbb C$ at no cost; @prop:gluing-and-uniqueness says it again.</p>
