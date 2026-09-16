const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

html = html.replace(/b\.classList\.replace\('brutal-btn-accent',\s*'bg-kinetic-surface'\);/g, "b.classList.remove('bg-kinetic-accent', 'text-kinetic-bg', 'border-kinetic-shadow'); b.classList.add('bg-kinetic-surface', 'text-kinetic-text', 'border-kinetic-border');");

fs.writeFileSync('index.html', html);
