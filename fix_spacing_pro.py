import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Main container clearance (tighten to precisely clear the 80px/96px header)
html = re.sub(r'<main class="pt-28 md:pt-32">', r'<main class="pt-24 md:pt-28">', html)

# 2. Home Tab (Tighten hero)
html = re.sub(
    r'<section class="relative pt-8 md:pt-16 pb-fluid-xl px-\[clamp\(1\.25rem,5vw,4rem\)\]',
    r'<section class="relative pt-4 md:pt-8 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)]',
    html
)

# 3. Impact Tab
html = re.sub(
    r'<section id="leadership" class="pt-12 md:pt-20 pb-fluid-xl px-\[clamp\(1\.25rem,5vw,4rem\)\]',
    r'<section id="leadership" class="pt-6 md:pt-10 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)]',
    html
)

# 4. Events Tab
html = re.sub(
    r'<section id="events" class="pt-12 md:pt-20 pb-fluid-xl px-\[clamp\(1\.25rem,5vw,4rem\)\]',
    r'<section id="events" class="pt-6 md:pt-10 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)]',
    html
)

# 5. Pricing Tab
html = re.sub(
    r'<section id="programs" class="pt-12 md:pt-20 pb-fluid-xl px-\[clamp\(1\.25rem,5vw,4rem\)\]',
    r'<section id="programs" class="pt-6 md:pt-10 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)]',
    html
)

# 6. Venues Tab
html = re.sub(
    r'<section id="safety" class="pt-12 md:pt-20 pb-fluid-xl px-\[clamp\(1\.25rem,5vw,4rem\)\]',
    r'<section id="safety" class="pt-6 md:pt-10 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)]',
    html
)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
