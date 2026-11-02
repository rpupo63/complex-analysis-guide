---
id: s8
slide: Slide 8
title: The linear system
---

::: definition {#def:discrete-problem name="discrete problem"}
Find $U\in \class{ntn-Vg}{V^g_\eps}$ such that
\[ \class{ntn-a}{a}(U,w)=0\qquad\text{for every } w\in \class{ntn-Vz}{V^0_\eps}. \]
The trial function and the test functions are both restricted to finite-dimensional sets. This is an instance of the [Galerkin method](apx:E7).
:::
<p>Every $w\in \class{ntn-Vz}{V^0_\eps}$ is a legitimate test function for the weak form: it is continuous, smooth on each open square, and zero on $\class{ntn-dOm}{\partial\Omega}$ ([Prop. #(b)](@prop:the-space-v-0-eps)). The discrete problem gives up testing against every test function and uses only these $n$.</p>

::: definition {#def:the-matrix-a name="the matrix $A$"}
For nodes $(i,j),(k,l)$,
\[ \class{ntn-A}{A_{kl,ij}}:=\class{ntn-a}{a}(\class{ntn-phi}{\varphi_{ij}},\class{ntn-phi}{\varphi_{kl}})=\iint_\Omega\nabla\class{ntn-phi}{\varphi_{ij}}\cdot\nabla\class{ntn-phi}{\varphi_{kl}}\,dA. \]
In engineering this is called the [stiffness matrix](apx:E7).
:::

::: proposition {#prop:the-equations name="the equations"}
Make the ansatz $U=\sum_{ij}c_{ij}\class{ntn-phi}{\varphi_{ij}}$ with $c_{ij}=g(x_i,y_j)$ at boundary nodes. Then $U$ solves the discrete problem if and only if
\[ \sum_{ij}\class{ntn-A}{A_{kl,ij}}\,c_{ij}=0\qquad\text{for every interior node }(k,l). \]
:::
::: proof
The ansatz puts $U$ in $\class{ntn-Vg}{V^g_\eps}$ (@cor:the-coefficients-are-the-nodal-values). By linearity of $a$ in its first slot,
\[ \class{ntn-a}{a}(U,\class{ntn-phi}{\varphi_{kl}})=a\Big(\sum_{ij}c_{ij}\class{ntn-phi}{\varphi_{ij}},\,\class{ntn-phi}{\varphi_{kl}}\Big)=\sum_{ij}c_{ij}\,\class{ntn-a}{a}(\class{ntn-phi}{\varphi_{ij}},\class{ntn-phi}{\varphi_{kl}})=\sum_{ij}\class{ntn-A}{A_{kl,ij}}\,c_{ij}. \]
(⇒) Each interior hat lies in $\class{ntn-Vz}{V^0_\eps}$ and is an admissible $w$, so each sum is $0$.<br>
(⇐) Any $w\in \class{ntn-Vz}{V^0_\eps}$ is $w=\sum_{(k,l)\in \class{ntn-I}{I}}d_{kl}\class{ntn-phi}{\varphi_{kl}}$ ([Prop. #(c)](@prop:the-space-v-0-eps)), and by linearity in the second slot $\class{ntn-a}{a}(U,w)=\sum d_{kl}\,\class{ntn-a}{a}(U,\class{ntn-phi}{\varphi_{kl}})=0$.
:::
<p>Count: one equation and one unknown $c_{kl}$ per interior node. The system is $n\times n$ whatever the shape of $\Omega$.</p>
