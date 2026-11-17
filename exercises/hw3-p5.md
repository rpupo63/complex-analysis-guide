---
label: ex:image-of-an-entire-function-is-dense
source: Homework 3, Problem 5
title: the image of an entire function is dense
placement: n16
order: 1
---
Prove that the image of a nonconstant entire function is dense in $\mathbb C$. Deduce that an entire function $f$ with $\operatorname{Re} f(z)\le(\operatorname{Im} f(z))^2$ for all $z\in\mathbb C$ is constant.
<details class="sol"><summary>Hint</summary>
If the image of $f$ misses a disk $\{|w-c|\lt r\}$, apply Liouville's theorem to $1/(f(z)-c)$. For the deduction, the disk $\{|w-2|\lt1\}$ lies entirely outside the region $\operatorname{Re} w\le(\operatorname{Im} w)^2$.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li><em>The image is dense.</em> Suppose $f$ is entire and nonconstant, and the image misses $\{|w-c|\lt r\}$ for some $c\in\mathbb C$ and $r\gt0$. Then $f(z)\ne c$ for every $z$, so $1/(f-c)$ is entire. Also $|f(z)-c|\ge r$, so $|1/(f(z)-c)|\le 1/r$. By @thm:liouville this function is constant, hence so is $f$, a contradiction. Every disk in $\mathbb C$ therefore meets the image.</li>
<li><em>The inequality misses a disk.</em> Let $|w-2|\lt1$. Then $\operatorname{Re} w\gt1$ and $|\operatorname{Im} w|\lt1$, so $(\operatorname{Im} w)^2\lt1\lt\operatorname{Re} w$. Such a $w$ does not satisfy $\operatorname{Re} w\le(\operatorname{Im} w)^2$. If $\operatorname{Re} f\le(\operatorname{Im} f)^2$ everywhere, the image of $f$ misses $\{|w-2|\lt1\}$. By step 1, $f$ is constant.</li>
</ol>
</details>
