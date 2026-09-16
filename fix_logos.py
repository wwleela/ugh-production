import re

with open('index.html', 'r') as f:
    content = f.read()

old_decathlon = r'<img src="/logo.jpg.jpeg"[^>]+>'
new_decathlon = '<img src="https://cdn.worldvectorlogo.com/logos/decathlon-1.svg" alt="Decathlon Atrium Mall" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm group-hover:scale-105 transition-transform duration-300 opacity-90 group-hover:opacity-100" />'

old_wallride = r'<img src="/WhatsApp%20Image%202026-09-17%20at%2002.02.25.jpeg"[^>]+>'
new_wallride = '<img src="https://placehold.co/400x150/2a2622/ffffff?text=WALLRIDE+PARK&font=montserrat" alt="Wallride Park" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm group-hover:scale-105 transition-transform duration-300 rounded-lg opacity-90 group-hover:opacity-100" />'

content = re.sub(old_decathlon, new_decathlon, content)
content = re.sub(old_wallride, new_wallride, content)

with open('index.html', 'w') as f:
    f.write(content)
