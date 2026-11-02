---
id: C8
title: The principal logarithm, powers and roots
status:
- defined
- cited
---
<p>For $z\ne0$ write $z=re^{i\theta}$ with $r=|z|$ and $-\pi\lt\theta\le\pi$; this $\theta$ is the <em>principal argument</em> $\operatorname{Arg}z$. The <em>principal logarithm</em> is $\log z:=\log r+i\theta$ (one branch of [E.3](apx:E3)). It satisfies $e^{\log z}=z$, and it is holomorphic on $\mathbb C\setminus(-\infty,0]$ with derivative $1/z$.</p>
<ul>
<li><em>Series.</em> For $|w|\lt1$, $1-w$ lies in the right half-plane, and $-\log(1-w)=\sum_{m\ge1}\frac{w^m}m$. Proof: both sides are holomorphic on $|w|\lt1$, with derivative $\frac1{1-w}=\sum w^{m-1}$ ([A.19](apx:A19)), and both vanish at $w=0$.</li>
<li><em>Powers.</em> For $t\gt0$ and complex $z$, $t^z:=e^{z\log t}$ with the real logarithm; then $|t^z|=t^{\operatorname{Re}z}$. For complex $\tau$ off $(-\infty,0]$, the principal square root is $\sqrt\tau:=e^{\frac12\log\tau}$; it has positive real part.</li>
<li><em>Caution.</em> $\log(zw)=\log z+\log w$ can fail by $2\pi i$ when the arguments add up beyond $(-\pi,\pi]$. In @sec:f18, $\sqrt{t(1-is)}=\sqrt t\sqrt{1-is}$ is safe because $t\gt0$ adds nothing to the argument.</li>
</ul>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Complex_logarithm#Principal_value" target="_blank" rel="noopener">Principal value of the logarithm</a> · <a href="https://en.wikipedia.org/wiki/Square_root#Principal_square_root_of_a_complex_number" target="_blank" rel="noopener">Principal square root</a></p>
