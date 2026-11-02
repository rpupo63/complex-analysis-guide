---
id: E20
title: 'Hadamard''s theorem: the idea of the proof'
status:
- context
---
<p>@thm:hadamard is stated without proof. By @cor:weierstrass-factorization (with $\class{ntn-Ep}{E_p}$ instead of $\class{ntn-Ep}{E_k}$, which converges by the argument of @sec:k13), $f=z^me^hQ$ with $Q:=\prod_k\class{ntn-Ep}{E_p}(z/a_k)$. It remains to show $h$ is a polynomial of degree $\le\rho$. By @lem:no-zeros with $k=\lfloor\rho\rfloor$, it is enough to bound $\operatorname{Re}h=\log|f|-m\log|z|-\log|Q|$ from above by $o(r^{k+1})$ on a sequence of circles. The term $\log|f|\le r^{\rho+\epsilon}$ is fine. The difficulty is a <em>lower</em> bound for $|Q|$, which is small near its zeros: one shows that $\log|Q(z)|\ge-r^{\rho+\epsilon}$ outside small disks around the $a_k$ (of total radius much less than $r$), so that suitable circles avoid them. This uses @thm:zeros-versus-order to control how many zeros there are.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Hadamard_factorization_theorem" target="_blank" rel="noopener">Hadamard factorization theorem</a> · <a href="https://en.wikipedia.org/wiki/Weierstrass_factorization_theorem" target="_blank" rel="noopener">Weierstrass factorization theorem</a></p>
