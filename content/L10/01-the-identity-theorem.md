---
id: k1
slide: Slide 2
title: The identity theorem
---
<p>Two tools from Part II's toolbox are proved in full first: the identity theorem (announced in Lecture 1 as @thm:identity-theorem) and the stability of holomorphy under uniform limits.</p>
<p>Notation: $\class{ntn-Dar}{D}(x,r):=\{z:|z-x|\lt r\}$, the open disk.</p>

::: theorem {#thm:identity-theorem-l10 name="identity theorem"}
Let $f,g$ be holomorphic on a [connected](apx:C4) open set $U$, and let $x_n\in U\setminus\{x\}$ with $x_n\to x\in U$. If $f(x_n)=g(x_n)$ for every $n$, then $f=g$ on $U$.
:::
<figure>{{fig:k1-1}}<figcaption>Step 1 kills $h$ on a disk about $x$, where the zeros $x_n$ accumulate; overlapping disks carry this along a chain to any $w\in U$.</figcaption></figure>
<p>This contains @thm:identity-theorem (a nonempty open set contains such a sequence) and @cor:isolated-zeros (take $g=0$). Let $h:=f-g$; the hypothesis says $h(x_n)=0$.</p>

::: proof {title="Proof, Step 1."}
<em>If zeros $x_n\ne x$ of $h$ tend to $x\in U$, then $h\equiv0$ on every disk $\class{ntn-Dar}{D}(x,r)\subset U$.</em>
<ol>
<li>Fix $\class{ntn-Dar}{D}(x,r)\subset U$. On each closed disk $|z-x|\le r'$ with $r'\lt r$, @thm:power-series gives $h(z)=\sum_ka_k(z-x)^k$, with coefficients $a_k=h^{(k)}(x)/k!$ that do not depend on $r'$. So the expansion holds on all of $\class{ntn-Dar}{D}(x,r)$.</li>
<li>Suppose some $a_k\ne0$, and let $a_m$ be the first. By the Taylor remainder (@cor:taylor-remainder with $N=m+1$), $h(z)=a_m(z-x)^m+O(|z-x|^{m+1})$, that is,
\[ \frac{h(z)}{(z-x)^m}=a_m+O(|z-x|)\qquad(z\to x). \]</li>
<li>Put $z=x_n$ (allowed, as $x_n\ne x$, and $x_n\in \class{ntn-Dar}{D}(x,r)$ for large $n$): $a_m=\lim_n\frac{h(x_n)}{(x_n-x)^m}=\lim_n0=0$, a contradiction. So all $a_k=0$, and $h\equiv0$ on $\class{ntn-Dar}{D}(x,r)$. <span class="qed">∎</span></li>
</ol>
:::
<p>Compare the proof of @thm:isolated-zeros, which ran the same argument through derivatives; this version is the one the slides use.</p>
