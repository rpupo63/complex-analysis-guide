---
id: A10
title: Lipschitz functions
status:
- defined
- cited
---
<p>A function $F$ is <em>Lipschitz</em> with constant $C$ if $|F(a)-F(b)|\le C|a-b|$ for all $a,b$; "1-Lipschitz" means $C=1$. Examples: $t\mapsto t^+$ and $t\mapsto|t|$ (1-Lipschitz), any $C^1$ function on a closed interval ($C=\max|F'|$), the distance function ([C.6](apx:C6)). Composing with a Lipschitz function keeps Lipschitz: if $f$ is $C$-Lipschitz, so is $f^+$. Products of bounded Lipschitz functions are Lipschitz.</p>
<div class="env"><span class="hd">Facts (cited).</span>
<ol>
<li><em>Rademacher's theorem.</em> A Lipschitz function on an open set of $\R^2$ (or an interval) is differentiable almost everywhere, with gradient bounded by $C$.</li>
<li><em>Fundamental theorem of calculus.</em> A Lipschitz function $F$ on $[a,b]$ satisfies $F(b)-F(a)=\int_a^bF'(x)\,dx$, the derivative existing almost everywhere. (Lipschitz functions are absolutely continuous.)</li>
</ol></div>
<p>Fact 2 is what Lecture 5 needs. $f^+$ can have infinitely many corners on a line (if $f$ crosses zero infinitely often), so the piecewise version [A.9](apx:A9) does not apply, but the Lipschitz version does. Lipschitz is the right replacement for "continuous and piecewise smooth": the step function of earlier discussions, which jumps, is not Lipschitz.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Lipschitz_continuity" target="_blank" rel="noopener">Lipschitz continuity</a> · <a href="https://en.wikipedia.org/wiki/Rademacher%27s_theorem" target="_blank" rel="noopener">Rademacher's theorem</a> · <a href="https://en.wikipedia.org/wiki/Absolute_continuity" target="_blank" rel="noopener">Absolute continuity</a></p>
