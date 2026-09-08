import re

with open('index.html', 'r') as f:
    html = f.read()

# Make the Search text responsive (hidden on very small viewports so the header doesn't overflow)
html = html.replace(
    '<span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1.1rem;">search</span> Search',
    '<span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1.2rem;">search</span> <span class="hidden min-[360px]:inline">Search</span>'
)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
