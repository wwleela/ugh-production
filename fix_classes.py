import re

with open('index.html', 'r') as f:
    html = f.read()

# Fix hero section
html = html.replace('py-32 px-6', 'py-fluid-xl px-[clamp(1.25rem,5vw,4rem)]')

# Remove redundant padding from brutal-btn
html = re.sub(r'brutal-btn (.*?) px-\d+ py-\d+', r'brutal-btn \1', html)
html = re.sub(r'brutal-btn(.*?) px-6 py-4', r'brutal-btn\1', html)
html = re.sub(r'brutal-btn(.*?) px-6 py-3', r'brutal-btn\1', html)
html = re.sub(r'brutal-btn flex-1 text-sm py-2', r'brutal-btn flex-1 text-sm', html) # fix wizard buttons

# The tabs could also use fluid padding or remain static
# The tabs are fine as is, but let's make sure images have aspect-ratio explicitly defined.
# I'll just leave images as they are mostly aspect-[ratio] classes in tailwind.

# For images missing explicit height/width but having aspect classes, Tailwind handles it. 
# But just in case, the prompt mentions "Explicit aspect-ratio definitions on all media containers".
# They are currently divs with aspect-video etc. 

# Re-read AI chat drawer requirement: 
# "AI Chat Drawer" - The current wizard-modal is a fixed centered modal. 
# For mobile, a drawer is better. Let's make it responsive: modal on desktop, drawer on mobile.
# A drawer implies it sticks to the bottom on mobile.

# Let's update the modal classes to act as a drawer on mobile
drawer_search = r'<div id="wizard-modal" class="fixed inset-0 z-\[100\] hidden bg-black/50 backdrop-blur-sm flex items-center justify-center p-4">'
drawer_replace = """<div id="wizard-modal" class="fixed inset-0 z-[100] hidden bg-black/50 backdrop-blur-sm flex items-end sm:items-center justify-center sm:p-4">"""

drawer_card_search = r'<div class="brutal-card bg-kinetic-surface w-full max-w-lg max-h-\[90vh\] flex flex-col relative overflow-hidden">'
drawer_card_replace = """<div class="brutal-card bg-kinetic-surface/80 w-full max-w-lg max-h-[90dvh] h-[90dvh] sm:h-auto sm:max-h-[85dvh] flex flex-col relative overflow-hidden sm:rounded-[1.5rem] rounded-t-[2rem] rounded-b-none sm:border border-b-0 border-kinetic-border">"""

html = html.replace(drawer_search, drawer_replace)
html = html.replace(drawer_card_search, drawer_card_replace)


with open('index.html', 'w') as f:
    f.write(html)

print("Applied fixes.")
