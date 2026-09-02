import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace desktop button text and icon
desktop_target = r'<span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1\.2rem;">bolt</span> Book'
desktop_replacement = r'<span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1.2rem;">search</span> Search'
html = re.sub(desktop_target, desktop_replacement, html)

# Replace mobile button text and icon
mobile_target = r'<span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1\.1rem;">bolt</span> Book'
mobile_replacement = r'<span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1.1rem;">search</span> Search'
html = re.sub(mobile_target, mobile_replacement, html)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
