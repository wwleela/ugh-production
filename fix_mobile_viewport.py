import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Header outer padding (responsive safe areas + top spacing)
html = re.sub(
    r'<header class="fixed top-4 w-full z-50 px-4 sm:px-\[clamp\(1\.25rem,5vw,4rem\)\] pointer-events-none">',
    r'<header class="fixed top-[max(0.5rem,env(safe-area-inset-top))] md:top-4 w-full z-50 px-[max(1rem,env(safe-area-inset-left))] sm:px-[clamp(1.25rem,5vw,4rem)] pointer-events-none transition-all duration-300">',
    html
)

# 2. Header inner div (adjust mobile height to fit tiny viewports elegantly)
html = re.sub(
    r'<div class="pointer-events-auto max-w-\[1440px\] mx-auto flex items-center justify-between bg-kinetic-surface/95 backdrop-blur-md border-kinetic-border shadow-\[4px_4px_0px_var\(--kinetic-shadow\)\] rounded-full border h-16 md:h-20 px-3 md:px-6">',
    r'<div class="pointer-events-auto w-full max-w-[1440px] mx-auto flex items-center justify-between bg-kinetic-surface/95 backdrop-blur-md border-kinetic-border shadow-[4px_4px_0px_var(--kinetic-shadow)] rounded-full border h-14 md:h-20 px-4 md:px-6">',
    html
)

# 3. Logo (ensure it never shrinks on very small screens)
html = re.sub(
    r'<a href="#home" class="tab-link flex items-center gap-3" data-tab="home">',
    r'<a href="#home" class="tab-link flex items-center gap-3 shrink-0" data-tab="home">',
    html
)

# 4. Main element top padding (dynamically scale with notch/status bar + header)
html = re.sub(
    r'<main class="pt-24 md:pt-28">',
    r'<main class="pt-[calc(4.5rem+env(safe-area-inset-top))] md:pt-[calc(7rem+env(safe-area-inset-top))]">',
    html
)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
