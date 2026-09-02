import re

with open('index.html', 'r') as f:
    html = f.read()

html = html.replace(r'\${p.name}', r'${p.name}')
html = html.replace(r'\${p.price}', r'${p.price}')

with open('index.html', 'w') as f:
    f.write(html)
print("done")
