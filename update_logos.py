import re

with open('index.html', 'r') as f:
    content = f.read()

old_brands = r'<div class="flex flex-wrap justify-center items-center gap-8 md:gap-16">\s*<div class="font-bold text-2xl tracking-tight opacity-75">DECATHLON</div>\s*<div class="font-bold text-2xl tracking-tight opacity-75">WALLRIDE PARK</div>\s*</div>'

new_brands = """<div class="flex flex-wrap justify-center items-center gap-12 md:gap-24">
           <div class="group relative flex items-center justify-center">
             <!-- Decathlon Logo -->
             <img src="/logo.jpg.jpeg" alt="Decathlon Atrium Mall Logo" class="h-20 md:h-28 w-auto object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-300" onerror="this.src='https://placehold.co/400x150/0f4b9b/ffffff?text=DECATHLON+Atrium+Mall&font=montserrat'">
           </div>
           <div class="group relative flex items-center justify-center">
             <!-- Wallride Park Logo -->
             <img src="/WhatsApp%20Image%202026-09-17%20at%2002.02.25.jpeg" alt="Wallride Park Logo" class="h-20 md:h-28 w-auto object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-300 rounded-xl" onerror="this.src='https://placehold.co/300x200/2a2622/ffffff?text=WALLRIDE+PARK&font=montserrat'">
           </div>
        </div>"""

content = re.sub(old_brands, new_brands, content)

with open('index.html', 'w') as f:
    f.write(content)
