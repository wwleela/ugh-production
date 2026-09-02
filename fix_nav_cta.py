import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace desktop button
desktop_target = r'<button id="wizard-cta" class="bg-kinetic-text text-kinetic-bg px-4 py-2 rounded-full font-display font-medium text-xs hover:scale-105 transition-transform flex items-center gap-1 uppercase tracking-wider ml-2 border border-transparent hover:border-kinetic-accent">.*?Book\s*</button>'
desktop_replacement = r'''<button id="wizard-cta" class="hover:text-kinetic-accent transition-colors flex items-center gap-1 cursor-pointer ml-2">
            <span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1.2rem;">bolt</span> Book
          </button>'''
html = re.sub(desktop_target, desktop_replacement, html, flags=re.DOTALL)

# Replace mobile button
mobile_target = r'<button onclick="document.getElementById\(\'wizard-modal\'\)\.classList\.remove\(\'hidden\'\)" class="bg-kinetic-text text-kinetic-bg px-3 py-1\.5 rounded-full font-display font-medium text-\[10px\] hover:scale-105 transition-transform flex items-center gap-1 uppercase tracking-wider mr-2 border border-transparent hover:border-kinetic-accent">.*?Book\s*</button>'
mobile_replacement = r'''<button onclick="document.getElementById('wizard-modal').classList.remove('hidden')" class="hover:text-kinetic-accent transition-colors flex items-center gap-1 cursor-pointer mr-3 font-mono font-bold text-xs uppercase tracking-widest">
            <span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1.1rem;">bolt</span> Book
          </button>'''
html = re.sub(mobile_target, mobile_replacement, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
