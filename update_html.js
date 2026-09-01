const fs = require('fs');
const cheerio = require('cheerio');

const html = fs.readFileSync('index.html', 'utf8');
const $ = cheerio.load(html);

// 1. Update Header
const header = $('header');
if (header.length) {
    const innerDiv = header.find('div').first();
    if (innerDiv.length) {
        innerDiv.removeClass('rounded-2xl border-2 h-20 px-4 sm:px-6');
        innerDiv.addClass('rounded-full border h-16 md:h-20 px-3 md:px-6');

        const logoImg = innerDiv.find('img').first();
        if (logoImg.length) {
            logoImg.removeClass('h-10 w-10 rounded-lg border-2');
            logoImg.addClass('h-8 w-8 md:h-10 md:w-10 rounded-full md:rounded-lg border md:border-2');
        }

        const waBtn = innerDiv.find('button:contains("Chat on WhatsApp")').first();
        if (waBtn.length) {
            waBtn.empty();
            waBtn.removeClass('rounded font-display font-bold uppercase tracking-widest text-xs gap-2');
            waBtn.addClass('rounded-full p-2 md:px-4 md:py-2 flex items-center justify-center transition-colors');
            
            waBtn.append('<span class="material-symbols-outlined">chat</span>');
            waBtn.append('<span class="hidden md:block font-display font-bold uppercase tracking-widest text-xs ml-2">WhatsApp</span>');
        }

        // Mobile Menu Toggle
        const nav = innerDiv.find('nav').first();
        if (nav.length) {
            const menuBtn = $('<button id="mobile-menu-btn" class="md:hidden material-symbols-outlined hover:text-kinetic-accent transition-colors ml-2">more_vert</button>');
            if (waBtn.length) {
                waBtn.after(menuBtn);
            } else {
                nav.after(menuBtn);
            }

            const dropdown = $('<div id="mobile-dropdown" class="hidden md:hidden absolute top-[calc(100%+8px)] right-4 bg-kinetic-surface border border-kinetic-border rounded-xl shadow-lg p-4 flex flex-col gap-4 z-50 min-w-[150px]"></div>');
            
            nav.find('a').each((i, a) => {
                const link = $(a).clone();
                link.addClass('font-mono text-sm uppercase tracking-widest hover:text-kinetic-accent transition-colors block text-right');
                dropdown.append(link);
            });

            const themeBtn = nav.find('#theme-toggle');
            if (themeBtn.length) {
                const newThemeBtn = themeBtn.clone();
                newThemeBtn.attr('id', 'mobile-theme-toggle');
                newThemeBtn.addClass('text-right');
                dropdown.append(newThemeBtn);
            }
            innerDiv.append(dropdown);
        }
    }
}

// 2. Update Leadership Section
const leadership = $('#leadership');
if (leadership.length) {
    const title = leadership.find('h2').first();
    if (title.length) {
        title.text('Skate Coaches');
    }

    const grid = leadership.find('.grid').first();
    if (grid.length) {
        grid.empty();
        
        const coaches = [
            {
                name: "Coach Leela",
                tag: "Founder / Experienced Skater",
                desc: "Making action sports accessible at the doorstep."
            },
            {
                name: "Tribhuvan Kokkula",
                tag: "Vice-Chairman",
                desc: "Vice-Chairman of the Skateboarding Sub-Committee (2026–2027 term)."
            },
            {
                name: "Ronnie",
                tag: "Park Manager",
                desc: "Wallride Park Manager, pro skateboarder, and experienced coach."
            },
            {
                name: "Pixie",
                tag: "Pro Skater",
                desc: "Pro skateboarder and founder of GirlsSk8Hyd, empowering women in action sports."
            }
        ];

        coaches.forEach(coach => {
            const card = '<div class="brutal-card p-4 md:p-6 flex flex-row gap-4 items-center md:items-start text-left">' +
              '<div class="w-16 h-16 md:w-20 md:h-20 rounded-full overflow-hidden border-2 border-kinetic-border flex-shrink-0 bg-kinetic-muted"></div>' +
              '<div class="min-w-0 flex-1">' +
                '<div class="flex flex-col md:flex-row md:items-center gap-1 md:gap-2 mb-1">' +
                  '<h3 class="text-lg md:text-xl font-display font-bold uppercase truncate">' + coach.name + '</h3>' +
                  '<span class="pill-tag bg-kinetic-surface-alt text-[10px] md:text-xs truncate max-w-full border-kinetic-border text-kinetic-text px-2 py-1">' + coach.tag + '</span>' +
                '</div>' +
                '<p class="text-kinetic-muted text-sm leading-snug font-body break-words line-clamp-3 mt-1">' + coach.desc + '</p>' +
              '</div>' +
            '</div>';
            grid.append(card);
        });
    }
}

// 3. Update Floating CTA
const cta = $('#wizard-cta');
if (cta.length) {
    cta.removeClass('right-6 md:right-10 bottom-6 md:bottom-10 shadow-brutal-lg animate-bounce brutal-btn brutal-btn-accent');
    cta.addClass('bottom-6 left-1/2 -translate-x-1/2 bg-kinetic-accent text-black px-6 py-3 rounded-full font-display font-bold uppercase tracking-widest text-sm shadow-lg hover:scale-105 transition-transform');
}

// Remove Mobile Sticky Footer (use a safer selector)
const divs = $('div');
divs.each((i, div) => {
    const classList = $(div).attr('class');
    if (classList && classList.includes('md:hidden') && classList.includes('fixed') && classList.includes('bottom-0')) {
        $(div).remove();
    }
});


// Add script
$('body').append('<script>' +
"document.addEventListener('DOMContentLoaded', () => {" +
"    const mobileMenuBtn = document.getElementById('mobile-menu-btn');" +
"    const mobileDropdown = document.getElementById('mobile-dropdown');" +
"    if(mobileMenuBtn && mobileDropdown) {" +
"        mobileMenuBtn.addEventListener('click', (e) => {" +
"            e.stopPropagation();" +
"            mobileDropdown.classList.toggle('hidden');" +
"        });" +
"        document.addEventListener('click', (e) => {" +
"            if (!mobileDropdown.contains(e.target) && !mobileMenuBtn.contains(e.target)) {" +
"                mobileDropdown.classList.add('hidden');" +
"            }" +
"        });" +
"        const dropLinks = mobileDropdown.querySelectorAll('a, button');" +
"        dropLinks.forEach(link => {" +
"            link.addEventListener('click', () => {" +
"                mobileDropdown.classList.add('hidden');" +
"            });" +
"        });" +
"    }" +
"    const mobileThemeToggleBtn = document.getElementById('mobile-theme-toggle');" +
"    const themeToggleBtn = document.getElementById('theme-toggle');" +
"    if (mobileThemeToggleBtn) {" +
"        mobileThemeToggleBtn.addEventListener('click', function() {" +
"            if (themeToggleBtn) themeToggleBtn.click();" +
"            mobileThemeToggleBtn.textContent = document.documentElement.classList.contains('dark') ? 'light_mode' : 'dark_mode';" +
"        });" +
"    }" +
"});" +
'</script>');

fs.writeFileSync('index.html', $.html());
console.log('Update complete.');
