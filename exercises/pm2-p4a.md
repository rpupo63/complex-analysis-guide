---
label: ex:the-slit-plane-onto-the-disk
source: Practice midterm 2, Problem 4(a)
title: the slit plane onto the disk
placement: n11
order: 2
---
Find a conformal map $F$ of the slit plane $\Omega:=\mathbb C\setminus(-\infty,0]$ onto $D(0,1)$.
<details class="sol"><summary>Hint</summary>
A square root maps $\Omega$ onto the right half-plane $\{\operatorname{Re}w\gt0\}$. Which Möbius map sends the right half-plane to the disk?
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li>The principal square root $\sqrt z=\sqrt r\,e^{i\theta/2}$ ($z=re^{i\theta}$, $-\pi\lt\theta\lt\pi$; [C.8](apx:C8)) is a bijection of $\Omega$ onto $\{\operatorname{Re}w\gt0\}$: arguments in $(-\pi,\pi)$ go to $(-\frac\pi2,\frac\pi2)$. It is holomorphic: it is the inverse of the injective holomorphic map $w\mapsto w^2$ on the right half-plane, so @thm:inverse applies (or see [C.8](apx:C8)).</li>
<li>$w\mapsto\frac{w-1}{w+1}$ maps the right half-plane onto the disk: $|w-1|\lt|w+1|\iff\operatorname{Re}w\gt0$ (closer to $1$ than to $-1$), and it is invertible, $w=\frac{1+\zeta}{1-\zeta}$, as in @prop:cayley-map. (It is the Cayley map after rotating by $i$.)</li>
</ol>
So $F(z)=\dfrac{\sqrt z-1}{\sqrt z+1}$, a composition of conformal maps, hence conformal (@def:conformal-map).
</details>
