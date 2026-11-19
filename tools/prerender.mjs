#!/usr/bin/env node
// Typeset every formula of the built page at build time, so the browser does no MathJax work.
//
//     node tools/prerender.mjs [build/guide.html] [build/index.html]
//
// Reads the TeX settings from theme/mathjax-config.js and renders with MathJax 4 to SVG.
// Formulas are split at operators into pieces the browser can wrap, so a formula that does
// not fit the column continues on the next line instead of scrolling sideways.
import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {mathjax} from '@mathjax/src/js/mathjax.js';
import {TeX} from '@mathjax/src/js/input/tex.js';
import {SVG} from '@mathjax/src/js/output/svg.js';
import {liteAdaptor} from '@mathjax/src/js/adaptors/liteAdaptor.js';
import {RegisterHTMLHandler} from '@mathjax/src/js/handlers/html.js';
import {STATE} from '@mathjax/src/js/core/MathItem.js';
import {handleRetriesFor} from '@mathjax/src/js/util/Retries.js';
import {length2em} from '@mathjax/src/js/util/lengths.js';
import {MmlMo} from '@mathjax/src/js/core/MmlTree/MmlNodes/mo.js';
import '@mathjax/src/js/util/asyncLoad/esm.js';
import '@mathjax/src/js/input/tex/ams/AmsConfiguration.js';
import '@mathjax/src/js/input/tex/newcommand/NewcommandConfiguration.js';
import '@mathjax/src/js/input/tex/noundefined/NoUndefinedConfiguration.js';
import '@mathjax/src/js/input/tex/configmacros/ConfigMacrosConfiguration.js';
import '@mathjax/src/js/input/tex/html/HtmlConfiguration.js';
import '@mathjax/src/js/input/tex/action/ActionConfiguration.js';
import '@mathjax/src/js/input/tex/amscd/AmsCdConfiguration.js';
import '@mathjax/src/js/input/tex/bbox/BboxConfiguration.js';
import '@mathjax/src/js/input/tex/boldsymbol/BoldsymbolConfiguration.js';
import '@mathjax/src/js/input/tex/braket/BraketConfiguration.js';
import '@mathjax/src/js/input/tex/cancel/CancelConfiguration.js';
import '@mathjax/src/js/input/tex/cases/CasesConfiguration.js';
import '@mathjax/src/js/input/tex/centernot/CenternotConfiguration.js';
import '@mathjax/src/js/input/tex/color/ColorConfiguration.js';
import '@mathjax/src/js/input/tex/colortbl/ColortblConfiguration.js';
import '@mathjax/src/js/input/tex/empheq/EmpheqConfiguration.js';
import '@mathjax/src/js/input/tex/enclose/EncloseConfiguration.js';
import '@mathjax/src/js/input/tex/extpfeil/ExtpfeilConfiguration.js';
import '@mathjax/src/js/input/tex/gensymb/GensymbConfiguration.js';
import '@mathjax/src/js/input/tex/mathtools/MathtoolsConfiguration.js';
import '@mathjax/src/js/input/tex/mhchem/MhchemConfiguration.js';
import '@mathjax/src/js/input/tex/upgreek/UpgreekConfiguration.js';
import '@mathjax/src/js/input/tex/unicode/UnicodeConfiguration.js';
import '@mathjax/src/js/input/tex/verb/VerbConfiguration.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const src = process.argv[2] || path.join(root, 'build/guide.html');
const out = process.argv[3] || path.join(root, 'build/index.html');

// Keep an equals sign at the end of the line. The operator default is to jump to the next line.
MmlMo.defaults.linebreakstyle = 'after';

// \, \: \; are spaces inside one term (an integrand, a product). \quad and \qquad separate clauses.
const origMarkBreaks = SVG.prototype.markInlineBreaks;
SVG.prototype.markInlineBreaks = function(node) {
  tightenBreaks(node);
  return origMarkBreaks.call(this, node);
};
function tightenBreaks(node) {
  if (!node || !node.childNodes) return;
  for (const child of node.childNodes) {
    if (child.isKind && child.isKind('mspace')) {
      const lb = child.attributes.get('linebreak');
      if ((lb === 'auto' || lb == null) && length2em(String(child.attributes.get('width'))) < 0.9) {
        child.attributes.set('linebreak', 'nobreak');
      }
    }
    tightenBreaks(child);
  }
}

// v4.1.3 reads math.display once, to decide whether to insert soft breaks, and that read is
// the only one that should see "inline". Later reads choose display style and must stay true.
const origToDOM = SVG.prototype.toDOM;
SVG.prototype.toDOM = function(math, node, html = null) {
  if (!math.display || !this.options.linebreaks.inline) return origToDOM.call(this, math, node, html);
  let reads = 0;
  Object.defineProperty(math, 'display', {
    configurable: true,
    get() { reads += 1; return reads > 1; },
  });
  try {
    return origToDOM.call(this, math, node, html);
  } finally {
    Object.defineProperty(math, 'display', {configurable: true, writable: true, value: true});
  }
};

const sandbox = {window: {}};
vm.runInNewContext(fs.readFileSync(path.join(root, 'theme/mathjax-config.js'), 'utf8'), sandbox);
const cfg = sandbox.window.MathJax;

// 'physics' is left out, as in the browser build: it redefines \Re, \Im and \div.
const packages = ['base', 'ams', 'newcommand', 'noundefined', 'configmacros', 'html', 'action', 'amscd',
  'bbox', 'boldsymbol', 'braket', 'cancel', 'cases', 'centernot', 'color', 'colortbl', 'empheq', 'enclose',
  'extpfeil', 'gensymb', 'mathtools', 'mhchem', 'upgreek', 'unicode', 'verb'];

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const svg = new SVG({fontCache: 'global', displayOverflow: 'linebreak', linebreaks: {inline: true, width: '100%'}});
// The lite adaptor cannot measure a container, and a zero width makes the ex-size NaN.
// Width used when a display formula cannot wrap in the browser (an alignment or a matrix).
// 300 of MathJax's px becomes about 240px of SVG, which still fits a padded phone column.
svg.getMetrics = (html) => {
  for (const math of html.math) {
    if (math.state() < STATE.METRICS) {
      math.setMetrics(16, 8, 300, 1);
      math.state(STATE.METRICS);
    }
  }
};
let html = fs.readFileSync(src, 'utf8')
  .replace(/<script>\s*window\.MathJax\s*=[\s\S]*?<\/script>\s*/, '')
  .replace(/<script src="[^"]*mathjax[^"]*"><\/script>\s*/, '');
const doc = mathjax.document(html, {
  InputJax: new TeX({
    ...cfg.tex,
    packages,
    inlineMath: cfg.tex.inlineMath,
    displayMath: cfg.tex.displayMath,
  }),
  OutputJax: svg,
});
await handleRetriesFor(() => doc.render());
adaptor.append(adaptor.head(doc.document), svg.styleSheet(doc));
const n = Array.from(doc.math).length;
// The lite adaptor drops the doctype; put it back so the page renders in standards mode.
// Soft-broken display math is marked justify="left"; the guide centers display formulas.
html = ('<!doctype html>\n' + adaptor.outerHTML(adaptor.root(doc.document)))
  .replace(/ data-c="[^"]*"/g, '')
  .replace(/ data-latex="[^"]*"/g, '')
  .replace(/ data-mml-node="(?!maction"|merror"|mtable")[^"]*"/g, '')
  .replace(/ justify="left"/g, '');
fs.writeFileSync(out, html);
console.log(`prerendered ${n} formulas -> ${path.relative(root, out)} (${html.length} bytes)`);
