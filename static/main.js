// ── 1. SCROLL REVEAL ──
    const revealEls = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          setTimeout(() => entry.target.classList.add('visible'), i * 80);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(el => observer.observe(el));

    // ── 2. TOAST NOTIFICATION ──
    const toast = document.getElementById('toast');
    setTimeout(() => {
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 4000);
    }, 2500);

    // ── 3. FLOATING BUTTON — collapse on scroll ──
    const floatBtn = document.querySelector('.float-wa');
    const floatLabel = floatBtn.querySelector('.float-label');
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
      const current = window.scrollY;
      if (current > 200 && current > lastScroll) {
        floatLabel.style.display = 'none';
        floatBtn.style.maxWidth = '56px';
        floatBtn.style.padding = '14px';
      } else {
        floatLabel.style.display = '';
        floatBtn.style.maxWidth = '220px';
        floatBtn.style.padding = '14px 22px';
      }
      lastScroll = current;
    });