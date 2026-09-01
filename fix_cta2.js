const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

const targetStr = `<button id="wizard-cta" class="fixed z-50 flex items-center gap-2 bottom-6 left-1/2 -translate-x-1/2 bg-kinetic-surface/90 backdrop-blur-md border border-kinetic-border text-kinetic-text px-4 py-2 rounded-full font-body font-medium text-sm shadow-lg hover:border-kinetic-accent transition-all hover:scale-105 hover:shadow-xl">
      <span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1.25rem;">event_available</span> 
      <span class="hidden sm:inline">Find Your Session</span>
      <span class="sm:hidden">Book</span>
    </button>`;

const newStr = `<button id="wizard-cta" class="fixed z-50 flex items-center gap-2 bottom-6 left-1/2 -translate-x-1/2 bg-kinetic-text text-kinetic-bg px-4 py-2 md:px-5 md:py-2.5 rounded-full font-display font-medium text-xs md:text-sm shadow-2xl hover:scale-105 transition-transform">
      <span class="material-symbols-outlined text-kinetic-accent" style="font-size: 1.1rem;">bolt</span> 
      <span>Book Session</span>
    </button>`;

html = html.replace(targetStr, newStr);
fs.writeFileSync('index.html', html);
console.log('done');
