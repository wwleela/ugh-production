
  const themeToggleBtn = document.getElementById('theme-toggle');
  
  // Check for saved user preference, if any, on load of the website
  if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
      if (themeToggleBtn) themeToggleBtn.textContent = 'light_mode';
  } else {
      document.documentElement.classList.remove('dark')
      if (themeToggleBtn) themeToggleBtn.textContent = 'dark_mode';
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', function() {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
            themeToggleBtn.textContent = 'dark_mode';
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
            themeToggleBtn.textContent = 'light_mode';
        }
    });
  }


document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.main-tab-content');
    const tabLinks = document.querySelectorAll('a.tab-link'); // limit to a tags or specific ones? Actually there are buttons too, wait.

    function switchTab(tabId) {
        tabs.forEach(tab => {
            if(tab.id === 'tab-' + tabId) {
                tab.classList.remove('hidden');
                tab.classList.add('block');
            } else {
                tab.classList.remove('block');
                tab.classList.add('hidden');
            }
        });
        
        tabLinks.forEach(link => {
            if(link.dataset.tab === tabId) {
                link.classList.add('text-kinetic-accent');
            } else {
                link.classList.remove('text-kinetic-accent');
            }
        });
        window.scrollTo(0, 0);
    }

    tabLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const tabId = link.dataset.tab;
            history.pushState(null, null, '#' + tabId);
            switchTab(tabId);
            // On mobile, maybe hide the mobile menu if there was one, but here we don't have one
        });
    });

    // Handle initial load
    const hash = window.location.hash.replace('#', '');
    if (hash && ['home', 'impact', 'events', 'pricing', 'venues'].includes(hash)) {
        switchTab(hash);
    } else {
        switchTab('home');
    }
    
    // Handle back button
    window.addEventListener('popstate', () => {
        const hash = window.location.hash.replace('#', '');
        if (hash && ['home', 'impact', 'events', 'pricing', 'venues'].includes(hash)) {
            switchTab(hash);
        } else {
            switchTab('home');
        }
    });
});


      document.addEventListener("DOMContentLoaded", () => {
        if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
          gsap.registerPlugin(ScrollTrigger);
          
          const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
          const cards = document.querySelectorAll('.discipline-card');
          
          cards.forEach((card, index) => {
            const icon = card.querySelector('.discipline-icon');
            if (!icon) return;
            
            if (prefersReducedMotion) {
              // Accessibility: Show icons directly without animation
              gsap.set(icon, { opacity: 1 });
              return;
            }
            
            // Alternate direction: even cards left, odd cards right
            const isEven = index % 2 === 0;
            const startX = isEven ? -80 : 80;
            const startY = -120;
            const startRot = isEven ? -25 : 25;
            
            gsap.set(icon, { 
              x: startX, 
              y: startY, 
              rotation: startRot, 
              scale: 1,
              transformOrigin: "center center"
            });
            
            const tl = gsap.timeline({
              scrollTrigger: {
                trigger: card,
                start: "top 85%", // Starts entering viewport
                end: "top 45%",   // Finishes landing 
                scrub: 0.5        // Scrubbing with physical weight
              }
            });
            
            // 1. Arced flight in
            tl.to(icon, {
              x: 0,
              opacity: 1,
              rotation: 0,
              duration: 0.7,
              ease: "power2.out"
            }, 0)
            .to(icon, {
              y: 0,
              duration: 0.7,
              ease: "back.out(1.2)" // Slight overshoot for arc trajectory
            }, 0);
            
            // 2. Landing Squash
            tl.to(icon, {
              scaleY: 0.85,
              scaleX: 1.15,
              duration: 0.15,
              transformOrigin: "bottom center",
              ease: "power1.out"
            }, 0.7)
            .to(icon, {
              scaleY: 1,
              scaleX: 1,
              duration: 0.15,
              ease: "power1.in"
            }, 0.85);
            
            // 3. Card physical reaction (nudge down)
            tl.to(card, {
              y: 4,
              duration: 0.15,
              ease: "power1.out"
            }, 0.7)
            .to(card, {
              y: 0,
              duration: 0.15,
              ease: "power1.in"
            }, 0.85);
          });
        }
      });
    
document.addEventListener('DOMContentLoaded', () => {    const mobileMenuBtn = document.getElementById('mobile-menu-btn');    const mobileDropdown = document.getElementById('mobile-dropdown');    if(mobileMenuBtn && mobileDropdown) {        mobileMenuBtn.addEventListener('click', (e) => {            e.stopPropagation();            mobileDropdown.classList.toggle('hidden');        });        document.addEventListener('click', (e) => {            if (!mobileDropdown.contains(e.target) && !mobileMenuBtn.contains(e.target)) {                mobileDropdown.classList.add('hidden');            }        });        const dropLinks = mobileDropdown.querySelectorAll('a, button');        dropLinks.forEach(link => {            link.addEventListener('click', () => {                mobileDropdown.classList.add('hidden');            });        });    }    const mobileThemeToggleBtn = document.getElementById('mobile-theme-toggle');    const themeToggleBtn = document.getElementById('theme-toggle');    if (mobileThemeToggleBtn) {        mobileThemeToggleBtn.addEventListener('click', function() {            if (themeToggleBtn) themeToggleBtn.click();            mobileThemeToggleBtn.textContent = document.documentElement.classList.contains('dark') ? 'light_mode' : 'dark_mode';        });    }});
