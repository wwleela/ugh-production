import re

with open('index.html', 'r') as f:
    html = f.read()

# 3. Update Community (Training Hubs)
community_search = r'<section id="community".*?</section>'
community_replace = """<section id="community" class="py-24 px-6 border-b border-kinetic-border">
        <div class="max-w-7xl mx-auto">
          <div class="text-center mb-16">
            <span class="pill-tag mb-4">Community Impact</span>
            <h2 class="text-4xl md:text-5xl font-display font-bold uppercase">Training Hubs</h2>
            <p class="mt-4 text-kinetic-muted max-w-2xl mx-auto font-body">Where we've coached across Hyderabad's premier residential complexes.</p>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Hub Cards -->
            <div class="brutal-card p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-display font-bold uppercase">Aparna Serene Park</h3>
                <span class="pill-tag">Kondapur</span>
              </div>
              <p class="font-mono text-xs text-kinetic-muted uppercase mb-4">Coach Leela</p>
            </div>
            
            <div class="brutal-card p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-display font-bold uppercase">Aparna Sarovar Zenith</h3>
                <span class="pill-tag">Nallagandla</span>
              </div>
              <p class="font-mono text-xs text-kinetic-muted uppercase mb-4">Coach Leela</p>
            </div>
            
            <div class="brutal-card p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-display font-bold uppercase">Aparna Sarovar Grande</h3>
                <span class="pill-tag">Nallagandla</span>
              </div>
              <p class="font-mono text-xs text-kinetic-muted uppercase mb-4">Coach Leela</p>
            </div>
            
            <div class="brutal-card p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-display font-bold uppercase">Aparna Hights I</h3>
                <span class="pill-tag">Kondapur</span>
              </div>
              <p class="font-mono text-xs text-kinetic-muted uppercase mb-4">Coach Leela</p>
            </div>
            
            <div class="brutal-card p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-display font-bold uppercase">PBEL City</h3>
                <span class="pill-tag">Peeramcheruvu</span>
              </div>
              <p class="font-mono text-xs text-kinetic-muted uppercase mb-4">Coach Tribhoovan</p>
            </div>
            
            <div class="brutal-card p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-display font-bold uppercase">My Home Tarkshya</h3>
                <span class="pill-tag">Kokapet</span>
              </div>
              <p class="font-mono text-xs text-kinetic-muted uppercase mb-4">Coach Leela</p>
            </div>
            
            <div class="brutal-card p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-display font-bold uppercase">My Home Navadweepa</h3>
                <span class="pill-tag">Madhapur</span>
              </div>
              <p class="font-mono text-xs text-kinetic-muted uppercase mb-4">Coach Leela</p>
            </div>
            
            <div class="brutal-card p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-display font-bold uppercase">Ananda Bay Hills</h3>
                <span class="pill-tag">Tellapur</span>
              </div>
              <p class="font-mono text-xs text-kinetic-muted uppercase mb-4">Coach Tribhoovan</p>
            </div>
          </div>
        </div>
      </section>"""
html = re.sub(community_search, community_replace, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
