import re

with open('index.html', 'r') as f:
    html = f.read()

css_search = r':root \{.*?\.\w+ \{.*?\}' # Won't match perfectly, let's use a better regex

# Let's replace the block from :root to .dark body {
css_search = r':root \{.*?\.dark body \{.*?\}'

css_replace = """:root {
        --kinetic-bg: #F2EBE1;
        --kinetic-surface: rgba(255, 255, 255, 0.6);
        --kinetic-surface-alt: #E5DAC7;
        --kinetic-border: rgba(42, 103, 102, 0.2); /* Teal with opacity */
        --kinetic-text: #193D3C;
        --kinetic-muted: #4A7A79;
        --kinetic-accent: #D85B2D;
        --kinetic-shadow: #2A6766;
      }
      .dark {
        --kinetic-bg: #111A1A;
        --kinetic-surface: rgba(42, 103, 102, 0.1);
        --kinetic-surface-alt: rgba(42, 103, 102, 0.2);
        --kinetic-border: rgba(42, 103, 102, 0.4);
        --kinetic-text: #F2EBE1;
        --kinetic-muted: #84A3A2;
        --kinetic-accent: #D85B2D;
        --kinetic-shadow: #080D0D;
      }
      
      body { 
        font-family: 'Hanken Grotesk', sans-serif; 
        background-color: var(--kinetic-bg);
        color: var(--kinetic-text);
        background-image: radial-gradient(var(--kinetic-border) 1px, transparent 1px);
        background-size: 24px 24px;
        transition: background-color 0.4s, color 0.4s;
        overflow-x: clip; /* Zero horizontal scroll */
        -webkit-font-smoothing: antialiased;
        min-height: 100dvh;
      }
      .dark body {
        background-image: radial-gradient(rgba(242,235,225,0.05) 1px, transparent 1px);
      }"""

html = re.sub(css_search, css_replace, html, flags=re.DOTALL)

# Also fix the brutal-btn colors
html = html.replace("color: #0B0C10; /* Ensure text is readable on white btn */", "color: var(--kinetic-bg); /* Contrast text */")
html = html.replace("color: #0B0C10;\n        border: 2px solid var(--kinetic-border);", "color: #FFFFFF;\n        border: 2px solid var(--kinetic-border);")

with open('index.html', 'w') as f:
    f.write(html)
