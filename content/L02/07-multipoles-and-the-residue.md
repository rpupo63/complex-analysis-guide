---
id: w7
slide: Slides 14–15
title: Multipoles and the residue
---

::: proposition {#prop:1-z-2-has-zero-charge name="$1/z^2$ has zero charge"}
$1/z^2$ is holomorphic on $\mathbb C\setminus\{0\}$ and singular at $0$, yet $\oint_{|z|=r}\frac{dz}{z^2}=0$. More generally $\oint_{|z-z_0|=r}\frac{dz}{(z-z_0)^m}=0$ for every integer $m\ge2$.
:::
::: proof
Holomorphic: as in @eg:a-charge-just-outside, the derivative is $-2/z^3$ for $z\ne0$. On the circle, $z=z_0+re^{i\theta}$ and $dz=ire^{i\theta}d\theta$, so
\[ \oint\frac{dz}{(z-z_0)^m}=\int_0^{2\pi}\frac{ire^{i\theta}}{r^me^{im\theta}}\,d\theta=i\,r^{1-m}\int_0^{2\pi}e^{i(1-m)\theta}\,d\theta=0, \]
since for an integer $k=1-m\ne0$, $\int_0^{2\pi}e^{ik\theta}d\theta=\int_0^{2\pi}(\cos k\theta+i\sin k\theta)\,d\theta=0$. With $m=2$ and $z_0=0$ this is the slide's $\frac ir\int_0^{2\pi}e^{-i\theta}d\theta=0$.
:::
<p>By Gauss's theorem, the <b>net charge</b> at $0$ is zero. What kind of singularity has zero total charge but a nonzero field?</p>

::: proposition {#prop:a-dipole name="a dipole"}
Put a charge $+q$ at $\delta$ and $-q$ at $0$, and let $\delta\to0$ with $q\delta=1$ fixed. Then for $z\ne0$
\[ \frac{q}{2\pi}\Big(\frac1{z-\delta}-\frac1z\Big)=\frac{q}{2\pi}\cdot\frac{\delta}{z(z-\delta)}\longrightarrow\frac1{2\pi}\cdot\frac1{z^2}. \]
:::
::: proof
Common denominator: $\frac1{z-\delta}-\frac1z=\frac{z-(z-\delta)}{z(z-\delta)}=\frac{\delta}{z(z-\delta)}$. Multiply by $\frac q{2\pi}$ and use $q\delta=1$: the expression is $\frac1{2\pi}\cdot\frac1{z(z-\delta)}$, which tends to $\frac1{2\pi z^2}$ as $\delta\to0$.
:::
<p>Two opposite charges, infinitely close and infinitely strong: total charge $0$, but a nonzero <em>dipole</em> charge distribution (a derivative of a delta) and hence a field nonetheless. Likewise $1/z^3$ is a quadrupole (two dipoles, merged the same way), and so on. Here $\delta$ is a small displacement, not the delta function.</p>

::: definition {#def:the-residue name="the residue"}
A singularity of $f$ at $z_0$ can be a whole combination of multipoles,
\[ \frac{\class{ntn-a1}{a_1}}{z-z_0}+\frac{a_2}{(z-z_0)^2}+\frac{a_3}{(z-z_0)^3}+\cdots, \]
plus a part holomorphic near $z_0$. The coefficient $\class{ntn-a1}{a_1}$ is the <em>residue</em> of $f$ at $z_0$. (That every isolated singularity has such an expansion is the theory of [Laurent series](apx:E5).)
:::

::: proposition {#prop:the-contour-integral-sees-only-the name="the contour integral sees only the residue"}
For $\gamma$ a small circle around $z_0$ (enclosing no other singularity), $\oint_\gamma f\,dz=2\pi i\,\class{ntn-a1}{a_1}$. If $\class{ntn-a1}{a_1}=\alpha+i\beta$, the net charge (flux) is $2\pi\alpha$ and the circulation is $-2\pi\beta$. For purely electric point charges $\class{ntn-a1}{a_1}$ is real, and the enclosed charge is $2\pi \class{ntn-a1}{a_1}$.
:::
::: proof
Integrate term by term (allowed when the series converges uniformly on the circle, [A.17](apx:A17)). The holomorphic part contributes $0$ (@cor:cauchys-theorem); the term $\class{ntn-a1}{a_1}/(z-z_0)$ contributes $2\pi i\,\class{ntn-a1}{a_1}$ (@cor:the-residue-theorem-point-charge-form); every term with $m\ge2$ contributes $0$ (@prop:1-z-2-has-zero-charge). So $\oint f\,dz=2\pi i(\alpha+i\beta)=-2\pi\beta+i\cdot2\pi\alpha$. Comparing with @prop:contour-integral-circulation-i-cdot-flux, $\text{circulation}+i\cdot\text{flux}$, the circulation is $-2\pi\beta$ and the flux $2\pi\alpha$. A point charge $q$ has $\class{ntn-a1}{a_1}=q/2\pi$ (@rem:consequence-the-singularity-is-the-charge), which is real, and then flux $=2\pi \class{ntn-a1}{a_1}=q$.
:::
