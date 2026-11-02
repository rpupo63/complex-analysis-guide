EX = []
def ex(sec, src, title, statement, hint, solution):
    EX.append(dict(sec=sec, src=src, title=title, statement=statement, hint=hint, solution=solution))

# ======================= HOMEWORK 1 =======================
ex('x16', 'Homework 1, Problem 1', 'a holomorphic flow',
r'''Consider the complex potential $F(z)=\frac{z^3}3$, with velocity field $V=\overline{F'(z)}$ (Prop. 1.10.2).
<ol>
<li>Write $V=(u,v)$ explicitly in terms of $x$ and $y$.</li>
<li>Verify directly that $V$ is divergence-free and curl-free.</li>
<li>Find an equation for the streamlines, and sketch the streamline $\operatorname{Im}F=0$ with several nearby streamlines. Indicate the direction of the flow.</li>
<li>Find every stagnation point and express the speed $|V|$ in terms of $|z|$.</li>
<li>Let $C$ be the vertical segment from $A=(0,-1)$ to $B=(0,1)$, oriented upward. Compute the flux across $C$ both directly and from $\operatorname{Im}F(B)-\operatorname{Im}F(A)$.</li>
</ol>''',
r'''<ul>
<li>If $F'=a+ib$, then $V=(a,-b)$.</li>
<li>Expand $(x+iy)^2$ and $(x+iy)^3$ before taking real and imaginary parts.</li>
<li>Streamlines are the level curves $\operatorname{Im}F=c$ (Prop. 1.11.2).</li>
<li>On an oriented curve, the convention is $n\,ds=(dy,-dx)$ (§1.12).</li>
<li>Your two flux calculations should agree in sign as well as size (Prop. 1.12.1).</li>
</ul>''',
r'''<ol>
<li>$F'(z)=z^2=(x^2-y^2)+2ixy$, so by Prop. 1.10.2 (velocity $=\overline{F'}$, with $F$ the complex potential of Def. 1.10.1) $V=\overline{F'}=(x^2-y^2,\,-2xy)$.</li>
<li>$\operatorname{div}V=\partial_x(x^2-y^2)+\partial_y(-2xy)=2x-2x=0$ and $\operatorname{curl}V=\partial_x(-2xy)-\partial_y(x^2-y^2)=-2y+2y=0$ (Def. 1.6.1). This is no accident: it is Prop. 1.6.2 applied to the holomorphic $F'$, and by Prop. 1.6.3 the flow is incompressible and irrotational.</li>
<li>$F=\frac13(x+iy)^3=\frac13\big(x^3-3xy^2\big)+\frac i3\big(3x^2y-y^3\big)$, so, as streamlines are the level sets of $\operatorname{Im}F$ (Def. 1.11.1, Prop. 1.11.2), they are
\[ \operatorname{Im}F=x^2y-\tfrac13y^3=y\big(x^2-\tfrac13y^2\big)=c. \]
For $c=0$: $y=0$ or $y=\pm\sqrt3\,x$, three lines through $0$ at angles $0°,60°,120°$. They cut the plane into six sectors, and the other streamlines are hyperbola-like curves in each sector, asymptotic to the two bounding lines. Direction: on the real axis $V=(x^2,0)$ points right, so the flow comes in along the negative real axis and leaves along the positive one; the pattern repeats with three-fold symmetry (a "monkey saddle" flow, compare the corner flow of Example 1.13.2).</li>
<li>$V=0\iff z^2=0\iff z=0$: the only stagnation point is the origin (compare the stagnation points of Prop. 1.15.2). Speed $|V|=|F'(z)|=|z|^2$, since the speed is $|F'|$ (Prop. 1.10.2).</li>
<li><em>Directly:</em> with the convention $n\,ds=(dy,-dx)$ of §1.12, on $C$ we have $x=0$, $dx=0$, so $n\,ds=(dy,0)$ and $V\cdot n\,ds=(x^2-y^2)\,dy=-y^2\,dy$. Flux $=\int_{-1}^1-y^2\,dy=-\frac23$.<br>
<em>From the stream function</em> (Prop. 1.12.1: flux $=\operatorname{Im}F(B)-\operatorname{Im}F(A)$): $\operatorname{Im}F(0,1)=1\cdot(0-\frac13)=-\frac13$ and $\operatorname{Im}F(0,-1)=(-1)(0-\frac13)=\frac13$, so the flux is $-\frac13-\frac13=-\frac23$. ✓ (Negative: the fluid crosses $C$ from right to left, against $n$, which points right for an upward curve.)</li>
</ol>''')

ex('w8', 'Homework 1, Problem 2', 'charges, dipoles and contour integrals',
r'''Consider the complex electric field
\[ f(z)=\frac1{2\pi}\Big(\frac2{z-1}-\frac1{z+1}\Big)+\frac1{(z-i)^2}. \]
All curves are positively oriented.
<ol>
<li>Locate and state the strengths of the point charges. What does the term $1/(z-i)^2$ represent, and what is its net charge?</li>
<li>Compute $\oint_\gamma f\,dz$ for $\gamma_1:|z-1|=\frac14$, $\gamma_2:|z-i|=\frac14$, $\gamma_3:|z|=2$.</li>
<li>For each curve, state the corresponding circulation and flux.</li>
<li>Explain why the real and imaginary parts of $f$ are harmonic away from the three singular points.</li>
</ol>''',
r'''<ul>
<li>A term $\frac{q}{2\pi(z-z_0)}$ represents a point charge $q$ at $z_0$ (Remark 2.4.4).</li>
<li>A second-order pole represents a dipole and has zero net charge (Prop. 2.7.1, Prop. 2.7.2).</li>
<li>$\oint_{|z-a|=r}\frac{dz}{z-a}=2\pi i$, and $\oint_{|z-a|=r}\frac{dz}{(z-a)^m}=0$ for $m\ge2$.</li>
<li>A term holomorphic on and inside a curve contributes zero (Cor. 2.6.3).</li>
<li>With $f=u-iv$, $\oint_\gamma f\,dz=\text{circulation}+i\cdot\text{flux}$ (Prop. 2.6.2).</li>
</ul>''',
r'''<ol>
<li>A term $\frac q{2\pi(z-z_0)}$ is the field of a charge $q$ at $z_0$ (Def. 2.4.1, Remark 2.4.4). So $\frac{2}{2\pi(z-1)}$: charge $+2$ at $z=1$; $\frac{-1}{2\pi(z+1)}$: charge $-1$ at $z=-1$. $\frac1{(z-i)^2}$ is a dipole at $i$ (Prop. 2.7.2) with net charge $0$ (Prop. 2.7.1).</li>
<li>$\gamma_1$ encloses only $1$: the charge term gives $\frac{2}{2\pi}\cdot2\pi i=2i$ (Cor. 2.6.4: $\oint\frac{dz}{z-z_j}=2\pi i$), and the other terms are holomorphic inside, so contribute $0$ (Cor. 2.6.3): $\oint_{\gamma_1}f\,dz=2i$. $\gamma_2$ encloses only $i$: $\oint\frac{dz}{(z-i)^2}=0$ (the residue is $0$: Def. 2.7.3, Prop. 2.7.4) and the rest is holomorphic inside, so $0$. $\gamma_3$ encloses all three: by Cor. 2.6.4 and Prop. 2.7.4, $\frac1{2\pi}(2\cdot2\pi i-2\pi i)+0=i$.</li>
<li>By Prop. 2.6.2, write each answer as circulation $+\,i\cdot$flux: $\gamma_1$: $2i$, circulation $0$, flux $2$. $\gamma_2$: circulation $0$, flux $0$. $\gamma_3$: $i$, circulation $0$, flux $1=2-1$, the total enclosed charge (Gauss, Theorem 2.5.1).</li>
<li>Away from $1,-1,i$, $f$ is holomorphic: each term is, as in Example 2.3.1. Write $f=u-iv$. By Cauchy–Riemann (Theorem 1.5.2) $u_x=-v_y$ and $u_y=v_x$, i.e. $u_x+v_y=0$ and $v_x-u_y=0$: the field $(u,v)$ has no divergence and no curl, as in Prop. 2.2.3. Here $u,v$ are smooth, being rational functions of $x,y$ away from the poles (in general, Cor. 6.6.2). So Prop. 2.8.1 gives $\Delta u=\Delta v=0$: $u$ and $v$ are harmonic (Def. 2.8.2), and so are $\operatorname{Re}f=u$ and $\operatorname{Im}f=-v$.</li>
</ol>''')

ex('s18', 'Homework 1, Problem 3', "Poincaré's inequality",
r'''Let $\Omega$ be a finite union of grid squares in the strip $0\lt x\lt L$, and $v$ continuous, piecewise $C^1$, zero on $\partial\Omega$. Extend $v$ by zero outside $\Omega$.
<ol>
<li>Explain why the extension is continuous and piecewise $C^1$.</li>
<li>Prove $\norm{v}_{L^2(\Omega)}\le L\norm{\nabla v}_{L^2(\Omega)}$.</li>
<li>Suppose every $v_n$ vanishes on $\partial\Omega$ and $\nabla v_n$ is Cauchy in $L^2$. Prove that $v_n$ is Cauchy in $L^2$. Where was this used in Lecture 3?</li>
</ol>''',
r'''<ul>
<li>After extending by zero, fix $y$ and write $v(x,y)=\int_0^x\partial_xv(s,y)\,ds$.</li>
<li>Apply <a class="x" href="#A12">Cauchy–Schwarz</a> to the one-dimensional integral.</li>
<li>Use $0\lt x\lt L$, then integrate first in $x$ and afterwards in $y$.</li>
<li>Bound $|\partial_xv|$ by $|\nabla v|$ after integrating.</li>
<li>For the last part, apply the inequality to $v_n-v_m$.</li>
</ul>''',
r'''<ol>
<li>(This is the extension used in the proof of Theorem 3.17.2.) <em>Continuous:</em> inside $\Omega$ and outside $\overline\Omega$ there is nothing to check; at a point of $\partial\Omega$, $v=0$ there, $v\to0$ from inside by continuity, and $v=0$ outside. <em>Piecewise $C^1$:</em> the grid squares cover the plane; on each square of $\Omega$, $v$ is $C^1$ by assumption, and on every other square it is $0$.</li>
<li>This is Theorem 3.17.2. Fix $y$. As $\Omega$ lies in $0\lt x\lt L$, $v(0,y)=0$, and by the <a class="x" href="#A9">fundamental theorem of calculus</a> for piecewise $C^1$ functions, $v(x,y)=\int_0^x\partial_xv(s,y)\,ds$. By Cauchy–Schwarz, for $0\lt x\lt L$,
\[ |v(x,y)|^2\le x\int_0^x|\partial_xv(s,y)|^2ds\le L\int_0^L|\partial_xv(s,y)|^2ds. \]
Integrate over $x\in(0,L)$: $\int_0^L|v(x,y)|^2dx\le L^2\int_0^L|\partial_xv(s,y)|^2ds$. Integrate over $y$ (<a class="x" href="#A13">Fubini</a>) and use $|\partial_xv|\le|\nabla v|$: $\norm{v}^2\le L^2\norm{\partial_xv}^2\le L^2\norm{\nabla v}^2$.</li>
<li>$v_n-v_m$ is continuous, piecewise $C^1$ and zero on $\partial\Omega$, so part 2 gives $\norm{v_n-v_m}\le L\norm{\nabla v_n-\nabla v_m}\to0$ (this is Cor. 3.17.3). In Lecture 3 this is how Prop. 3.18.1 gets the $L^2$ limit $u$: the gradients $\nabla U_n$ are Cauchy (Prop. 3.16.1), and $U_n-U_k$ vanishes on $\partial\Omega$, so the $U_n$ themselves are Cauchy.</li>
</ol>''')

ex('s11', 'Homework 1, Problem 4', 'triangles instead of squares',
r'''Let $T$ be the triangle with corners $A=(0,0)$, $B=(1,0)$, $C=(0,1)$. A linear function on $T$ has the form $a+bx+cy$.
<ol>
<li>Find linear $\phi_A,\phi_B,\phi_C$, each $1$ at the corner named and $0$ at the other two, and their gradients.</li>
<li>Compute $A_{PQ}=\iint_T\nabla\phi_P\cdot\nabla\phi_Q\,dA$ for all $P,Q\in\{A,B,C\}$, as a $3\times3$ table.</li>
<li>Divide the unit square into four triangles by joining its centre $p_0=(\frac12,\frac12)$ to the corners $p_1=(0,0)$, $p_2=(1,0)$, $p_3=(1,1)$, $p_4=(0,1)$. Let $U$ be continuous, linear on each triangle, with $U(p_j)=g_j$ and unknown $c=U(p_0)$, and let $\phi_0$ be $1$ at the centre, $0$ at the corners, linear on each triangle. Compute $\iint\nabla U\cdot\nabla\phi_0\,dA$ one triangle at a time, and show that setting it to $0$ gives $c=\frac{g_1+g_2+g_3+g_4}4$.</li>
<li>Two continuous piecewise-linear functions have the same boundary values and both satisfy $\iint\nabla U\cdot\nabla v=0$ for every continuous piecewise-linear $v$ vanishing on the boundary. Let $W$ be their difference; take $v=W$ and prove $W=0$.</li>
</ol>''',
r'''<ul>
<li>Substitute the three corner values into $a+bx+cy$ and solve.</li>
<li>Gradients are constant; the area of $T$ is $\frac12$. The table is symmetric and each row sums to $0$.</li>
<li>On the bottom triangle $p_1p_2p_0$, $\phi_0=2y$. Do that triangle first; the others follow by rotation.</li>
<li>$v=W$ gives $\iint|\nabla W|^2=0$. What does that say about $W$ on a connected square? Then use the boundary values. Compare Theorem 3.9.3.</li>
</ul>''',
r'''<ol>
<li>$\phi_A=1-x-y$, $\phi_B=x$, $\phi_C=y$, with gradients $(-1,-1)$, $(1,0)$, $(0,1)$. These are the triangle analogues of the hat functions of Def. 3.4.3: each is $1$ at its own node and $0$ at the others (compare Lemma 3.5.1).</li>
<li>These are the entries of the stiffness matrix of Def. 3.7.2, restricted to one element, as in Lemma 3.10.2 for a square. Each entry is (dot product of gradients) $\times\frac12$:
\[ \big(A_{PQ}\big)=\begin{pmatrix}1&-\frac12&-\frac12\\-\frac12&\frac12&0\\-\frac12&0&\frac12\end{pmatrix}\qquad(\text{rows and columns }A,B,C). \]
Rows sum to $0$ because $\phi_A+\phi_B+\phi_C=1$ has gradient $0$. The table is symmetric, as in Lemma 3.9.1.</li>
<li>Setting $\iint\nabla U\cdot\nabla\phi_0=0$ is the discrete equation of Def. 3.7.1 and Prop. 3.7.3 at the one interior node. Bottom triangle $p_1p_2p_0$ (area $\frac14$): $U=g_1+(g_2-g_1)x+\beta y$ with $U(p_0)=c$ giving $\beta=2c-g_1-g_2$. So $\nabla U=(g_2-g_1,\,2c-g_1-g_2)$ and $\nabla\phi_0=(0,2)$, and the triangle contributes $\frac14\cdot2(2c-g_1-g_2)=\frac12(2c-g_1-g_2)$. By the rotational symmetry of the configuration, the triangle with corners $p_j,p_{j+1}$ contributes $\frac12(2c-g_j-g_{j+1})$ (indices mod $4$). Summing,
\[ \tfrac12\big(8c-2(g_1+g_2+g_3+g_4)\big)=4c-(g_1+g_2+g_3+g_4)=0\iff c=\tfrac{g_1+g_2+g_3+g_4}4. \]
The centre value is the average of the four corners: the triangle-mesh analogue of the eight-neighbour rule, Cor. 3.10.4.</li>
<li>$W=U_1-U_2$ is zero on the boundary and $\iint\nabla W\cdot\nabla v=0$ for all admissible $v$ (subtract the two equations). $W$ itself is admissible, so $\iint|\nabla W|^2=0$: the energy of $W$ (Lemma 3.9.2, Def. 3.13.1) is zero. $\nabla W$ is constant on each triangle, so it is $0$ on each triangle, and $W$ is constant on each; being continuous on the connected square, $W$ is one constant, which is $0$ on the boundary. So $W\equiv0$. This is the argument of Theorem 3.9.3 (zero energy forces zero coefficients), which gives uniqueness of the discrete solution (Def. 3.9.4).</li>
</ol>''')

ex('s21', 'Homework 1, optional FreeFEM++ bonus', 'equilibrium temperature and WiFi',
r'''<b>Part A.</b> On $\Omega=(0,4)\times(0,3)$, a radiator on $0.5\lt x\lt1.5$ of the bottom edge is held at $40°$, a window on $1.5\lt x\lt2.5$ of the top edge at $5°$, and the rest of the boundary at $15°$. Mesh $\Omega$ with separate boundary labels, solve $\Delta T=0$ with continuous $P_1$ elements, plot isotherms, and report the numerical minimum and maximum. How does the maximum principle check your result?<br>
<b>Part B.</b> Run the official FreeFEM++ tutorial <em>WiFi Propagation</em>, which models the field by $\Delta E+\frac{k^2}{n^2}E=0$ ($n$ the refractive index, complex inside walls; $E=1$ on a small circular hotspot). (1) Submit a mesh and a signal plot. (2) Identify the outer boundary, the walls and the hotspot in the code; explain <code>on(2,v=1)</code>. (3) The program uses $\iint_\Omega\big(\frac{k^2}{n^2}Ew-\nabla E\cdot\nabla w\big)\,dA$: explain why, starting from the equation. (4) Compare three hotspot positions with a stated coverage criterion. (5) Change the wall absorption and explain the difference.''',
r'''<ul>
<li>Part A: split the top and bottom borders where the boundary values change; plot the mesh before solving. The core of the script is
<pre>fespace Vh(Th,P1);
Vh T,v;
problem heat(T,v)
    = int2d(Th)(dx(T)*dx(v)+dy(T)*dy(v))
    + on(/* wall labels */,T=15)
    + on(/* window label */,T=5)
    + on(/* radiator label */,T=40);</pre>
This is exactly the weak form of Def. 3.3.4, solved over $P_1$ (linear-on-triangles) functions instead of bilinear ones.</li>
<li>Check that $5\le T\le40$ up to round-off.</li>
<li>Part B(3): multiply the equation by $w$ and integrate the $\Delta E$ term by parts. The test function vanishes on the hotspot; the other boundaries carry the natural zero-normal-derivative condition.</li>
<li><code>wall()</code> distinguishes air from wall; <code>wallreflexion</code> and <code>wallabsorption</code> set the complex index. The hotspot has label $2$. The plotted quantity is <code>log(real(v)^2+imag(v)^2)</code>. Keep everything else fixed when comparing.</li>
</ul>''',
r'''<p>The plots and runs are computational and not reproduced here. The mathematical parts:</p>
<ul>
<li><b>Part A, maximum principle.</b> The temperature is harmonic (it is the solution of the Dirichlet problem, Def. 3.1.2, and the weak solution of Theorem 3.19.1 is classical by Cor. 4.9.6), so its maximum and minimum over $\overline\Omega$ are attained on $\partial\Omega$ (Cor. 4.4.1), where the data take values $5$, $15$, $40$. So $5\le T\le40$ everywhere, and the extreme values occur on the window and the radiator. The discrete solution obeys the same bound by the discrete maximum principle (Theorem 3.11.3 and Cor. 3.12.2 are the versions for squares; for $P_1$ elements it holds on meshes without obtuse angles). A computed value outside $[5,40]$ beyond round-off signals a labelling or mesh error.</li>
<li><b>Part B(2).</b> <code>on(2,v=1)</code> imposes the Dirichlet condition $E=1$ on the boundary with label $2$, the hotspot circle: the analogue of fixing $U=g$ at the boundary nodes in Def. 3.7.1 (the affine space $V^g_\eps$ of Def. 3.6.3).</li>
<li><b>Part B(3), the weak form.</b> Multiply $\Delta E+\frac{k^2}{n^2}E=0$ by a test function $w$ vanishing on the hotspot and integrate. By Green's identity (<a class="x" href="#A6">A.6</a>),
\[ \iint_\Omega(\Delta E)w\,dA=\oint_{\partial\Omega}w\,\partial_nE\,ds-\iint_\Omega\nabla E\cdot\nabla w\,dA. \]
The boundary integral vanishes: on the hotspot $w=0$, and on the outer boundary the natural condition is $\partial_nE=0$. So $\iint_\Omega\big(\frac{k^2}{n^2}Ew-\nabla E\cdot\nabla w\big)dA=0$ for all such $w$, which is what the program solves. Compare §3.3, where the same integration by parts (Prop. 3.3.3) turns $\Delta u=0$ into $a(u,w)=0$, the weak form of Def. 3.3.4.</li>
<li><b>Part B(4)–(5).</b> Any clearly stated criterion is acceptable (for instance, the area where the plotted log-power is below a threshold). More absorption makes the field decay faster through walls, so rooms separated from the hotspot by more walls get weaker signal; less absorption gives more reflection and interference patterns.</li>
</ul>''')

# ======================= HOMEWORK 2 =======================
ex('m10', 'Homework 2, Problem 1(a); Practice midterm 1, Problem 3', 'one solution in the disk',
r'''Let $\lambda\gt1$. Show that $z\,e^{\lambda-z}=1$ has exactly one solution in $D(0,1)$, and that this solution is real and lies in $(0,1)$.''',
r'''Compare $z\,e^{\lambda-z}-1$ with $z\,e^{\lambda-z}$ on $|z|=1$ using Theorem 11.10.1. For "real", use the intermediate value theorem on $[0,1]$.''',
r'''<ol>
<li><em>Rouché.</em> Let $f(z):=z\,e^{\lambda-z}$ and $g:=f-1$, both entire. On $|z|=1$, $|f(z)|=|z|\,|e^{\lambda-z}|=e^{\lambda-\operatorname{Re}z}\ge e^{\lambda-1}\gt1=|f-g|$, as $\operatorname{Re}z\le1$ and $\lambda\gt1$. By Theorem 11.10.1, $g$ has as many zeros in $D(0,1)$ as $f$, counted with multiplicity. $f$ has exactly one: $e^{\lambda-z}\ne0$, so its only zero is at $0$, of order $1$ (Def. 7.1.1).</li>
<li><em>It is real.</em> $\phi(x):=x\,e^{\lambda-x}-1$ is continuous on $[0,1]$ with $\phi(0)=-1\lt0$ and $\phi(1)=e^{\lambda-1}-1\gt0$, so it vanishes at some $x_0\in(0,1)$ by the intermediate value theorem (<a class="x" href="#A24">A.24</a>). That is a solution in $D(0,1)$, and by step 1 there is only one, so it is $x_0$.</li>
</ol>''')

ex('m10', 'Homework 2, Problem 1(b)', "Hurwitz's theorem",
r'''Let $U$ be a connected open set, and $f_N\to f$ uniformly on every closed disk in $U$, each $f_N$ holomorphic on $U$ with no zeros in $U$. Show that either $f\equiv0$ or $f$ has no zeros in $U$.''',
r'''$f$ is holomorphic by Theorem 10.3.1. Suppose $f\not\equiv0$ and fix $a\in U$. Choose $r\gt0$ with $\overline{D(a,r)}\subset U$ and $f\ne0$ on $|z-a|=r$ (why is this possible?), and count the zeros of $f$ in $D(a,r)$ with Rouché.''',
r'''<ol>
<li>$f$ is holomorphic on $U$ (Theorem 10.3.1). Suppose $f\not\equiv0$ and fix $a\in U$.</li>
<li><em>Choosing $r$.</em> Take $\overline{D(a,r_0)}\subset U$. As $U$ is connected and $f\not\equiv0$, only finitely many zeros of $f$ lie in the compact disk $\overline{D(a,r_0)}$: infinitely many would have a limit point in that disk (<a class="x" href="#C5">C.5</a>), hence in $U$, and the identity theorem (Theorem 10.1.1 with $g=0$) would give $f\equiv0$. Pick $r\in(0,r_0)$ different from all their distances to $a$: then $f\ne0$ on the circle $|z-a|=r$, and $\mu:=\min_{|z-a|=r}|f|\gt0$.</li>
<li><em>Rouché.</em> By uniform convergence on $\overline{D(a,r)}$, for large $N$, $|f_N-f|\lt\mu\le|f|$ on the circle (<a class="x" href="#A17">A.17</a>). Rouché, Theorem 11.10.1, applied to $f$ and $f_N$: $f$ and $f_N$ have equally many zeros in $D(a,r)$, namely none. In particular $f(a)\ne0$. As $a$ was arbitrary, $f$ has no zeros.</li>
</ol>''')

ex('m10', 'Homework 2, Problem 1(c)', 'limits of injective maps',
r'''Under the hypotheses of the previous exercise, but with each $f_N$ injective instead of zero-free, show that $f$ is injective or constant.''',
r'''Fix $b\in U$ and apply the previous exercise to $f_N(z)-f_N(b)$ on $U\setminus\{b\}$. Is $U\setminus\{b\}$ connected?''',
r'''Suppose $f$ is not constant, and fix $b\in U$. On $U':=U\setminus\{b\}$, the functions $g_N(z):=f_N(z)-f_N(b)$ have no zeros ($f_N$ is injective), and converge uniformly on closed disks in $U'$ to $g(z):=f(z)-f(b)$ (a closed disk in $U'$ is one in $U$, and $f_N(b)\to f(b)$). $U'$ is open, and connected: a path in $U$ between two points of $U'$ can be rerouted around the single point $b$ (<a class="x" href="#C4">C.4</a>). By Hurwitz (Exercise 11.10.4), $g\equiv0$ on $U'$ or $g$ has no zeros on $U'$. The first would make $f\equiv f(b)$ on $U'$, hence on $U$ by continuity: constant, excluded. So $f(z)\ne f(b)$ for every $z\ne b$. As $b$ is arbitrary, $f$ is injective.''')

ex('m10', 'Homework 2, Problem 1(d)–(e)', 'zeros of partial sums of the exponential',
r'''Let $s_N(z):=\sum_{n=0}^N\frac{z^n}{n!}$. (d) Show that for every $R\gt0$ there is $N_0$ such that $s_N$ has no zeros in $\overline{D(0,R)}$ for $N\ge N_0$. (e) (Optional) Plot the zeros of $s_N(Nz)$ for $N=20,50,100$; they approach the Szegő curve $|z\,e^{1-z}|=1$, $|z|\le1$. Root-finding needs high precision (about 30 digits for $N=100$, e.g. <code>mpmath</code>).''',
r'''(d) $s_N\to e^z$ uniformly on compact sets, and $e^z$ has no zeros. You don't need Rouché: compare $|s_N|$ with $|e^z|$ directly. (e) Use <code>mpmath.polyroots</code> with <code>mp.dps = 30</code>.''',
r'''(d) The power series of $e^z$ converges uniformly on $\overline{D(0,R)}$ (<a class="x" href="#A19">A.19</a>), so $\max_{|z|\le R}|s_N-e^z|\to0$. Let $\mu:=\min_{|z|\le R}|e^z|=e^{-R}\gt0$, and take $N_0$ with $|s_N-e^z|\lt\mu$ on the disk for $N\ge N_0$. Then $|s_N(z)|\ge|e^z|-|s_N(z)-e^z|\gt0$ there. (This is Hurwitz's theorem, Exercise 11.10.4, in a quantitative form; the same comparison is the hypothesis of Rouché, Theorem 11.10.1, with $e^z$ having no zeros.)<br>
(e) A script:
<pre>from mpmath import mp, polyroots, factorial, exp
mp.dps = 30
N = 50
coeffs = [N**n/factorial(n) for n in range(N, -1, -1)]   # s_N(Nz), highest power first
roots = polyroots(coeffs, maxsteps=200, extraprec=200)</pre>
Plot the roots with the curve $|z|e^{1-\operatorname{Re}z}=1$ in $|z|\le1$. Why that curve: by Stirling, $s_N(Nz)\approx e^{Nz}$ inside it and $\approx\frac{(Nz)^N}{N!}\approx\frac{(ze)^N}{\sqrt{2\pi N}}$ outside; zeros sit where the two sizes balance, $|e^{z}|=|ze|$, i.e. $|z\,e^{1-z}|=1$.''')

ex('j6', 'Homework 2, Problem 2(a)', 'zeros at the integers force slow growth',
r'''Let $f$ be entire with $f(n)=0$ for $n=1,2,3,\dots$ and $|f(z)|\le Ce^{c|z|}$ for all $z$, where $c\lt1$. Show $f\equiv0$.''',
r'''If $f\not\equiv0$, divide by a power of $z$ so that $f(0)\ne0$, and apply Jensen's formula (Theorem 9.5.1) on $|z|=R$ with $N\lt R\lt N+1$, $f\ne0$ on $|z|=R$. Show $N\log N-\log N!\ge N-1-\log N$ by comparing $\log N!$ with $\int_1^N\log t\,dt$.''',
r'''<ol>
<li><em>Normalize.</em> If $f\not\equiv0$, let $k$ be the order of its zero at $0$ (Def. 6.7.2; $k=0$ if $f(0)\ne0$) and write $f=z^kg$ with $g$ entire, $g(0)\ne0$ (Theorem 6.7.1); $g$ still vanishes at $1,2,\dots$, and $|g(z)|\le Ce^{c|z|}$ for $|z|\ge1$.</li>
<li><em>Jensen.</em> For $N\lt R\lt N+1$ with $g\ne0$ on $|z|=R$ (all but finitely many such $R$: by Theorem 10.1.1 there are only finitely many zeros in $|z|\le N+1$), Jensen's formula (Theorem 9.5.1) applies. Every zero in $|z|\lt R$ contributes a positive term $\log\frac R{|a_j|}$, so keeping only $1,\dots,N$, and bounding the mean of $\log|g|$ by its maximum (compare Cor. 9.6.2):
\[ \log|g(0)|+\sum_{n=1}^N\log\frac Rn\le\frac1{2\pi}\int_0^{2\pi}\log|g(Re^{i\theta})|\,d\theta\le\log C+cR\le\log C+c(N+1). \]</li>
<li><em>Stirling-type bound.</em> $\sum_{n\le N}\log\frac Rn\ge N\log N-\log N!$, and since $\log$ is increasing, $\log N!=\sum_{n=2}^N\log n\le\int_1^N\log t\,dt+\log N=N\log N-N+1+\log N$. So $\sum\ge N-1-\log N$.</li>
<li><em>Contradiction.</em> Combining, $(1-c)N\le\log C-\log|g(0)|+1+c+\log N$ for all large $N$. The left side grows linearly and the right side logarithmically, impossible as $c\lt1$. So $f\equiv0$.</li>
</ol>
<p>Remark: $\sin\pi z$ vanishes on $\mathbb Z$ and satisfies the bound with $c=\pi$; Carlson's theorem shows $c\lt\pi$ already forces $f\equiv0$. Jensen alone gives $c\lt1$.</p>''')

ex('j5', 'Homework 2, Problem 2(b)', 'Mahler measure',
r'''For $p(z)=a_d\prod_{j=1}^d(z-\alpha_j)$ with $a_d\ne0$, the Mahler measure is $M(p):=|a_d|\prod_j\max(1,|\alpha_j|)$. Show that if no $\alpha_j$ lies on $|z|=1$, then $\frac1{2\pi}\int_0^{2\pi}\log|p(e^{i\theta})|\,d\theta=\log M(p)$. Deduce that if $p$ has integer coefficients, the geometric mean of $|p|$ on the unit circle is at least $1$.''',
r'''Take logarithms of the product and use Lemma 9.4.1 with $R=1$ on each factor.''',
r'''$\log|p(e^{i\theta})|=\log|a_d|+\sum_j\log|e^{i\theta}-\alpha_j|$. By Lemma 9.4.1 with $R=1$ (allowed, as $|\alpha_j|\ne1$), each factor averages to $\log\max(1,|\alpha_j|)$. Summing gives $\log|a_d|+\sum_j\log\max(1,|\alpha_j|)=\log M(p)$. (When $p(0)\ne0$ this is Jensen's formula, Theorem 9.5.1, for $p$ on $|z|=1$.) The geometric mean is $\exp$ of the average of $\log|p|$, i.e. $M(p)\ge|a_d|\ge1$ when $a_d$ is a nonzero integer.
<p>Remark: for monic $p\in\mathbb Z[z]$ with $p(0)\ne0$, $M(p)=1$ exactly when $p$ is a product of cyclotomic polynomials (Kronecker). Whether $M(p)\ge1+\delta$ for some absolute $\delta\gt0$ otherwise is Lehmer's open problem (1933); the smallest known value is $1.17628\ldots$, for $z^{10}+z^9-z^7-z^6-z^5-z^4-z^3+z+1$.</p>''')

ex('j6', 'Homework 2, Problem 2(c)', 'the Blaschke condition',
r'''Let $f$ be holomorphic and bounded on $D(0,1)$, $f\not\equiv0$, with zeros $a_1,a_2,\dots$ (listed by multiplicity). Show $\sum_k(1-|a_k|)\lt\infty$.''',
r'''Assume $f(0)\ne0$. Apply Jensen on $|z|=r\lt1$, then let $r\to1$. Use $\log\frac1x\ge1-x$ for $0\lt x\le1$.''',
r'''<ol>
<li><em>Normalize.</em> If $f$ has a zero of order $k$ at $0$, replace $f$ by $f/z^k$: still holomorphic (Def. 6.7.2, or Lemma 9.1.1, the singularity at $0$ being removable) and bounded (bounded by $2^kM$ for $|z|\ge\frac12$, and continuous on $|z|\le\frac12$), and it drops only finitely many terms from the sum. So assume $f(0)\ne0$ and $|f|\le M$.</li>
<li><em>Jensen.</em> For $r\lt1$ with no zero on $|z|=r$ (all but countably many $r$: by Theorem 10.1.1, only finitely many zeros lie in each $|z|\le r'\lt1$), Theorem 9.5.1 gives
\[ \sum_{|a_k|\lt r}\log\frac r{|a_k|}=\frac1{2\pi}\int_0^{2\pi}\log|f(re^{i\theta})|\,d\theta-\log|f(0)|\le\log M-\log|f(0)|=:K. \]</li>
<li><em>Let $r\to1$.</em> Fix $n$. For $r\gt\max_{k\le n}|a_k|$, all terms are $\ge0$, so $\sum_{k\le n}\log\frac r{|a_k|}\le K$; letting $r\to1$, $\sum_{k\le n}\log\frac1{|a_k|}\le K$ for every $n$.</li>
<li>As $\log\frac1x\ge1-x$, $\sum_k(1-|a_k|)\le K\lt\infty$.</li>
</ol>''')

ex('k5', 'Homework 2, Problem 2(d) (optional)', 'Blaschke products',
r'''Let $0\lt|a_k|\lt1$ with $\sum_k(1-|a_k|)\lt\infty$. Show that $B(z):=\prod_k\frac{|a_k|}{a_k}\cdot\frac{a_k-z}{1-\bar a_kz}$ converges uniformly on each $\overline{D(0,r)}$, $r\lt1$, to a holomorphic function on $D(0,1)$ with $|B|\le1$, whose zeros are exactly the $a_k$.''',
r'''For $|z|\le r$, the factor differs from $1$ by at most $(1-|a_k|)\frac{1+r}{1-r}$. Then use Lemma 10.4.1.''',
r'''<ol>
<li><em>The factor minus one.</em> With $b_k(z):=\frac{|a_k|}{a_k}\cdot\frac{a_k-z}{1-\bar a_kz}$,
\[ b_k(z)-1=\frac{|a_k|(a_k-z)-a_k(1-\bar a_kz)}{a_k(1-\bar a_kz)}=\frac{-(1-|a_k|)\,(a_k+|a_k|z)}{a_k(1-\bar a_kz)}. \]
For $|z|\le r$: $|a_k+|a_k|z|\le|a_k|(1+r)$ and $|1-\bar a_kz|\ge1-r$, so $|b_k-1|\le(1-|a_k|)\frac{1+r}{1-r}$.</li>
<li><em>Products.</em> These bounds are summable, so Lemma 10.4.1 (with $U=D(0,1)$ and $u_k=b_k-1$) gives uniform convergence on each $\overline{D(0,r)}$ to a holomorphic $B$ whose zeros are those of the factors: $b_k$ vanishes only at $a_k$, simply.</li>
<li><em>$|B|\le1$.</em> Each factor is $\frac{|a_k|}{a_k}\varphi_{a_k}$, a rotation of the automorphism of Def. 12.13.1, so it maps the disk into itself (Lemma 12.13.2, Lecture 12). Directly, each factor has modulus $\lt1$ on the disk: $|1-\bar az|^2-|a-z|^2=(1-|a|^2)(1-|z|^2)\gt0$ for $|a|,|z|\lt1$ (expand both sides). So partial products have modulus $\lt1$, and so does their limit (at most $1$).</li>
</ol>
<p>With the previous exercise: the zero sets of bounded holomorphic functions on the disk are exactly the sequences with $\sum(1-|a_k|)\lt\infty$.</p>''')

ex('f11', 'Homework 2, Problem 3(a)', 'derangements',
r'''Let $D_n$ be the number of permutations of $\{1,\dots,n\}$ without fixed points ($D_0=1$). Choosing the set of fixed points gives $n!=\sum_k\binom nkD_{n-k}$. Deduce $\sum_nD_n\frac{z^n}{n!}=\frac{e^{-z}}{1-z}$ on $D(0,1)$. Show that $\frac{e^{-z}-e^{-1}}{1-z}$ extends to an entire function, and conclude $\big|\frac{D_n}{n!}-\frac1e\big|\le C_RR^{-n}$ for every $R\gt0$.''',
r'''Products of exponential generating functions multiply as $\sum a_n\frac{z^n}{n!}\cdot\sum b_n\frac{z^n}{n!}=\sum_n\big(\sum_k\binom nka_kb_{n-k}\big)\frac{z^n}{n!}$. For the entire function, write $e^{-z}-e^{-1}=e^{-1}(e^{1-z}-1)$. Finish with Cauchy's estimate (Cor. 6.5.2).''',
r'''<ol>
<li><em>Generating function.</em> With $a_k=1$ (so $\sum a_k\frac{z^k}{k!}=e^z$) and $b_m=D_m$, the identity $n!=\sum_k\binom nkD_{n-k}$ says $e^z\cdot\sum_nD_n\frac{z^n}{n!}=\sum_nn!\frac{z^n}{n!}=\frac1{1-z}$ for $|z|\lt1$ (products of absolutely convergent series, <a class="x" href="#A21">A.21</a>). Divide by $e^z$.</li>
<li><em>Entire.</em> $\frac{e^{-z}-e^{-1}}{1-z}=e^{-1}\,E(1-z)$ with $E(w):=\frac{e^w-1}w=\sum_{n\ge1}\frac{w^{n-1}}{n!}$ for $w\ne0$. The power series has infinite radius (<a class="x" href="#A19">A.19</a>), so it defines an entire function. (Equivalently: $E$ is holomorphic on $w\ne0$ and bounded near $0$, so the singularity is removable, Lemma 9.1.1.) So $H(z):=\frac{e^{-z}}{1-z}-\frac{e^{-1}}{1-z}$ is entire.</li>
<li><em>Coefficients.</em> $\frac{e^{-1}}{1-z}=\sum_ne^{-1}z^n$ for $|z|\lt1$, so on $D(0,1)$ the power series of $H$ has $n$-th coefficient $\frac{D_n}{n!}-\frac1e$. These are the Taylor coefficients $H^{(n)}(0)/n!$ (Theorem 6.6.1), so they are the same on every circle $|z|=R$ (Theorem 6.4.1). By Cauchy's estimate (Cor. 6.5.2) on $|z|=R$, the coefficient is at most $M_RR^{-n}$, $M_R:=\max_{|z|=R}|H|$.</li>
</ol>
<p>So $D_n/n!\to1/e$ faster than any geometric rate: the "probability that a random permutation has no fixed point" is $1/e$ to within $10^{-k}$ after very few terms. The single pole at $z=1$ gives the main term; there is no second singularity, hence no error term of geometric size.</p>''')

ex('f11', 'Homework 2, Problem 3(b)', 'horse races',
r'''A <b>finish</b> of $n$ horses, with ties allowed, is a list $(S_1,\dots,S_k)$ of nonempty sets partitioning $\{1,\dots,n\}$ ($S_1$ tied for first, and so on). Let $F_n$ be the number of finishes ($F_0:=1$); e.g. $F_2=3$, $F_3=13$. Show $\sum_nF_n\frac{z^n}{n!}=\frac1{2-e^z}$ near $0$.''',
r'''Let $F_{n,k}$ count finishes with exactly $k$ places and $\Phi_k(z):=\sum_nF_{n,k}\frac{z^n}{n!}$. Choosing $S_1$ ($j\ge1$ horses) gives $F_{n,k}=\sum_{j\ge1}\binom njF_{n-j,k-1}$, i.e. $\Phi_k=(e^z-1)\Phi_{k-1}$. So $\Phi_k=(e^z-1)^k$. Sum over $k$: a geometric series, for $|z|\lt\log2$.''',
r'''<ol>
<li>The recursion is the product rule of Exercise 6.11.5 with $a_0=0$, $a_j=1$ for $j\ge1$ ($\sum a_j\frac{z^j}{j!}=e^z-1$): $\Phi_k=(e^z-1)\Phi_{k-1}$, and $\Phi_0=1$, so $\Phi_k=(e^z-1)^k$.</li>
<li>$F_n=\sum_kF_{n,k}$ (a finite sum, $k\le n$). For $|z|\lt\log2$, $|e^z-1|\le e^{|z|}-1\lt1$, and all coefficients are $\ge0$, so the double series converges absolutely and may be summed over $k$ first (A.21):
\[ \sum_nF_n\frac{z^n}{n!}=\sum_k(e^z-1)^k=\frac1{1-(e^z-1)}=\frac1{2-e^z}. \]</li>
<li>Check: $\frac1{2-e^z}=\frac1{1-(z+\frac{z^2}2+\dots)}=1+z+\frac32z^2+\dots$, so $F_2=2!\cdot\frac32=3$. ✓</li>
</ol>''')

ex('f11', 'Homework 2, Problem 3(c)', 'asymptotics of horse races',
r'''Show that the poles of $\frac1{2-e^z}$ are the points $\log2+2\pi ik$, $k\in\mathbb Z$, all simple, and that $\frac1{2-e^z}-\frac1{2\log2}\cdot\frac1{1-z/\log2}$ extends holomorphically to $D(0,\rho)$, $\rho:=|\log2+2\pi i|=6.32\ldots$. Deduce $F_n=\frac{n!}{2(\log2)^{n+1}}+O(n!\,r^{-n})$ for every $r\lt\rho$.''',
r'''Residue at a simple pole: Prop. 6.8.4 (with $B=2-e^z$; the proof works for holomorphic $B$). Subtracting the principal part leaves a function holomorphic at $\log2$ (the $h$ of Prop. 6.8.2). Then Cauchy's estimate on $|z|=r$.''',
r'''<ol>
<li><em>Poles.</em> $2-e^z=0\iff e^z=2\iff z=\log2+2\pi ik$ (<a class="x" href="#C8">C.8</a>). With $B:=2-e^z$ and $\zeta$ one of these points, $B'(\zeta)=-e^\zeta=-2\ne0$, so $B(z)=(z-\zeta)B_1(z)$ with $B_1$ holomorphic and $B_1(\zeta)=B'(\zeta)$ (a zero of order $1$, Def. 6.7.2). So $\frac1B=\frac{1/B_1}{z-\zeta}$ has a simple pole (Def. 6.8.1) with residue $\frac1{B_1(\zeta)}=-\frac12$ (Def. 6.8.3). This is Prop. 6.8.4 with $A=1$; there $B$ is a polynomial, but the proof only uses this factorization.</li>
<li><em>Principal part at $\log2$.</em> $\frac{-1/2}{z-\log2}=\frac{1/2}{\log2-z}=\frac1{2\log2}\cdot\frac1{1-z/\log2}$, exactly the subtracted term. Subtracting the principal part leaves the function $h$ of Prop. 6.8.2, holomorphic on a punctured disk about $\log2$ and bounded there, hence holomorphic at $\log2$ too (Lemma 9.1.1; or directly from the power series formula for $h$).</li>
<li><em>The disk.</em> The other poles have $|\log2+2\pi ik|\ge|\log2+2\pi i|=\rho$ for $k\ne0$ (the imaginary part is at least $2\pi$ in size). So the difference $D(z)$ is holomorphic on $D(0,\rho)$.</li>
<li><em>Coefficients.</em> $\frac{F_n}{n!}=[z^n]\frac1{2-e^z}=\frac1{2\log2}\cdot\frac1{(\log2)^n}+[z^n]D$ (Taylor coefficients at $0$, Theorem 6.4.1, with $\frac1{1-z/\log2}=\sum(z/\log2)^n$). By Cauchy's estimate (Cor. 6.5.2) on $|z|=r$, $|[z^n]D|\le M_rr^{-n}$ for $r\lt\rho$. Multiply by $n!$. This is the same method as the stamp formula, Theorem 6.11.3: the poles nearest $0$ give the main term.</li>
</ol>
<p>The nearest singularity ($\log2\approx0.693$) gives the main term $\frac{n!}{2(\log2)^{n+1}}$; the next ones ($\log2\pm2\pi i$) control the error. This is the "analytic combinatorics" principle stated in the homework.</p>''')

# ======================= PRACTICE MIDTERMS =======================
ex('h16', 'Practice midterm 1, Problem 1', 'a trigonometric integral',
r'''Compute $\displaystyle\int_0^{2\pi}\frac{d\theta}{5+3\cos\theta}$.''',
r'''Write it as a contour integral over $|z|=1$ with $z=e^{i\theta}$, $\cos\theta=\frac12(z+z^{-1})$, $d\theta=\frac{dz}{iz}$, as in Exercise 8.16.2.''',
r'''The integral becomes (as in Exercise 8.16.2) $\oint_{|z|=1}\frac{2\,dz}{i(3z^2+10z+3)}=\oint\frac{2\,dz}{3i(z+\frac13)(z+3)}$. Only $-\frac13$ is inside, a simple pole with residue $\frac{2}{3i(-\frac13+3)}=\frac{2}{8i}=\frac1{4i}$ (Prop. 6.8.4). By the residue theorem (Theorem 6.9.1), the integral is $2\pi i\cdot\frac1{4i}=\frac\pi2$. (Check: $\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}=\frac{2\pi}{\sqrt{a^2-b^2}}=\frac{2\pi}4$.)''')

ex('h16', 'Practice midterm 2, Problem 1', 'a trigonometric integral',
r'''Compute $\displaystyle\int_0^{2\pi}\frac{d\theta}{5-4\sin\theta}$.''',
r'''$\sin\theta=\frac1{2i}(z-z^{-1})$, $d\theta=\frac{dz}{iz}$. Find which root of the denominator is inside $|z|=1$.''',
r'''$5-4\sin\theta=5+2i(z-z^{-1})$, and multiplying by $iz$: $i(5z+2iz^2-2i)=-(2z^2-5iz-2)$. So the integral is $-\oint_{|z|=1}\frac{dz}{2z^2-5iz-2}$. The roots of $2z^2-5iz-2$ are $\frac{5i\pm3i}4=2i,\frac i2$; only $\frac i2$ is inside. With $2z^2-5iz-2=2(z-2i)(z-\frac i2)$, the residue of $\frac{-1}{2(z-2i)(z-i/2)}$ at the simple pole $\frac i2$ is $\frac{-1}{2(-\frac{3i}2)}=\frac1{3i}$ (Prop. 6.8.4). By Theorem 6.9.1 the integral is $2\pi i\cdot\frac1{3i}=\frac{2\pi}3$. (Check: $\frac{2\pi}{\sqrt{25-16}}$.)''')

ex('h16', 'Practice midterm 3, Problem 1', 'a trigonometric integral',
r'''Compute $\displaystyle\int_0^{2\pi}\frac{d\theta}{3+2\sin\theta}$.''',
r'''As in the previous exercise; the roots of the denominator involve $\sqrt5$.''',
r'''$3+2\sin\theta=3-i(z-z^{-1})$; multiplying by $iz$ gives $z^2+3iz-1$. So the integral is $\oint_{|z|=1}\frac{dz}{z^2+3iz-1}$, with roots $z_{1,2}=\frac{(-3\pm\sqrt5)i}2$. Only $z_1=\frac{(-3+\sqrt5)i}2\approx-0.38i$ is inside; the residue at this simple pole is $\frac1{z_1-z_2}=\frac1{i\sqrt5}$ (Prop. 6.8.4). By Theorem 6.9.1 the integral is $2\pi i\cdot\frac1{i\sqrt5}=\frac{2\pi}{\sqrt5}$. (Check: $\frac{2\pi}{\sqrt{9-4}}$.)''')

ex('f5', 'Practice midterm 1, Problem 2(a)', 'a growth bound forces zero',
r'''Let $f$ be entire with $|f(z)|\le|z|^{5/2}$ for all $z\in\mathbb C$. Show that $f\equiv0$.''',
r'''Write $f=\sum a_nz^n$ and use Cauchy's estimate (Cor. 6.5.2) on $|z|=R$: once with $R\to\infty$, once with $R\to0$. (Compare Remark 12.16.4.)''',
r'''$f$ is entire, so $f=\sum a_nz^n$ on all of $\mathbb C$, with $a_n=f^{(n)}(0)/n!$ independent of the circle used (Theorems 6.4.1 and 6.6.1). By Cauchy's estimate (Cor. 6.5.2) on $|z|=R$, with $M=\max_{|z|=R}|f|\le R^{5/2}$, $|a_n|\le R^{5/2}R^{-n}=R^{5/2-n}$ for every $R\gt0$. For $n\ge3$ the exponent is negative: let $R\to\infty$, so $a_n=0$. For $n\le2$ it is positive: let $R\to0$, so $a_n=0$. Hence $f\equiv0$. (In words: the bound makes $f$ grow too slowly at $\infty$ for degree $\ge3$, and vanish too fast at $0$ for degree $\le2$.)''')

ex('f5', 'Practice midterm 2, Problem 2(a)', 'polynomial times exponential',
r'''Let $f$ be entire with $|f(z)|\le(1+|z|)\,|e^z|$ for all $z$. Show that $f(z)=(a+bz)e^z$ for some $a,b\in\mathbb C$.''',
r'''Consider $g:=f\,e^{-z}$, and apply Cauchy's estimate to $g$.''',
r'''$g:=fe^{-z}$ is entire (a product of entire functions) with $|g|=|f|\,|e^z|^{-1}\le1+|z|$. Write $g=\sum b_nz^n$ (Theorem 6.4.1; the $b_n=g^{(n)}(0)/n!$ do not depend on $R$, Theorem 6.6.1). Cauchy's estimate (Cor. 6.5.2) on $|z|=R$: $|b_n|\le(1+R)R^{-n}\to0$ as $R\to\infty$ for $n\ge2$. So $g(z)=a+bz$ and $f=(a+bz)e^z$. This is Remark 12.16.4 with $k=1$.''')

ex('f6', 'Practice midterm 3, Problem 2(a)', 'a bound on the derivative',
r'''Let $f$ be entire with $|f'(z)|\le1+|z|$ for all $z$. Show that $f$ is a polynomial of degree at most $2$.''',
r'''$f'$ is entire (Cor. 6.6.2). Apply Cauchy's estimate to $f'$.''',
r'''$f'$ is entire (Cor. 6.6.2), and Cauchy's estimate (Cor. 6.5.2) on $|z|=R$ gives its Taylor coefficients $|c_n|\le(1+R)R^{-n}\to0$ for $n\ge2$. So $f'(z)=\alpha+\beta z$. The coefficients of $f$ are $a_{n+1}=\frac{c_n}{n+1}$ (Theorem 6.6.1: $a_n=f^{(n)}(0)/n!$), so $f(z)=a_0+\alpha z+\frac\beta2z^2$.''')

ex('k2', 'Practice midterm 1, Problem 2(b)', 'prescribed values at $1/n$',
r'''Is there an entire function $f$ with $f(\frac1n)=\frac1{n^2}$ for all integers $n\ge1$, and $f(2)=2$?''',
r'''Which entire function takes the values $\frac1{n^2}$ at $\frac1n$? Use the identity theorem (Theorem 10.1.1).''',
r'''No. $f$ and $z^2$ are entire and agree at the points $\frac1n\to0\in\mathbb C$, so $f=z^2$ on the connected (<a class="x" href="#C4">C.4</a>) set $\mathbb C$ by the identity theorem, Theorem 10.1.1 (the limit point $0$ lies in $\mathbb C$, and $\frac1n\ne0$). Then $f(2)=4\ne2$.''')

ex('k2', 'Practice midterm 2, Problem 2(b)', 'zeros at $1/n$ or at $n$',
r'''Is there an entire function $f\not\equiv0$ with $f(\frac1n)=0$ for all integers $n\ge1$? Is there one with $f(n)=0$ for all integers $n\ge1$?''',
r'''Where do the zeros accumulate in each case?''',
r'''First: no. The zeros $\frac1n$ accumulate at $0\in\mathbb C$, so $f\equiv0$ by the identity theorem, Theorem 10.1.1 (with $g=0$; compare Cor. 1.3.2). Second: yes, for example $\sin\pi z$. The zeros $1,2,3,\dots$ have no limit point in $\mathbb C$, so the identity theorem says nothing. (Any sequence $|a_k|\to\infty$ is the zero set of an entire function: Theorem 10.11.1.)''')

ex('k2', 'Practice midterm 3, Problem 2(b)', 'holomorphic on the disk but not entire',
r'''Is there a holomorphic $f:D(0,1)\to\mathbb C$ with $f(\frac1n)=\frac1{n+1}$ for all integers $n\ge2$? Is there an entire one?''',
r'''Write $\frac1{n+1}$ as a function of $\frac1n$. For the entire question, where would that function have to be singular?''',
r'''<ul>
<li><em>On the disk: yes.</em> $\frac1{n+1}=\frac{1/n}{1+1/n}$, so $f(z)=\frac z{1+z}$ works; its only pole, $-1$, is outside $D(0,1)$. (It is the only one, by Theorem 10.1.1 on the connected set $D(0,1)$.)</li>
<li><em>Entire: no.</em> If $F$ were entire with these values, then $F$ and $\frac z{1+z}$ are holomorphic on the connected (<a class="x" href="#C4">C.4</a>) open set $\mathbb C\setminus\{-1\}$ and agree at the points $\frac1n\to0$, so $F=\frac z{1+z}$ on all of $\mathbb C\setminus\{-1\}$ by the identity theorem (Theorem 10.1.1). But $\frac z{1+z}\to\infty$ as $z\to-1$, while $F$ is continuous at $-1$. Contradiction.</li>
</ul>''')

ex('m10', 'Practice midterm 2, Problem 3', 'counting solutions with Rouché',
r'''Let $n\ge1$ and $|a|\gt e$. Show that $e^z=az^n$ has exactly $n$ solutions in $D(0,1)$, counted with multiplicity.''',
r'''Which of $az^n$ and $e^z$ is bigger on $|z|=1$?''',
r'''On $|z|=1$: $|az^n|=|a|\gt e\ge e^{\operatorname{Re}z}=|e^z|$. Take $f=az^n$ and $g=az^n-e^z$ in Theorem 11.10.1: $|f-g|=|e^z|\lt|f|$, so $g$ has as many zeros in $D(0,1)$ as $az^n$, namely $n$ (a zero of order $n$ at $0$, Def. 7.1.1). The zeros of $g$ are exactly the solutions of $e^z=az^n$.''')

ex('m10', 'Practice midterm 3, Problem 3', 'one real zero',
r'''Show that $p(z)=z^4+6z+3$ has exactly one zero in $D(0,1)$, counted with multiplicity, and that this zero is real.''',
r'''Compare $p$ with $6z$ on $|z|=1$. For "real": coefficients are real, so non-real zeros come in conjugate pairs.''',
r'''<ol>
<li><em>Rouché.</em> On $|z|=1$, $|p-6z|=|z^4+3|\le4\lt6=|6z|$. By Theorem 11.10.1 (with $f=6z$, $g=p$), $p$ has as many zeros in $D(0,1)$ as $6z$: exactly one.</li>
<li><em>Real.</em> $p(-1)=1-6+3=-2\lt0$ and $p(0)=3\gt0$, so $p$ has a real zero in $(-1,0)\subset D(0,1)$ (intermediate value theorem, <a class="x" href="#A24">A.24</a>). It is the only one. (Alternatively: $p$ has real coefficients, so $\overline{p(z)}=p(\bar z)$; a non-real zero $z_0$ in the disk would bring $\bar z_0\ne z_0$, giving two.)</li>
</ol>''')

ex('n11', 'Practice midterm 1, Problem 4(a)', 'a sector onto the disk',
r'''Find a conformal map $F$ of the sector $\{z\ne0:0\lt\arg z\lt\frac\pi3\}$ onto $D(0,1)$.''',
r'''First map the sector onto $\mathbb H$ with a power of $z$ (compare Example 12.10.2), then use the Cayley map (Prop. 12.4.1).''',
r'''$z\mapsto z^3$ maps the sector onto $\mathbb H$, as $z^2$ maps the quadrant onto $\mathbb H$ in Example 12.10.2: $z=re^{i\theta}$ with $0\lt\theta\lt\frac\pi3$ goes to $r^3e^{3i\theta}$, $3\theta\in(0,\pi)$, and every point of $\mathbb H$ has exactly one such preimage (modulus and argument determine $r$ and $\theta$). So $z^3$ is a holomorphic bijection of the sector onto $\mathbb H$, a conformal map (Def. 12.9.2). Compose with the Cayley map $C$ (Prop. 12.4.1), a conformal map of $\mathbb H$ onto $D(0,1)$:
\[ F(z)=\frac{z^3-i}{z^3+i}. \]
A composition of conformal maps is conformal (Def. 12.9.2).''')

ex('n11', 'Practice midterm 2, Problem 4(a)', 'the slit plane onto the disk',
r'''Find a conformal map $F$ of the slit plane $\Omega:=\mathbb C\setminus(-\infty,0]$ onto $D(0,1)$.''',
r'''A square root maps $\Omega$ onto the right half-plane $\{\operatorname{Re}w\gt0\}$. Which Möbius map sends the right half-plane to the disk?''',
r'''<ol>
<li>The principal square root $\sqrt z=\sqrt r\,e^{i\theta/2}$ ($z=re^{i\theta}$, $-\pi\lt\theta\lt\pi$; <a class="x" href="#C8">C.8</a>) is a bijection of $\Omega$ onto $\{\operatorname{Re}w\gt0\}$: arguments in $(-\pi,\pi)$ go to $(-\frac\pi2,\frac\pi2)$. It is holomorphic: it is the inverse of the injective holomorphic map $w\mapsto w^2$ on the right half-plane, so Theorem 12.9.1 applies (or see <a class="x" href="#C8">C.8</a>).</li>
<li>$w\mapsto\frac{w-1}{w+1}$ maps the right half-plane onto the disk: $|w-1|\lt|w+1|\iff\operatorname{Re}w\gt0$ (closer to $1$ than to $-1$), and it is invertible, $w=\frac{1+\zeta}{1-\zeta}$, as in Prop. 12.4.1. (It is the Cayley map after rotating by $i$.)</li>
</ol>
So $F(z)=\dfrac{\sqrt z-1}{\sqrt z+1}$, a composition of conformal maps, hence conformal (Def. 12.9.2).''')

ex('n11', 'Practice midterm 3, Problem 4(a)', 'the upper half-disk onto the disk',
r'''Find a conformal map $F$ of the upper half-disk $D^+:=\{|z|\lt1,\ \operatorname{Im}z\gt0\}$ onto $D(0,1)$. You may use without proof that $w=\frac{1+z}{1-z}$ maps $D^+$ onto the quadrant $\{\operatorname{Re}w\gt0,\operatorname{Im}w\gt0\}$.''',
r'''Then square (Example 12.10.2), then apply the Cayley map.''',
r'''Quadrant $\xrightarrow{w^2}\mathbb H\xrightarrow{C}D(0,1)$: squaring maps the quadrant onto $\mathbb H$ bijectively (Example 12.10.2), and the Cayley map $C$ maps $\mathbb H$ onto the disk (Prop. 12.4.1). So with $w=\frac{1+z}{1-z}$,
\[ F(z)=\frac{w^2-i}{w^2+i}=\frac{(1+z)^2-i(1-z)^2}{(1+z)^2+i(1-z)^2}. \]
Each step is a conformal map, so the composition is one (Def. 12.9.2).''')

ex('n14', 'Practice midterm 1, Problem 4(b)', 'a double zero at the origin',
r'''Let $f:D(0,1)\to D(0,1)$ be holomorphic with $f(0)=f'(0)=0$. Let $g(z):=f(z)/z$ for $z\ne0$, $g(0):=0$. (i) Show $g$ is holomorphic on $D(0,1)$. (ii) Show $g$ maps $D(0,1)$ into $D(0,1)$. (iii) Apply the Schwarz lemma to $g$ to conclude $|f(z)|\le|z|^2$.''',
r'''(i) Lemma 9.1.1. (ii) The Schwarz lemma for $f$ gives $|g|\le1$; rule out $|g|=1$ at an interior point using $g(0)=0$ and Remark 12.7.2.''',
r'''<ol type="i">
<li>$\frac{f(z)}z=\frac{f(z)-f(0)}z\to f'(0)=0$ as $z\to0$: bounded near $0$, so removable (Lemma 9.1.1), with value $0$.</li>
<li>By the Schwarz lemma for $f$ (Theorem 12.14.1), $|f(z)|\le|z|$, so $|g|\le1$. If $|g(z_0)|=1$ for some $z_0$, then $|g|$ has an interior maximum, so $g$ is constant (Remark 12.7.2), contradicting $g(0)=0$. So $|g|\lt1$.</li>
<li>$g$ maps the disk into itself with $g(0)=0$, so $|g(z)|\le|z|$ by the Schwarz lemma (Theorem 12.14.1), i.e. $|f(z)|\le|z|^2$.</li>
</ol>''')

ex('n14', 'Practice midterm 2, Problem 4(b)', 'Schwarz on the half-plane',
r'''Let $f:\mathbb H\to\mathbb H$ be holomorphic with $f(i)=i$. Let $C(z)=\frac{z-i}{z+i}$ and $g:=C\circ f\circ C^{-1}$. (i) Show $g$ maps $D(0,1)$ into $D(0,1)$, $g(0)=0$, and deduce $|g'(0)|\le1$. (ii) Show $g'(0)=f'(i)$. (iii) Conclude $|f'(i)|\le1$, and check equality for $f(z)=-1/z$.''',
r'''(ii) Chain rule, with $(C^{-1})'(0)=1/C'(i)$ (Theorem 12.9.1).''',
r'''<ol type="i">
<li>$C^{-1}$ maps the disk to $\mathbb H$, $f$ maps $\mathbb H$ to $\mathbb H$, and $C$ maps $\mathbb H$ to the disk (Prop. 12.4.1). $g$ is holomorphic as a composition. $g(0)=C(f(C^{-1}(0)))=C(f(i))=C(i)=0$. Schwarz lemma (Theorem 12.14.1): $|g'(0)|\le1$.</li>
<li>Chain rule: $g'(0)=C'(f(i))\,f'(i)\,(C^{-1})'(0)=C'(i)\,f'(i)\,\frac1{C'(i)}=f'(i)$, using $C^{-1}(0)=i$ and $(C^{-1})'(0)=1/C'(i)$ from the inverse theorem (Theorem 12.9.1). (Explicitly $C'(z)=\frac{2i}{(z+i)^2}$, so $C'(i)=\frac1{2i}$.)</li>
<li>$|f'(i)|=|g'(0)|\le1$. For $f(z)=-\frac1z$: if $z=re^{i\theta}$ with $0\lt\theta\lt\pi$, then $-\frac1z=\frac1re^{i(\pi-\theta)}\in\mathbb H$; $f(i)=-\frac1i=i$; and $f'(z)=\frac1{z^2}$, so $f'(i)=-1$, $|f'(i)|=1$.</li>
</ol>''')

ex('n14', 'Practice midterm 3, Problem 4(b)', 'moving the zero to the centre',
r'''Let $f:D(0,1)\to D(0,1)$ be holomorphic with $f(\frac12)=0$. Let $\varphi(z):=\frac{\frac12-z}{1-\frac12z}$ and $g:=f\circ\varphi$. (i) Show $g$ maps $D(0,1)$ into $D(0,1)$ and $g(0)=0$. (ii) Show $f(0)=g(\frac12)$, and conclude $|f(0)|\le\frac12$. (iii) Find an $f$ with $f(\frac12)=0$ and $|f(0)|=\frac12$.''',
r'''$\varphi=\varphi_{1/2}$ of Lemma 12.13.2: it swaps $0$ and $\frac12$.''',
r'''<ol type="i">
<li>$\varphi=\varphi_{1/2}$ in the notation of Def. 12.13.1, an automorphism of the disk (Lemma 12.13.2), so $g=f\circ\varphi$ maps the disk into itself, and $g(0)=f(\varphi(0))=f(\frac12)=0$.</li>
<li>$\varphi(\frac12)=0$ (Lemma 12.13.2), so $g(\frac12)=f(\varphi(\frac12))=f(0)$. Schwarz lemma (Theorem 12.14.1) for $g$: $|f(0)|=|g(\frac12)|\le\frac12$.</li>
<li>$f=\varphi$ itself: it maps the disk into itself (Lemma 12.13.2), $f(\frac12)=0$ and $f(0)=\frac12$. (So does any $e^{i\theta}\varphi$.)</li>
</ol>''')
