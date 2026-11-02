---
label: ex:equilibrium-temperature-and-wifi
source: Homework 1, optional FreeFEM++ bonus
title: equilibrium temperature and WiFi
placement: s21
order: 1
---
<b>Part A.</b> On $\Omega=(0,4)\times(0,3)$, a radiator on $0.5\lt x\lt1.5$ of the bottom edge is held at $40°$, a window on $1.5\lt x\lt2.5$ of the top edge at $5°$, and the rest of the boundary at $15°$. Mesh $\Omega$ with separate boundary labels, solve $\Delta T=0$ with continuous $P_1$ elements, plot isotherms, and report the numerical minimum and maximum. How does the maximum principle check your result?<br>
<b>Part B.</b> Run the official FreeFEM++ tutorial <em>WiFi Propagation</em>, which models the field by $\Delta E+\frac{k^2}{n^2}E=0$ ($n$ the refractive index, complex inside walls; $E=1$ on a small circular hotspot). (1) Submit a mesh and a signal plot. (2) Identify the outer boundary, the walls and the hotspot in the code; explain <code>on(2,v=1)</code>. (3) The program uses $\iint_\Omega\big(\frac{k^2}{n^2}Ew-\nabla E\cdot\nabla w\big)\,dA$: explain why, starting from the equation. (4) Compare three hotspot positions with a stated coverage criterion. (5) Change the wall absorption and explain the difference.
<details class="sol"><summary>Hint</summary>
<ul>
<li>Part A: split the top and bottom borders where the boundary values change; plot the mesh before solving. The core of the script is
<pre>fespace Vh(Th,P1);
Vh T,v;
problem heat(T,v)
    = int2d(Th)(dx(T)*dx(v)+dy(T)*dy(v))
    + on(/* wall labels */,T=15)
    + on(/* window label */,T=5)
    + on(/* radiator label */,T=40);</pre>
This is exactly the weak form of @def:weak-form-of-the-dirichlet-problem, solved over $P_1$ (linear-on-triangles) functions instead of bilinear ones.</li>
<li>Check that $5\le T\le40$ up to round-off.</li>
<li>Part B(3): multiply the equation by $w$ and integrate the $\Delta E$ term by parts. The test function vanishes on the hotspot; the other boundaries carry the natural zero-normal-derivative condition.</li>
<li><code>wall()</code> distinguishes air from wall; <code>wallreflexion</code> and <code>wallabsorption</code> set the complex index. The hotspot has label $2$. The plotted quantity is <code>log(real(v)^2+imag(v)^2)</code>. Keep everything else fixed when comparing.</li>
</ul>
</details>
<details class="sol"><summary>Solution</summary>
<p>The plots and runs are computational and not reproduced here. The mathematical parts:</p>
<ul>
<li><b>Part A, maximum principle.</b> The temperature is harmonic (it is the solution of the Dirichlet problem, @def:dirichlet-problem, and the weak solution of @thm:existence-of-a-weak-solution is classical by @cor:the-lecture-3-limit-is-a), so its maximum and minimum over $\overline\Omega$ are attained on $\partial\Omega$ (@cor:maximum-principle), where the data take values $5$, $15$, $40$. So $5\le T\le40$ everywhere, and the extreme values occur on the window and the radiator. The discrete solution obeys the same bound by the discrete maximum principle (@thm:discrete-maximum-principle and @cor:a-bound are the versions for squares; for $P_1$ elements it holds on meshes without obtuse angles). A computed value outside $[5,40]$ beyond round-off signals a labelling or mesh error.</li>
<li><b>Part B(2).</b> <code>on(2,v=1)</code> imposes the Dirichlet condition $E=1$ on the boundary with label $2$, the hotspot circle: the analogue of fixing $U=g$ at the boundary nodes in @def:discrete-problem (the affine space $V^g_\eps$ of @def:by-lemma-3-6-2).</li>
<li><b>Part B(3), the weak form.</b> Multiply $\Delta E+\frac{k^2}{n^2}E=0$ by a test function $w$ vanishing on the hotspot and integrate. By Green's identity ([A.6](apx:A6)),
\[ \iint_\Omega(\Delta E)w\,dA=\oint_{\partial\Omega}w\,\partial_nE\,ds-\iint_\Omega\nabla E\cdot\nabla w\,dA. \]
The boundary integral vanishes: on the hotspot $w=0$, and on the outer boundary the natural condition is $\partial_nE=0$. So $\iint_\Omega\big(\frac{k^2}{n^2}Ew-\nabla E\cdot\nabla w\big)dA=0$ for all such $w$, which is what the program solves. Compare @sec:s4, where the same integration by parts (@prop:the-slides-computation) turns $\Delta u=0$ into $a(u,w)=0$, the weak form of @def:weak-form-of-the-dirichlet-problem.</li>
<li><b>Part B(4)–(5).</b> Any clearly stated criterion is acceptable (for instance, the area where the plotted log-power is below a threshold). More absorption makes the field decay faster through walls, so rooms separated from the hotspot by more walls get weaker signal; less absorption gives more reflection and interference patterns.</li>
</ul>
</details>
