import re

with open('index.html', 'r') as f:
    content = f.read()

skate_icon = r'<div class="discipline-icon material-symbols-outlined text-4xl text-kinetic-muted group-hover:text-kinetic-accent group-hover:scale-110 group-hover:-rotate-12 transition-all duration-500 ease-\[cubic-bezier\(0.175,0.885,0.32,1.275\)\] relative z-10" style="font-variation-settings: \'FILL\' 1;">skateboarding</div>'
inline_icon = r'<div class="discipline-icon material-symbols-outlined text-4xl text-kinetic-muted group-hover:text-kinetic-accent group-hover:scale-110 group-hover:-rotate-12 transition-all duration-500 ease-\[cubic-bezier\(0.175,0.885,0.32,1.275\)\] relative z-10" style="font-variation-settings: \'FILL\' 1;">roller_skating</div>'
bmx_icon = r'<div class="discipline-icon material-symbols-outlined text-4xl text-kinetic-muted group-hover:text-kinetic-accent group-hover:scale-110 group-hover:-rotate-12 transition-all duration-500 ease-\[cubic-bezier\(0.175,0.885,0.32,1.275\)\] relative z-10" style="font-variation-settings: \'FILL\' 1;">pedal_bike</div>'

new_skate = '<img src="https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Skateboard/3D/skateboard_3d.png" alt="Skateboard" class="w-12 h-12 object-contain group-hover:scale-125 group-hover:-rotate-12 transition-all duration-500 ease-[cubic-bezier(0.175,0.885,0.32,1.275)] relative z-10 filter drop-shadow-md grayscale opacity-80 group-hover:opacity-100 group-hover:grayscale-0" />'
new_inline = '<img src="https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Roller%20skate/3D/roller_skate_3d.png" alt="Inline Skate" class="w-12 h-12 object-contain group-hover:scale-125 group-hover:-rotate-12 transition-all duration-500 ease-[cubic-bezier(0.175,0.885,0.32,1.275)] relative z-10 filter drop-shadow-md grayscale opacity-80 group-hover:opacity-100 group-hover:grayscale-0" />'
new_bmx = '<img src="https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Bicycle/3D/bicycle_3d.png" alt="BMX Bike" class="w-12 h-12 object-contain group-hover:scale-125 group-hover:-rotate-12 transition-all duration-500 ease-[cubic-bezier(0.175,0.885,0.32,1.275)] relative z-10 filter drop-shadow-md grayscale opacity-80 group-hover:opacity-100 group-hover:grayscale-0" />'

content = re.sub(skate_icon, new_skate, content)
content = re.sub(inline_icon, new_inline, content)
content = re.sub(bmx_icon, new_bmx, content)

with open('index.html', 'w') as f:
    f.write(content)
