import re

with open('index.html', 'r') as f:
    html = f.read()

# Add explicit width and height attributes to images
html = html.replace('<img src="2_social_media_square.png" alt="UGH Logo" class="h-10 w-10', '<img src="2_social_media_square.png" alt="UGH Logo" width="40" height="40" class="h-10 w-10')
html = html.replace('<img src="2_social_media_square.png" alt="UGH Logo" class="h-16 w-16', '<img src="2_social_media_square.png" alt="UGH Logo" width="64" height="64" class="h-16 w-16')
html = html.replace('<img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" class="w-5 h-5', '<img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" width="20" height="20" class="w-5 h-5')

with open('index.html', 'w') as f:
    f.write(html)
