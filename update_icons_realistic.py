import re

with open('index.html', 'r') as f:
    html = f.read()

skate_old = r'<!-- Skateboard SVG -->\s*<div class="discipline-icon[^>]*>.*?</div>'
skate_new = '''<!-- Skateboard SVG -->
              <div class="discipline-icon absolute -top-10 -right-6 w-28 h-28 z-10 pointer-events-none opacity-0" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full text-kinetic-accent animate-float-icon transition-all duration-300">
                  <path d="M6 24 C 8 30, 16 32, 24 32 H 40 C 48 32, 56 30, 58 24" fill="currentColor" fill-opacity="0.1"/>
                  <path d="M6 24 C 8 30, 16 32, 24 32 H 40 C 48 32, 56 30, 58 24" stroke-width="2.5" />
                  <path d="M6 27 C 8 33, 16 35, 24 35 H 40 C 48 35, 56 33, 58 27" stroke-width="1" opacity="0.6"/>
                  <path d="M18 35 L 20 40 H 26 L 28 35 Z" fill="currentColor" fill-opacity="0.2"/>
                  <path d="M36 35 L 38 40 H 44 L 46 35 Z" fill="currentColor" fill-opacity="0.2"/>
                  <line x1="23" y1="40" x2="23" y2="45" stroke-width="2"/>
                  <line x1="41" y1="40" x2="41" y2="45" stroke-width="2"/>
                  <rect x="19" y="45" width="8" height="6" rx="2" fill="currentColor"/>
                  <rect x="37" y="45" width="8" height="6" rx="2" fill="currentColor"/>
                  <circle cx="20" cy="32" r="1" fill="currentColor" stroke="none"/>
                  <circle cx="26" cy="32" r="1" fill="currentColor" stroke="none"/>
                  <circle cx="38" cy="32" r="1" fill="currentColor" stroke="none"/>
                  <circle cx="44" cy="32" r="1" fill="currentColor" stroke="none"/>
                </svg>
              </div>'''
html = re.sub(skate_old, skate_new, html, flags=re.DOTALL)

inline_old = r'<!-- Inline Skate SVG -->\s*<div class="discipline-icon[^>]*>.*?</div>'
inline_new = '''<!-- Inline Skate SVG -->
              <div class="discipline-icon absolute -top-10 -right-6 w-28 h-28 z-10 pointer-events-none opacity-0" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full text-kinetic-accent animate-float-icon transition-all duration-300" style="animation-delay: 0.2s;">
                  <path d="M26 12 H 36 C 38 12, 38 16, 38 20 C 38 24, 46 30, 48 34 C 49 38, 48 40, 44 40 H 18 C 16 40, 14 38, 14 34 C 14 26, 20 22, 22 16 C 22 14, 24 12, 26 12 Z" fill="currentColor" fill-opacity="0.1"/>
                  <path d="M26 12 H 36 C 38 12, 38 16, 38 20 C 38 24, 46 30, 48 34 C 49 38, 48 40, 44 40 H 18 C 16 40, 14 38, 14 34 C 14 26, 20 22, 22 16 C 22 14, 24 12, 26 12 Z" />
                  <circle cx="26" cy="28" r="1.5" fill="currentColor"/>
                  <path d="M 18 40 L 16 48 H 50 L 46 40" fill="currentColor" fill-opacity="0.2"/>
                  <path d="M 18 40 L 16 48 H 50 L 46 40 Z" />
                  <line x1="18" y1="44" x2="46" y2="44" opacity="0.5"/>
                  <circle cx="20" cy="50" r="5" stroke-width="2" fill="currentColor" fill-opacity="0.1"/>
                  <circle cx="30" cy="50" r="5" stroke-width="2" fill="currentColor" fill-opacity="0.1"/>
                  <circle cx="40" cy="50" r="5" stroke-width="2" fill="currentColor" fill-opacity="0.1"/>
                  <circle cx="50" cy="50" r="5" stroke-width="2" fill="currentColor" fill-opacity="0.1"/>
                  <circle cx="20" cy="50" r="1" fill="currentColor" stroke="none"/>
                  <circle cx="30" cy="50" r="1" fill="currentColor" stroke="none"/>
                  <circle cx="40" cy="50" r="1" fill="currentColor" stroke="none"/>
                  <circle cx="50" cy="50" r="1" fill="currentColor" stroke="none"/>
                  <path d="M 36 18 H 22" stroke-width="1.5"/>
                  <path d="M 38 24 H 24" stroke-width="1.5"/>
                  <path d="M 44 32 H 30" stroke-width="1.5"/>
                </svg>
              </div>'''
html = re.sub(inline_old, inline_new, html, flags=re.DOTALL)

bmx_old = r'<!-- BMX SVG -->\s*<div class="discipline-icon[^>]*>.*?</div>'
bmx_new = '''<!-- BMX SVG -->
              <div class="discipline-icon absolute -top-10 -right-6 w-28 h-28 z-10 pointer-events-none opacity-0" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full text-kinetic-accent animate-float-icon transition-all duration-300" style="animation-delay: 0.5s;">
                  <circle cx="14" cy="46" r="11" stroke-width="3"/>
                  <circle cx="50" cy="46" r="11" stroke-width="3"/>
                  <circle cx="14" cy="46" r="2" fill="currentColor"/>
                  <circle cx="50" cy="46" r="2" fill="currentColor"/>
                  <path d="M 14 46 L 26 28" />
                  <path d="M 14 46 L 32 46" />
                  <path d="M 26 28 L 43 24" />
                  <path d="M 32 46 L 45 28" />
                  <path d="M 26 28 L 32 46" />
                  <path d="M 43 24 L 45 28" stroke-width="3" />
                  <path d="M 45 28 L 50 46" />
                  <path d="M 43 24 L 41 16 H 48 L 50 12" />
                  <path d="M 42 16 H 48" stroke-width="2" />
                  <path d="M 26 28 L 24 20" />
                  <path d="M 20 20 H 28" stroke-width="4" stroke-linecap="round" />
                  <circle cx="32" cy="46" r="4" />
                  <path d="M 32 46 L 36 52" stroke-width="2" />
                </svg>
              </div>'''
html = re.sub(bmx_old, bmx_new, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("Realistic icons injected!")
