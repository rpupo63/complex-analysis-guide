---
id: s9
slide: Slide 9
title: Block form
---
::: definition {#def:split-the-coefficient-vector-by}
Split the coefficient vector by node type: $\class{ntn-cI}{c_I}=(c_p)_{p\in \class{ntn-I}{I}}$ is unknown and $\class{ntn-cB}{c_B}=\class{ntn-gB}{g_B}:=(g(x_q,y_q))_{q\in \class{ntn-B}{B}}$ is known. Split the matrix the same way: $\class{ntn-AII}{A_{II}}=(\class{ntn-A}{A_{pq}})_{p,q\in \class{ntn-I}{I}}$ and $\class{ntn-AIB}{A_{IB}}=(\class{ntn-A}{A_{pq}})_{p\in \class{ntn-I}{I},\,q\in \class{ntn-B}{B}}$. Here $p,q$ stand for node labels such as $(k,l)$ and $(i,j)$.
:::

::: proposition {#prop:the-equations-of-prop-3}
The equations of @prop:the-equations are equivalent to
\[ \class{ntn-AII}{A_{II}}\,\class{ntn-cI}{c_I}=-\class{ntn-AIB}{A_{IB}}\,\class{ntn-gB}{g_B}. \]
:::
::: proof
For each $p\in \class{ntn-I}{I}$, split the sum over all nodes according to where $q$ lies:
\[ 0=\sum_q \class{ntn-A}{A_{pq}}c_q=\sum_{q\in \class{ntn-I}{I}}\class{ntn-A}{A_{pq}}c_q+\sum_{q\in \class{ntn-B}{B}}\class{ntn-A}{A_{pq}}g_q=(\class{ntn-AII}{A_{II}}\class{ntn-cI}{c_I})_p+(\class{ntn-AIB}{A_{IB}}\class{ntn-gB}{g_B})_p. \]
Move the known term to the right-hand side.
:::
<p>The boundary data sits on the right and the unknowns on the left. It remains to show that $\class{ntn-AII}{A_{II}}$ is invertible.</p>
