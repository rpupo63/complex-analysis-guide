---
label: ex:injective-entire-functions
source: Homework 3, Problem 8
title: injective entire functions
placement: n16
order: 2
---
Let $f$ be an injective entire function. In the following steps we prove that $f(z)=az+b$ for some constants $a\ne0$ and $b$. Let $c=f(0)$. Since $f$ is injective, it is not constant.
<ol type="a">
<li>Use the open mapping theorem to show that there is an $r\gt0$ such that the disk $\{|w-c|\lt r\}$ is contained in $f(D(0,1))$.</li>
<li>Show that $|f(z)-c|\ge r$ for every $z$ with $|z|\ge 1$. Hint: if $|z|\ge 1$, can $f(z)$ lie in $f(D(0,1))$?</li>
<li>Since $f$ is injective, $z=0$ is the only zero of $f(z)-c$. Show that $f(z)-c=z^ku(z)$ for some integer $k\ge 1$ and some entire function $u$ with no zeros at all.</li>
<li>The function $h=1/u$ is entire, and $h(z)=z^k/(f(z)-c)$ for $z\ne0$. Show that $|h(z)|\le|z|^k/r$ for $|z|\ge 1$.</li>
<li>Use Cauchy's estimates, as in Homework 3, Problem 4, to show that $h$ is a polynomial of degree at most $k$. Since $h$ has no zeros, conclude that $h$ is constant.</li>
<li>Deduce that $f(z)=c+az^k$ for some $a\ne0$. Use injectivity to show that $k=1$.</li>
</ol>
<details class="sol"><summary>Hint</summary>
(a) is @thm:open-mapping. (c) removes the zero at $0$ by @lem:removable-singularities. (e) is @cor:cauchys-estimate, as in @ex:entire-functions-of-square-root-growth, and then @cor:fundamental-theorem-of-algebra.
</details>
<details class="sol"><summary>Solution</summary>
<ol type="a">
<li>$f(D(0,1))$ is open by @thm:open-mapping, since $f$ is holomorphic and not constant on the connected set $D(0,1)$. The point $c=f(0)$ is therefore an interior point: some disk $\{|w-c|\lt r\}$ lies in $f(D(0,1))$.</li>
<li>Suppose $|z|\ge1$ and $|f(z)-c|\lt r$. Then $f(z)=f(z_1)$ for some $|z_1|\lt1$. Injectivity forces $z=z_1$, which is impossible. So $|f(z)-c|\ge r$.</li>
<li>Injectivity gives $f(z)=c$ only at $z=0$, so $0$ is the only zero of $f-c$. It is a zero ($f(0)=c$), and not of infinite order ($f$ is not constant), so the order $k$ is a finite integer $k\ge1$ (@thm:isolated-zeros: the Taylor coefficients are not all $0$). Then $(f(z)-c)/z^k$ is holomorphic on $\mathbb C\setminus\{0\}$ and bounded near $0$, because the Taylor series of $f-c$ at $0$ starts at degree $k$. By @lem:removable-singularities it extends to an entire function $u$, and $u(0)$ is the first non-zero coefficient, so $u(0)\ne0$. A zero of $u$ anywhere else would be a zero of $f-c$. So $u$ has no zeros, and $f(z)-c=z^ku(z)$.</li>
<li>$h:=1/u$ is entire because $u$ is entire and never $0$. For $z\ne0$, $h(z)=z^k/(f(z)-c)$. For $|z|\ge1$, step (b) gives $|h(z)|\le|z|^k/r$.</li>
<li>On the circle $|z|=R$ with $R\ge1$, $|h|\le R^k/r$. By @thm:power-series, $h(z)=\sum_na_nz^n$, and @cor:cauchys-estimate gives $|a_n|\le(R^k/r)R^{-n}$. For $n\gt k$ the right side tends to $0$ as $R\to\infty$, so $a_n=0$. Thus $h$ is a polynomial of degree at most $k$. A non-constant polynomial has a zero (@cor:fundamental-theorem-of-algebra). Since $h$ has no zeros, $h$ is constant.</li>
<li>$u=1/h$ is a non-zero constant $a$. So $f(z)=c+az^k$ with $a\ne0$. If $k\ge2$, then $1\ne e^{2\pi i/k}$ but $1^k=(e^{2\pi i/k})^k$, so $f(1)=f(e^{2\pi i/k})$, contradicting injectivity. Thus $k=1$, and $f(z)=az+c$.</li>
</ol>
</details>
