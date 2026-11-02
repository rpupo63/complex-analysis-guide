---
label: ex:the-upper-half-disk-onto-the
source: Practice midterm 3, Problem 4(a)
title: the upper half-disk onto the disk
placement: n11
order: 3
---
Find a conformal map $F$ of the upper half-disk $D^+:=\{|z|\lt1,\ \operatorname{Im}z\gt0\}$ onto $D(0,1)$. You may use without proof that $w=\frac{1+z}{1-z}$ maps $D^+$ onto the quadrant $\{\operatorname{Re}w\gt0,\operatorname{Im}w\gt0\}$.
<details class="sol"><summary>Hint</summary>
Then square (@eg:z-2-doubles-angles-at-0), then apply the Cayley map.
</details>
<details class="sol"><summary>Solution</summary>
Quadrant $\xrightarrow{w^2}\mathbb H\xrightarrow{C}D(0,1)$: squaring maps the quadrant onto $\mathbb H$ bijectively (@eg:z-2-doubles-angles-at-0), and the Cayley map $C$ maps $\mathbb H$ onto the disk (@prop:cayley-map). So with $w=\frac{1+z}{1-z}$,
\[ F(z)=\frac{w^2-i}{w^2+i}=\frac{(1+z)^2-i(1-z)^2}{(1+z)^2+i(1-z)^2}. \]
Each step is a conformal map, so the composition is one (@def:conformal-map).
</details>
