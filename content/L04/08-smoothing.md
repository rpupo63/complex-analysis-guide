---
id: t9
slide: Slide 9
title: 'Weyl''s lemma: smoothing'
toc: Smoothing
---
<p>From here to @sec:t10, $u$ is any function in $L^2(\Omega)$ satisfying the hypothesis of Weyl's lemma.</p>

::: definition {#def:defined-on-def-4-5}
$\class{ntn-ud}{u_\delta}:=u\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}$, defined on $\class{ntn-Omd}{\Omega_\delta}$ (@def:the-shrunken-domain-and-convolution). The integral exists: it is $\iint u(\zeta)\,\class{ntn-chid}{\chi_\delta}(z-\zeta)\,dA(\zeta)$ over the disk of radius $\delta$ about $z$ (the weight $\class{ntn-chid}{\chi_\delta}(z-\cdot)$, the function $\zeta\mapsto\class{ntn-chid}{\chi_\delta}(z-\zeta)$, is zero elsewhere), and Cauchy–Schwarz bounds it by $\norm{u}\,\norm{\class{ntn-chid}{\chi_\delta}}$.
:::

::: proposition {#prop:u-delta-is-smooth name="$\class{ntn-ud}{u_\delta}$ is smooth"}
$\class{ntn-ud}{u_\delta}$ is smooth on $\class{ntn-Omd}{\Omega_\delta}$, and its derivatives are obtained by differentiating $\class{ntn-chid}{\chi_\delta}$:
\[ \partial^\alpha \class{ntn-ud}{u_\delta}(z)=\iint u(\zeta)\,\partial_z^\alpha\big[\class{ntn-chid}{\chi_\delta}(z-\zeta)\big]\,dA(\zeta)\quad\text{for every partial derivative }\partial^\alpha. \]
:::
::: proof
In $\class{ntn-ud}{u_\delta}(z)=\iint u(\zeta)\class{ntn-chid}{\chi_\delta}(z-\zeta)\,dA(\zeta)$ the variable $z$ appears only inside the smooth weight. Fix $z_1\in\class{ntn-Omd}{\Omega_\delta}$. Since $\class{ntn-Omd}{\Omega_\delta}$ is open ([C.5](apx:C5)), there is $\rho\gt0$ such that for all $z$ within $\rho$ of $z_1$ the weight $\class{ntn-chid}{\chi_\delta}(z-\cdot)$ is zero outside one fixed compact disk $B\subset\Omega$, of radius $\delta+\rho$ about $z_1$. On $B$, $u$ is integrable (Cauchy–Schwarz with the function $1$), and every $z$-derivative of $\class{ntn-chid}{\chi_\delta}(z-\zeta)$ is continuous and bounded. Under these conditions [differentiation under the integral sign](apx:A4) is allowed, and since the result has the same form, it can be repeated any number of times.
:::

::: proposition {#prop:u-delta-is-harmonic name="$\class{ntn-ud}{u_\delta}$ is harmonic"}
$\class{ntn-Delta}{\Delta} \class{ntn-ud}{u_\delta}=0$ on $\class{ntn-Omd}{\Omega_\delta}$.
:::
::: proof
Fix $z\in\class{ntn-Omd}{\Omega_\delta}$ and put $\eta(\zeta):=\class{ntn-chid}{\chi_\delta}(z-\zeta)$.
<ol>
<li><em>$\eta$ is a test function.</em> It is smooth, and it vanishes outside the closed disk of radius $\delta$ about $z$, which is a compact subset of $\Omega$ because $z\in\class{ntn-Omd}{\Omega_\delta}$.</li>
<li><em>$\class{ntn-Delta}{\Delta}_z$ and $\class{ntn-Delta}{\Delta}_\zeta$ agree on a function of $z-\zeta$.</em> Write $\phi:=\class{ntn-chid}{\chi_\delta}$ and look at $\phi(z-\zeta)$. Differentiating in the first coordinate of $z$ gives $(\partial_1\phi)(z-\zeta)$; in the first coordinate of $\zeta$ it gives $-(\partial_1\phi)(z-\zeta)$, by the chain rule. Differentiating twice, the minus sign appears twice and cancels: both give $(\partial_1^2\phi)(z-\zeta)$. The same holds in the second coordinate. So $\class{ntn-Delta}{\Delta}_z[\class{ntn-chid}{\chi_\delta}(z-\zeta)]=\class{ntn-Delta}{\Delta}_\zeta[\class{ntn-chid}{\chi_\delta}(z-\zeta)]=\class{ntn-Delta}{\Delta}\eta(\zeta)$.</li>
<li><em>Combine.</em> By @prop:u-delta-is-smooth and Step 2,
\[ \class{ntn-Delta}{\Delta} \class{ntn-ud}{u_\delta}(z)=\iint u(\zeta)\,\class{ntn-Delta}{\Delta}_z\big[\class{ntn-chid}{\chi_\delta}(z-\zeta)\big]\,dA(\zeta)=\iint u\,\class{ntn-Delta}{\Delta}\eta\,dA=0, \]
the last step being the hypothesis of Weyl's lemma applied to the test function $\eta$. <span class="qed">∎</span></li>
</ol>
:::

::: fact {#fact:smoothing name=smoothing status=cited class=def}
If $u\in L^2(\Omega)$, then $u\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}\to u$ in $L^2(K)$ ([$L^2$ on $K$](apx:D2)) as $\delta\to0$, for every compact $K\subset\Omega$. (For small $\delta$, $K\subset\class{ntn-Omd}{\Omega_\delta}$, so $u\class{ntn-conv}{*}\class{ntn-chid}{\chi_\delta}$ is defined on $K$.) The slides state this as a standard fact; see [mollifiers](apx:D5).
:::
<p>So $\class{ntn-ud}{u_\delta}$ is a smooth harmonic function that approximates $u$. The remaining question is whether these approximations settle down to a single function as $\delta\to0$. @sec:t10 shows they do not change at all.</p>
