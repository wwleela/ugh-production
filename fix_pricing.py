import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace titles
html = html.replace('"Monthly Academy"', '"Month-in Session"')
html = html.replace('"Apartment/Society — Standard"', '"Residential — Standard"')
html = html.replace('"Apartment/Society — Plus"', '"Residential — Plus"')

# Replace template
target_template_title = r'<h3 class="text-fluid-h2 font-display font-bold mb-2 uppercase">\${p.name}</h3>'
target_template_price = r'<span class="text-fluid-h2 font-display font-bold">₹\${p.price}</span>'

# Actually looking at the template again
# <h3 class="text-fluid-h2 font-display font-bold mb-2 uppercase">${p.name}</h3>
# <span class="text-fluid-h2 font-display font-bold">₹${p.price}</span>

new_template_title = r'<h3 class="text-2xl sm:text-3xl font-display font-bold mb-2 uppercase break-words">\${p.name}</h3>'
new_template_price = r'<span class="text-3xl sm:text-4xl font-display font-bold break-words">₹\${p.price}</span>'

html = re.sub(target_template_title, new_template_title, html)
html = re.sub(target_template_price, new_template_price, html)

with open('index.html', 'w') as f:
    f.write(html)
print("done")
