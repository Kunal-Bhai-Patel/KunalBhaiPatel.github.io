/**
 * Kunal Bhai Patel — Portfolio Client Script
 * Lightweight, accessible interactions:
 * - Instantaneous, zero-FOUC theme switching (Dark/Light) synced with localStorage
 * - Path-preserving bilingual language switcher
 * - Project gallery category filtering (All / Professional / Personal)
 * - Accessible mobile navigation drawer
 * - Smooth back-to-top scrolling
 */

(function () {
  'use strict';

  // 1. Theme Toggle System
  const themeToggle = document.getElementById('themeToggle');
  const mobileThemeToggle = document.getElementById('mobileThemeToggle');

  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const targetTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', targetTheme);
    try {
      localStorage.setItem('kunal_portfolio_theme', targetTheme);
    } catch (e) {
      // LocalStorage might be disabled in private mode
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }
  if (mobileThemeToggle) {
    mobileThemeToggle.addEventListener('click', toggleTheme);
  }

  // 2. Mobile Navigation Toggle
  const navToggle = document.getElementById('mobileNavToggle');
  const mobileDrawer = document.getElementById('mobileDrawer');

  if (navToggle && mobileDrawer) {
    navToggle.addEventListener('click', function () {
      const isOpen = mobileDrawer.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      navToggle.innerHTML = isOpen ? '✕' : '☰';
    });

    // Close drawer on escape key
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mobileDrawer.classList.contains('is-open')) {
        mobileDrawer.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.innerHTML = '☰';
        navToggle.focus();
      }
    });

    // Close drawer when a mobile link is clicked
    const drawerLinks = mobileDrawer.querySelectorAll('a');
    drawerLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileDrawer.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.innerHTML = '☰';
      });
    });
  }

  // 3. Project Category Filtering
  const filterButtons = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  if (filterButtons.length && projectCards.length) {
    filterButtons.forEach(function (button) {
      button.addEventListener('click', function () {
        const filter = button.getAttribute('data-filter');

        // Update active button state
        filterButtons.forEach(btn => {
          btn.classList.remove('active');
          btn.setAttribute('aria-selected', 'false');
        });
        button.classList.add('active');
        button.setAttribute('aria-selected', 'true');

        // Filter cards smoothly
        projectCards.forEach(function (card) {
          const category = card.getAttribute('data-category');
          if (filter === 'all' || category === filter) {
            card.style.display = 'flex';
            requestAnimationFrame(() => {
              card.style.opacity = '1';
              card.style.transform = 'translateY(0)';
            });
          } else {
            card.style.opacity = '0';
            card.style.transform = 'translateY(4px)';
            setTimeout(() => {
              card.style.display = 'none';
            }, 180);
          }
        });
      });
    });
  }

  // 4. Language preference storage
  const langButtons = document.querySelectorAll('.lang-btn');
  langButtons.forEach(btn => {
    btn.addEventListener('click', function () {
      const lang = btn.getAttribute('data-lang');
      if (lang) {
        try {
          localStorage.setItem('kunal_portfolio_lang', lang);
        } catch (e) {
          // LocalStorage may be blocked in strict private browsing
        }
      }
    });
  });

  // 5. Smooth back to top
  const backToTop = document.getElementById('backToTop');
  if (backToTop) {
    backToTop.addEventListener('click', function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 6. Viewport-Aware Autoplay for Videos
  const autoplayVideos = document.querySelectorAll('video.autoplay-when-visible');
  if (autoplayVideos.length) {
    const attemptPlay = (v) => {
      v.muted = true;
      v.defaultMuted = true;
      const p = v.play();
      if (p && typeof p.catch === 'function') {
        p.catch(() => {});
      }
    };

    if ('IntersectionObserver' in window) {
      const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          const v = entry.target;
          if (entry.isIntersecting && entry.intersectionRatio >= 0.35) {
            attemptPlay(v);
          } else if (!v.paused) {
            v.pause();
          }
        });
      }, { threshold: [0, 0.35, 0.65] });

      autoplayVideos.forEach(v => videoObserver.observe(v));
    } else {
      autoplayVideos.forEach(attemptPlay);
    }
  }

  // 7. Technical Image Lightbox (Zoom Modal)
  const zoomableImgs = document.querySelectorAll('[data-zoomable]');
  if (zoomableImgs.length) {
    let lightbox = document.getElementById('lightboxModal');
    if (!lightbox) {
      lightbox = document.createElement('div');
      lightbox.id = 'lightboxModal';
      lightbox.className = 'lightbox-modal';
      lightbox.setAttribute('role', 'dialog');
      lightbox.setAttribute('aria-modal', 'true');
      lightbox.setAttribute('aria-label', 'Image preview');
      lightbox.innerHTML = `
        <div class="lightbox-content">
          <button type="button" class="lightbox-close" aria-label="Close dialog">&times;</button>
          <img src="" alt="" />
          <div class="lightbox-caption"></div>
        </div>
      `;
      document.body.appendChild(lightbox);
    }

    const modalImg = lightbox.querySelector('img');
    const modalCap = lightbox.querySelector('.lightbox-caption');
    const closeBtn = lightbox.querySelector('.lightbox-close');

    function openLightbox(img) {
      modalImg.src = img.currentSrc || img.src;
      modalImg.alt = img.alt || '';
      
      const fig = img.closest('figure');
      const figCap = fig ? fig.querySelector('figcaption') : null;
      modalCap.textContent = figCap ? (figCap.textContent.replace(/🔍\s*(Click to zoom|Zoom)/gi, '').trim()) : (img.alt || '');

      lightbox.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      closeBtn.focus();
    }

    function closeLightbox() {
      lightbox.classList.remove('is-open');
      document.body.style.overflow = '';
      modalImg.src = '';
    }

    zoomableImgs.forEach(img => {
      img.addEventListener('click', (e) => {
        e.stopPropagation();
        openLightbox(img);
      });
      const wrap = img.closest('[data-lightbox]');
      if (wrap && wrap !== img) {
        wrap.addEventListener('click', () => openLightbox(img));
      }
    });

    closeBtn.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox || e.target.classList.contains('lightbox-content')) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && lightbox.classList.contains('is-open')) {
        closeLightbox();
      }
    });
  }

  // 5. One-Click Copy Email to Clipboard with Accessible Visual Feedback
  function setupCopyEmail() {
    window.copyEmailAddress = function (btn, email) {
      if (!btn) return;
      email = email || btn.getAttribute('data-email') || 'kunalbhaipatel@gmail.com';
      const copyIcon = btn.querySelector('.copy-icon');
      const copyText = btn.querySelector('.copy-text');
      const originalText = btn.getAttribute('data-orig-text') || (copyText ? copyText.textContent : '');
      const originalIcon = btn.getAttribute('data-orig-icon') || (copyIcon ? copyIcon.textContent : '📋');

      if (!btn.getAttribute('data-orig-text') && copyText) {
        btn.setAttribute('data-orig-text', originalText);
      }
      if (!btn.getAttribute('data-orig-icon') && copyIcon) {
        btn.setAttribute('data-orig-icon', originalIcon);
      }

      // Synchronous immediate visual reaction and green animation
      btn.classList.add('btn-copied');
      if (copyIcon) copyIcon.textContent = '✓';
      if (copyText) {
        const isDe = document.documentElement.lang === 'de';
        copyText.textContent = isDe ? 'E-Mail kopiert!' : 'Email Copied!';
      }

      function fallbackCopy(text) {
        try {
          const ta = document.createElement('textarea');
          ta.value = text;
          ta.setAttribute('readonly', '');
          ta.style.position = 'fixed';
          ta.style.top = '-9999px';
          ta.style.left = '-9999px';
          document.body.appendChild(ta);
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
        } catch (err) {
          console.error('Fallback copy failed', err);
        }
      }

      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(email).catch(() => {
            fallbackCopy(email);
          });
        } else {
          fallbackCopy(email);
        }
      } catch (e) {
        fallbackCopy(email);
      }

      if (btn._copyTimer) clearTimeout(btn._copyTimer);
      btn._copyTimer = setTimeout(() => {
        btn.classList.remove('btn-copied');
        if (copyIcon) copyIcon.textContent = originalIcon;
        if (copyText) copyText.textContent = originalText;
      }, 2500);
    };

    const copyBtns = document.querySelectorAll('.contact-copy-btn');
    copyBtns.forEach(btn => {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        const email = this.getAttribute('data-email') || 'kunalbhaipatel@gmail.com';
        window.copyEmailAddress(this, email);
      });
    });
  }

  setupCopyEmail();
})();
