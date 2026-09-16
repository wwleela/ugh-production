const fs = require('fs');
const cheerio = require('cheerio');

let html = fs.readFileSync('index.html', 'utf8');

// First, remove the custom CSS classes .brutal-card, .brutal-btn, .brutal-btn-accent
// I will just use regex to remove those lines from the style tag
html = html.replace(/\.brutal-card,\s*\.brutal-btn,\s*\.pill-tag\s*\{[^}]+\}/g, '');
html = html.replace(/\.brutal-card\s*\{[^}]+\}/g, '');
html = html.replace(/\.brutal-card:hover\s*\{[^}]+\}/g, '');
html = html.replace(/\.brutal-btn\s*\{[^}]+\}/g, '');
html = html.replace(/\.brutal-btn:hover\s*\{[^}]+\}/g, '');
html = html.replace(/\.brutal-btn-accent\s*\{[^}]+\}/g, '');

const $ = cheerio.load(html);

// Fix modal wrapper
$('.brutal-card').removeClass('brutal-card').addClass('border-4 border-kinetic-border shadow-[12px_12px_0px_var(--kinetic-shadow)]');

// Replace brutal-btn classes on step 1 buttons
$('.discipline-btn, .level-btn').removeClass('brutal-btn').addClass('font-bold uppercase tracking-wider p-4 border-2 shadow-[4px_4px_0px_var(--kinetic-shadow)] hover:-translate-y-1 hover:shadow-[6px_6px_0px_var(--kinetic-shadow)] transition-all');

// Fix step 3 Google login btn
$('#google-login-btn').removeClass('brutal-btn brutal-btn-accent').addClass('bg-kinetic-accent text-kinetic-bg border-2 border-kinetic-border px-8 py-4 font-bold uppercase tracking-widest shadow-[6px_6px_0px_var(--kinetic-shadow)] hover:bg-kinetic-text hover:text-kinetic-bg hover:-translate-y-1 hover:shadow-[8px_8px_0px_var(--kinetic-shadow)] transition-all');

// Fix step 4 WhatsApp btn
$('#whatsapp-sync-btn').removeClass('brutal-btn brutal-btn-accent').addClass('bg-kinetic-accent text-kinetic-bg border-2 border-kinetic-border px-8 py-4 font-bold uppercase tracking-widest shadow-[6px_6px_0px_var(--kinetic-shadow)] hover:bg-kinetic-text hover:text-kinetic-bg hover:-translate-y-1 hover:shadow-[8px_8px_0px_var(--kinetic-shadow)] transition-all');

// Write back changes from cheerio
html = $.html();

// Fix JavaScript selection toggle
// discBtns and levelBtns
html = html.replace(/b\.classList\.replace\('brutal-btn-accent', 'bg-kinetic-surface'\);/g, "b.classList.remove('bg-kinetic-accent', 'text-kinetic-bg', 'border-kinetic-shadow'); b.classList.add('bg-kinetic-surface', 'text-kinetic-text', 'border-kinetic-border');");

html = html.replace(/b\.classList\.remove\('brutal-btn-accent', 'text-black', 'border-black'\);/g, "b.classList.remove('bg-kinetic-accent', 'text-kinetic-bg', 'border-kinetic-shadow');");

html = html.replace(/e\.target\.classList\.add\('brutal-btn-accent', 'text-black', 'border-black'\);/g, "e.target.classList.add('bg-kinetic-accent', 'text-kinetic-bg', 'border-kinetic-shadow');");

// The Proceed to Checkout button generated via JS
html = html.replace(/class="brutal-btn brutal-btn-accent w-full mt-2"/g, 'class="bg-kinetic-accent text-kinetic-bg border-2 border-kinetic-border px-8 py-4 font-bold uppercase tracking-widest shadow-[6px_6px_0px_var(--kinetic-shadow)] hover:bg-kinetic-text hover:text-kinetic-bg hover:-translate-y-1 hover:shadow-[8px_8px_0px_var(--kinetic-shadow)] transition-all w-full mt-2"');

fs.writeFileSync('index.html', html);
