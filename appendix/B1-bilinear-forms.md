---
id: B1
title: Bilinear forms
status:
- defined
---
<p>Let $V$ be a real vector space. A <em>bilinear form</em> is a map $a:V\times V\to\R$ that is linear in each argument when the other is held fixed:
\[ a(\alpha u_1+\beta u_2,w)=\alpha a(u_1,w)+\beta a(u_2,w),\qquad a(u,\alpha w_1+\beta w_2)=\alpha a(u,w_1)+\beta a(u,w_2). \]
It is <em>symmetric</em> if $a(u,w)=a(w,u)$, and <em>positive semidefinite</em> if $a(v,v)\ge0$ for all $v$. If also $a(v,v)=0$ only for $v=0$, it is an <em>inner product</em>. The energy form $a$ is positive definite on each $\class{ntn-Vz}{V^0_\eps}$ (@thm:a-ii-is-positive-definite), but not on all functions, since constants have zero energy.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Bilinear_form" target="_blank" rel="noopener">Bilinear form</a> · <a href="https://en.wikipedia.org/wiki/Inner_product_space" target="_blank" rel="noopener">Inner product space</a></p>
