import re

with open('index.html', 'r') as f:
    html = f.read()

# Skateboard
skate_old = r'<!-- Skateboard SVG -->\s*<div class="discipline-icon[^>]*>.*?</div>'
skate_new = '''<!-- Skateboard SVG -->
              <div class="discipline-icon absolute -top-10 -right-6 w-28 h-28 z-10 pointer-events-none opacity-0" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="currentColor" class="w-full h-full text-kinetic-accent animate-float-icon transition-all duration-300">
                  <!-- Deck Shadow -->
                  <path d="M 6 46 Q 25 58 50 58 Q 75 58 94 46 A 3 3 0 0 1 97 49 Q 75 62 50 62 Q 25 62 3 49 A 3 3 0 0 1 6 46 Z" opacity="0.3"/>
                  <!-- Grip tape -->
                  <path d="M 8 44 Q 25 54 50 54 Q 75 54 92 44 L 94 45.5 Q 75 55.5 50 55.5 Q 25 55.5 6 45.5 Z" opacity="0.95"/>
                  <!-- Wood Plys -->
                  <path d="M 6 45.5 Q 25 55.5 50 55.5 Q 75 55.5 94 45.5 L 95 47 Q 75 57 50 57 Q 25 57 5 47 Z" opacity="0.5"/>
                  <path d="M 5 47 Q 25 57 50 57 Q 75 57 95 47 L 96 48.5 Q 75 58.5 50 58.5 Q 25 58.5 4 48.5 Z" opacity="0.75"/>
                  <!-- Bolts -->
                  <rect x="25" y="52" width="2" height="2" fill="#fff" opacity="0.5"/>
                  <rect x="29" y="52.5" width="2" height="2" fill="#fff" opacity="0.5"/>
                  <rect x="69" y="52.5" width="2" height="2" fill="#fff" opacity="0.5"/>
                  <rect x="73" y="52" width="2" height="2" fill="#fff" opacity="0.5"/>
                  <!-- LEFT TRUCK -->
                  <path d="M 22 57 L 32 58 L 31 60 L 23 59 Z" opacity="0.9"/>
                  <path d="M 28 60 L 30 65 L 28 65 Z" opacity="0.5"/>
                  <path d="M 24 59 L 28 59 L 31 66 L 24 66 Z" opacity="0.7"/>
                  <path d="M 23 66 L 32 66 L 30 71 L 25 71 Z" opacity="0.9"/>
                  <!-- RIGHT TRUCK -->
                  <path d="M 68 58 L 78 57 L 77 59 L 69 60 Z" opacity="0.9"/>
                  <path d="M 70 60 L 72 65 L 70 65 Z" opacity="0.5"/>
                  <path d="M 72 59 L 76 59 L 76 66 L 69 66 Z" opacity="0.7"/>
                  <path d="M 68 66 L 77 66 L 75 71 L 70 71 Z" opacity="0.9"/>
                  <!-- WHEELS BACK -->
                  <rect x="20" y="67" width="8" height="13" rx="2.5" opacity="0.4"/>
                  <rect x="72" y="67" width="8" height="13" rx="2.5" opacity="0.4"/>
                  <!-- WHEELS FRONT -->
                  <rect x="26" y="69" width="9" height="14" rx="2.5" opacity="1"/>
                  <rect x="65" y="69" width="9" height="14" rx="2.5" opacity="1"/>
                  <!-- Bearings -->
                  <line x1="30.5" y1="69" x2="30.5" y2="83" stroke="#fff" stroke-width="1.5" opacity="0.6"/>
                  <line x1="69.5" y1="69" x2="69.5" y2="83" stroke="#fff" stroke-width="1.5" opacity="0.6"/>
                </svg>
              </div>'''
html = re.sub(skate_old, skate_new, html, flags=re.DOTALL)

inline_old = r'<!-- Inline Skate SVG -->\s*<div class="discipline-icon[^>]*>.*?</div>'
inline_new = '''<!-- Inline Skate SVG -->
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
              </div>'''
html = re.sub(inline_old, inline_new, html, flags=re.DOTALL)

bmx_old = r'<!-- BMX SVG -->\s*<div class="discipline-icon[^>]*>.*?</div>'
bmx_new = '''<!-- BMX SVG -->
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
              </div>'''
html = re.sub(bmx_old, bmx_new, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("Ultra-realistic icons injected!")
