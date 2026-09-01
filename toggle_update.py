import re

with open('index.html', 'r') as f:
    html = f.read()

# Make sure body has dark class if user prefers it (we'll handle toggle in js)
html = html.replace('<body class="bg-dark-bg text-dark-text antialiased">', '<body class="antialiased">')

# Header
header_nav = """        <nav class="hidden md:flex gap-8 font-bold text-sm uppercase tracking-widest font-mono">
          <a href="#community" class="hover:text-kinetic-accent transition-colors">Impact</a>
          <a href="#events" class="hover:text-kinetic-accent transition-colors">Events</a>
          <a href="#programs" class="hover:text-kinetic-accent transition-colors">Pricing</a>
          <a href="#venues" class="hover:text-kinetic-accent transition-colors">Venues</a>
          <button id="theme-toggle" class="material-symbols-outlined hover:text-kinetic-accent transition-colors">dark_mode</button>
        </nav>"""
html = re.sub(r'<nav.*?</nav>', header_nav, html, flags=re.DOTALL)

# Header bg
html = html.replace('bg-dark-bg/95', 'bg-kinetic-bg/95')
html = html.replace('border-dark-border', 'border-kinetic-border')
html = html.replace('text-ugh-orange', 'text-kinetic-accent')

with open('index.html', 'w') as f:
    f.write(html)
