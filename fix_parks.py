import re

with open('index.html', 'r') as f:
    html = f.read()

target = r'<div class="grid grid-cols-\[repeat\(auto-fit,minmax\(280px,1fr\)\)\] gap-fluid-md">.*?</div>\s*</div>\s*</section>'

replacement = '''<div class="grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-fluid-md">
            <!-- Wall Ride Park -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Public Access</span>
              <h3 class="text-2xl sm:text-3xl font-display font-bold mb-1 break-words">Wall Ride Park</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Hyderabad</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">India's first Swiss-made pump track. Rewarded for bringing skate culture to the state, featuring ramps and bowls for ultimate progression.</p>
            </div>
            <!-- Emptyhead Skate Park -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Public Access</span>
              <h3 class="text-2xl sm:text-3xl font-display font-bold mb-1 break-words">Emptyhead Skate Park</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Hyderabad</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">Known for its unmatched vibe, seamlessly blending music, dance, and skateboarding into a unique cultural experience.</p>
            </div>
            <!-- Primo Skatepark -->
            <div class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col">
              <span class="inline-block self-start px-3 py-1 bg-kinetic-surface-alt text-kinetic-text text-[10px] font-bold uppercase tracking-widest rounded-full mb-4 border border-kinetic-border break-words">Public Access</span>
              <h3 class="text-2xl sm:text-3xl font-display font-bold mb-1 break-words">Primo Skatepark</h3>
              <p class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words">Hyderabad</p>
              <p class="text-kinetic-muted text-sm flex-1 break-words">A dedicated skate park and shop built specifically to grow and support the local skateboarding culture and community.</p>
            </div>
          </div>
        </div>
      </section>'''

html = re.sub(target, replacement, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
