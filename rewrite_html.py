from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Update Nav Links
nav = soup.find('nav')
if nav:
    for a in nav.find_all('a'):
        href = a['href'].replace('#', '')
        if href == 'community': href = 'impact'
        if href == 'programs': href = 'pricing'
        a['href'] = f'#{href}'
        a['data-tab'] = href
        a['class'] = a.get('class', []) + ['tab-link']

# Logo link
logo = soup.find('a', string=lambda s: s and 'Urban Gliding' in s)
if not logo: # try finding by content
    for a in soup.find_all('a'):
        if 'Urban Gliding' in a.get_text():
            logo = a
            break
if logo:
    logo['href'] = '#home'
    logo['data-tab'] = 'home'
    logo['class'] = logo.get('class', []) + ['tab-link']

# Wrap sections into tabs
main = soup.find('main')
if main:
    # Get all direct children of main
    children = list(main.children)
    
    # We will create tab wrappers
    tabs = {
        'home': soup.new_tag('div', id='tab-home', attrs={'class': 'tab-content block'}),
        'impact': soup.new_tag('div', id='tab-impact', attrs={'class': 'tab-content hidden'}),
        'events': soup.new_tag('div', id='tab-events', attrs={'class': 'tab-content hidden'}),
        'pricing': soup.new_tag('div', id='tab-pricing', attrs={'class': 'tab-content hidden'}),
        'venues': soup.new_tag('div', id='tab-venues', attrs={'class': 'tab-content hidden'})
    }
    
    # Append tabs to main
    main.clear()
    for tab_id, tab_el in tabs.items():
        main.append(tab_el)
    
    current_tab = 'home'
    for child in children:
        if child.name == 'section':
            sec_id = child.get('id')
            if sec_id in ['leadership', 'community', 'alliances']:
                tabs['impact'].append(child)
            elif sec_id in ['events']:
                tabs['events'].append(child)
            elif sec_id in ['programs', 'faq']: # Let's put pricing and faq in pricing
                tabs['pricing'].append(child)
            elif sec_id in ['venues', 'safety']:
                tabs['venues'].append(child)
            else:
                tabs['home'].append(child)
        else:
            tabs['home'].append(child)

# Now apply other updates (hero text, buttons)
hero_section = tabs['home'].find('section') # first section is hero
if hero_section:
    h1 = hero_section.find('h1')
    if h1:
        h1.clear()
        span1 = soup.new_tag('span', attrs={'class': 'text-kinetic-accent', 'style': 'text-shadow: 2px 2px 0px var(--kinetic-shadow), -2px -2px 0px var(--kinetic-shadow), 2px -2px 0px var(--kinetic-shadow), -2px 2px 0px var(--kinetic-shadow);'})
        span1.string = "Master"
        h1.append(span1)
        h1.append(" the Concrete.")
        br = soup.new_tag('br')
        h1.append(br)
        span2 = soup.new_tag('span', attrs={'class': 'italic text-kinetic-muted text-5xl md:text-7xl'})
        span2.string = "Defy Gravity."
        h1.append(span2)

    p = hero_section.find('p')
    if p:
        p.string = "Hyderabad's premier action sports coaching. From static balance to transition carving across Skateboarding, Inline, and BMX."

    # Add trust badges
    p_parent = p.parent
    if p_parent:
        badges_div = soup.new_tag('div', attrs={'class': 'flex flex-wrap justify-center gap-4 mb-10'})
        for text in ['RSFI-Credentialed Coaching', 'Doorstep & Park Sessions', '9 Communities Trained']:
            span = soup.new_tag('span', attrs={'class': 'pill-tag bg-kinetic-surface border-kinetic-border text-kinetic-text text-xs'})
            span.string = text
            badges_div.append(span)
        p.insert_after(badges_div)

    # Hero buttons
    btn_div = hero_section.find('div', attrs={'class': lambda c: c and 'sm:flex-row' in c})
    if btn_div:
        btn_div.clear()
        
        btn1 = soup.new_tag('button', attrs={'onclick': "document.getElementById('wizard-modal').classList.remove('hidden')", 'class': 'brutal-btn brutal-btn-accent'})
        btn1.string = 'Book a Session'
        btn_div.append(btn1)
        
        btn2 = soup.new_tag('a', href='#pricing', attrs={'class': 'tab-link brutal-btn bg-kinetic-surface text-kinetic-text border-kinetic-border', 'data-tab': 'pricing'})
        btn2.string = 'See Pricing'
        btn_div.append(btn2)
        
        btn3 = soup.new_tag('a', href='#venues', attrs={'class': 'tab-link brutal-btn bg-kinetic-surface text-kinetic-text border-kinetic-border', 'data-tab': 'venues'})
        btn3.string = 'Find a Venue'
        btn_div.append(btn3)

# Update Mobile Bottom Bar
mobile_bar = soup.find('div', attrs={'class': lambda c: c and 'fixed bottom-0' in c})
if mobile_bar:
    mobile_bar.clear()
    a = soup.new_tag('a', href='#pricing', attrs={'class': 'tab-link brutal-btn flex-1 text-center bg-kinetic-surface text-kinetic-text border-kinetic-border text-xs', 'data-tab': 'pricing'})
    a.string = 'View Pricing'
    btn = soup.new_tag('button', attrs={'onclick': "document.getElementById('wizard-modal').classList.remove('hidden')", 'class': 'brutal-btn brutal-btn-accent flex-1 text-center text-xs'})
    btn.string = 'Book Session'
    mobile_bar.append(a)
    mobile_bar.append(btn)

# Ensure Pricing items are expanded (remove any details/summary if they exist, or just make them fully visible)
# Let's check how pricing is implemented currently
pricing_sec = tabs['pricing'].find('section', id='programs')
if pricing_sec:
    # Actually, the prompt says: "PRICING tab: all 5 plans visible immediately ... no "Compare All Plans" button needed here."
    # Let's look for a button and remove it, and any hidden rows.
    compare_btn = pricing_sec.find('button', string=lambda s: s and 'Compare' in s)
    if compare_btn:
        compare_btn.extract()
    # If there's a hidden div for additional plans, unhide it
    hidden_plans = pricing_sec.find_all(attrs={'class': lambda c: c and 'hidden' in c})
    for hp in hidden_plans:
        # Check if it's a grid item or something
        classes = hp['class']
        classes.remove('hidden')
        if 'md:hidden' in classes:
            classes.remove('md:hidden')
        hp['class'] = classes

# Add tab script logic at the end of body
script = soup.new_tag('script')
script.string = """
document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.tab-content');
    const tabLinks = document.querySelectorAll('.tab-link');

    function switchTab(tabId) {
        tabs.forEach(tab => {
            if(tab.id === 'tab-' + tabId) {
                tab.classList.remove('hidden');
                tab.classList.add('block');
            } else {
                tab.classList.remove('block');
                tab.classList.add('hidden');
            }
        });
        
        tabLinks.forEach(link => {
            if(link.dataset.tab === tabId) {
                link.classList.add('text-kinetic-accent');
            } else {
                link.classList.remove('text-kinetic-accent');
            }
        });
        window.scrollTo(0, 0);
    }

    tabLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const tabId = link.dataset.tab;
            history.pushState(null, null, '#' + tabId);
            switchTab(tabId);
        });
    });

    // Handle initial load
    const hash = window.location.hash.replace('#', '');
    if (hash && ['home', 'impact', 'events', 'pricing', 'venues'].includes(hash)) {
        switchTab(hash);
    } else {
        switchTab('home');
    }
    
    // Handle back button
    window.addEventListener('popstate', () => {
        const hash = window.location.hash.replace('#', '');
        if (hash && ['home', 'impact', 'events', 'pricing', 'venues'].includes(hash)) {
            switchTab(hash);
        } else {
            switchTab('home');
        }
    });
});
"""
soup.body.append(script)

# Save changes
with open('index.html', 'w') as f:
    f.write(str(soup))
