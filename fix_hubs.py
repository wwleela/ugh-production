import re

with open('index.html', 'r') as f:
    html = f.read()

target = r'<section id="community".*?</section>'

replacement = '''<section id="community" class="py-fluid-xl px-[clamp(1.25rem,5vw,4rem)] border-b border-kinetic-border">
        <div class="max-w-[1440px] mx-auto">
          <div class="text-center mb-fluid-lg">
            <span class="pill-tag mb-4">Community Impact</span>
            <h2 class="text-4xl md:text-5xl font-display font-bold uppercase">Training Hubs</h2>
            <p class="mt-4 text-kinetic-muted max-w-2xl mx-auto font-body">Where we've coached across Hyderabad's premier residential complexes.</p>
          </div>
          <div class="grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-fluid-md">
            <!-- Hub 1 -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col hover:-translate-y-1 transition-transform">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Doorstep Coaching</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold mb-1 break-words">Aparna Serene Park</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Kondapur / Gachibowli</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">Conducted introductory skateboarding and inline skating workshops in this expansive ~19-acre community. Our coaching sessions brought action sports directly to the ~1,680 units.</p>
            </div>
            <!-- Hub 2 -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col hover:-translate-y-1 transition-transform">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Doorstep Coaching</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold mb-1 break-words">Aparna Sarovar Zenith</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Nallagandla</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">Ran dedicated coaching sessions across this ~24.6-acre residential space. We introduced safe, structured inline skating and skateboarding fundamentals.</p>
            </div>
            <!-- Hub 3 -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col hover:-translate-y-1 transition-transform">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Doorstep Coaching</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold mb-1 break-words">Aparna Sarovar Grande</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Nallagandla</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">Led active youth workshops in this ~10.5-acre property. Our focus on certified safety gear and progressive learning helped residents master the concrete safely.</p>
            </div>
            <!-- Hub 4 -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col hover:-translate-y-1 transition-transform">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Doorstep Coaching</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold mb-1 break-words">Aparna Hights I</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Kondapur</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">Conducted action sports clinics for the residents, bringing our doorstep coaching model to life. Sessions focused on balance, agility, and fundamental skate mechanics.</p>
            </div>
            <!-- Hub 5 -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col hover:-translate-y-1 transition-transform">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Doorstep Coaching</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold mb-1 break-words">PBEL City</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Peerancheru</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">Ran summer camp clinics and recurring coaching batches for residents. We transformed the community spaces into active learning zones for action sports.</p>
            </div>
            <!-- Hub 6 -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col hover:-translate-y-1 transition-transform">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Doorstep Coaching</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold mb-1 break-words">Ananda Bay Hills</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Narsingi</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">Provided structured doorstep coaching within this ~5.29-acre community. We introduced fundamental ramp transitions and flat-ground skills to the youth.</p>
            </div>
            <!-- Hub 7 -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col hover:-translate-y-1 transition-transform">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Doorstep Coaching</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold mb-1 break-words">My Home Tarkshya</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Kokapet</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">Conducted safe, structured skating sessions for residents. Our coaches focused on foundational skills and proper safety protocols.</p>
            </div>
            <!-- Hub 8 -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col hover:-translate-y-1 transition-transform">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Doorstep Coaching</span>
              <h3 class="text-xl sm:text-2xl font-display font-bold mb-1 break-words">My Home Navadweepa</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Madhapur / HITEC City</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">Ran introductory and progression workshops for the community. We delivered professional action sports instruction directly to the residents' doorsteps.</p>
            </div>
          </div>
        </div>
      </section>'''

html = re.sub(target, replacement, html, flags=re.DOTALL)
with open('index.html', 'w') as f:
    f.write(html)
print("done")
