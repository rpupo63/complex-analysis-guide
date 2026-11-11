---
id: q7
slide: Slide 8
title: Why the formula
---

::: convention {#conv:powers-of-x-minus-xk name="powers of $x-x_k$"}
For real $x\ne x_k$ and real $\beta$, $(x-x_k)^\beta:=|x-x_k|^\beta e^{i\beta\arg(x-x_k)}$, with $\arg(x-x_k)=\pi$ for $x\lt x_k$ and $0$ for $x\gt x_k$. These are the boundary values of the branch $e^{\beta\log(z-x_k)}$ on $\mathbb H$ with $0\lt\arg(z-x_k)\lt\pi$.
:::

<p>A heuristic, assuming $F$ is differentiable on $\mathbb R$:</p>
<ul>
<li><b>What $F'$ must do on $\mathbb R$.</b> For $x_k\lt x\lt x_{k+1}$, $F(x)$ moves along the side $[w_k,w_{k+1}]$, so $F'(x)$ points in the direction of that side. At $x_k$ this direction turns left by $(1-\alpha_k)\pi$.</li>
<li><b>What $\prod_k(z-x_k)^{\alpha_k-1}$ does on $\mathbb R$.</b> Its argument is constant between consecutive $x_k$. As $x$ increases past $x_k$, $\arg(x-x_k)^{\alpha_k-1}$ goes from $(\alpha_k-1)\pi$ to $0$: it increases by $(1-\alpha_k)\pi$. No other factor changes.</li>
</ul>
<p>So both turn by the same angles at the same places. This suggests
\[ F'(z)=A\prod_{k=1}^n(z-x_k)^{\alpha_k-1}. \]</p>
