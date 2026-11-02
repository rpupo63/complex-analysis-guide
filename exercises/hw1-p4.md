---
label: ex:triangles-instead-of-squares
source: Homework 1, Problem 4
title: triangles instead of squares
placement: s11
order: 1
---
Let $T$ be the triangle with corners $A=(0,0)$, $B=(1,0)$, $C=(0,1)$. A linear function on $T$ has the form $a+bx+cy$.
<ol>
<li>Find linear $\phi_A,\phi_B,\phi_C$, each $1$ at the corner named and $0$ at the other two, and their gradients.</li>
<li>Compute $A_{PQ}=\iint_T\nabla\phi_P\cdot\nabla\phi_Q\,dA$ for all $P,Q\in\{A,B,C\}$, as a $3\times3$ table.</li>
<li>Divide the unit square into four triangles by joining its centre $p_0=(\frac12,\frac12)$ to the corners $p_1=(0,0)$, $p_2=(1,0)$, $p_3=(1,1)$, $p_4=(0,1)$. Let $U$ be continuous, linear on each triangle, with $U(p_j)=g_j$ and unknown $c=U(p_0)$, and let $\phi_0$ be $1$ at the centre, $0$ at the corners, linear on each triangle. Compute $\iint\nabla U\cdot\nabla\phi_0\,dA$ one triangle at a time, and show that setting it to $0$ gives $c=\frac{g_1+g_2+g_3+g_4}4$.</li>
<li>Two continuous piecewise-linear functions have the same boundary values and both satisfy $\iint\nabla U\cdot\nabla v=0$ for every continuous piecewise-linear $v$ vanishing on the boundary. Let $W$ be their difference; take $v=W$ and prove $W=0$.</li>
</ol>
<details class="sol"><summary>Hint</summary>
<ul>
<li>Substitute the three corner values into $a+bx+cy$ and solve.</li>
<li>Gradients are constant; the area of $T$ is $\frac12$. The table is symmetric and each row sums to $0$.</li>
<li>On the bottom triangle $p_1p_2p_0$, $\phi_0=2y$. Do that triangle first; the others follow by rotation.</li>
<li>$v=W$ gives $\iint|\nabla W|^2=0$. What does that say about $W$ on a connected square? Then use the boundary values. Compare @thm:a-ii-is-positive-definite.</li>
</ul>
</details>
<details class="sol"><summary>Solution</summary>
<ol>
<li>$\phi_A=1-x-y$, $\phi_B=x$, $\phi_C=y$, with gradients $(-1,-1)$, $(1,0)$, $(0,1)$. These are the triangle analogues of the hat functions of @def:tent-and-hat-functions: each is $1$ at its own node and $0$ at the others (compare @lem:key-property).</li>
<li>These are the entries of the stiffness matrix of @def:the-matrix-a, restricted to one element, as in @lem:integrating-over-one-square for a square. Each entry is (dot product of gradients) $\times\frac12$:
\[ \big(A_{PQ}\big)=\begin{pmatrix}1&-\frac12&-\frac12\\-\frac12&\frac12&0\\-\frac12&0&\frac12\end{pmatrix}\qquad(\text{rows and columns }A,B,C). \]
Rows sum to $0$ because $\phi_A+\phi_B+\phi_C=1$ has gradient $0$. The table is symmetric, as in @lem:symmetry.</li>
<li>Setting $\iint\nabla U\cdot\nabla\phi_0=0$ is the discrete equation of @def:discrete-problem and @prop:the-equations at the one interior node. Bottom triangle $p_1p_2p_0$ (area $\frac14$): $U=g_1+(g_2-g_1)x+\beta y$ with $U(p_0)=c$ giving $\beta=2c-g_1-g_2$. So $\nabla U=(g_2-g_1,\,2c-g_1-g_2)$ and $\nabla\phi_0=(0,2)$, and the triangle contributes $\frac14\cdot2(2c-g_1-g_2)=\frac12(2c-g_1-g_2)$. By the rotational symmetry of the configuration, the triangle with corners $p_j,p_{j+1}$ contributes $\frac12(2c-g_j-g_{j+1})$ (indices mod $4$). Summing,
\[ \tfrac12\big(8c-2(g_1+g_2+g_3+g_4)\big)=4c-(g_1+g_2+g_3+g_4)=0\iff c=\tfrac{g_1+g_2+g_3+g_4}4. \]
The centre value is the average of the four corners: the triangle-mesh analogue of the eight-neighbour rule, @cor:each-interior-value-is-the-average.</li>
<li>$W=U_1-U_2$ is zero on the boundary and $\iint\nabla W\cdot\nabla v=0$ for all admissible $v$ (subtract the two equations). $W$ itself is admissible, so $\iint|\nabla W|^2=0$: the energy of $W$ (@lem:the-quadratic-form-is-the-energy, @def:energy) is zero. $\nabla W$ is constant on each triangle, so it is $0$ on each triangle, and $W$ is constant on each; being continuous on the connected square, $W$ is one constant, which is $0$ on the boundary. So $W\equiv0$. This is the argument of @thm:a-ii-is-positive-definite (zero energy forces zero coefficients), which gives uniqueness of the discrete solution (@def:the-discrete-solution).</li>
</ol>
</details>
