---
id: E17
title: The argument principle and winding numbers
status:
- context
---
<p>Why "argument"? Along a small arc of $C$ where $f\ne0$, choose a branch of $\log f$ ([E.3](apx:E3)); then $\frac{f'}f=(\log f)'$, and $\int\frac{f'}fdz$ is the change of $\log f=\log|f|+i\arg f$ along the arc. Around the closed curve $C$, $\log|f|$ returns to its starting value, while $\arg f$ may increase by a multiple of $2\pi$. So
\[ \frac1{2\pi i}\oint_C\frac{f'}f\,dz=\frac{\text{total change of }\arg f(z)}{2\pi}=\text{the number of times }f(C)\text{ winds around }0. \]
This number is the <em>winding number</em> of the image curve $f(C)$ about $0$. @thm:argument-principle says it equals $Z-P$. Rouché's theorem (@thm:rouche) then says: if $|g-f|\lt|f|$ on $C$, the curves $f(C)$ and $g(C)$ wind around $0$ equally often, because the segment from $f(z)$ to $g(z)$ never passes through $0$ (the "dog on a leash").</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Argument_principle" target="_blank" rel="noopener">Argument principle</a> · <a href="https://en.wikipedia.org/wiki/Winding_number" target="_blank" rel="noopener">Winding number</a> · <a href="https://en.wikipedia.org/wiki/Rouch%C3%A9%27s_theorem" target="_blank" rel="noopener">Rouché's theorem</a></p>
