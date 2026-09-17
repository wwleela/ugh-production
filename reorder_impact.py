import re

with open('index.html', 'r') as f:
    content = f.read()

# Match the entire IMPACT TAB block
impact_match = re.search(r'(<!-- IMPACT TAB -->.*?)(<!-- EVENTS TAB -->)', content, re.DOTALL)
if impact_match:
    impact_html = impact_match.group(1)
    
    # Split the impact_html into the two sections
    # They are separated by </section> \n <section
    sections = re.split(r'</section>\s*<section', impact_html)
    
    if len(sections) == 2:
        # Reconstruct the string with sections swapped
        # sections[0] contains the opening of the first section
        # sections[1] contains the rest of the second section
        
        # We need to accurately grab just the sections
        # Let's use regex to grab the two sections explicitly
        section1_match = re.search(r'(<section class="pt-8 md:pt-16 pb-12.*?</section>)', impact_html, re.DOTALL)
        section2_match = re.search(r'(<section class="py-12 px-\[clamp.*?</section>)', impact_html, re.DOTALL)
        
        if section1_match and section2_match:
            sec1 = section1_match.group(1)
            sec2 = section2_match.group(1)
            
            # Now reconstruct the impact tab with sec2 first, then sec1
            new_impact_html = f"""<!-- IMPACT TAB -->
<div id="tab-impact" class="hidden main-tab-content">
  {sec2}
  {sec1}
</div>
"""
            content = content.replace(impact_html, new_impact_html)
            
            with open('index.html', 'w') as f:
                f.write(content)
            print("Successfully reordered sections.")
        else:
            print("Could not match individual sections.")
    else:
        print("Could not split sections.")
