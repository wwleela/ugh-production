import urllib.request
import json
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_svg_repo(query):
    url = f"https://www.svgrepo.com/vectors/{query}/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        # find the first href that looks like /show/12345/skateboard.svg
        matches = re.findall(r'href="/show/(\d+/[^"]+)"', html)
        if matches:
            svg_url = f"https://www.svgrepo.com/show/{matches[0]}"
            print(f"Found for {query}: {svg_url}")
            svg_req = urllib.request.Request(svg_url, headers={'User-Agent': 'Mozilla/5.0'})
            svg_data = urllib.request.urlopen(svg_req, context=ctx).read().decode('utf-8')
            return svg_data
        else:
            print(f"No match for {query}")
    except Exception as e:
        print(f"Error fetching {query}: {e}")
    return None

skate = fetch_svg_repo('skateboard')
inline = fetch_svg_repo('inline-skate')
bmx = fetch_svg_repo('bmx')

with open('svgs.txt', 'w') as f:
    f.write(f"SKATEBOARD:\n{skate}\n\nINLINE:\n{inline}\n\nBMX:\n{bmx}")
