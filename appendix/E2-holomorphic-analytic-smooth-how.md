---
id: E2
title: 'Holomorphic, analytic, smooth: how the definitions meet'
status:
- context
---
<p>The course uses three conditions on a function $f$ on an open set:</p>
<ol>
<li>a complex derivative at every point (@def:holomorphic);</li>
<li>a complex derivative at every point, with $C^1$ real and imaginary parts (@conv:holomorphic-near-k);</li>
<li>locally a convergent power series (@def:complex-analytic).</li>
</ol>
<p>Lecture 6 proves (2) ⇒ (3): @thm:power-series, through Cauchy's theorem, whose proof by Green's theorem needs the $C^1$ parts. Power series give (3) ⇒ (2) ([A.19](apx:A19)), and @cor:holomorphic-functions-are-smooth adds that such functions are $C^\infty$. Clearly (2) ⇒ (1).</p>
<p>The remaining step, (1) ⇒ (2), is <em>Goursat's theorem</em>: Cauchy's theorem holds for every $f$ with a complex derivative at each point, with no continuity assumed. The proof avoids Green's theorem: it subdivides a triangle into four, picks the piece with the largest integral, and repeats; the nested triangles shrink to a point where $f$ is differentiable, and that forces the integral to be $0$. So all three conditions are equivalent, and the $C^1$ requirement of @conv:holomorphic-near-k is a convenience, not a restriction. A converse, <em>Morera's theorem</em>, says a continuous $f$ whose integral around every small circle vanishes is holomorphic.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Goursat%27s_theorem" target="_blank" rel="noopener">Goursat's theorem</a> · <a href="https://en.wikipedia.org/wiki/Analytic_function" target="_blank" rel="noopener">Analytic function</a> · <a href="https://en.wikipedia.org/wiki/Morera%27s_theorem" target="_blank" rel="noopener">Morera's theorem</a></p>
