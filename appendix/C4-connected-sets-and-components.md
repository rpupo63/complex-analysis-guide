---
id: C4
title: Connected sets and components
status:
- defined
- cited
---
<p>Let $S\subset\Omega$. $S$ is <em>closed in $\Omega$</em> if every limit of points of $S$ that lies in $\Omega$ is itself in $S$. (Limits outside $\Omega$, on $\class{ntn-dOm}{\partial\Omega}$, don't count.)</p>
<p>An open set $\Omega$ is <em>connected</em> if it cannot be split into two disjoint nonempty open sets. Equivalently, the only subsets of $\Omega$ that are both open and closed in $\Omega$ are $\emptyset$ and $\Omega$. This is the form used in @thm:strong-maximum-principle. For open sets in $\R^2$ it is equivalent (cited) to being <em>path-connected</em>: any two points can be joined by a continuous path inside $\Omega$. Disks are connected.</p>
<p>A <em>connected component</em> is a maximal connected subset. Every open set is the disjoint union of its components, and each component is open: a small disk about a point of the component lies in $\Omega$, is connected, and meets the component, so by maximality it lies in the component.</p>
<p>For a grid region the components are exactly the clusters used in @thm:a-ii-is-positive-definite: squares chained through shared edges. The proof there works with clusters directly, so it needs no general topology.</p>
<p class="ext">Further reading: <a href="https://en.wikipedia.org/wiki/Connected_space" target="_blank" rel="noopener">Connected space</a></p>
