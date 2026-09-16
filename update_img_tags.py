import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace Decathlon img
old_decathlon = r'<img src="/logo\.jpg\.jpeg"[^>]+>'
new_decathlon = '<img src="/logo.jpg.jpeg" alt="Decathlon Atrium Mall" class="h-24 md:h-32 w-auto object-contain shadow-lg group-hover:scale-105 transition-transform duration-300 rounded-xl" />'

# Replace Wallride img
old_wallride = r'<img src="/WhatsApp[^>]+>'
new_wallride = '<img src="/WhatsApp%20Image%202026-09-17%20at%2002.02.25.jpeg" alt="Wallride Park" class="h-24 md:h-32 w-auto object-contain shadow-lg group-hover:scale-105 transition-transform duration-300 rounded-xl" />'

content = re.sub(old_decathlon, new_decathlon, content)
content = re.sub(old_wallride, new_wallride, content)

with open('index.html', 'w') as f:
    f.write(content)
