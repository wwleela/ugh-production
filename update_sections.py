import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update Hero to use kinetic styles
hero_search = r'<section class="hero-bg text-white py-32 px-6 text-center">.*?</section>'
hero_replace = """<section class="py-32 px-6 text-center border-b border-kinetic-border">
        <div class="max-w-5xl mx-auto">
          <span class="pill-tag mb-8">Elevate Your Flow</span>
          <h1 class="text-6xl md:text-8xl font-display font-bold mb-8 leading-tight tracking-tight uppercase">
            <span class="text-kinetic-accent" style="text-shadow: 2px 2px 0px var(--kinetic-border), -2px -2px 0px var(--kinetic-border), 2px -2px 0px var(--kinetic-border), -2px 2px 0px var(--kinetic-border);">Urban</span> Gliding<br>
            <span class="italic text-kinetic-muted text-5xl md:text-7xl">Skateboarding, Inline & BMX</span>
          </h1>
          <p class="text-lg md:text-xl text-kinetic-muted mb-12 max-w-2xl mx-auto leading-relaxed font-body">
            Hyderabad's premier doorstep skating coach. Professional workshops and vibrant community events across residential complexes.
          </p>
          <div class="flex flex-col sm:flex-row justify-center gap-4">
            <button onclick="window.open('https://wa.me/916304895686', '_blank')" class="brutal-btn brutal-btn-accent">Book a Session</button>
            <a href="#programs" class="brutal-btn bg-kinetic-surface text-kinetic-text border-kinetic-border">View Pricing</a>
          </div>
        </div>
      </section>"""
html = re.sub(hero_search, hero_replace, html, flags=re.DOTALL)

# 2. Update Leadership (Our Coaches)
coaches_search = r'<section id="leadership".*?</section>'
coaches_replace = """<section id="leadership" class="py-24 px-6 border-b border-kinetic-border bg-kinetic-surface-alt">
        <div class="max-w-7xl mx-auto">
          <div class="text-center mb-16">
            <span class="pill-tag mb-4">The Crew</span>
            <h2 class="text-4xl md:text-5xl font-display font-bold uppercase">Our Coaches</h2>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
            <!-- Coach Leela -->
            <div class="brutal-card p-6 flex flex-col md:flex-row gap-6 items-center md:items-start text-left">
              <div class="w-32 h-32 rounded-full overflow-hidden border-2 border-kinetic-border flex-shrink-0 bg-kinetic-muted">
                <!-- Image placeholder -->
              </div>
              <div>
                <div class="flex items-center gap-3 mb-2">
                  <h3 class="text-2xl font-display font-bold uppercase">Coach Leela</h3>
                  <span class="pill-tag bg-kinetic-accent text-black border-black">Founder</span>
                </div>
                <p class="font-mono text-sm text-kinetic-muted uppercase tracking-wider mb-4">Head Coach</p>
                <p class="text-kinetic-text leading-relaxed font-body mb-4">Founder and principal coach of Urban Gliding Hyderabad. Bringing doorstep training and advanced ramp skills to residential hubs across the city.</p>
              </div>
            </div>
            
            <!-- Coach Tribhoovan -->
            <div class="brutal-card p-6 flex flex-col md:flex-row gap-6 items-center md:items-start text-left">
              <div class="w-32 h-32 rounded-full overflow-hidden border-2 border-kinetic-border flex-shrink-0 bg-kinetic-muted">
                <!-- Image placeholder -->
              </div>
              <div>
                <div class="flex items-center gap-3 mb-2">
                  <h3 class="text-2xl font-display font-bold uppercase">Tribhoovan</h3>
                  <span class="pill-tag">RSFI</span>
                </div>
                <p class="font-mono text-sm text-kinetic-muted uppercase tracking-wider mb-4">Skateboarding & Inline</p>
                <p class="text-kinetic-text leading-relaxed font-body mb-4">RSFI-affiliated coach specializing in competitive skateboarding and aggressive inline skating progression.</p>
              </div>
            </div>
          </div>
        </div>
      </section>"""
html = re.sub(coaches_search, coaches_replace, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
