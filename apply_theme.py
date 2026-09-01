import re

with open('index.html', 'r') as f:
    html = f.read()

# Tailwind config: add new dark colors
config_search = r"colors: \{"
config_replace = r"""colors: {
              'dark-bg': '#0D0D0D',
              'dark-surface': '#1A1A1A',
              'dark-border': '#333333',
              'dark-text': '#F5F5F5',
              'dark-muted': '#A3A3A3',"""
html = re.sub(config_search, config_replace, html, count=1)

# Body
html = html.replace('bg-off-white text-charcoal', 'bg-dark-bg text-dark-text')

# Header
html = html.replace('bg-white/95', 'bg-dark-bg/95')
html = html.replace('border-border-gray', 'border-dark-border')

# Backgrounds
html = html.replace('bg-white', 'bg-dark-surface')
html = html.replace('bg-light-sand', 'bg-[#141414]')
html = html.replace('bg-gray-100', 'bg-[#2A2A2A]')
html = html.replace('bg-gray-200', 'bg-[#2A2A2A]')

# Borders
html = html.replace('border-gray-300', 'border-dark-border')
html = html.replace('border-gray-200', 'border-dark-border')

# Text
html = html.replace('text-charcoal', 'text-dark-text')
html = html.replace('text-gray-600', 'text-dark-muted')
html = html.replace('text-gray-500', 'text-[#777]')
html = html.replace('text-gray-400', 'text-dark-muted')

# Specific component fixes
# Event cards
html = html.replace('bg-charcoal text-white', 'bg-dark-surface text-dark-text')
html = html.replace('border-charcoal', 'border-[#444]')
html = html.replace('shadow-[8px_8px_0px_#1A1A1A]', 'shadow-[8px_8px_0px_#000]')
html = html.replace('hover:shadow-[12px_12px_0px_#1A1A1A]', 'hover:shadow-[12px_12px_0px_#000]')

# Footer and Pricing sections (were originally dark)
# Revert them to be visually distinct if needed, or keep them dark
html = html.replace('bg-charcoal', 'bg-[#111]')
html = html.replace('bg-[#2A2A2A] text-white border border-gray-700', 'bg-[#222] text-dark-text border border-[#444]')
html = html.replace('bg-gray-600', 'bg-[#444]')

# Event button
html = html.replace("class=\"w-full py-4 bg-[#111] text-dark-text", "class=\"w-full py-4 bg-ugh-teal text-white")

with open('index.html', 'w') as f:
    f.write(html)
