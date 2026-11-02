---
id: B4
title: Symmetric and positive definite matrices
status:
- defined
- derived
---
<div class="env"><span class="hd">Definitions.</span> A square matrix $M$ is <em>symmetric</em> if $M^{\mathsf T}=M$, i.e. $M_{pq}=M_{qp}$. A symmetric $M$ is <em>positive definite</em> if $c^{\mathsf T}Mc\gt0$ for every nonzero vector $c$. A <em>principal submatrix</em> keeps the rows and columns with the same index set, as $\class{ntn-AII}{A_{II}}$ does.</div>
<div class="env"><span class="hd">Proposition.</span> A positive definite matrix is invertible.</div>
::: proof
If $Mc=0$ then $c^{\mathsf T}Mc=0$, so $c=0$. So the kernel of $M$ is $\{0\}$. For a square $n\times n$ matrix, the rank–nullity theorem (cited) gives rank $n$, so $M$ is onto as well as one-to-one, hence invertible.
:::
<p>Positive definite systems are also the ones solved well in practice: conjugate gradients and Cholesky factorization both require this property.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Symmetric_matrix" target="_blank" rel="noopener">Symmetric matrix</a> · <a href="https://en.wikipedia.org/wiki/Definite_matrix" target="_blank" rel="noopener">Definite matrix</a> · <a href="https://en.wikipedia.org/wiki/Rank%E2%80%93nullity_theorem" target="_blank" rel="noopener">Rank–nullity theorem</a></p>
