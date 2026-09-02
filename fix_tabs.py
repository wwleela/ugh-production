import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update the HTML structure of the alliances section to have proper `hidden` and `grid` classes.
target_alliances = r'<section id="alliances".*?</section>'
replacement_alliances = '''<section id="alliances" class="py-fluid-xl px-[clamp(1.25rem,5vw,4rem)] bg-kinetic-surface-alt border-t border-kinetic-border">
        <div class="max-w-[1440px] mx-auto">
          <div class="text-center mb-fluid-md">
            <span class="pill-tag mb-4">Ecosystem</span>
            <h2 class="text-4xl md:text-5xl font-display font-bold mt-2">Alliances &amp; Experience</h2>
          </div>
          
          <!-- Interactive Tabs -->
          <div class="flex flex-wrap justify-center border-b border-kinetic-border mb-10 overflow-x-auto hide-scrollbar gap-2 sm:gap-0">
            <button class="tab-btn active px-6 py-4 font-display font-bold uppercase tracking-widest text-sm border-b-2 border-kinetic-text text-kinetic-text hover:text-kinetic-accent transition-colors whitespace-nowrap" data-target="brands">Brands &amp; Partners</button>
            <button class="tab-btn px-6 py-4 font-display font-bold uppercase tracking-widest text-sm border-b-2 border-transparent hover:text-kinetic-accent transition-colors text-kinetic-muted whitespace-nowrap" data-target="events-hosted">Events Hosted</button>
            <button class="tab-btn px-6 py-4 font-display font-bold uppercase tracking-widest text-sm border-b-2 border-transparent hover:text-kinetic-accent transition-colors text-kinetic-muted whitespace-nowrap" data-target="media">Media &amp; Features</button>
          </div>

          <!-- Brands Gallery -->
          <div id="brands" class="tab-content grid grid-cols-2 md:grid-cols-4 gap-fluid-md animate-fade-in">
            <div class="group relative aspect-video bg-kinetic-surface border border-kinetic-border overflow-hidden rounded-lg hover:border-kinetic-accent transition-colors shadow-sm">
              <img src="https://images.unsplash.com/photo-1528249227670-9ba48616014f?q=80&w=600&auto=format&fit=crop" alt="Brand Partner" class="w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-105 transition-all duration-500 grayscale group-hover:grayscale-0" />
              <div class="absolute inset-0 flex items-center justify-center bg-kinetic-bg/50 group-hover:bg-transparent transition-colors">
                <span class="text-kinetic-text font-display font-bold text-sm uppercase tracking-widest group-hover:opacity-0 transition-opacity drop-shadow-md">Decathlon</span>
              </div>
            </div>
            <div class="group relative aspect-video bg-kinetic-surface border border-kinetic-border overflow-hidden rounded-lg hover:border-kinetic-accent transition-colors shadow-sm">
              <img src="https://images.unsplash.com/photo-1595152772835-219674b2a8a6?q=80&w=600&auto=format&fit=crop" alt="Brand Partner" class="w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-105 transition-all duration-500 grayscale group-hover:grayscale-0" />
              <div class="absolute inset-0 flex items-center justify-center bg-kinetic-bg/50 group-hover:bg-transparent transition-colors">
                <span class="text-kinetic-text font-display font-bold text-sm uppercase tracking-widest group-hover:opacity-0 transition-opacity drop-shadow-md">Vans</span>
              </div>
            </div>
            <div class="group relative aspect-video bg-kinetic-surface border border-kinetic-border overflow-hidden rounded-lg hover:border-kinetic-accent transition-colors shadow-sm">
              <img src="https://images.unsplash.com/photo-1518170886166-51f67fce57cb?q=80&w=600&auto=format&fit=crop" alt="Brand Partner" class="w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-105 transition-all duration-500 grayscale group-hover:grayscale-0" />
              <div class="absolute inset-0 flex items-center justify-center bg-kinetic-bg/50 group-hover:bg-transparent transition-colors">
                <span class="text-kinetic-text font-display font-bold text-sm uppercase tracking-widest group-hover:opacity-0 transition-opacity drop-shadow-md">Red Bull</span>
              </div>
            </div>
            <div class="group relative aspect-video bg-kinetic-surface border border-kinetic-border overflow-hidden rounded-lg hover:border-kinetic-accent transition-colors shadow-sm">
              <img src="https://images.unsplash.com/photo-1518063319789-7217e6706b04?q=80&w=600&auto=format&fit=crop" alt="Brand Partner" class="w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-105 transition-all duration-500 grayscale group-hover:grayscale-0" />
              <div class="absolute inset-0 flex items-center justify-center bg-kinetic-bg/50 group-hover:bg-transparent transition-colors">
                <span class="text-kinetic-text font-display font-bold text-sm uppercase tracking-widest group-hover:opacity-0 transition-opacity drop-shadow-md">G-Shock</span>
              </div>
            </div>
          </div>

          <!-- Events Hosted Gallery -->
          <div id="events-hosted" class="tab-content hidden grid-cols-1 md:grid-cols-3 gap-fluid-md animate-fade-in">
            <div class="group relative aspect-[4/3] bg-kinetic-surface border border-kinetic-border overflow-hidden rounded-lg shadow-sm">
              <img src="https://images.unsplash.com/photo-1564982752979-3f7bc974d29a?q=80&w=800&auto=format&fit=crop" alt="Event" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex flex-col justify-end p-6">
                <p class="text-white text-xs font-bold uppercase tracking-widest mb-1 opacity-80">Go Skateboarding Day</p>
                <h3 class="text-white text-xl font-display font-bold">Annual Hyd Skate Jam</h3>
              </div>
            </div>
            <div class="group relative aspect-[4/3] bg-kinetic-surface border border-kinetic-border overflow-hidden rounded-lg shadow-sm">
              <img src="https://images.unsplash.com/photo-1520045892732-304bc3ac5d8e?q=80&w=800&auto=format&fit=crop" alt="Event" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex flex-col justify-end p-6">
                <p class="text-white text-xs font-bold uppercase tracking-widest mb-1 opacity-80">Community Outreach</p>
                <h3 class="text-white text-xl font-display font-bold">Wall Ride Progression</h3>
              </div>
            </div>
            <div class="group relative aspect-[4/3] bg-kinetic-surface border border-kinetic-border overflow-hidden rounded-lg shadow-sm">
              <img src="https://images.unsplash.com/photo-1518880313888-2122b07f8279?q=80&w=800&auto=format&fit=crop" alt="Event" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex flex-col justify-end p-6">
                <p class="text-white text-xs font-bold uppercase tracking-widest mb-1 opacity-80">Youth Development</p>
                <h3 class="text-white text-xl font-display font-bold">PBEL Summer Camp</h3>
              </div>
            </div>
          </div>

          <!-- Media Gallery -->
          <div id="media" class="tab-content hidden grid-cols-1 md:grid-cols-3 gap-fluid-md animate-fade-in">
            <div class="group relative aspect-square bg-kinetic-surface border border-kinetic-border overflow-hidden rounded-lg shadow-sm flex flex-col items-center justify-center p-8 text-center hover:border-kinetic-accent transition-colors">
              <span class="material-symbols-outlined text-4xl text-kinetic-accent mb-4">newspaper</span>
              <h3 class="text-2xl font-display font-bold mb-2">The Hindu</h3>
              <p class="text-kinetic-muted text-sm line-clamp-3">"Urban Gliding Hyderabad is reshaping the concrete landscape of the city, bringing structured extreme sports to the grassroots level."</p>
              <span class="mt-6 text-xs font-bold uppercase tracking-widest border-b border-kinetic-accent text-kinetic-text pb-1">Read Feature</span>
            </div>
            <div class="group relative aspect-square bg-kinetic-surface border border-kinetic-border overflow-hidden rounded-lg shadow-sm flex flex-col items-center justify-center p-8 text-center hover:border-kinetic-accent transition-colors">
              <span class="material-symbols-outlined text-4xl text-kinetic-accent mb-4">article</span>
              <h3 class="text-2xl font-display font-bold mb-2">Times of India</h3>
              <p class="text-kinetic-muted text-sm line-clamp-3">"Hyderabad's skate scene explodes with new talent as premium doorstep coaching programs gain massive traction."</p>
              <span class="mt-6 text-xs font-bold uppercase tracking-widest border-b border-kinetic-accent text-kinetic-text pb-1">Read Feature</span>
            </div>
            <div class="group relative aspect-square bg-kinetic-surface border border-kinetic-border overflow-hidden rounded-lg shadow-sm flex flex-col items-center justify-center p-8 text-center hover:border-kinetic-accent transition-colors">
              <span class="material-symbols-outlined text-4xl text-kinetic-accent mb-4">play_circle</span>
              <h3 class="text-2xl font-display font-bold mb-2">Red Bull TV</h3>
              <p class="text-kinetic-muted text-sm line-clamp-3">"Local crews in Hyderabad showcase immense progression at the newly built Wall Ride Park."</p>
              <span class="mt-6 text-xs font-bold uppercase tracking-widest border-b border-kinetic-accent text-kinetic-text pb-1">Watch Clip</span>
            </div>
          </div>
        </div>
      </section>'''

html = re.sub(target_alliances, replacement_alliances, html, flags=re.DOTALL)


# 2. Update the javascript for the inner tabs to correctly apply tailwind grid vs hidden classes.
# The original JS:
js_target = r'// Tab interaction.*?const tabs = document\.querySelectorAll\(\'\.tab-btn\'\);.*?const contents = document\.querySelectorAll\(\'\.tab-content\'\);.*?tabs\.forEach\(tab => \{.*?tab\.addEventListener\(\'click\', \(\) => \{.*?tabs\.forEach\(t => \{ t\.classList\.remove\(\'active\'\); t\.classList\.add\(\'text-\[#777\]\'\); \}\);.*?contents\.forEach\(c => c\.classList\.remove\(\'active\'\)\);.*?tab\.classList\.add\(\'active\'\);.*?tab\.classList\.remove\(\'text-\[#777\]\'\);.*?document\.getElementById\(tab\.dataset\.target\)\.classList\.add\(\'active\'\);.*?\}\);.*?\}\);'

js_replacement = '''// Tab interaction (Alliances Section)
      const tabs = document.querySelectorAll('.tab-btn');
      const contents = document.querySelectorAll('.tab-content');
      tabs.forEach(tab => {
        tab.addEventListener('click', () => {
          // Reset all tabs
          tabs.forEach(t => { 
            t.classList.remove('active', 'border-kinetic-text', 'text-kinetic-text'); 
            t.classList.add('border-transparent', 'text-kinetic-muted'); 
          });
          // Reset all contents (hide them)
          contents.forEach(c => {
            c.classList.remove('grid');
            c.classList.add('hidden');
          });
          
          // Activate clicked tab
          tab.classList.add('active', 'border-kinetic-text', 'text-kinetic-text');
          tab.classList.remove('border-transparent', 'text-kinetic-muted');
          
          // Show target content
          const target = document.getElementById(tab.dataset.target);
          target.classList.remove('hidden');
          target.classList.add('grid');
        });
      });'''

html = re.sub(js_target, js_replacement, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print("done")
