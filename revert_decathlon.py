import re

with open('index.html', 'r') as f:
    content = f.read()

old_decathlon = r'<img src="https://cdn.worldvectorlogo.com/logos/decathlon-1.svg"[^>]+>'
new_decathlon = '<img src="/logo.jpg.jpeg" alt="Decathlon Atrium Mall" class="h-24 md:h-32 w-auto object-contain shadow-lg group-hover:scale-105 transition-transform duration-300 rounded-xl" />'

content = re.sub(old_decathlon, new_decathlon, content)

with open('index.html', 'w') as f:
    f.write(content)
