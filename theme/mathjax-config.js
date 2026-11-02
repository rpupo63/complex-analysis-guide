window.MathJax = {
  loader: { load: ['[tex]/html'] },
  tex: { packages: {'[+]': ['html']}, inlineMath: [['$','$']], displayMath: [['\\[','\\]']],
    macros: { eps: '\\varepsilon', R: '\\mathbb{R}', norm: ['\\lVert #1 \\rVert', 1] } },
  svg: { fontCache: 'global' }
};
