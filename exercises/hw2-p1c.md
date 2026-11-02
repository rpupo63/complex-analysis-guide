---
label: ex:limits-of-injective-maps
source: Homework 2, Problem 1(c)
title: limits of injective maps
placement: m10
order: 3
---
Under the hypotheses of the previous exercise, but with each $f_N$ injective instead of zero-free, show that $f$ is injective or constant.
<details class="sol"><summary>Hint</summary>
Fix $b\in U$ and apply the previous exercise to $f_N(z)-f_N(b)$ on $U\setminus\{b\}$. Is $U\setminus\{b\}$ connected?
</details>
<details class="sol"><summary>Solution</summary>
Suppose $f$ is not constant, and fix $b\in U$. On $U':=U\setminus\{b\}$, the functions $g_N(z):=f_N(z)-f_N(b)$ have no zeros ($f_N$ is injective), and converge uniformly on closed disks in $U'$ to $g(z):=f(z)-f(b)$ (a closed disk in $U'$ is one in $U$, and $f_N(b)\to f(b)$). $U'$ is open, and connected: a path in $U$ between two points of $U'$ can be rerouted around the single point $b$ ([C.4](apx:C4)). By Hurwitz (@ex:hurwitzs-theorem), $g\equiv0$ on $U'$ or $g$ has no zeros on $U'$. The first would make $f\equiv f(b)$ on $U'$, hence on $U$ by continuity: constant, excluded. So $f(z)\ne f(b)$ for every $z\ne b$. As $b$ is arbitrary, $f$ is injective.
</details>
