import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace Decathlon img with external fallback to ensure it renders if they can't upload to public
old_decathlon = r'<img src="/logo\.jpg\.jpeg"[^>]+>'
new_decathlon = '<img src="https://cdn.worldvectorlogo.com/logos/decathlon-1.svg" alt="Decathlon Atrium Mall" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm group-hover:scale-105 transition-transform duration-300 opacity-90 group-hover:opacity-100" />'

content = re.sub(old_decathlon, new_decathlon, content)

with open('index.html', 'w') as f:
    f.write(content)
