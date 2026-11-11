---
id: q2
slide: Slide 3
title: The method of images
---

::: example {#eg:a-charge-above-a-grounded-plane name="a charge above a grounded plane"}
A line charge at $a\in\mathbb H$ above the grounded conducting plane $\mathbb R$ has the potential $\log\frac1{|z-a|}$ ([E.6](apx:E6)). This is not $0$ on $\mathbb R$. Put a charge of the opposite sign at the mirror point $\bar a$:
\[ u(z)=\log\frac1{|z-a|}-\log\frac1{|z-\bar a|}=\log\left|\frac{z-\bar a}{z-a}\right|. \]
Then $u$ is harmonic on $\mathbb H\setminus\{a\}$ ($\bar a\notin\mathbb H$), it has the singularity of the charge at $a$, and it is $0$ on $\mathbb R$, because $|x-\bar a|=|x-a|$ for real $x$. The equipotentials $\{|z-\bar a|=c\,|z-a|\}$ are circles (circles of Apollonius), and their mirror images are the equipotentials of the image charge.
:::
<figure>{{fig:q2-1}}<figcaption>The charge at $a$ (blue) and its image at $\bar a$ (brown). The equipotentials of $u$ in $\mathbb H$ are circles around $a$; the dashed circles are their mirror images.</figcaption></figure>

::: example {#eg:a-charge-inside-a-grounded-circle name="a charge inside a grounded circle"}
For $a\in D(0,1)$, the image charge sits at the mirror point $1/\bar a$ of $a$ in the unit circle:
\[ u(z)=\log\left|\frac{1-\bar az}{z-a}\right|=-\log|\varphi_a(z)|. \]
This is $0$ on $|z|=1$, because $|\varphi_a|=1$ there (@lem:is-an-automorphism-of-with). For $a\ne0$, $1-\bar az=-\bar a\,(z-1/\bar a)$, so $u$ is the potential of the charge at $a$ and of an opposite charge at $1/\bar a$, plus the constant $\log|a|$.
:::

::: remark {#rem:greens-functions-of-h-and-d name="Green's functions"}
These two functions are the Green's functions of $\mathbb H$ and $D(0,1)$ with pole $a$. In Lecture 13 the Green's function of $\Omega$ is $-\log|f|$, with $f$ the conformal map of $\Omega$ onto $D(0,1)$ and $f(z_0)=0$ (@rem:greens-function). The second example is the case $\Omega=D(0,1)$, $f=\varphi_a$, $z_0=a$.
:::
