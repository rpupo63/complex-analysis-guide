---
label: ex:square-root-of-cosine
source: Homework 3, Problem 9
title: a square root of $\cos z$
placement: p4
order: 1
---
For which $r\gt0$ is there a holomorphic function $g$ on $D(0,r)$ with $g(z)^2=\cos z$ for all $z\in D(0,r)$?
<details class="sol"><summary>Hint</summary>
If $\cos z$ has no zeros in $D(0,r)$, the disk is simply connected, so $\cos z$ has a holomorphic logarithm (@cor:logarithms-and-square-roots). If it has a zero in $D(0,r)$, compare the order of that zero with the order of a square.
</details>
<details class="sol"><summary>Solution</summary>
<p>Such a $g$ exists if and only if $r\le\pi/2$.</p>
<ol>
<li><em>The zeros of $\cos$.</em> As in @eg:for-all-here-and-are, $\cos z=(e^{iz}+e^{-iz})/2$ and $\sin z=(e^{iz}-e^{-iz})/(2i)$, so $\cos'z=-\sin z$. Then $\cos z=0$ if and only if $e^{2iz}=-1$. For $w=u+iv$, $|e^w|=e^u$ (since $e^{iv}=\cos v+i\sin v$ by the series in [A.19](apx:A19), and $\cos^2v+\sin^2v=1$). So $e^w=-1$ forces $u=0$ and $\cos v=-1$, $\sin v=0$, hence $v=(2k+1)\pi$. The solutions are $z=\pi/2+\pi k$. The nearest to $0$ are $\pm\pi/2$, of modulus $\pi/2$. At each of them $\sin(\pi/2+\pi k)=(-1)^k\ne0$, so the zero has order $1$ (@def:zero-of-order-m).</li>
<li><em>No zero in the disk: $r\le\pi/2$.</em> Then $\cos$ has no zero in $D(0,r)$. A disk is simply connected (@def:simply-connected). By @cor:logarithms-and-square-roots there is a holomorphic $G$ on $D(0,r)$ with $\cos z=e^{G(z)}$. Then $g:=e^{G/2}$ is holomorphic and $g^2=\cos z$.</li>
<li><em>A zero in the disk: $r\gt\pi/2$.</em> Then $\pi/2\in D(0,r)$, a zero of order $1$. Suppose $g^2=\cos z$ with $g$ holomorphic. At a zero of $g$ of order $m\ge1$, the Taylor series of $g$ starts with degree $m$, so the series of $g^2$ starts with degree $2m$ (@def:zero-of-order-m). The order would be even. Order $1$ is odd, so no such $g$ exists.</li>
</ol>
</details>
