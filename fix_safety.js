const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

const targetStr = `<div class="grid grid-cols-1 md:grid-cols-2 gap-fluid-md">
            <div class="p-6 bg-kinetic-surface border border-kinetic-border flex flex-col items-center text-center brutal-card">
              <img src="p2924075.jpeg" alt="Skating Helmet" class="w-full max-w-[200px] h-auto object-contain mb-4 rounded-lg">
              <h4 class="font-display font-bold text-xl mb-2">Helmet</h4>
              <p class="text-kinetic-muted text-sm leading-relaxed">A certified, well-fitted helmet is required to protect against impacts.</p>
            </div>
            <div class="p-6 bg-kinetic-surface border border-kinetic-border flex flex-col items-center text-center brutal-card">
              <img src="p2402406.jpeg" alt="Safety Kit Pads" class="w-full max-w-[250px] h-auto object-contain mb-4 rounded-lg">
              <h4 class="font-display font-bold text-xl mb-2">Full Pad Kit</h4>
              <p class="text-kinetic-muted text-sm leading-relaxed">Wrist guards, elbow pads, and knee pads are essential to prevent scrapes and fractures.</p>
            </div>
          </div>`;

const newStr = `<div class="grid grid-cols-1 sm:grid-cols-2 gap-6 md:gap-8 max-w-4xl mx-auto mt-8">
            <div class="p-6 md:p-8 bg-kinetic-surface border-2 border-kinetic-border shadow-[4px_4px_0px_var(--kinetic-shadow)] rounded-2xl flex flex-col items-center text-center h-full transition-transform hover:-translate-y-1">
              <div class="flex-1 flex items-center justify-center min-h-[180px] md:min-h-[220px] w-full mb-6">
                <img src="p2924075.jpeg" alt="Skating Helmet" class="max-h-[180px] md:max-h-[220px] w-auto object-contain drop-shadow-md mix-blend-multiply dark:mix-blend-normal rounded-lg">
              </div>
              <h4 class="font-display font-bold text-2xl mb-2 uppercase tracking-tight">Helmet</h4>
              <p class="text-kinetic-muted text-sm md:text-base leading-relaxed">A certified, well-fitted helmet is required to protect against impacts.</p>
            </div>
            <div class="p-6 md:p-8 bg-kinetic-surface border-2 border-kinetic-border shadow-[4px_4px_0px_var(--kinetic-shadow)] rounded-2xl flex flex-col items-center text-center h-full transition-transform hover:-translate-y-1">
              <div class="flex-1 flex items-center justify-center min-h-[180px] md:min-h-[220px] w-full mb-6">
                <img src="p2402406.jpeg" alt="Safety Kit Pads" class="max-h-[180px] md:max-h-[220px] w-auto object-contain drop-shadow-md mix-blend-multiply dark:mix-blend-normal rounded-lg">
              </div>
              <h4 class="font-display font-bold text-2xl mb-2 uppercase tracking-tight">Full Pad Kit</h4>
              <p class="text-kinetic-muted text-sm md:text-base leading-relaxed">Wrist guards, elbow pads, and knee pads are essential to prevent scrapes and fractures.</p>
            </div>
          </div>`;

html = html.replace(targetStr, newStr);

fs.writeFileSync('index.html', html);
console.log('done');
