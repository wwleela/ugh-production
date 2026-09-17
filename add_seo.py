with open('index.html', 'r') as f:
    html = f.read()

# Current meta description:
old_meta = '<meta name="description" content="Urban Gliding Hyderabad (UGH) - Hyderabad\'s premier doorstep skating coach. Professional skateboarding, inline skating, and BMX workshops, plus vibrant community events across residential complexes.">'

# We want to replace it with a comprehensive SEO block
new_meta = """<meta name="description" content="Urban Gliding Hyderabad (UGH) - Hyderabad's premier doorstep skating coach. Professional skateboarding, inline skating, and BMX workshops, plus vibrant community events across residential complexes.">
    <!-- OpenGraph Social Cards -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="UGH - Urban Gliding Hyderabad">
    <meta property="og:description" content="Hyderabad's premier doorstep skating coach. Professional skateboarding, inline skating, and BMX workshops.">
    <meta property="og:site_name" content="Urban Gliding Hyderabad">
    <meta property="og:url" content="https://ugh.co.in/">
    
    <!-- Twitter / X Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="UGH - Urban Gliding Hyderabad">
    <meta name="twitter:description" content="Hyderabad's premier doorstep skating coach. Professional skateboarding, inline skating, and BMX workshops.">
    
    <!-- Mobile & PWA tags -->
    <meta name="theme-color" content="#F2EBE1" media="(prefers-color-scheme: light)">
    <meta name="theme-color" content="#111A1A" media="(prefers-color-scheme: dark)">"""

html = html.replace(old_meta, new_meta)

with open('index.html', 'w') as f:
    f.write(html)
