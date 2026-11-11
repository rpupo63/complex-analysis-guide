#!/usr/bin/env node
// Typeset every formula of the built page at build time, so the browser does no MathJax work.
//
//     node tools/prerender.mjs [build/guide.html] [build/index.html]
//
// Reads the TeX settings from theme/mathjax-config.js (the same ones the browser used), renders
// with mathjax-full 3.2.2 to SVG with one shared glyph cache, and removes the MathJax <script>s.
import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {mathjax} from 'mathjax-full/js/mathjax.js';
import {TeX} from 'mathjax-full/js/input/tex.js';
import {SVG} from 'mathjax-full/js/output/svg.js';
import {liteAdaptor} from 'mathjax-full/js/adaptors/liteAdaptor.js';
import {RegisterHTMLHandler} from 'mathjax-full/js/handlers/html.js';
import 'mathjax-full/js/input/tex/AllPackages.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const src = process.argv[2] || path.join(root, 'build/guide.html');
const out = process.argv[3] || path.join(root, 'build/index.html');

const sandbox = {window: {}};
vm.runInNewContext(fs.readFileSync(path.join(root, 'theme/mathjax-config.js'), 'utf8'), sandbox);
const cfg = sandbox.window.MathJax;

// The browser's tex-svg.js loads these packages, plus the ones its autoloader would pull in on use.
// 'physics' is left out, as in the browser: it redefines \Re, \Im and \div.
const packages = ['base', 'ams', 'newcommand', 'noundefined', 'configmacros', 'html', 'action', 'amscd',
  'bbox', 'boldsymbol', 'braket', 'cancel', 'cases', 'centernot', 'color', 'colortbl', 'empheq', 'enclose',
  'extpfeil', 'gensymb', 'mathtools', 'mhchem', 'upgreek', 'unicode', 'verb'];

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
let html = fs.readFileSync(src, 'utf8')
  .replace(/<script>\s*window\.MathJax\s*=[\s\S]*?<\/script>\s*/, '')
  .replace(/<script src="[^"]*mathjax[^"]*"><\/script>\s*/, '');
const doc = mathjax.document(html, {
  InputJax: new TeX({...cfg.tex, packages}),
  OutputJax: new SVG({fontCache: 'global'}),
});
doc.render();
const n = Array.from(doc.math).length;
// Drop attributes only MathJax's own (now absent) scripts read; keep the node types the SVG CSS styles.
html = (adaptor.doctype(doc.document) + adaptor.outerHTML(adaptor.root(doc.document)))
  .replace(/ data-c="[^"]*"/g, '')
  .replace(/ data-mml-node="(?!maction"|merror"|mtable")[^"]*"/g, '');
fs.writeFileSync(out, html);
console.log(`prerendered ${n} formulas -> ${path.relative(root, out)} (${html.length} bytes)`);
