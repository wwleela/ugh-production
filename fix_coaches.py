import re

with open('index.html', 'r') as f:
    html = f.read()

target = r'<div class="grid grid-cols-1 md:grid-cols-2 gap-fluid-md max-w-5xl mx-auto"><div class="brutal-card p-4 md:p-6 flex flex-row gap-4 items-center md:items-start text-left">.*?</p></div></div></div>'

replacement = '''<div class="grid grid-cols-1 md:grid-cols-2 gap-fluid-md max-w-5xl mx-auto">
            <!-- Coach 1 -->
            <div class="brutal-card p-4 md:p-6 flex flex-row gap-4 items-center text-left h-full">
              <div class="w-16 h-16 md:w-20 md:h-20 rounded-full overflow-hidden border-2 border-kinetic-border flex-shrink-0 bg-kinetic-muted"></div>
              <div class="min-w-0 flex-1 flex flex-col justify-center">
                <div class="flex flex-wrap items-center gap-2 mb-2">
                  <h3 class="text-lg md:text-xl font-display font-bold uppercase break-words">Coach Leela</h3>
                  <span class="pill-tag bg-kinetic-surface-alt text-[10px] md:text-xs border-kinetic-border text-kinetic-text px-2 py-1 whitespace-normal text-left break-words">Founder / Experienced Skater</span>
                </div>
                <p class="text-kinetic-muted text-sm leading-snug font-body break-words mt-1">Making action sports accessible at the doorstep.</p>
              </div>
            </div>
            <!-- Coach 2 -->
            <div class="brutal-card p-4 md:p-6 flex flex-row gap-4 items-center text-left h-full">
              <div class="w-16 h-16 md:w-20 md:h-20 rounded-full overflow-hidden border-2 border-kinetic-border flex-shrink-0 bg-kinetic-muted"></div>
              <div class="min-w-0 flex-1 flex flex-col justify-center">
                <div class="flex flex-wrap items-center gap-2 mb-2">
                  <h3 class="text-lg md:text-xl font-display font-bold uppercase break-words">Tribhuvan Kokkula</h3>
                  <span class="pill-tag bg-kinetic-surface-alt text-[10px] md:text-xs border-kinetic-border text-kinetic-text px-2 py-1 whitespace-normal text-left break-words">Vice-Chairman</span>
                </div>
                <p class="text-kinetic-muted text-sm leading-snug font-body break-words mt-1">Vice-Chairman of the Skateboarding Sub-Committee (2026–2027 term).</p>
              </div>
            </div>
            <!-- Coach 3 -->
            <div class="brutal-card p-4 md:p-6 flex flex-row gap-4 items-center text-left h-full">
              <div class="w-16 h-16 md:w-20 md:h-20 rounded-full overflow-hidden border-2 border-kinetic-border flex-shrink-0 bg-kinetic-muted"></div>
              <div class="min-w-0 flex-1 flex flex-col justify-center">
                <div class="flex flex-wrap items-center gap-2 mb-2">
                  <h3 class="text-lg md:text-xl font-display font-bold uppercase break-words">Ronnie</h3>
                  <span class="pill-tag bg-kinetic-surface-alt text-[10px] md:text-xs border-kinetic-border text-kinetic-text px-2 py-1 whitespace-normal text-left break-words">Park Manager</span>
                </div>
                <p class="text-kinetic-muted text-sm leading-snug font-body break-words mt-1">Wallride Park Manager, pro skateboarder, and experienced coach.</p>
              </div>
            </div>
            <!-- Coach 4 -->
            <div class="brutal-card p-4 md:p-6 flex flex-row gap-4 items-center text-left h-full">
              <div class="w-16 h-16 md:w-20 md:h-20 rounded-full overflow-hidden border-2 border-kinetic-border flex-shrink-0 bg-kinetic-muted"></div>
              <div class="min-w-0 flex-1 flex flex-col justify-center">
                <div class="flex flex-wrap items-center gap-2 mb-2">
                  <h3 class="text-lg md:text-xl font-display font-bold uppercase break-words">Pixie</h3>
                  <span class="pill-tag bg-kinetic-surface-alt text-[10px] md:text-xs border-kinetic-border text-kinetic-text px-2 py-1 whitespace-normal text-left break-words">Pro Skater</span>
                </div>
                <p class="text-kinetic-muted text-sm leading-snug font-body break-words mt-1">Pro skateboarder and founder of GirlsSk8Hyd, empowering women in action sports.</p>
              </div>
            </div>
          </div>'''

html = re.sub(target, replacement, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
