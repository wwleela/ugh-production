import re

with open('index.html', 'r') as f:
    html = f.read()

target = r'<section id="disciplines".*?</section>'

replacement = '''<section id="disciplines" class="py-fluid-xl px-[clamp(1.25rem,5vw,4rem)] border-b border-kinetic-border">
        <div class="max-w-[1440px] mx-auto">
          <div class="text-center mb-fluid-lg">
            <span class="pill-tag mb-4">Core Disciplines</span>
            <h2 class="text-4xl md:text-5xl font-display font-bold mt-2">What We Teach</h2>
          </div>
          <div class="grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-fluid-md">
            <div class="discipline-card relative p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border hover:border-kinetic-accent transition-colors">
              <h3 class="text-2xl sm:text-3xl font-display font-bold mb-4 uppercase break-words pr-8 sm:pr-0">Skateboarding</h3>
              <!-- Skateboard SVG -->
              <div class="discipline-icon absolute -top-12 -right-6 w-36 h-36 z-10 pointer-events-none opacity-0" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 130" class="w-full h-full animate-float-icon transition-all duration-300">
                  <defs>
                    <linearGradient id="deckGrip" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stop-color="#2a2a2a"/>
                      <stop offset="100%" stop-color="#111111"/>
                    </linearGradient>
                    <linearGradient id="deckWood" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stop-color="#e6ccb2"/>
                      <stop offset="50%" stop-color="#ddb892"/>
                      <stop offset="100%" stop-color="#9c6644"/>
                    </linearGradient>
                    <linearGradient id="deckGraphic" x1="0" y1="0" x2="1" y2="0">
                      <stop offset="0%" stop-color="#D85B2D"/>
                      <stop offset="25%" stop-color="#ff7b47"/>
                      <stop offset="75%" stop-color="#ff7b47"/>
                      <stop offset="100%" stop-color="#D85B2D"/>
                    </linearGradient>
                    <linearGradient id="metal" x1="0" y1="0" x2="1" y2="1">
                      <stop offset="0%" stop-color="#f8f9fa"/>
                      <stop offset="50%" stop-color="#ced4da"/>
                      <stop offset="100%" stop-color="#6c757d"/>
                    </linearGradient>
                    <linearGradient id="wheelUrethane" x1="0" y1="0" x2="1" y2="0">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#d3d3d3"/>
                    </linearGradient>
                    <filter id="realShadow" x="-20%" y="-20%" width="140%" height="140%">
                      <feDropShadow dx="0" dy="12" stdDeviation="8" flood-color="#000" flood-opacity="0.4"/>
                    </filter>
                  </defs>
                  <g filter="url(#realShadow)">
                    <!-- Grip Tape (Top Layer) -->
                    <path d="M 12 34 Q 30 50 50 50 L 150 50 Q 170 50 188 34 A 3 3 0 0 1 192 37 Q 170 54 150 54 L 50 54 Q 30 54 8 37 A 3 3 0 0 1 12 34 Z" fill="url(#deckGrip)"/>
                    
                    <!-- Wood Plys (Middle Layer) -->
                    <path d="M 8 37 Q 30 54 50 54 L 150 54 Q 170 54 192 37 A 2 2 0 0 1 193 39 Q 170 56 150 56 L 50 56 Q 30 56 7 39 A 2 2 0 0 1 8 37 Z" fill="url(#deckWood)"/>
                    
                    <!-- Graphic (Bottom Layer) -->
                    <path d="M 7 39 Q 30 56 50 56 L 150 56 Q 170 56 193 39 A 3 3 0 0 1 192 43 Q 170 60 150 60 L 50 60 Q 30 60 8 43 A 3 3 0 0 1 7 39 Z" fill="url(#deckGraphic)"/>

                    <!-- Hardware Bolts -->
                    <!-- Left -->
                    <rect x="45" y="55" width="2" height="3" fill="#fff" opacity="0.6"/>
                    <rect x="52" y="55" width="2" height="3" fill="#fff" opacity="0.6"/>
                    <!-- Right -->
                    <rect x="146" y="55" width="2" height="3" fill="#fff" opacity="0.6"/>
                    <rect x="153" y="55" width="2" height="3" fill="#fff" opacity="0.6"/>

                    <!-- Back Wheels -->
                    <rect x="42" y="70" width="16" height="24" rx="4" fill="#777"/>
                    <rect x="142" y="70" width="16" height="24" rx="4" fill="#777"/>

                    <!-- LEFT TRUCK -->
                    <!-- Baseplate -->
                    <path d="M 40 59 L 60 59 L 58 64 L 42 64 Z" fill="url(#metal)"/>
                    <!-- Hanger -->
                    <path d="M 48 64 L 52 64 L 56 82 L 44 82 Z" fill="url(#metal)"/>
                    <!-- Bushings -->
                    <rect x="48" y="64" width="8" height="12" rx="3" fill="#e76f51" transform="rotate(15 52 70)"/>

                    <!-- RIGHT TRUCK -->
                    <!-- Baseplate -->
                    <path d="M 140 59 L 160 59 L 158 64 L 142 64 Z" fill="url(#metal)"/>
                    <!-- Hanger -->
                    <path d="M 148 64 L 152 64 L 156 82 L 144 82 Z" fill="url(#metal)"/>
                    <!-- Bushings -->
                    <rect x="148" y="64" width="8" height="12" rx="3" fill="#e76f51" transform="rotate(-15 152 70)"/>

                    <!-- Front Wheels -->
                    <rect x="34" y="76" width="20" height="30" rx="6" fill="url(#wheelUrethane)"/>
                    <rect x="146" y="76" width="20" height="30" rx="6" fill="url(#wheelUrethane)"/>
                    
                    <!-- Bearings -->
                    <circle cx="44" cy="91" r="4.5" fill="#222"/>
                    <circle cx="44" cy="91" r="2" fill="url(#metal)"/>
                    
                    <circle cx="156" cy="91" r="4.5" fill="#222"/>
                    <circle cx="156" cy="91" r="2" fill="url(#metal)"/>
                    
                    <!-- Wheel Highlights / Shine -->
                    <rect x="37" y="79" width="4" height="24" rx="2" fill="#fff" opacity="0.8"/>
                    <rect x="149" y="79" width="4" height="24" rx="2" fill="#fff" opacity="0.8"/>
                  </g>
                </svg>
              </div>
              <p class="text-kinetic-muted leading-relaxed relative z-20">Master the concrete waves. From static balance to ollies, flip tricks, and transition carving.</p>
            </div>
            
            <div class="discipline-card relative p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border hover:border-kinetic-accent transition-colors">
              <h3 class="text-2xl sm:text-3xl font-display font-bold mb-4 uppercase break-words pr-8 sm:pr-0">Inline Skating</h3>
              <!-- Inline Skate SVG -->
              <div class="discipline-icon absolute -top-10 -right-6 w-28 h-28 z-10 pointer-events-none opacity-0" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="currentColor" class="w-full h-full text-kinetic-accent animate-float-icon transition-all duration-300" style="animation-delay: 0.2s;">
                  <!-- Cuff Back -->
                  <path d="M 35 15 C 35 10, 45 10, 50 15 L 52 35 C 55 45, 65 50, 75 52 C 80 53, 85 58, 85 65 L 25 65 C 20 40, 30 20, 35 15 Z" opacity="0.6"/>
                  <path d="M 32 20 C 32 15, 42 15, 48 20 L 50 35 L 30 35 Z" opacity="0.8"/>
                  <!-- Hard Shell Boot -->
                  <path d="M 28 35 L 50 35 C 55 45, 65 50, 78 52 C 82 53, 85 58, 85 65 C 85 70, 80 72, 75 72 L 20 72 C 15 72, 18 55, 28 35 Z" opacity="0.95"/>
                  <!-- Boot Details / Highlights -->
                  <path d="M 28 35 L 32 35 C 32 50, 25 60, 22 72 L 20 72 C 15 72, 18 55, 28 35 Z" fill="#fff" opacity="0.2"/>
                  <rect x="30" y="25" width="18" height="4" rx="2" fill="#fff" opacity="0.9"/>
                  <rect x="35" y="45" width="20" height="5" rx="2" fill="#fff" opacity="0.9"/>
                  <circle cx="48" cy="27" r="1.5" fill="#111"/>
                  <circle cx="53" cy="47.5" r="1.5" fill="#111"/>
                  <!-- Frame Shadow -->
                  <path d="M 22 72 L 80 72 L 75 82 L 25 82 Z" opacity="0.5"/>
                  <!-- Frame Main -->
                  <path d="M 25 82 L 75 82 L 73 86 L 27 86 Z" opacity="0.9"/>
                  <!-- Wheels -->
                  <circle cx="32" cy="85" r="7" opacity="1"/>
                  <circle cx="46" cy="85" r="7" opacity="1"/>
                  <circle cx="60" cy="85" r="7" opacity="1"/>
                  <circle cx="74" cy="85" r="7" opacity="1"/>
                  <!-- Wheel Hubs/Bearings -->
                  <circle cx="32" cy="85" r="3" fill="#fff" opacity="0.7"/>
                  <circle cx="46" cy="85" r="3" fill="#fff" opacity="0.7"/>
                  <circle cx="60" cy="85" r="3" fill="#fff" opacity="0.7"/>
                  <circle cx="74" cy="85" r="3" fill="#fff" opacity="0.7"/>
                  <circle cx="32" cy="85" r="1" fill="#111" opacity="0.8"/>
                  <circle cx="46" cy="85" r="1" fill="#111" opacity="0.8"/>
                  <circle cx="60" cy="85" r="1" fill="#111" opacity="0.8"/>
                  <circle cx="74" cy="85" r="1" fill="#111" opacity="0.8"/>
                </svg>
              </div>
              <p class="text-kinetic-muted leading-relaxed relative z-20">Speed, agility, and precision. Learn strides, crossovers, stopping mechanics, and freestyle slalom.</p>
            </div>
            
            <div class="discipline-card relative p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border hover:border-kinetic-accent transition-colors">
              <h3 class="text-2xl sm:text-3xl font-display font-bold mb-4 uppercase break-words pr-8 sm:pr-0">BMX</h3>
              <!-- BMX SVG -->
              <div class="discipline-icon absolute -top-10 -right-6 w-28 h-28 z-10 pointer-events-none opacity-0" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="currentColor" class="w-full h-full text-kinetic-accent animate-float-icon transition-all duration-300" style="animation-delay: 0.5s;">
                  <!-- Tires -->
                  <circle cx="25" cy="70" r="18" fill="none" stroke="currentColor" stroke-width="5.5" opacity="0.95"/>
                  <circle cx="75" cy="70" r="18" fill="none" stroke="currentColor" stroke-width="5.5" opacity="0.95"/>
                  <!-- Rims -->
                  <circle cx="25" cy="70" r="15" fill="none" stroke="#fff" stroke-width="1.5" opacity="0.4"/>
                  <circle cx="75" cy="70" r="15" fill="none" stroke="#fff" stroke-width="1.5" opacity="0.4"/>
                  <!-- Hubs -->
                  <circle cx="25" cy="70" r="2.5" opacity="1"/>
                  <circle cx="75" cy="70" r="2.5" opacity="1"/>
                  <!-- Spokes -->
                  <path d="M 25 55 L 25 85 M 10 70 L 40 70 M 14 59 L 36 81 M 14 81 L 36 59" stroke="#fff" stroke-width="0.5" opacity="0.5"/>
                  <path d="M 75 55 L 75 85 M 60 70 L 90 70 M 64 59 L 86 81 M 64 81 L 86 59" stroke="#fff" stroke-width="0.5" opacity="0.5"/>
                  
                  <!-- Chainstay & Seatstay -->
                  <line x1="25" y1="70" x2="48" y2="70" stroke="currentColor" stroke-width="3.5" opacity="0.8"/>
                  <line x1="25" y1="70" x2="40" y2="45" stroke="currentColor" stroke-width="3" opacity="0.8"/>
                  
                  <!-- Main Diamond Frame -->
                  <line x1="40" y1="45" x2="65" y2="40" stroke="currentColor" stroke-width="4.5" opacity="0.95"/>
                  <line x1="48" y1="70" x2="65" y2="40" stroke="currentColor" stroke-width="5" opacity="0.95"/>
                  
                  <!-- Fork -->
                  <line x1="75" y1="70" x2="65" y2="40" stroke="currentColor" stroke-width="4.5" opacity="0.9"/>
                  <!-- Head Tube -->
                  <line x1="64" y1="43" x2="66" y2="37" stroke="currentColor" stroke-width="6" opacity="1"/>
                  <line x1="65" y1="40" x2="61" y2="30" stroke="currentColor" stroke-width="3.5" opacity="0.9"/>
                  
                  <!-- Handlebars -->
                  <path d="M 61 30 L 61 22 L 53 22" fill="none" stroke="currentColor" stroke-width="3.5" opacity="1"/>
                  <!-- Grips -->
                  <line x1="50" y1="22" x2="56" y2="22" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity="0.8"/>
                  
                  <!-- Seat post -->
                  <line x1="48" y1="70" x2="40" y2="45" stroke="currentColor" stroke-width="4.5" opacity="0.9"/>
                  <line x1="40" y1="45" x2="36" y2="33" stroke="currentColor" stroke-width="3" opacity="0.8"/>
                  
                  <!-- Seat -->
                  <path d="M 28 33 L 42 33 Q 45 35 40 37 L 30 36 Z" opacity="1"/>
                  
                  <!-- Sprocket / Crank -->
                  <circle cx="48" cy="70" r="7" opacity="0.9"/>
                  <circle cx="48" cy="70" r="3.5" fill="#fff" opacity="0.6"/>
                  <line x1="48" y1="70" x2="55" y2="78" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" opacity="1"/>
                  <line x1="52" y1="78" x2="58" y2="78" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity="0.9"/>
                  
                  <!-- Chain -->
                  <line x1="25" y1="66" x2="48" y2="64" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2 2" opacity="0.8"/>
                  <line x1="25" y1="74" x2="48" y2="76" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2 2" opacity="0.8"/>
                </svg>
              </div>
              <p class="text-kinetic-muted leading-relaxed relative z-20">Two-wheeled progression. From basic pump track rhythm to bunny hops and manual control.</p>
            </div>
          </div>
        </div>
      </section>'''

html = re.sub(target, replacement, html, flags=re.DOTALL)
with open('index.html', 'w') as f:
    f.write(html)
print("done")
