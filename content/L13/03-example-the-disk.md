---
id: o3
slide: Slide 4
title: 'Example: the disk'
---

::: example {#eg:the-riemann-map-of-the-disk name="the Riemann map of the disk at $a$" status=derived}
For $\Omega=D(0,1)$ and $z_0=a$, the Riemann map is $f(z)=\dfrac{z-a}{1-\bar az}=-\varphi_a(z)$.
:::
::: proof
Follow @prop:what-a-riemann-map-must-look.
<ol>
<li><em>The Dirichlet problem.</em> For $|z|=1$, $|z-a|=|1-\bar az|$ (step 2 of @lem:is-an-automorphism-of-with). So $h(z):=\log|1-\bar az|$ has the right boundary values. It is harmonic on the disk because $1-\bar az$ is holomorphic with no zeros on $|z|\lt1/|a|$ (@lem:if-is-holomorphic-and-zero), and continuous on the closed disk.</li>
<li><em>The modulus.</em> $|f(z)|=|z-a|e^{-h(z)}=\Big|\dfrac{z-a}{1-\bar az}\Big|$.</li>
<li><em>The map.</em> $\frac{z-a}{1-\bar az}=-\varphi_a(z)$ is an automorphism (@lem:is-an-automorphism-of-with) with this modulus and value $0$ at $a$, and its derivative at $a$ is $\frac1{1-|a|^2}\gt0$. By uniqueness it is the Riemann map. <span class="qed">∎</span></li>
</ol>
:::
