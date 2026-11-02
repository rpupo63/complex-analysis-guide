---
id: o6
slide: Slide 7
title: 'Counting: examples'
---

::: example {#eg:z-d-on-the-disk name="$z^d$ on the disk"}
$z^d$ on $D(0,1)$ has $|z^d|\to1$ at the boundary and a zero of order $d$ at $0$. Each $w\ne0$ has $d$ distinct $d$-th roots, and $w=0$ is a zero of order $d$: every value is taken $d$ times, as @prop:counting says.
:::

::: example {#eg:blaschke-products name="Blaschke products" status=derived}
For $|a_1|,\dots,|a_d|\lt1$, the <em>Blaschke product</em>
\[ B(z):=\prod_{k=1}^d\frac{z-a_k}{1-\bar a_kz} \]
has $|B|=1$ on $|z|=1$ and zeros $a_1,\dots,a_d$. So $B(z)=w$ has exactly $d$ solutions in $D(0,1)$ for every $|w|\lt1$.
:::
::: proof
Each factor is $-\varphi_{a_k}$, holomorphic near the closed disk with modulus $1$ on the circle (@lem:is-an-automorphism-of-with). So $B$ is continuous on the closed disk with $|B|=1$ on the circle, hence $|B(z)|\to1$ as $|z|\to1$. Apply @prop:counting.
:::

::: corollary {#cor:a-non-constant-holomorphic-on}
A non-constant holomorphic $f$ on a bounded connected open set $\Omega$, with $|f|\to1$ at $\partial\Omega$, has a zero.
:::
::: proof
$d\ge1$ in @prop:counting.
:::
