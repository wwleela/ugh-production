import re

with open('index.html', 'r') as f:
    html = f.read()

skate_old = r'<!-- Skateboard SVG -->\s*<div class="discipline-icon[^>]*>.*?</div>'

skate_new = '''<!-- Skateboard SVG -->
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
'''

html = re.sub(skate_old, skate_new, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
