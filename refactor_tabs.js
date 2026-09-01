const fs = require('fs');
const cheerio = require('cheerio');

const html = fs.readFileSync('index.html', 'utf8');
const $ = cheerio.load(html);

// Update Nav Links
const nav = $('nav');
if (nav.length) {
    nav.find('a').each((i, a) => {
        let href = $(a).attr('href').replace('#', '');
        if (href === 'community') href = 'impact';
        if (href === 'programs') href = 'pricing';
        $(a).attr('href', '#' + href);
        $(a).attr('data-tab', href);
        $(a).addClass('tab-link');
    });
}

// Logo link
const logo = $('a:contains("Urban Gliding")').first();
if (logo.length) {
    logo.attr('href', '#home');
    logo.attr('data-tab', 'home');
    logo.addClass('tab-link');
}

// Wrap sections into tabs
const main = $('main');
if (main.length) {
    const children = main.children().toArray();
    
    main.empty();
    
    main.append('<div id="tab-home" class="tab-content block"></div>');
    main.append('<div id="tab-impact" class="tab-content hidden"></div>');
    main.append('<div id="tab-events" class="tab-content hidden"></div>');
    main.append('<div id="tab-pricing" class="tab-content hidden"></div>');
    main.append('<div id="tab-venues" class="tab-content hidden"></div>');
    
    children.forEach(child => {
        const sec = $(child);
        if (sec[0].name === 'section') {
            const secId = sec.attr('id');
            if (['leadership', 'community', 'alliances'].includes(secId)) {
                $('#tab-impact').append(sec);
            } else if (secId === 'events') {
                $('#tab-events').append(sec);
            } else if (['programs', 'faq'].includes(secId)) {
                $('#tab-pricing').append(sec);
            } else if (['venues', 'safety'].includes(secId)) {
                $('#tab-venues').append(sec);
            } else {
                $('#tab-home').append(sec);
            }
        } else {
            $('#tab-home').append(sec);
        }
    });
}

// Update Hero text and buttons
const heroSection = $('#tab-home section').first();
if (heroSection.length) {
    const h1 = heroSection.find('h1');
    if (h1.length) {
        h1.empty();
        h1.append('<span class="text-kinetic-accent" style="text-shadow: 2px 2px 0px var(--kinetic-shadow), -2px -2px 0px var(--kinetic-shadow), 2px -2px 0px var(--kinetic-shadow), -2px 2px 0px var(--kinetic-shadow);">Master</span> the Concrete.<br><span class="italic text-kinetic-muted text-5xl md:text-7xl">Defy Gravity.</span>');
    }

    const p = heroSection.find('p').first();
    if (p.length) {
        p.text("Hyderabad's premier action sports coaching. From static balance to transition carving across Skateboarding, Inline, and BMX.");
        
        p.after(`
          <div class="flex flex-wrap justify-center gap-4 mb-10">
            <span class="pill-tag bg-kinetic-surface border-kinetic-border text-kinetic-text text-xs">RSFI-Credentialed Coaching</span>
            <span class="pill-tag bg-kinetic-surface border-kinetic-border text-kinetic-text text-xs">Doorstep & Park Sessions</span>
            <span class="pill-tag bg-kinetic-surface border-kinetic-border text-kinetic-text text-xs">9 Communities Trained</span>
          </div>
        `);
    }

    const btnDiv = heroSection.find('div.sm\\:flex-row');
    if (btnDiv.length) {
        btnDiv.empty();
        btnDiv.append(`
            <button onclick="document.getElementById('wizard-modal').classList.remove('hidden')" class="brutal-btn brutal-btn-accent">Book a Session</button>
            <a href="#pricing" class="tab-link brutal-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-tab="pricing">See Pricing</a>
            <a href="#venues" class="tab-link brutal-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-tab="venues">Find a Venue</a>
        `);
    }
}

// Update Mobile Bottom Bar
const mobileBar = $('div.md\\:hidden.fixed.bottom-0');
if (mobileBar.length) {
    mobileBar.empty();
    mobileBar.append(`
      <a href="#pricing" class="tab-link brutal-btn flex-1 text-center bg-kinetic-surface text-kinetic-text border-kinetic-border text-xs" data-tab="pricing">View Pricing</a>
      <button onclick="document.getElementById('wizard-modal').classList.remove('hidden')" class="brutal-btn brutal-btn-accent flex-1 text-center text-xs">Book Session</button>
    `);
}

// PRICING Tab Modifications
const pricingSec = $('#programs');
if (pricingSec.length) {
    // Remove "Compare All Plans" button
    pricingSec.find('button:contains("Compare")').remove();
    // Expand hidden rows
    pricingSec.find('.hidden').removeClass('hidden md:hidden');
}

// Add tab switching script
$('body').append(`
<script>
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
            // On mobile, maybe hide the mobile menu if there was one, but here we don't have one
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
</script>
`);

fs.writeFileSync('index.html', $.html());
console.log('Done!');
