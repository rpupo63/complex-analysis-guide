---
label: ex:modulus-one-on-the-circle
source: Homework 3, Problem 6
title: modulus one on the circle
placement: j6
order: 3
---
Let $f$ be holomorphic on a neighborhood of the closed disk $\{|z|\le 1\}$, with $|f(z)|=1$ whenever $|z|=1$. In the following steps we prove that
\[ f(z)=\lambda\prod_{k=1}^m\frac{z-a_k}{1-\bar a_k z} \]
for some constant $\lambda$ with $|\lambda|=1$ and points $a_1,\dots,a_m\in D(0,1)$ (the case $m=0$, where the product is $1$, is allowed).
<ol type="a">
<li>Let $g$ be holomorphic on a neighborhood of the closed disk, with $|g(z)|=1$ whenever $|z|=1$ and with no zeros in $D(0,1)$. Since $|g|=1$ on the unit circle, $g$ has no zeros on the closed disk, so $1/g$ is holomorphic on a neighborhood of the closed disk. Apply the maximum modulus principle to $g$ to show that $|g(z)|\le 1$ for $z\in D(0,1)$, and to $1/g$ to show that $|g(z)|\ge 1$ for $z\in D(0,1)$.</li>
<li>Show that a holomorphic function on $D(0,1)$ whose modulus is constant is itself constant.</li>
<li>For a point $a\in D(0,1)$, let $\varphi_a(z)=(z-a)/(1-\bar a z)$. Show that $\varphi_a$ is holomorphic on a neighborhood of the closed disk, that its only zero there is a simple zero at $z=a$, and that $|\varphi_a(z)|=1$ when $|z|=1$.</li>
<li>Show that $f$ has only finitely many zeros in $D(0,1)$.</li>
<li>Let $a_1,\dots,a_m$ be the zeros of $f$ in $D(0,1)$, each listed as many times as its multiplicity, and let $B(z)=\varphi_{a_1}(z)\cdots\varphi_{a_m}(z)$. Show that $f/B$ extends to a function $g$ that is holomorphic on a neighborhood of the closed disk, has no zeros in $D(0,1)$, and has modulus $1$ on the unit circle. Apply (a) and (b) to $g$ to finish the proof.</li>
</ol>
<details class="sol"><summary>Hint</summary>
(a) is @lem:maximum-modulus, applied to $g$ and to $1/g$. (b) turns a constant modulus into a harmonic function that attains its maximum. (c) is a direct computation on $|z|=1$, where $\bar z=1/z$. (d) is @thm:isolated-zeros. (e) divides the zeros out by @prop:factorization-in-a-disk.
</details>
<details class="sol"><summary>Solution</summary>
<ol type="a">
<li>By @lem:maximum-modulus, $|g(z)|\le\max_{|z|=1}|g|=1$ for $|z|\le1$. The same lemma applied to $1/g$ gives $|1/g|\le1$ on the disk, so $|g|\ge1$. Thus $|g|=1$ on $D(0,1)$.</li>
<li>Let $|f|\equiv c$ on $D(0,1)$. If $c=0$, then $f\equiv0$. If $c\gt0$, fix $z_0\in D(0,1)$ and choose a real $\alpha$ with $e^{-i\alpha}f(z_0)=c$. The real part $u$ of $e^{-i\alpha}f$ is harmonic (@cor:holomorphic-functions-are-smooth), and $u\le|f|=c$ with $u(z_0)=c$. By @thm:strong-maximum-principle, $u\equiv c$ on the connected set $D(0,1)$. Then the imaginary part of $e^{-i\alpha}f$ is $0$, because its square is $c^2-u^2$. So $e^{-i\alpha}f\equiv c$, and $f$ is constant.</li>
<li>If $a=0$, then $\varphi_0(z)=z$, which is entire, with a single simple zero at $0$, and $|\varphi_0|=1$ on $|z|=1$. If $a\ne0$, the denominator vanishes at $1/\bar a$, and $|1/\bar a|=1/|a|\gt1$. The distance from the closed unit disk to that point is $1/|a|-1\gt0$, so $\varphi_a$ is holomorphic on a neighborhood of $\{|z|\le1\}$. The numerator vanishes only at $a$, and the denominator there equals $1-|a|^2\ne0$, so $\varphi_a(z)=(z-a)h(z)$ with $h$ holomorphic and $h(a)\ne0$. By @def:zero-of-order-m this is a simple zero, and it is the only zero in that neighborhood. On $|z|=1$, $\bar z=1/z$, so
\[ |z-a|^2=(z-a)\Big(\frac1z-\bar a\Big)=\frac{(z-a)(1-\bar a z)}{z}, \]
and the same computation with $a$ and $\bar a$ exchanged gives $|1-\bar a z|^2=|z-a|^2$. Thus $|\varphi_a(z)|=1$.</li>
<li>$|f|=1$ on $|z|=1$, so $f$ has no zero on the circle, and $f\not\equiv0$. The zeros in the compact disk $|z|\le1$ are finite: an infinite set would have a limit point there ([C.5](apx:C5)), which would be a non-isolated zero, so $f\equiv0$ on the connected neighborhood of the disk by @thm:isolated-zeros. That limit point cannot lie on $|z|=1$ either, because $|f|=1$ there.</li>
<li>By @prop:factorization-in-a-disk, applied on $|z|\le1$ (no zeros on the circle), $f(z)=\prod_{k=1}^m(z-a_k)\,q(z)$ with $q$ holomorphic and zero-free near the closed disk. Each factor $1-\bar a_k z$ is holomorphic and non-zero on a neighborhood of the closed disk, as in (c). So
\[ \frac fB=q(z)\prod_{k=1}^m(1-\bar a_k z) \]
extends to a holomorphic zero-free function $g$ on that neighborhood. On $|z|=1$, $|\varphi_{a_k}|=1$ by (c), so $|B|=1$ and $|g|=|f|=1$. By (a), $|g|=1$ on $D(0,1)$. By (b), $g$ is constant. The constant $\lambda$ has $|\lambda|=1$, and $f=\lambda B$. If $m=0$, then $B=1$ and $f$ itself is the constant.</li>
</ol>
</details>
