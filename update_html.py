from bs4 import BeautifulSoup
import re

with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# 1. Update Header
header = soup.find('header')
if header:
    inner_div = header.find('div')
    if inner_div:
        # Update classes on inner div to match Pill shape
        classes = inner_div.get('class', [])
        # Remove rounded-2xl, border-2, h-20, px-4, sm:px-6
        for cls in ['rounded-2xl', 'border-2', 'h-20', 'px-4', 'sm:px-6']:
            if cls in classes:
                classes.remove(cls)
        # Add new classes
        classes.extend(['rounded-full', 'border', 'h-16', 'md:h-20', 'px-3', 'md:px-6'])
        inner_div['class'] = classes

        # Logo update
        logo_img = inner_div.find('img')
        if logo_img:
            logo_classes = logo_img.get('class', [])
            for cls in ['h-10', 'w-10', 'rounded-lg', 'border-2']:
                if cls in logo_classes:
                    logo_classes.remove(cls)
            logo_classes.extend(['h-8', 'w-8', 'md:h-10', 'md:w-10', 'rounded-full', 'md:rounded-lg', 'border', 'md:border-2'])
            logo_img['class'] = logo_classes
            
        ugh_text = inner_div.find('span', string=lambda t: t and 'UGH' in t)
        if ugh_text:
            classes = ugh_text.get('class', [])
            if 'hidden' in classes:
                classes.remove('hidden')
            if 'sm:block' in classes:
                classes.remove('sm:block')
            classes.extend(['hidden', 'md:block'])
            ugh_text['class'] = classes
            
        # WhatsApp button mobile optimization
        wa_btn = inner_div.find('button', string=lambda t: t and 'Chat on WhatsApp' in t)
        if wa_btn:
            # We want to replace it entirely with a circular one on mobile and keep text on desktop?
            # Or just replace it with a circular WhatsApp icon button to save horizontal space.
            wa_btn.clear()
            wa_btn['class'] = ['brutal-btn', 'brutal-btn-accent', 'rounded-full', 'p-2', 'md:px-4', 'md:py-2', 'flex', 'items-center', 'justify-center', 'transition-colors']
            # We will use an SVG or Material icon for WhatsApp. Since material icons don't have standard whatsapp, let's use an SVG or an icon.
            # I will use a simple "chat" icon for now and text for desktop
            wa_icon = soup.new_tag('span')
            wa_icon['class'] = 'material-symbols-outlined'
            wa_icon.string = 'chat'
            wa_text = soup.new_tag('span')
            wa_text['class'] = 'hidden md:block font-display font-bold uppercase tracking-widest text-xs ml-2'
            wa_text.string = 'WhatsApp'
            wa_btn.append(wa_icon)
            wa_btn.append(wa_text)
            
        # Mobile Menu Toggle (3-dot)
        nav = inner_div.find('nav')
        if nav:
            menu_btn = soup.new_tag('button')
            menu_btn['id'] = 'mobile-menu-btn'
            menu_btn['class'] = 'md:hidden material-symbols-outlined hover:text-kinetic-accent transition-colors ml-2'
            menu_btn.string = 'more_vert'
            # insert after wa_btn or right before it
            if wa_btn:
                wa_btn.insert_after(menu_btn)
            else:
                nav.insert_after(menu_btn)
                
            # Create Dropdown Menu
            dropdown = soup.new_tag('div')
            dropdown['id'] = 'mobile-dropdown'
            dropdown['class'] = 'hidden md:hidden absolute top-full right-4 mt-2 bg-kinetic-surface border border-kinetic-border rounded-xl shadow-lg p-4 flex flex-col gap-4 z-50'
            
            # Copy links from nav
            for a in nav.find_all('a'):
                new_a = soup.new_tag('a', href=a['href'])
                new_a['class'] = 'tab-link font-mono text-sm uppercase tracking-widest hover:text-kinetic-accent transition-colors'
                new_a['data-tab'] = a['data-tab']
                new_a.string = a.string
                dropdown.append(new_a)
                
            # Copy theme toggle
            theme_btn = nav.find('button', id='theme-toggle')
            if theme_btn:
                new_theme = soup.new_tag('button')
                new_theme['id'] = 'mobile-theme-toggle'
                new_theme['class'] = 'material-symbols-outlined hover:text-kinetic-accent transition-colors text-left'
                new_theme.string = theme_btn.string
                dropdown.append(new_theme)
                
            inner_div.append(dropdown)


# 2. Update Leadership Section
leadership = soup.find('section', id='leadership')
if leadership:
    title = leadership.find('h2')
    if title:
        title.string = "Skate Coaches"
        
    grid = leadership.find('div', class_=lambda c: c and 'grid-cols-1 md:grid-cols-2' in c)
    if grid:
        # Clear grid and repopulate with 4 coaches
        grid.clear()
        
        coaches = [
            {
                "name": "Coach Leela",
                "tag": "Founder / Experienced Skater",
                "desc": "Making action sports accessible at the doorstep."
            },
            {
                "name": "Tribhuvan Kokkula",
                "tag": "Vice-Chairman",
                "desc": "Vice-Chairman of the Skateboarding Sub-Committee (2026–2027 term)."
            },
            {
                "name": "Ronnie",
                "tag": "Park Manager",
                "desc": "Wallride Park Manager, pro skateboarder, and experienced coach."
            },
            {
                "name": "Pixie",
                "tag": "Pro Skater",
                "desc": "Pro skateboarder and founder of GirlsSk8Hyd, empowering women in action sports."
            }
        ]
        
        for coach in coaches:
            card = soup.new_tag('div')
            card['class'] = 'brutal-card p-4 md:p-6 flex flex-row gap-4 items-center md:items-start text-left'
            
            img_div = soup.new_tag('div')
            img_div['class'] = 'w-16 h-16 md:w-20 md:h-20 rounded-full overflow-hidden border-2 border-kinetic-border flex-shrink-0 bg-kinetic-muted'
            card.append(img_div)
            
            text_div = soup.new_tag('div')
            text_div['class'] = 'min-w-0 flex-1'
            
            header_div = soup.new_tag('div')
            header_div['class'] = 'flex flex-wrap items-center gap-2 mb-1'
            
            h3 = soup.new_tag('h3')
            h3['class'] = 'text-lg md:text-xl font-display font-bold uppercase truncate'
            h3.string = coach['name']
            header_div.append(h3)
            
            tag = soup.new_tag('span')
            tag['class'] = 'pill-tag bg-kinetic-surface-alt text-[10px] md:text-xs truncate max-w-full border-kinetic-border text-kinetic-text'
            tag.string = coach['tag']
            header_div.append(tag)
            
            text_div.append(header_div)
            
            desc = soup.new_tag('p')
            desc['class'] = 'text-kinetic-muted text-sm leading-snug font-body break-words line-clamp-3'
            desc.string = coach['desc']
            text_div.append(desc)
            
            card.append(text_div)
            grid.append(card)

# 3. Update Floating CTA
cta = soup.find('button', id='wizard-cta')
if cta:
    classes = cta.get('class', [])
    # Remove right-6, md:right-10, bottom-6, md:bottom-10, shadow-brutal-lg, animate-bounce
    for cls in ['right-6', 'md:right-10', 'bottom-6', 'md:bottom-10', 'shadow-brutal-lg', 'animate-bounce', 'brutal-btn', 'brutal-btn-accent']:
        if cls in classes:
            classes.remove(cls)
    
    classes.extend([
        'bottom-6', 'left-1/2', '-translate-x-1/2', 
        'bg-kinetic-accent', 'text-black', 'px-6', 'py-3', 
        'rounded-full', 'font-display', 'font-bold', 'uppercase', 'tracking-widest', 'text-sm',
        'shadow-lg', 'hover:scale-105', 'transition-transform'
    ])
    cta['class'] = classes

# Remove Mobile Sticky Footer if it exists
# Previously we had <div class="md:hidden fixed bottom-0 left-0 w-full ...
mobile_footer = soup.find('div', class_=lambda c: c and 'fixed bottom-0' in c and 'md:hidden' in c)
if mobile_footer:
    mobile_footer.decompose()

# Add script for mobile menu toggle
script = soup.new_tag('script')
script.string = """
document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileDropdown = document.getElementById('mobile-dropdown');
    
    if(mobileMenuBtn && mobileDropdown) {
        mobileMenuBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            mobileDropdown.classList.toggle('hidden');
        });
        
        // Close when clicking outside
        document.addEventListener('click', (e) => {
            if (!mobileDropdown.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                mobileDropdown.classList.add('hidden');
            }
        });
        
        // Close when a link is clicked
        const dropLinks = mobileDropdown.querySelectorAll('a, button');
        dropLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileDropdown.classList.add('hidden');
            });
        });
    }

    // Sync mobile theme toggle with main theme toggle logic
    const mobileThemeToggleBtn = document.getElementById('mobile-theme-toggle');
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (mobileThemeToggleBtn) {
        mobileThemeToggleBtn.addEventListener('click', function() {
            if (themeToggleBtn) themeToggleBtn.click();
            mobileThemeToggleBtn.textContent = document.documentElement.classList.contains('dark') ? 'light_mode' : 'dark_mode';
        });
    }
});
"""
soup.body.append(script)

with open('index.html', 'w') as f:
    f.write(str(soup))
