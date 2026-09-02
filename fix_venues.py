import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace the text-fluid-h2 with responsive sizing in venues section specifically
target_section = r'<section id="venues".*?</section>'

def replacer(match):
    section_html = match.group(0)
    
    # 1. Update Decathlon Atrium to Emptyhead Skate Park
    section_html = section_html.replace('Decathlon Atrium', 'Emptyhead Skate Park')
    
    # 2. Update Wall Ride Park location
    section_html = section_html.replace('[VENUE ADDRESS — CONFIRM]', 'Hyderabad')
    
    # 3. Fix the spacing and text overflow in cards
    # Change padding from p-8 to p-6 sm:p-8
    section_html = section_html.replace('class="p-8 bg-kinetic-surface border border-kinetic-border"', 
                                        'class="p-6 sm:p-8 bg-kinetic-surface border border-kinetic-border h-full flex flex-col"')
    
    # Change text-fluid-h2 to text-2xl sm:text-3xl break-words
    section_html = section_html.replace('class="text-fluid-h2 font-display font-bold mb-1"', 
                                        'class="text-2xl sm:text-3xl font-display font-bold mb-1 break-words"')
    
    # For safety, let's also make the location pill/text break-words
    section_html = section_html.replace('class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display"',
                                        'class="text-kinetic-accent text-xs font-bold uppercase tracking-widest mb-4 font-display break-words"')

    return section_html

html = re.sub(target_section, replacer, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
