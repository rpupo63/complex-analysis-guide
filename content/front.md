<header>
  <div class="eyebrow">A textbook companion · Lectures 1–15</div>
  <h1>Holomorphic Functions</h1>
  <p class="lede">A textbook built from the slides of a thirteen-lecture course in complex analysis. Part I asks whether a harmonic function is determined by, and can be found from, its boundary values, and answers with finite elements. Part II develops Cauchy's integral theory. Part III uses it to compute integrals and Fourier transforms and to prove the sampling theorem. Part IV studies entire functions through their zeros, ending with the Gamma function. Part V studies conformal maps and closes the circle: the solution of Part I's Dirichlet problem produces the Riemann map.</p>
<p>The main text follows the slides one by one, with every step justified. Background the slides take for granted is collected in a lettered appendix.</p>
</header>

<h3>How to read this guide</h3>
<p>Every numbered item is labelled by its logical status. A definition names something and cannot be wrong. A derived result is proved from earlier items. An assumption limits which situations the argument covers.</p>
<div class="legend">
  <div><span class="tag d">Defined</span> A name or convention we choose.</div>
  <div><span class="tag r">Derived</span> Proved here from earlier items.</div>
  <div><span class="tag a">Assumed</span> A hypothesis on $\Omega$, the grid, or $g$.</div>
  <div><span class="tag c">Cited</span> A standard result, used without proof; details in the appendix.</div>
</div>
<p>Three kinds of reference help you move around.</p>
<ul>
<li><b>Lecture notation.</b> Symbols the lecture defines, such as $\class{ntn-Vg}{V^g_\eps}$, $\class{ntn-Ue}{U_\eps}$, $\class{ntn-a}{a}(u,w)$ or $m_n$, are tinted inside formulas. Hover over one to see what it means. Click it (or, on a touch screen, tap it and use the link in the box) to go to its definition.</li>
<li><b>Numbered results.</b> Mentions of numbered items, such as @prop:v-g-eps-is-affine-not or @sec:s12, are links. Hovering shows the statement; clicking takes you there.</li>
<li><b>Background.</b> A dotted link with a small box, such as [Cauchy–Schwarz](apx:A12), goes to the appendix.</li>
</ul>
<p>Each lecture opens with an overview box: its goal, its main results, what it uses from earlier lectures and where it is used later. Exercises, where the slides have them, come with worked solutions that stay folded until you open them.</p>
<p>After any jump, the <b>Back</b> button in the corner returns you to where you clicked, one step at a time. Each appendix entry lists every place that cites it, and the outside references (Wikipedia and similar) are kept there.</p>

<h3 id="roadmap">How the course fits together</h3>
<p>The course was taught as a sequence of self-contained lectures. Read as a book, it falls into five parts.</p>
<div class="tbl"><table class="roadmap">
<thead><tr><th>Part</th><th>Question</th><th>Answer</th></tr></thead>
<tbody>
{{roadmap-rows}}
</tbody></table></div>

<p><b>Threads across the parts.</b> The parts were taught separately, but they lean on each other:</p>
<ul>
<li><em>Two views of one theory.</em> The real and imaginary parts of a holomorphic function are harmonic (@prop:if-satisfy-the-cauchy-riemann, @cor:holomorphic-functions-are-smooth), and the mean value property of Part I (@thm:mean-value-property) is Cauchy's formula of Part II (@thm:cauchys-integral-formula) at the centre of the circle.</li>
<li><em>Part I's tools reused in Part IV.</em> Jensen's formula is the mean value property applied to $\log|f|$, the potential of point charges at the zeros (@sec:j3, @lem:the-mean-of-a-logarithmic-potential, [logarithmic potential](apx:E6)); the maximum modulus lemma is Lecture 4's maximum principle (@lem:maximum-modulus, @cor:maximum-principle).</li>
<li><em>Uniform limits.</em> Harmonic (@cor:uniform-limits) and holomorphic (@thm:uniform-limits) functions survive uniform limits for the same reason: an integral formula with no derivatives in it.</li>
<li><em>Promises kept.</em> Lecture 1 announced the identity theorem and isolated zeros (@thm:identity-theorem, @cor:isolated-zeros): they are proved as @thm:identity-theorem-l10 and @thm:isolated-zeros. Standing @asm:from-now-on-holomorphic-functions (smooth parts) is proved as @cor:holomorphic-functions-are-smooth. The Gaussian integral used in @sec:f18 and @sec:h3 is @cor:the-value-at-frac12-and-the; the Basel sum used in @lem:on-the-real-axis follows from Euler's product ([E.18](apx:E18)).</li>
<li><em>The circle closes.</em> Part I solved the Dirichlet problem on unions of squares (@thm:the-dirichlet-problem-on-a-union). Part V uses that solution, with boundary values $\log|z-z_0|$, to build the conformal map onto the disk (@thm:riemann-mapping-theorem); conversely, a conformal map moves Dirichlet problems to the disk (@cor:transporting-harmonic-functions). The harmonic conjugate of @lem:harmonic-conjugate-on-a-disk is Lecture 1's stream function.</li>
<li><em>Counting zeros.</em> The argument principle (@thm:argument-principle) leads to Rouché's theorem (@thm:rouche); Jensen's formula (@thm:jensens-formula) leads to Hadamard's theorem (@thm:hadamard).</li>
</ul>

<p><b>Recurring techniques.</b> A handful of moves do most of the work. Recognising them makes new proofs much shorter to read.</p>
<div class="tbl"><table>
<thead><tr><th>Technique</th><th>Examples</th></tr></thead>
<tbody>
<tr><td>Open and closed in a connected set: show the good set is nonempty, open and closed</td><td>@thm:strong-maximum-principle, @thm:isolated-zeros, @thm:identity-theorem-l10</td></tr>
<tr><td>The first nonzero Taylor coefficient dominates near the point</td><td>@thm:isolated-zeros, @lem:logarithmic-derivative, @prop:factorization-in-a-disk, @thm:identity-theorem-l10</td></tr>
<tr><td>Move the contour: Cauchy's theorem on the region between two curves</td><td>@lem:moving-the-circle, @prop:the-gaussian-is-its-own-transform, @thm:strips-and-decay, @thm:paley-wiener-a-simple-form</td></tr>
<tr><td>Estimate the added piece by length times maximum ([ML estimate](apx:A25))</td><td>@thm:power-series, @prop:counting-by-residues, @prop:x, @prop:for</td></tr>
<tr><td>Add a margin, prove a strict statement, let the margin go to $0$</td><td>@lem:comparison, @thm:cauchys-integral-formula, @thm:residue-theorem, @thm:step-4-boundary-values</td></tr>
<tr><td>Positivity: a one-sided bound, or energy, controls everything</td><td>@thm:uniqueness, @prop:step-2-its-energy-tends-to, @lem:lemma-b, @lem:no-zeros</td></tr>
<tr><td>Choose the radius to balance growth against decay</td><td>@cor:cauchys-estimate, @thm:upper-bound, @cor:counting-zeros, @thm:zeros-versus-order</td></tr>
</tbody></table></div>

<h3 id="problems">Homework and practice midterms</h3>
<p>Every problem from the two homework sets and the three practice midterms appears as an exercise, placed in the section that supplies the last tool it needs. Each has a hidden hint (the official hint where the sheet gives one) and a full solution. The practice midterms share a pattern: Problem 1 is a trigonometric integral by residues (Lecture 8), Problem 2 is growth bounds and the identity theorem (Lectures 6 and 10), Problem 3 is Rouché (Lecture 11), and Problem 4 is conformal maps and the Schwarz lemma (Lecture 12).</p>
{{problems-table}}
<h3>Contents</h3>
{{toc}}<p class="toc-unit">Reference</p>
<ol class="toc">
  <li><span class="n">Roadmap</span><a href="#roadmap">How the course fits together</a></li>
  <li><span class="n">Problems</span><a href="#problems">Homework and practice midterms</a></li>
  <li><span class="n">Index</span><a href="#index">Index of the main text</a></li>
  <li><span class="n">Notation</span><a href="#notation">Index of notation</a></li>
  <li><span class="n">App. A</span><a href="#apxA">Calculus and analysis</a></li>
  <li><span class="n">App. B</span><a href="#apxB">Linear algebra</a></li>
  <li><span class="n">App. C</span><a href="#apxC">Sets and topology</a></li>
  <li><span class="n">App. D</span><a href="#apxD">Function spaces</a></li>
  <li><span class="n">App. E</span><a href="#apxE">Context and previews</a></li>
</ol>

