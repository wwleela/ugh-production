import re

with open('index.html', 'r') as f:
    html = f.read()

target = r'<section class="py-fluid-xl px-\[clamp\(1\.25rem,5vw,4rem\)\] text-center border-b border-kinetic-border">.*?<div class="max-w-5xl mx-auto">.*?<span class="pill-tag mb-8">Elevate Your Flow</span>.*?<h1 class="text-6xl md:text-8xl font-display font-bold mb-8 leading-tight tracking-tight uppercase"><span class="text-kinetic-accent".*?>Master</span> the Pavement\.</h1>.*?<p class="text-lg md:text-xl text-kinetic-muted mb-fluid-md max-w-2xl mx-auto leading-relaxed font-body">Hyderabad\'s premier action sports coaching\. From static balance to transition carving across Skateboarding, Inline, and BMX\.</p>.*?<div class="flex flex-col sm:flex-row justify-center gap-4">.*?<button onclick="document\.getElementById\(\'wizard-modal\'\)\.classList\.remove\(\'hidden\'\)" class="brutal-btn brutal-btn-accent">Book a Session</button>.*?<a href="#pricing" class="tab-link brutal-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-tab="pricing">See Pricing</a>.*?<a href="#venues" class="tab-link brutal-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-tab="venues">Find a Venue</a>.*?</div>.*?</div>.*?</section>'

replacement = '''<section class="relative py-[clamp(4rem,10vw,8rem)] px-[clamp(1.25rem,5vw,4rem)] text-center border-b border-kinetic-border overflow-hidden">
        <!-- Subtle Dot Grid Background Pattern -->
        <div class="absolute inset-0 z-0 opacity-10 dark:opacity-20 pointer-events-none" style="background-image: radial-gradient(var(--kinetic-text) 1px, transparent 1px); background-size: 24px 24px; background-position: center;"></div>
        
        <div class="relative z-10 max-w-5xl mx-auto flex flex-col items-center">
          <span class="inline-block px-4 py-1.5 bg-kinetic-surface-alt border border-kinetic-border rounded-full text-kinetic-text text-xs font-bold font-mono uppercase tracking-[0.2em] mb-8 shadow-sm">Elevate Your Flow</span>
          
          <h1 class="text-[clamp(3.5rem,8vw,7rem)] font-display font-bold mb-6 leading-[0.9] tracking-tighter uppercase flex flex-wrap justify-center items-center gap-y-4">
            <span class="inline-block bg-kinetic-accent text-kinetic-bg px-6 pt-3 pb-1 -rotate-2 shadow-[6px_6px_0px_var(--kinetic-shadow)] border-2 border-kinetic-shadow mr-2 sm:mr-4">Master</span> 
            <span>the Pavement.</span>
          </h1>
          
          <p class="text-lg md:text-2xl text-kinetic-muted mb-12 max-w-3xl mx-auto leading-relaxed font-body font-medium">
            Hyderabad's premier action sports coaching. From static balance to transition carving across Skateboarding, Inline, and BMX.
          </p>
          
          <div class="flex flex-col sm:flex-row items-center justify-center gap-4 sm:gap-6 w-full sm:w-auto">
            <button onclick="document.getElementById('wizard-modal').classList.remove('hidden')" class="w-full sm:w-auto group relative px-8 py-4 bg-kinetic-text text-kinetic-bg font-display font-bold text-lg uppercase tracking-wider rounded-none overflow-hidden transition-all hover:scale-105 active:scale-95 shadow-[8px_8px_0px_var(--kinetic-accent)] border-2 border-kinetic-text flex items-center justify-center gap-2">
              <span class="relative z-10">Book a Session</span>
              <span class="material-symbols-outlined relative z-10 group-hover:translate-x-1 transition-transform">arrow_forward</span>
            </button>
            
            <div class="flex items-center gap-4 w-full sm:w-auto justify-center">
              <a href="#pricing" class="tab-link text-kinetic-text font-mono font-bold text-sm uppercase tracking-widest hover:text-kinetic-accent transition-colors underline-offset-8 hover:underline decoration-2" data-tab="pricing">See Pricing</a>
              <span class="text-kinetic-muted/30">|</span>
              <a href="#venues" class="tab-link text-kinetic-text font-mono font-bold text-sm uppercase tracking-widest hover:text-kinetic-accent transition-colors underline-offset-8 hover:underline decoration-2" data-tab="venues">Find Venue</a>
            </div>
          </div>
        </div>
      </section>'''

html = re.sub(target, replacement, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
