const fs = require('fs');
const cheerio = require('cheerio');

const html = fs.readFileSync('index.html', 'utf8');
const $ = cheerio.load(html);

// Change main tab content class to main-tab-content
$('#tab-home, #tab-impact, #tab-events, #tab-pricing, #tab-venues').each((i, el) => {
    $(el).removeClass('tab-content');
    $(el).addClass('main-tab-content');
});

// Update the script
let htmlStr = $.html();
htmlStr = htmlStr.replace("const tabs = document.querySelectorAll('.tab-content');", "const tabs = document.querySelectorAll('.main-tab-content');");
htmlStr = htmlStr.replace("const tabLinks = document.querySelectorAll('.tab-link');", "const tabLinks = document.querySelectorAll('a.tab-link'); // limit to a tags or specific ones? Actually there are buttons too, wait.");

// Wait, the mobile bottom bar has a button: 
// <a href="#pricing" class="tab-link ...">
// It is fine to use .tab-link for all main tab links.
// Let's make sure the inner alliances tabs are not using .tab-link.
// Let's check alliances inner tabs.

fs.writeFileSync('index.html', htmlStr);
console.log('Fixed tab content classes.');
