import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. We already replaced <style> with link to CSS.
# Let's extract the JS logic at the bottom.
# Find all scripts at the end of the body.
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)

# Keep the tailwind config script and json-ld in the head
# But the ones that are actual logic (like DOMContentLoaded) we put in main.js
js_content = ""
for script in scripts:
    if "tailwind.config" in script or "@context" in script:
        continue # leave tailwind and json-ld alone
    js_content += script + "\n"

with open('public/js/main.js', 'w') as f:
    f.write(js_content)

# Now remove those specific scripts from HTML and add script tag
for script in scripts:
    if "tailwind.config" not in script and "@context" not in script:
        html = html.replace(f"<script>{script}</script>", "")

# Insert <script src="/public/js/main.js"></script> before </body>
html = html.replace('</body>', '    <script src="/public/js/main.js"></script>\n</body>')

with open('index.html', 'w') as f:
    f.write(html)
