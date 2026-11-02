---
label: ex:horse-races
source: Homework 2, Problem 3(b)
title: horse races
placement: f11
order: 2
---
A <b>finish</b> of $n$ horses, with ties allowed, is a list $(S_1,\dots,S_k)$ of nonempty sets partitioning $\{1,\dots,n\}$ ($S_1$ tied for first, and so on). Let $F_n$ be the number of finishes ($F_0:=1$); e.g. $F_2=3$, $F_3=13$. Show $\sum_nF_n\frac{z^n}{n!}=\frac1{2-e^z}$ near $0$.
<details class="sol"><summary>Hint</summary>
Let $F_{n,k}$ count finishes with exactly $k$ places and $\Phi_k(z):=\sum_nF_{n,k}\frac{z^n}{n!}$. Choosing $S_1$ ($j\ge1$ horses) gives $F_{n,k}=\sum_{j\ge1}\binom njF_{n-j,k-1}$, i.e. $\Phi_k=(e^z-1)\Phi_{k-1}$. So $\Phi_k=(e^z-1)^k$. Sum over $k$: a geometric series, for $|z|\lt\log2$.
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li>The recursion is the product rule of @ex:derangements with $a_0=0$, $a_j=1$ for $j\ge1$ ($\sum a_j\frac{z^j}{j!}=e^z-1$): $\Phi_k=(e^z-1)\Phi_{k-1}$, and $\Phi_0=1$, so $\Phi_k=(e^z-1)^k$.</li>
<li>$F_n=\sum_kF_{n,k}$ (a finite sum, $k\le n$). For $|z|\lt\log2$, $|e^z-1|\le e^{|z|}-1\lt1$, and all coefficients are $\ge0$, so the double series converges absolutely and may be summed over $k$ first ([A.21](apx:A21)):
\[ \sum_nF_n\frac{z^n}{n!}=\sum_k(e^z-1)^k=\frac1{1-(e^z-1)}=\frac1{2-e^z}. \]</li>
<li>Check: $\frac1{2-e^z}=\frac1{1-(z+\frac{z^2}2+\dots)}=1+z+\frac32z^2+\dots$, so $F_2=2!\cdot\frac32=3$. ✓</li>
</ol>
</details>
