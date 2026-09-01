import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Add GSAP & ScrollTrigger to <head>
gsap_scripts = """
    <!-- GSAP for animations -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
</head>"""
html = html.replace('</head>', gsap_scripts)

# 2. Add classes to the "What We Teach" section cards and insert the SVG icons
# Card 1: Skateboarding
card1_regex = r'(<div class=")(p-8 bg-kinetic-surface border border-kinetic-border hover:border-kinetic-accent transition-colors)(">\s*<h3 class="text-fluid-h2 font-display font-bold mb-4 uppercase">Skateboarding</h3>)'
card1_repl = r'\1discipline-card relative \2\3\n              <!-- Skateboard SVG -->\n              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="currentColor" class="discipline-icon absolute -top-8 -right-4 w-20 h-20 text-kinetic-accent opacity-0 z-10 pointer-events-none drop-shadow-lg" style="opacity: 0;"><path d="M54 28H10c-3.3 0-6 2.7-6 6s2.7 6 6 6h44c3.3 0 6-2.7 6-6s-2.7-6-6-6zM14 44c-3.3 0-6 2.7-6 6s2.7 6 6 6 6-2.7 6-6-2.7-6-6-6zm36 0c-3.3 0-6 2.7-6 6s2.7 6 6 6 6-2.7 6-6-2.7-6-6-6z"/></svg>'
html = re.sub(card1_regex, card1_repl, html)

# Card 2: Inline Skating
card2_regex = r'(<div class=")(p-8 bg-kinetic-surface border border-kinetic-border hover:border-kinetic-accent transition-colors)(">\s*<h3 class="text-fluid-h2 font-display font-bold mb-4 uppercase">Inline Skating</h3>)'
card2_repl = r'\1discipline-card relative \2\3\n              <!-- Inline Skate SVG -->\n              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="currentColor" class="discipline-icon absolute -top-8 -right-4 w-20 h-20 text-kinetic-accent opacity-0 z-10 pointer-events-none drop-shadow-lg" style="opacity: 0;"><path d="M46 36H24V14c0-3.3-2.7-6-6-6h-6c-3.3 0-6 2.7-6 6v28c0 4.4 3.6 8 8 8h32c4.4 0 8-3.6 8-8v-4c0-3.3-2.7-6-6-6zM12 58c-2.2 0-4-1.8-4-4s1.8-4 4-4 4 1.8 4 4-1.8 4-4 4zm16 0c-2.2 0-4-1.8-4-4s1.8-4 4-4 4 1.8 4 4-1.8 4-4 4zm16 0c-2.2 0-4-1.8-4-4s1.8-4 4-4 4 1.8 4 4-1.8 4-4 4zm16 0c-2.2 0-4-1.8-4-4s1.8-4 4-4 4 1.8 4 4-1.8 4-4 4z"/></svg>'
html = re.sub(card2_regex, card2_repl, html)

# Card 3: BMX
card3_regex = r'(<div class=")(p-8 bg-kinetic-surface border border-kinetic-border hover:border-kinetic-accent transition-colors)(">\s*<h3 class="text-fluid-h2 font-display font-bold mb-4 uppercase">BMX</h3>)'
card3_repl = r'\1discipline-card relative \2\3\n              <!-- BMX SVG -->\n              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" class="discipline-icon absolute -top-8 -right-4 w-20 h-20 text-kinetic-accent opacity-0 z-10 pointer-events-none drop-shadow-lg" style="opacity: 0;"><circle cx="16" cy="46" r="12"/><circle cx="48" cy="46" r="12"/><path d="M16 46l12-18h14l6 18M34 28l-4-14h-6M42 28l-2-8h6"/></svg>'
html = re.sub(card3_regex, card3_repl, html)


# 3. Add GSAP script logic before </body>
gsap_logic = """
    <!-- GSAP ScrollTrigger Logic -->
    <script>
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
    </script>
</body>"""
html = html.replace('</body>', gsap_logic)

with open('index.html', 'w') as f:
    f.write(html)
