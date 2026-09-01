import re

with open('index.html', 'r') as f:
    html = f.read()

events_search = r'<section id="events".*?</section>'
events_replace = """<section id="events" class="py-24 px-6 border-b border-kinetic-border bg-kinetic-surface-alt">
        <div class="max-w-7xl mx-auto">
          <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
            <div>
              <span class="pill-tag mb-4">The Schedule</span>
              <h2 class="text-4xl md:text-5xl font-display font-bold uppercase mt-2">Monthly Events</h2>
            </div>
            <div class="flex gap-2">
              <span class="pill-tag bg-kinetic-surface border-kinetic-border">Aug 2026</span>
            </div>
          </div>
          
          <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Featured Event -->
            <div class="lg:col-span-2 brutal-card overflow-hidden flex flex-col">
              <div class="bg-kinetic-muted h-48 sm:h-64 flex items-center justify-center border-b-2 border-kinetic-border relative">
                 <span class="absolute top-4 left-4 pill-tag bg-kinetic-accent text-black border-black shadow-[2px_2px_0px_#000]">Featured</span>
                 <span class="material-symbols-outlined text-6xl text-kinetic-bg">skateboarding</span>
              </div>
              <div class="p-8 flex-1 flex flex-col">
                <div class="flex flex-wrap gap-3 mb-4">
                  <span class="font-mono text-xs uppercase font-bold text-kinetic-text bg-kinetic-surface border border-kinetic-border px-2 py-1 rounded">Aug 29, 2026</span>
                  <span class="font-mono text-xs uppercase font-bold text-kinetic-text bg-kinetic-surface border border-kinetic-border px-2 py-1 rounded">4:00 PM Onwards</span>
                </div>
                <h3 class="text-3xl font-display font-bold mb-2 uppercase">Fam Jam</h3>
                <p class="font-mono text-sm text-kinetic-accent font-bold uppercase mb-4 flex items-center gap-1">
                  <span class="material-symbols-outlined text-sm">location_on</span> [VENUE ADDRESS — CONFIRM]
                </p>
                <p class="text-kinetic-muted font-body mb-8 leading-relaxed flex-1">
                  Monthly skateboarding competition, beginner workshop, and youth culture event. Join us for an evening of progression, local music, and breakdance performances.
                </p>
                <button onclick="window.open('https://wa.me/916304895686?text=Hi%2C%20I%20want%20to%20inquire%20about%20the%20Fam%20Jam%20event.', '_blank')" class="brutal-btn brutal-btn-accent w-full text-center">RSVP / Inquire</button>
              </div>
            </div>
            
            <!-- Upcoming List -->
            <div class="flex flex-col gap-6">
              <h3 class="text-2xl font-display font-bold uppercase mb-2">Upcoming This Week</h3>
              
              <!-- List Item -->
              <div class="brutal-card p-6 flex flex-col">
                <div class="flex justify-between items-start mb-2">
                  <span class="font-mono text-xs font-bold uppercase">Sundays</span>
                  <span class="pill-tag">Morning</span>
                </div>
                <h4 class="text-xl font-display font-bold uppercase mb-2">Sunday Skateboarding Workshop</h4>
                <p class="font-mono text-xs text-kinetic-accent font-bold uppercase mb-4">[VENUE ADDRESS — CONFIRM]</p>
                <p class="text-kinetic-muted text-sm font-body mb-6">Our recurring weekend action sports clinic. Fundamental skateboarding and progressive ramp skills.</p>
                <button onclick="window.open('https://wa.me/916304895686?text=Hi%2C%20I%20want%20to%20inquire%20about%20the%20Sunday%20Skateboarding%20Workshop.', '_blank')" class="brutal-btn w-full text-center text-xs py-2">Book Slot</button>
              </div>
              
              <div class="brutal-card p-6 flex flex-col justify-center items-center text-center bg-kinetic-surface-alt border-dashed border-2">
                 <p class="text-kinetic-muted font-mono text-sm uppercase">More dates dropping soon</p>
              </div>
            </div>
          </div>
        </div>
      </section>"""
html = re.sub(events_search, events_replace, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
