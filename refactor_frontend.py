import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Replace tailwind.config
tailwind_script = """    <script>
      tailwind.config = {
        darkMode: 'class',
        theme: {
          extend: {
            colors: {
              'kinetic-bg': 'var(--kinetic-bg)',
              'kinetic-surface': 'var(--kinetic-surface)',
              'kinetic-border': 'var(--kinetic-border)',
              'kinetic-text': 'var(--kinetic-text)',
              'kinetic-muted': 'var(--kinetic-muted)',
              'kinetic-accent': 'var(--kinetic-accent)',
              'kinetic-shadow': 'var(--kinetic-shadow)',
              'kinetic-surface-alt': 'var(--kinetic-surface-alt)'
            },
            spacing: {
              'fluid-xs': 'clamp(0.5rem, 1vw, 0.75rem)',
              'fluid-sm': 'clamp(0.75rem, 1.5vw, 1.25rem)',
              'fluid-md': 'clamp(1.5rem, 3vw, 2.5rem)',
              'fluid-lg': 'clamp(3rem, 6vw, 5rem)',
              'fluid-xl': 'clamp(5rem, 10vw, 8rem)',
            },
            fontSize: {
              'fluid-h1': ['clamp(2.5rem, 6vw + 1rem, 5rem)', { lineHeight: '1.05', letterSpacing: '-0.03em' }],
              'fluid-h2': ['clamp(1.8rem, 4vw + 0.5rem, 3.2rem)', { lineHeight: '1.15', letterSpacing: '-0.02em' }],
              'fluid-body': ['clamp(1rem, 0.95rem + 0.3vw, 1.15rem)', { lineHeight: '1.6' }],
            },
            fontFamily: {
              display: ['Sora', 'sans-serif'],
              body: ['Hanken Grotesk', 'sans-serif'],
              mono: ['JetBrains Mono', 'monospace']
            },
            borderRadius: {
              '2xl': '1.5rem',
              '3xl': '2rem',
            },
            boxShadow: {
              'brutal': '4px 4px 0px var(--kinetic-shadow)',
              'brutal-lg': '8px 8px 0px var(--kinetic-shadow)',
              'brutal-hover': '12px 12px 0px var(--kinetic-shadow)',
            }
          }
        }
      }
    </script>"""

html = re.sub(r'<script>\s*tailwind\.config = \{.*?\n\s*\}\s*</script>', tailwind_script, html, flags=re.DOTALL)

# 2. Update CSS Variables & Micro-transitions
css_block = """    <style>
      :root {
        --kinetic-bg: #0B0C10;
        --kinetic-surface: rgba(25, 27, 36, 0.6);
        --kinetic-surface-alt: #1F222E;
        --kinetic-border: rgba(255,255,255,0.08);
        --kinetic-text: #F5F5F7;
        --kinetic-muted: #8A8F9E;
        --kinetic-accent: #00F0FF;
        --kinetic-shadow: rgba(0, 0, 0, 0.5);
      }
      .dark {
        --kinetic-bg: #0B0C10;
        --kinetic-surface: rgba(25, 27, 36, 0.6);
        --kinetic-surface-alt: #1F222E;
        --kinetic-border: rgba(255,255,255,0.08);
        --kinetic-text: #F5F5F7;
        --kinetic-muted: #8A8F9E;
        --kinetic-accent: #00F0FF;
        --kinetic-shadow: rgba(0, 0, 0, 0.5);
      }
      
      body { 
        font-family: 'Hanken Grotesk', sans-serif; 
        background-color: var(--kinetic-bg);
        color: var(--kinetic-text);
        background-image: radial-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px);
        background-size: 24px 24px;
        transition: background-color 0.4s, color 0.4s;
        overflow-x: clip; /* Zero horizontal scroll */
        -webkit-font-smoothing: antialiased;
        min-height: 100dvh;
      }
      .dark body {
        background-image: radial-gradient(rgba(255,255,255,0.05) 1px, transparent 1px);
      }
      
      h1, h2, h3, h4, h5, h6, .font-display { font-family: 'Sora', sans-serif; }
      .font-mono { font-family: 'JetBrains Mono', monospace; }
      
      html { scroll-behavior: smooth; }
      
      .brutal-card, .brutal-btn, .pill-tag {
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
      }
      
      .brutal-card {
        background: var(--kinetic-surface);
        backdrop-filter: blur(16px);
        border: 1px solid var(--kinetic-border);
        border-radius: 1.5rem;
        box-shadow: 4px 4px 0px var(--kinetic-shadow);
      }
      .brutal-card:hover {
        transform: translate(-4px, -4px);
        box-shadow: 8px 8px 0px var(--kinetic-shadow);
      }
      
      .brutal-btn {
        background: var(--kinetic-text);
        color: #0B0C10; /* Ensure text is readable on white btn */
        border: 2px solid transparent;
        border-radius: 9999px;
        font-family: 'JetBrains Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-weight: 700;
        font-size: 0.875rem;
        padding: 0.75rem 1.5rem;
        min-height: 48px;
        min-width: 48px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
      }
      .brutal-btn:hover {
        transform: translateY(-4px);
        box-shadow: 0px 4px 0px var(--kinetic-shadow);
      }
      .brutal-btn-accent {
        background: var(--kinetic-accent);
        color: #0B0C10;
        border: 2px solid var(--kinetic-border);
      }
      
      .pill-tag {
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        background: var(--kinetic-surface-alt);
        color: var(--kinetic-text);
        border: 1px solid var(--kinetic-border);
      }
    </style>"""

html = re.sub(r'<style>.*?</style>', css_block, html, flags=re.DOTALL)

# 3. Apply fluid layout and typography replacements
# Containers
html = html.replace('max-w-7xl mx-auto px-6', 'max-w-[1440px] mx-auto px-[clamp(1.25rem,5vw,4rem)]')
html = html.replace('max-w-7xl mx-auto', 'max-w-[1440px] mx-auto')

# Spacing
html = re.sub(r'py-24 px-6', 'py-fluid-xl px-[clamp(1.25rem,5vw,4rem)]', html)
html = re.sub(r'py-12 px-6', 'py-fluid-lg px-[clamp(1.25rem,5vw,4rem)]', html)
html = re.sub(r'mb-16', 'mb-fluid-lg', html)
html = re.sub(r'mb-12', 'mb-fluid-md', html)
html = re.sub(r'mb-6', 'mb-fluid-sm', html)
html = re.sub(r'gap-6', 'gap-fluid-md', html)
html = re.sub(r'gap-8', 'gap-fluid-md', html)

# Typography
html = re.sub(r'text-4xl md:text-6xl font-bold', 'text-fluid-h1 font-bold', html)
html = re.sub(r'text-5xl md:text-7xl font-bold', 'text-fluid-h1 font-bold', html)
html = re.sub(r'text-6xl md:text-8xl font-bold', 'text-fluid-h1 font-bold', html)
html = re.sub(r'text-4xl font-display font-bold', 'text-fluid-h2 font-display font-bold', html)
html = re.sub(r'text-3xl font-display font-bold', 'text-fluid-h2 font-display font-bold', html)
html = re.sub(r'text-2xl font-display font-bold', 'text-fluid-h2 font-display font-bold', html)
html = re.sub(r'text-lg font-body', 'text-fluid-body font-body', html)
html = re.sub(r'text-lg leading-relaxed', 'text-fluid-body leading-relaxed', html)
html = re.sub(r'text-lg mb-12', 'text-fluid-body mb-fluid-md', html)

# Grid Layouts - make them auto-fit for tablets
html = re.sub(r'grid-cols-1 md:grid-cols-3', 'grid-cols-[repeat(auto-fit,minmax(280px,1fr))]', html)
html = re.sub(r'grid-cols-1 md:grid-cols-2 lg:grid-cols-3', 'grid-cols-[repeat(auto-fit,minmax(280px,1fr))]', html)
html = re.sub(r'grid-cols-2 md:grid-cols-4', 'grid-cols-[repeat(auto-fit,minmax(140px,1fr))] md:grid-cols-[repeat(auto-fit,minmax(240px,1fr))]', html)

# Mobile Bottom Bar adjustments (if any exist, update classes to match glassmorphism)
mobile_nav_search = r'<div class="md:hidden fixed bottom-0 left-0 w-full.*?</div>'
mobile_nav_replace = """<div class="md:hidden fixed bottom-0 left-0 w-full bg-kinetic-surface/80 backdrop-blur-xl border-t border-kinetic-border p-[clamp(0.5rem,2vw,1rem)] flex gap-3 z-40">
      <a href="#programs" class="brutal-btn flex-1 text-center bg-kinetic-surface text-kinetic-text border-kinetic-border text-xs">View Pricing</a>
      <button onclick="window.open('https://wa.me/916304895686', '_blank')" class="brutal-btn brutal-btn-accent flex-1 text-center text-xs">WhatsApp</button>
    </div>"""
html = re.sub(mobile_nav_search, mobile_nav_replace, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print("Refactored layout successfully.")
