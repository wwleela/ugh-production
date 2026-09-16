import re

with open('index.html', 'r') as f:
    content = f.read()

old_btn = r'<button onclick="document\.getElementById\(\'faq-modal\'\)\.classList\.remove\(\'hidden\'\)" class="fixed bottom-6 right-6 md:bottom-10 md:right-10 z-\[90\] w-14 h-14 bg-kinetic-text text-kinetic-bg rounded-full shadow-\[4px_4px_0px_var\(--kinetic-accent\)] flex items-center justify-center hover:-translate-y-1 hover:shadow-\[6px_6px_0px_var\(--kinetic-accent\)] transition-all focus:outline-none focus-visible:ring-4 focus-visible:ring-kinetic-accent group border-2 border-transparent hover:border-kinetic-accent">\s*<span class="material-symbols-outlined text-3xl">help_outline</span>\s*</button>'

new_btn = """<div id="floating-faq-container" class="fixed bottom-6 right-6 md:bottom-10 md:right-10 z-[90] flex items-center gap-2">
      <!-- Dismiss Button -->
      <button onclick="document.getElementById('floating-faq-container').remove()" class="w-8 h-8 rounded-full bg-kinetic-surface border border-kinetic-border flex items-center justify-center text-kinetic-muted hover:text-kinetic-accent hover:border-kinetic-accent transition-colors shadow-sm" aria-label="Dismiss FAQ button">
        <span class="material-symbols-outlined text-sm">close</span>
      </button>
      
      <!-- FAQ Trigger -->
      <button onclick="document.getElementById('faq-modal').classList.remove('hidden')" class="px-6 h-12 bg-kinetic-text text-kinetic-bg rounded-full shadow-[4px_4px_0px_var(--kinetic-accent)] flex items-center justify-center hover:-translate-y-1 hover:shadow-[6px_6px_0px_var(--kinetic-accent)] transition-all focus:outline-none focus-visible:ring-4 focus-visible:ring-kinetic-accent group border-2 border-transparent hover:border-kinetic-accent font-display font-bold uppercase tracking-wider text-sm">
        FAQ
      </button>
    </div>"""

content = re.sub(old_btn, new_btn, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

