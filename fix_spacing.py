import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update <main class="pt-32"> to <main class="pt-24 md:pt-28"> (96px to 112px top padding)
html = re.sub(r'<main class="pt-32">', r'<main class="pt-28 md:pt-32">', html)

# 2. Update the Home tab hero padding
# from: class="relative py-[clamp(4rem,10vw,8rem)] px-[clamp(1.25rem,5vw,4rem)] text-center border-b border-kinetic-border overflow-hidden"
# to: class="relative pt-10 md:pt-16 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)] text-center border-b border-kinetic-border overflow-hidden"
html = re.sub(
    r'<section class="relative py-\[clamp\(4rem,10vw,8rem\)\] px-\[clamp\(1\.25rem,5vw,4rem\)\]',
    r'<section class="relative pt-8 md:pt-16 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)]',
    html
)

# 3. Update Impact tab first section (leadership)
html = re.sub(
    r'<section id="leadership" class="py-fluid-xl px-\[clamp\(1\.25rem,5vw,4rem\)\]',
    r'<section id="leadership" class="pt-12 md:pt-20 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)]',
    html
)

# 4. Update Events tab first section (events)
html = re.sub(
    r'<section id="events" class="py-fluid-xl px-\[clamp\(1\.25rem,5vw,4rem\)\] border-b border-kinetic-border bg-kinetic-surface-alt">',
    r'<section id="events" class="pt-12 md:pt-20 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)] border-b border-kinetic-border bg-kinetic-surface-alt">',
    html
)

# 5. Update Pricing tab first section (programs)
html = re.sub(
    r'<section id="programs" class="py-fluid-xl px-\[clamp\(1\.25rem,5vw,4rem\)\] bg-kinetic-surface text-kinetic-text">',
    r'<section id="programs" class="pt-12 md:pt-20 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)] bg-kinetic-surface text-kinetic-text">',
    html
)

# 6. Update Venues tab first section (safety)
html = re.sub(
    r'<section id="safety" class="py-fluid-xl px-\[clamp\(1\.25rem,5vw,4rem\)\] text-center border-b border-kinetic-border">',
    r'<section id="safety" class="pt-12 md:pt-20 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)] text-center border-b border-kinetic-border">',
    html
)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
