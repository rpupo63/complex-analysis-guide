---
id: n13
slide: Slide 14
title: Automorphisms of the disk
---

::: definition {#def:automorphism-varphi-a name="automorphism; $\varphi_a$"}
An <em>automorphism</em> of $D(0,1)$ is a conformal map of $D(0,1)$ onto itself. For $|a|\lt1$ let
\[ \varphi_a(z):=\frac{a-z}{1-\bar az}. \]
:::

::: lemma {#lem:is-an-automorphism-of-with}
$\varphi_a$ is an automorphism of $D(0,1)$, with $\varphi_a(0)=a$, $\varphi_a(a)=0$, and $\varphi_a\circ\varphi_a=\mathrm{id}$.
:::
::: proof

<ol>
<li><em>Holomorphic near the closed disk.</em> The only pole is $z=1/\bar a$, with $|1/\bar a|\gt1$ (none if $a=0$, when $\varphi_0(z)=-z$). So $\varphi_a$ is holomorphic on $|z|\lt1/|a|$, which contains $\overline{D(0,1)}$.</li>
<li><em>Modulus $1$ on the circle.</em> For $|z|=1$, $z\bar z=1$, so $1-\bar az=z\bar z-\bar az=z(\bar z-\bar a)$, and $|1-\bar az|=|\bar z-\bar a|=|a-z|$. Hence $|\varphi_a(z)|=1$.</li>
<li><em>Into the disk.</em> By maximum modulus (@lem:maximum-modulus), $|\varphi_a|\le1$ on the closed disk; and $|\varphi_a|\lt1$ inside, since a non-constant holomorphic function has no interior maximum of its modulus (@rem:maximum-modulus-again).</li>
<li><em>Values.</em> $\varphi_a(0)=a$ and $\varphi_a(a)=0$ by substitution.</li>
<li><em>Its own inverse.</em> Multiply numerator and denominator of $\varphi_a(\varphi_a(z))=\frac{a-\varphi_a(z)}{1-\bar a\varphi_a(z)}$ by $1-\bar az$:
\[ \varphi_a(\varphi_a(z))=\frac{a(1-\bar az)-(a-z)}{(1-\bar az)-\bar a(a-z)}=\frac{(1-|a|^2)\,z}{1-|a|^2}=z. \]
So $\varphi_a$ maps the disk into itself and is its own inverse there: a bijection, holomorphic both ways. <span class="qed">∎</span></li>
</ol>
:::
<p>So the disk "looks the same from every point": any point $a$ can be moved to the centre by an automorphism. That is what makes the disk a good standard model.</p>
