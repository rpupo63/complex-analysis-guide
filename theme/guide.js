(function(){
  var NOTE = __NOTE__;
  var stack = [];
  var btn = document.getElementById('backbtn');
  var lbl = btn.querySelector('.lbl');
  var cnt = btn.querySelector('.cnt');
  var tip = document.getElementById('tip');
  var mq = function(q){ return window.matchMedia ? window.matchMedia(q).matches : false; };
  var reduce = mq('(prefers-reduced-motion: reduce)');
  var canHover = mq('(hover: hover) and (pointer: fine)');
  var showT = null, hideT = null, cur = null;

  function ntKey(el){
    var c = el.getAttribute && el.getAttribute('class');
    var m = c && c.match(/ntn-(\w+)/);
    return m ? m[1] : null;
  }
  function trigger(el){
    if (!el || !el.closest || tip.contains(el)) return null;
    return el.closest('[class*="ntn-"], a.ir, a.x');
  }
  function anchorEl(el){
    // SVG pieces cannot be scrolled to or flashed nicely; use their formula
    return (el.closest && el.closest('mjx-container')) || el;
  }
  function whereOf(el){
    var apx = el.closest('.apx');
    if (apx) return 'Appendix ' + apx.querySelector('.apx-n').textContent;
    var sec = el.closest('section');
    var s = sec && sec.querySelector('.eyebrow') ? sec.querySelector('.eyebrow').textContent : 'the introduction';
    var env = el.closest('.env[data-label]');
    if (!env){
      var pr = el.closest('.proof');
      if (pr){
        var p = pr.previousElementSibling;
        while (p && !(p.matches && p.matches('.env[data-label]'))) p = p.previousElementSibling;
        env = p;
      }
    }
    return s + (env ? ' · ' + env.getAttribute('data-label') : '');
  }

  // ---------- jumping and going back ----------
  function flash(el){
    el.classList.remove('flash'); void el.offsetWidth; el.classList.add('flash');
  }
  function go(el){
    // Off-screen sections are not laid out (content-visibility), so a long smooth scroll aims at a
    // position that moves while it runs. Jump far targets instantly, then re-aim once laid out.
    var near = Math.abs(el.getBoundingClientRect().top) < 2 * innerHeight;
    el.scrollIntoView({behavior: reduce || !near ? 'auto' : 'smooth', block: 'center'});
    if (!near) requestAnimationFrame(function(){ requestAnimationFrame(function(){
      el.scrollIntoView({block: 'center'});
    }); });
    flash(el);
  }
  function update(){
    if (!stack.length){ btn.hidden = true; return; }
    btn.hidden = false;
    lbl.textContent = 'Back to ' + stack[stack.length-1].label;
    cnt.textContent = stack.length > 1 ? '(' + stack.length + ')' : '';
  }
  function jump(target, fromEl, label){
    hideTip(true);
    stack.push({el: anchorEl(fromEl), label: label});
    go(target); update();
  }
  btn.addEventListener('click', function(){
    var s = stack.pop();
    if (s){ go(s.el); try { s.el.focus({preventScroll:true}); } catch(_){} }
    update();
  });

  // ---------- tooltip ----------
  function esc(t){ return String(t).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function stripIds(node){
    if (node.removeAttribute){ node.removeAttribute('id'); }
    var all = node.querySelectorAll ? node.querySelectorAll('[id]') : [];
    for (var i = 0; i < all.length; i++) all[i].removeAttribute('id');
    return node;
  }
  function fill(trg){
    tip.innerHTML = '';
    var key = ntKey(trg);
    if (key && NOTE[key]){
      var n = NOTE[key];
      tip.innerHTML = '<div class="tip-k">Notation</div><div class="tip-h">' + n.h + '</div><div class="tip-d">' + n.d +
        '</div><a class="ir tip-go" href="#' + n.t + '">Defined in ' + esc(n.tl) + ' →</a>' +
        (canHover ? '<div class="tip-hint">Click the symbol to go to its definition.</div>' : '');
      return true;
    }
    var href = trg.getAttribute && trg.getAttribute('href');
    if (!href || href.charAt(0) !== '#') return false;
    var t = document.getElementById(href.slice(1));
    if (!t) return false;
    var kind = document.createElement('div');
    kind.className = 'tip-k';
    if (t.matches('.env')){
      kind.textContent = t.getAttribute('data-label') + ' · ' + (t.closest('section').querySelector('.eyebrow') || {textContent:''}).textContent;
      tip.appendChild(kind);
      tip.appendChild(stripIds(t.cloneNode(true)));
    } else if (t.matches('.apx')){
      kind.textContent = 'Appendix ' + t.querySelector('.apx-n').textContent;
      tip.appendChild(kind);
      var c = stripIds(t.cloneNode(true));
      var hd = c.querySelector('.apx-n'); if (hd) hd.remove();
      tip.appendChild(c);
    } else if (t.matches('section')){
      kind.textContent = (t.querySelector('.eyebrow') || {textContent:''}).textContent;
      tip.appendChild(kind);
      var h = document.createElement('div'); h.className = 'tip-h';
      h.textContent = t.querySelector('h2').textContent;
      tip.appendChild(h);
    } else return false;
    return true;
  }
  function place(trg){
    var r = trg.getBoundingClientRect();
    tip.style.left = '0px'; tip.style.top = '0px';
    tip.hidden = false;
    var tw = tip.offsetWidth, th = tip.offsetHeight;
    var vw = document.documentElement.clientWidth, vh = window.innerHeight;
    var left = Math.max(12, Math.min(r.left + r.width/2 - tw/2, vw - tw - 12));
    var top = r.top - th - 10;
    if (top < 8) top = Math.min(r.bottom + 10, Math.max(8, vh - th - 8));
    tip.style.left = left + 'px'; tip.style.top = top + 'px';
  }
  function showTip(trg){
    clearTimeout(hideT); clearTimeout(showT);
    if (!fill(trg)){ hideTip(true); return; }
    cur = trg; tip._trigger = trg; tip.scrollTop = 0;
    place(trg);
  }
  function hideTip(now){
    clearTimeout(showT); clearTimeout(hideT);
    var f = function(){ tip.hidden = true; cur = null; };
    if (now) f(); else hideT = setTimeout(f, 220);
  }

  document.addEventListener('pointerover', function(e){
    if (e.pointerType !== 'mouse') return;
    if (tip.contains(e.target)){ clearTimeout(hideT); return; }
    var trg = trigger(e.target);
    if (!trg) return;
    if (trg === cur){ clearTimeout(hideT); return; }
    clearTimeout(showT);
    showT = setTimeout(function(){ showTip(trg); }, cur ? 60 : 160);
  });
  document.addEventListener('pointerout', function(e){
    if (e.pointerType !== 'mouse') return;
    var to = e.relatedTarget;
    if (to && (tip.contains(to) || (cur && cur.contains && cur.contains(to)))) return;
    if (tip.contains(e.target) || trigger(e.target)){ clearTimeout(showT); if (cur) hideTip(false); }
  });
  window.addEventListener('scroll', function(){ if (!tip.hidden) hideTip(true); }, {passive:true});
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape') hideTip(true); });
  document.addEventListener('focusin', function(e){
    var a = e.target.closest && e.target.closest('a.ir, a.x');
    if (a && !tip.contains(a) && canHover && e.target.matches(':focus-visible')) showTip(a);
  });

  // ---------- clicks ----------
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a.x, a.ir, a.bk');
    if (a){
      var t = document.getElementById(a.getAttribute('href').slice(1));
      if (!t) return;
      e.preventDefault();
      var inTip = tip.contains(a);
      var from = inTip ? tip._trigger : a;
      var label = inTip ? whereOf(tip._trigger) : (a.getAttribute('data-from') || whereOf(a));
      jump(t, from, label);
      return;
    }
    var n = e.target.closest && !tip.contains(e.target) && e.target.closest('[class*="ntn-"]');
    if (n){
      var k = ntKey(n);
      if (canHover && NOTE[k]){
        var d = document.getElementById(NOTE[k].t);
        if (d) jump(d, n, whereOf(n));
      } else {
        showTip(n);
      }
      return;
    }
    if (!tip.contains(e.target)) hideTip(true);
  });
})();
