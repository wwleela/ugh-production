import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace Decathlon img src
old_decathlon = r'<img src="/logo\.jpg\.jpeg"([^>]+)>'
new_decathlon = r'<img src="/src/assets/images/regenerated_image_1789593354658.jpg"\1>'

# Replace Wallride img src
old_wallride = r'<img src="/WhatsApp%20Image%202026-09-17%20at%2002\.02\.25\.jpeg"([^>]+)>'
new_wallride = r'<img src="/src/assets/images/regenerated_image_1789593359927.jpg"\1>'

content = re.sub(old_decathlon, new_decathlon, content)
content = re.sub(old_wallride, new_wallride, content)

with open('index.html', 'w') as f:
    f.write(content)
