import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Remove floating CTA
floating_target = r'<!-- Floating CTA -->\s*<button id="wizard-cta" class="fixed z-50.*?</span>\s*</button>'
html = re.sub(floating_target, '', html, flags=re.DOTALL)

# 2. Add to desktop Nav
nav_target = r'(<button id="theme-toggle" class="material-symbols-outlined hover:text-kinetic-accent transition-colors">dark_mode</button>\s*</nav>)'
nav_replacement = r'''<button id="theme-toggle" class="material-symbols-outlined hover:text-kinetic-accent transition-colors">dark_mode</button>
          <button id="wizard-cta" class="bg-kinetic-text text-kinetic-bg px-4 py-2 rounded-full font-display font-medium text-xs hover:scale-105 transition-transform flex items-center gap-1 uppercase tracking-wider ml-2 border border-transparent hover:border-kinetic-accent">
            <span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1rem;">bolt</span> Book
          </button>
        </nav>'''
html = re.sub(nav_target, nav_replacement, html)

# 3. Update Mobile Menu Toggle area
mobile_target = r'(<button id="mobile-menu-btn" class="md:hidden material-symbols-outlined hover:text-kinetic-accent transition-colors ml-2">more_vert</button>)'
mobile_replacement = r'''<div class="flex items-center md:hidden">
          <button onclick="document.getElementById('wizard-modal').classList.remove('hidden')" class="bg-kinetic-text text-kinetic-bg px-3 py-1.5 rounded-full font-display font-medium text-[10px] hover:scale-105 transition-transform flex items-center gap-1 uppercase tracking-wider mr-2 border border-transparent hover:border-kinetic-accent">
            <span class="material-symbols-outlined text-kinetic-accent" style="font-size: 0.9rem;">bolt</span> Book
          </button>
          <button id="mobile-menu-btn" class="material-symbols-outlined hover:text-kinetic-accent transition-colors">more_vert</button>
        </div>'''
html = re.sub(mobile_target, mobile_replacement, html)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
