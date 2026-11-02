---
id: D7
title: The Fourier transform and Fourier inversion
status:
- defined
- cited
---
<p>For integrable $f$ on $\R$, $\class{ntn-hat}{\hat f}(\xi)=\int f(x)e^{-2\pi ix\xi}dx$ (@def:fourier-transform). With the $2\pi$ inside the exponent, the transform and its inverse are symmetric, and $e^{-\pi x^2}$ is its own transform (@prop:the-gaussian-is-its-own-transform). $\class{ntn-hat}{\hat f}$ is continuous ([A.22](apx:A22)) and bounded by $\int|f|$.</p>
<div class="env"><span class="hd">Inversion theorem (cited).</span> If $f$ and $\class{ntn-hat}{\hat f}$ are both integrable, then $f(x)=\int\class{ntn-hat}{\hat f}(\xi)e^{2\pi ix\xi}d\xi$ at every point where $f$ is continuous; in particular everywhere, if $f$ is continuous. This is @fact:fourier-inversion.</div>
<p>Rules that make the examples of Lecture 8 quick: shifting $f(x-a)$ multiplies $\class{ntn-hat}{\hat f}$ by $e^{-2\pi ia\xi}$; scaling $f(x/T)$ gives $T\class{ntn-hat}{\hat f}(T\xi)$ (used in @cor:sampling-at-rate-t); $\class{ntn-hat}{\widehat{f'}}=2\pi i\xi\class{ntn-hat}{\hat f}$ (the integration by parts of @thm:paley-wiener-a-simple-form); and convolution becomes multiplication, which is why the triangle, the convolution of two boxes, has transform $\class{ntn-sinc}{\operatorname{sinc}}^2$ (@ex:find-for-the-triangle-is).</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Fourier_transform" target="_blank" rel="noopener">Fourier transform</a> · <a href="https://en.wikipedia.org/wiki/Fourier_inversion_theorem" target="_blank" rel="noopener">Fourier inversion theorem</a> · <a href="https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem" target="_blank" rel="noopener">Sampling theorem</a></p>
