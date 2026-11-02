---
id: x2
slide: Slide 3
title: The main difference with real analysis
toc: Difference with real analysis
---
<p>At first sight the only difference is that <em>taking a derivative is more constraining</em>.</p>
<ul>
<li><b>On $\R$:</b> two directions, two limits, required to match:
\[ \lim_{h\to0^-}\frac{f(x_0+h)-f(x_0)}{h}=\lim_{h\to0^+}\frac{f(x_0+h)-f(x_0)}{h}. \]</li>
<li><b>On $\mathbb C$:</b> left, right, top, bottom, and everything in between, all required to match. Writing $h=e^{i\theta}t$ with $t$ real and $\theta$ fixed picks a direction:
\[ \lim_{t\to0}\frac{f(z_0+t)-f(z_0)}{t}=\lim_{t\to0}\frac{f(z_0+it)-f(z_0)}{it}=\lim_{t\to0}\frac{f(z_0+e^{i\theta}t)-f(z_0)}{e^{i\theta}t}. \]</li>
</ul>
<p>And more: @def:holomorphic asks that the quotient converge as $h\to0$ along <em>any</em> path, not just straight lines. The next sections show that, for functions that are differentiable as maps $\R^2\to\R^2$, two directions already decide everything (@thm:cauchy-riemann).</p>
