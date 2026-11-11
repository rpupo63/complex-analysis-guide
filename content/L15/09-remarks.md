---
id: q9
slide: Slide 12
title: Remarks
---

::: remark {#rem:the-prevertices name="the prevertices"}
Three prevertices can be chosen freely, in cyclic order on $\mathbb R\cup\{\infty\}$, by composing with an automorphism of $\mathbb H$ (@prop:automorphisms-of-h). The other $n-3$ are then determined by the ratios of the side lengths of $P$, in general only numerically. For a triangle nothing is left to determine.
:::

::: theorem {#thm:schwarz-christoffel-converse name="the converse" status=cited}
Let $0\lt\alpha_k\lt1$ with $\sum_k(1-\alpha_k)=2$, and let $x_1\lt\dots\lt x_n$ be real; or let $x_1\lt\dots\lt x_{n-1}$ be real and $x_n=\infty$, and leave out the factor of $x_n$. Then for $A\ne0$ the formula of @thm:schwarz-christoffel maps $\mathbb H$ conformally onto the interior of a convex polygon with angles $\alpha_k\pi$.
:::
<p>Why: the image of $\mathbb R\cup\{\infty\}$ is a closed polygonal curve that turns left by $(1-\alpha_k)\pi\in(0,\pi)$ at each $F(x_k)$, and by $2\pi$ in total, so it bounds a convex polygon. Injectivity follows from the argument principle (@thm:argument-principle). The slide only sketches this, so it is marked as cited.</p>

::: remark {#rem:vertices-at-infinity name="vertices at $\infty$"}
With step 2 of the proof adapted, the formula also holds for unbounded polygons. At a vertex at $\infty$ the turn is again $(1-\alpha_k)\pi$, now with $-2\le\alpha_k\le0$. Two cases occur below:
<ul>
<li>$\alpha_k=0$: the two sides are parallel and run in opposite directions (a <em>channel</em>, as at the end of a half-strip);</li>
<li>$\alpha_k=-1$: the incoming and outgoing sides run in the same direction (as for $\mathbb H$ itself, or outside a semi-infinite plate).</li>
</ul>
If a vertex has prevertex $\infty$, its factor is left out.
:::

::: remark {#rem:correction-angle-at-infinity name="correction to the slide"}
The slide says $-1\le\alpha_k\le0$ at a vertex at $\infty$. That is too narrow. The sector $\{0\lt\arg w\lt\phi\}$, $0\lt\phi\lt2\pi$, has the vertex $0$ with turn $\pi-\phi$, so the turn at $\infty$ is $2\pi-(\pi-\phi)=\pi+\phi=(1-\alpha_\infty)\pi$, and $\alpha_\infty=-\phi/\pi$. For $\phi=3\pi/2$ this is $-3/2$. The correct range is $-2\le\alpha_k\le0$.
:::
