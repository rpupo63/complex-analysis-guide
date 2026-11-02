---
id: n7
slide: Slide 8
title: The open mapping theorem
---

::: theorem {#thm:open-mapping name="open mapping"}
Let $f$ be holomorphic and not constant on a connected open set $U$. Then $f(U)$ is open.
:::
<p>That is: if $w_0=f(z_0)$, every $w$ close enough to $w_0$ is also a value of $f$. This fails for real functions: $x^2$ takes the value $0$ but no value $\lt0$. In contrast, every $w\in\mathbb C$ is a value of $z^2$.</p>
::: proof
Let $z_0\in U$ and $w_0:=f(z_0)$. If all Taylor coefficients of $f-w_0$ at $z_0$ vanished, $f\equiv w_0$ on a disk about $z_0$, hence on $U$ by the identity theorem (@thm:identity-theorem-l10): but $f$ is not constant. So $f-w_0$ has a zero of finite order $m\ge1$ at $z_0$, and by @thm:local-behaviour, $D(w_0,\delta)\subseteq f(D(z_0,r))\subseteq f(U)$ for some $\delta\gt0$.
:::

::: remark {#rem:maximum-modulus-again name="maximum modulus, again"}
If $|f|$ had a maximum at an interior point $z_0$, then $f(U)$ would contain a disk about $f(z_0)$, which contains points of larger modulus. So a non-constant holomorphic function on a connected open set has no interior maximum of $|f|$. This is a second proof of @lem:maximum-modulus, and it is used that way in @sec:n13–@sec:n14 and @sec:o5.
:::
