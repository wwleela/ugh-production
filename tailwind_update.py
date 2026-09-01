import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace fonts
font_links = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600&family=JetBrains+Mono:wght@500;700&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />"""

html = re.sub(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">.*?<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^>]+>', font_links, html, flags=re.DOTALL)

# Replace tailwind config
config = """      tailwind.config = {
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
      }"""

html = re.sub(r'tailwind\.config = \{.*?\n      \}', config, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
