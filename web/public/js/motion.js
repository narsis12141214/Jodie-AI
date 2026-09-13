/* Hadi Photography London — scroll motion
   No dependencies. One rAF-throttled scroll pass drives every continuous effect.
   Discrete reveals use IntersectionObserver so they work everywhere. */
(() => {
  'use strict';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const clamp = (n, a = 0, b = 1) => Math.min(b, Math.max(a, n));

  /* ---------- 1. reveal on enter ---------- */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
  $$('.r, .lines').forEach((el) => io.observe(el));

  if (reduce) { $$('.r, .lines').forEach((el) => el.classList.add('in')); return; }

  /* ---------- 2. hero opening ---------- */
  requestAnimationFrame(() => $('.hero .lines')?.classList.add('in'));

  /* ---------- 3. chapter rail ---------- */
  const sections = $$('[data-chapter]');
  const rail = $('#rail');
  if (rail && sections.length) {
    sections.forEach((s) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('aria-label', s.dataset.chapter);
      b.addEventListener('click', () => window.lenis ? window.lenis.scrollTo(s) : s.scrollIntoView({ behavior: 'smooth' }));
      rail.appendChild(b);
    });
    const dots = $$('button', rail);
    sections.forEach((s, i) => {
      new IntersectionObserver(([e]) => {
        if (e.isIntersecting) dots.forEach((d, n) => d.setAttribute('aria-current', String(n === i)));
      }, { threshold: 0.45 }).observe(s);
    });
  }

  /* ---------- 4. cached geometry ---------- */
  const hero      = $('.hero__media');
  const nav       = $('#nav');
  const bar       = $('#progress');
  const pin       = $('.pin');
  const pinLayers = $$('.pin__layer');
  const pinSlots  = $$('.pin__slot > *');
  const gal       = $('.gal');
  const track     = $('.gal__track');
  const guideImg  = $('.guide__fig img');
  const zoom      = $('.zoom');
  const zoomLayers = $$('.zoom__layer').map((el) => ({ el, to: parseFloat(el.dataset.scale) || 4 }));
  const supportsSDA = CSS.supports('animation-timeline: scroll()');

  let vh = innerHeight, geo = {};
  const measure = () => {
    vh = innerHeight;
    geo = {
      pin:   pin   ? { top: pin.offsetTop,   h: pin.offsetHeight }   : null,
      gal:   gal   ? { top: gal.offsetTop,   h: gal.offsetHeight }   : null,
      guide: guideImg ? { top: guideImg.closest('.guide').offsetTop, h: guideImg.closest('.guide').offsetHeight } : null,
      zoom:  zoom  ? { top: zoom.offsetTop,  h: zoom.offsetHeight }  : null,
      overflow: track ? Math.max(0, track.scrollWidth - innerWidth + 24) : 0,
      doc: document.documentElement.scrollHeight - vh,
    };
  };
  measure();
  addEventListener('resize', () => { measure(); frame(); }, { passive: true });
  addEventListener('load',   () => { measure(); frame(); });

  /* ---------- 5. the single scroll pass ---------- */
  let active = -1;
  function frame() {
    const y = scrollY;

    if (bar && !supportsSDA) bar.style.transform = `scaleX(${clamp(y / (geo.doc || 1))})`;
    if (nav) nav.classList.toggle('on', y > vh * 0.85);
    if (rail) rail.classList.toggle('on', y > vh * 0.85);

    // hero: slow drift + settle
    if (hero && y < vh * 1.2) hero.style.transform = `translate3d(0,${y * 0.32}px,0) scale(${1 + y / vh * 0.06})`;

    // pinned three-way: progress through the section picks the active panel
    if (geo.pin && pinLayers.length) {
      const p = clamp((y - geo.pin.top) / (geo.pin.h - vh));
      const i = Math.min(pinLayers.length - 1, Math.floor(p * pinLayers.length + 0.0001));
      if (i !== active && y + vh > geo.pin.top && y < geo.pin.top + geo.pin.h) {
        active = i;
        pinLayers.forEach((l, n) => l.classList.toggle('on', n === i));
        pinSlots.forEach((s, n) => s.classList.toggle('on', n === i));
      }
    }

    // zoom parallax: every layer scales from 1 to its target as you travel the section
    if (geo.zoom && zoomLayers.length) {
      const p = clamp((y - geo.zoom.top) / (geo.zoom.h - vh));
      for (const { el, to } of zoomLayers) el.style.transform = `scale(${1 + p * (to - 1)})`;
    }

    // horizontal gallery driven by vertical scroll
    if (geo.gal && track) {
      const p = clamp((y - geo.gal.top) / (geo.gal.h - vh));
      track.style.transform = `translate3d(${-p * geo.overflow}px,0,0)`;
    }

    // guide portrait parallax inside its frame
    if (geo.guide && guideImg) {
      const p = clamp((y + vh - geo.guide.top) / (geo.guide.h + vh)) - 0.5;
      guideImg.style.transform = `translate3d(0,${p * -7}%,0)`;
    }
  }

  let ticking = false;
  addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => { frame(); ticking = false; });
  }, { passive: true });

  frame();
  // only default to the first panel if the scroll pass did not already pick one
  if (active === -1) {
    pinLayers[0]?.classList.add('on');
    pinSlots[0]?.classList.add('on');
  }
})();
