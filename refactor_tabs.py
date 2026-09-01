import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update the Header Navigation
nav_regex = r'<nav class="hidden md:flex .*?</nav>'
new_nav = """<nav class="hidden md:flex gap-fluid-md font-bold text-sm uppercase tracking-widest font-mono">
          <a href="#impact" class="tab-link hover:text-kinetic-accent transition-colors" data-tab="impact">Impact</a>
          <a href="#events" class="tab-link hover:text-kinetic-accent transition-colors" data-tab="events">Events</a>
          <a href="#pricing" class="tab-link hover:text-kinetic-accent transition-colors" data-tab="pricing">Pricing</a>
          <a href="#venues" class="tab-link hover:text-kinetic-accent transition-colors" data-tab="venues">Venues</a>
          <button id="theme-toggle" class="material-symbols-outlined hover:text-kinetic-accent transition-colors">dark_mode</button>
        </nav>"""
html = re.sub(nav_regex, new_nav, html, flags=re.DOTALL)

# Also update the Logo to point to #home and act as a tab link
logo_regex = r'<a href="#" class="flex items-center gap-3">'
new_logo = '<a href="#home" class="tab-link flex items-center gap-3" data-tab="home">'
html = html.replace(logo_regex, new_logo)

# Update Hero Quick Action Buttons
# "Book a Session" (opens Session Matcher modal), "See Pricing" (switches to Pricing tab), "Find a Venue" (switches to Venues tab)
# Wait, Book a Session currently opens whatsapp? Let's check.
# Hero buttons:
# <button onclick="window.open('https://wa.me/916304895686', '_blank')" class="brutal-btn brutal-btn-accent">Book a Session</button>
# <a href="#programs" class="brutal-btn bg-kinetic-surface text-kinetic-text border-kinetic-border">View Pricing</a>
# Prompt says: "Book a Session" (opens Session Matcher modal)
hero_btns_regex = r'<div class="flex flex-col sm:flex-row justify-center gap-4">\s*<button.*?</button>\s*<a.*?</a>\s*</div>'
new_hero_btns = """<div class="flex flex-col sm:flex-row justify-center gap-4">
            <button onclick="document.getElementById('wizard-modal').classList.remove('hidden')" class="brutal-btn brutal-btn-accent">Book a Session</button>
            <a href="#pricing" class="tab-link brutal-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-tab="pricing">See Pricing</a>
            <a href="#venues" class="tab-link brutal-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-tab="venues">Find a Venue</a>
          </div>"""
html = re.sub(hero_btns_regex, new_hero_btns, html, flags=re.DOTALL)

# Update Hero Title and Trust Badges
# Hero: "Master the Concrete. Defy Gravity." + subhead + trust badge row
# (RSFI-Credentialed Coaching / Doorstep & Park Sessions / 9 Communities Trained)
hero_text_regex = r'<span class="pill-tag mb-8">Elevate Your Flow</span>\s*<h1.*?</h1>\s*<p.*?</p>'
new_hero_text = """<span class="pill-tag mb-8">Elevate Your Flow</span>
          <h1 class="text-6xl md:text-8xl font-display font-bold mb-8 leading-tight tracking-tight uppercase">
            <span class="text-kinetic-accent" style="text-shadow: 2px 2px 0px var(--kinetic-shadow), -2px -2px 0px var(--kinetic-shadow), 2px -2px 0px var(--kinetic-shadow), -2px 2px 0px var(--kinetic-shadow);">Master</span> the Concrete.<br>
            <span class="italic text-kinetic-muted text-5xl md:text-7xl">Defy Gravity.</span>
          </h1>
          <p class="text-lg md:text-xl text-kinetic-muted mb-fluid-md max-w-2xl mx-auto leading-relaxed font-body">
            Hyderabad's premier action sports coaching. From static balance to transition carving across Skateboarding, Inline, and BMX.
          </p>
          <div class="flex flex-wrap justify-center gap-4 mb-10">
            <span class="pill-tag bg-kinetic-surface border-kinetic-border text-kinetic-text text-xs">RSFI-Credentialed Coaching</span>
            <span class="pill-tag bg-kinetic-surface border-kinetic-border text-kinetic-text text-xs">Doorstep & Park Sessions</span>
            <span class="pill-tag bg-kinetic-surface border-kinetic-border text-kinetic-text text-xs">9 Communities Trained</span>
          </div>"""
html = re.sub(hero_text_regex, new_hero_text, html, flags=re.DOTALL)

# 2. Update Mobile Bottom Bar
mobile_bar_regex = r'<div class="md:hidden fixed bottom-0 left-0 w-full.*?</div>'
new_mobile_bar = """<div class="md:hidden fixed bottom-0 left-0 w-full bg-kinetic-surface/80 backdrop-blur-xl border-t border-kinetic-border p-[clamp(0.5rem,2vw,1rem)] flex gap-3 z-40">
      <a href="#pricing" class="tab-link brutal-btn flex-1 text-center bg-kinetic-surface text-kinetic-text border-kinetic-border text-xs" data-tab="pricing">View Pricing</a>
      <button onclick="document.getElementById('wizard-modal').classList.remove('hidden')" class="brutal-btn brutal-btn-accent flex-1 text-center text-xs">Book Session</button>
    </div>"""
html = re.sub(mobile_bar_regex, new_mobile_bar, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
