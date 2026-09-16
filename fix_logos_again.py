import re

with open('index.html', 'r') as f:
    content = f.read()

old_decathlon = r'<img src="https://cdn.worldvectorlogo.com/logos/decathlon-1.svg"[^>]+>'
new_decathlon = '<img src="/logo.jpg.jpeg" alt="Decathlon Atrium Mall" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm group-hover:scale-105 transition-transform duration-300 opacity-90 group-hover:opacity-100" onerror="this.src=\'https://cdn.worldvectorlogo.com/logos/decathlon-1.svg\'" />'

old_wallride = r'<img src="https://placehold.co/400x150/2a2622/ffffff\?text=WALLRIDE\+PARK&font=montserrat"[^>]+>'
new_wallride = '<img src="/WhatsApp%20Image%202026-09-17%20at%2002.02.25.jpeg" alt="Wallride Park" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm group-hover:scale-105 transition-transform duration-300 rounded-lg opacity-90 group-hover:opacity-100" onerror="this.src=\'https://placehold.co/400x150/2a2622/ffffff?text=WALLRIDE+PARK&font=montserrat\'" />'

content = re.sub(old_decathlon, new_decathlon, content)
content = re.sub(old_wallride, new_wallride, content)

with open('index.html', 'w') as f:
    f.write(content)
