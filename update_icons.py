import re

with open('index.html', 'r') as f:
    html = f.read()

# Add keyframes and class to <style>
style_addition = """
      @keyframes float-icon {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        33% { transform: translateY(-8px) rotate(2deg); }
        66% { transform: translateY(-4px) rotate(-2deg); }
      }
      .animate-float-icon {
        animation: float-icon 5s ease-in-out infinite;
        transform-origin: center center;
        filter: drop-shadow(0px 8px 16px rgba(216, 91, 45, 0.4));
      }
      .dark .animate-float-icon {
        filter: drop-shadow(0px 8px 16px rgba(216, 91, 45, 0.6));
      }
      .discipline-card:hover .animate-float-icon {
        animation-duration: 2s;
        filter: drop-shadow(0px 12px 24px rgba(216, 91, 45, 0.7));
      }
"""

if "keyframes float-icon" not in html:
    html = html.replace('</style>', style_addition + '</style>')

# Replace Skateboarding SVG
skate_old = r'<!-- Skateboard SVG -->\s*<svg[^>]*class="discipline-icon[^>]*>.*?</svg>'
skate_new = '''<!-- Skateboard SVG -->
              <div class="discipline-icon absolute -top-10 -right-6 w-28 h-28 z-10 pointer-events-none opacity-0" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full text-kinetic-accent animate-float-icon transition-all duration-300">
                  <path d="M52 24H12c-4.4 0-8 3.6-8 8s3.6 8 8 8h40c4.4 0 8-3.6 8-8s-3.6-8-8-8z" fill="currentColor" fill-opacity="0.1"/>
                  <path d="M8 24h48" stroke-dasharray="4 4" stroke-opacity="0.5"/>
                  <circle cx="16" cy="46" r="5" fill="currentColor"/>
                  <path d="M16 40v-6"/>
                  <circle cx="48" cy="46" r="5" fill="currentColor"/>
                  <path d="M48 40v-6"/>
                  <path d="M12 24c-2 0-4-2-4-4 0-1.1.9-2 2-2h44c1.1 0 2 .9 2 2 0 2-2 4-4 4" opacity="0.6"/>
                </svg>
              </div>'''
html = re.sub(skate_old, skate_new, html, flags=re.DOTALL)

# Replace Inline Skate SVG
inline_old = r'<!-- Inline Skate SVG -->\s*<svg[^>]*class="discipline-icon[^>]*>.*?</svg>'
inline_new = '''<!-- Inline Skate SVG -->
              <div class="discipline-icon absolute -top-10 -right-6 w-28 h-28 z-10 pointer-events-none opacity-0" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full text-kinetic-accent animate-float-icon transition-all duration-300" style="animation-delay: 0.2s;">
                  <path d="M38 40H16V14c0-4.4-3.6-8-8-8h-2" stroke-linecap="round"/>
                  <path d="M16 20h14l4 10h6c3.3 0 6 2.7 6 6v4H16"/>
                  <path d="M46 40c4.4 0 8-3.6 8-8v-2" stroke-dasharray="4 4"/>
                  <path d="M12 46h38" stroke-width="4"/>
                  <circle cx="16" cy="54" r="4" fill="currentColor"/>
                  <circle cx="28" cy="54" r="4" fill="currentColor"/>
                  <circle cx="40" cy="54" r="4" fill="currentColor"/>
                  <circle cx="52" cy="54" r="4" fill="currentColor"/>
                  <path d="M16 14h14" opacity="0.5"/>
                  <path d="M16 26h10" opacity="0.5"/>
                </svg>
              </div>'''
html = re.sub(inline_old, inline_new, html, flags=re.DOTALL)

# Replace BMX SVG
bmx_old = r'<!-- BMX SVG -->\s*<svg[^>]*class="discipline-icon[^>]*>.*?</svg>'
bmx_new = '''<!-- BMX SVG -->
              <div class="discipline-icon absolute -top-10 -right-6 w-28 h-28 z-10 pointer-events-none opacity-0" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full text-kinetic-accent animate-float-icon transition-all duration-300" style="animation-delay: 0.5s;">
                  <circle cx="14" cy="46" r="12" stroke-width="3"/>
                  <circle cx="50" cy="46" r="12" stroke-width="3"/>
                  <circle cx="14" cy="46" r="3" fill="currentColor"/>
                  <circle cx="50" cy="46" r="3" fill="currentColor"/>
                  <path d="M14 46l14-22h14l8 22"/>
                  <path d="M34 24l-6-16h-8"/>
                  <path d="M42 24l-4-10h8"/>
                  <path d="M22 8h8" stroke-width="3"/>
                  <circle cx="34" cy="46" r="4" fill="currentColor"/>
                  <path d="M34 46l-6-8"/>
                  <path d="M46 14h-6" stroke-width="3"/>
                </svg>
              </div>'''
html = re.sub(bmx_old, bmx_new, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("Updated icons!")
