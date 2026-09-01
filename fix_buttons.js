const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

const targetStr1 = `<div class="flex flex-wrap gap-3">
                <button class="brutal-btn flex-1 text-sm discipline-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="Skateboarding">Skateboarding</button>
                <button class="brutal-btn flex-1 text-sm discipline-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="Inline">Inline</button>
                <button class="brutal-btn flex-1 text-sm discipline-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="Quad">Quad</button>
              </div>`;

const newStr1 = `<div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                <button class="brutal-btn w-full text-sm discipline-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="Skateboarding">Skateboarding</button>
                <button class="brutal-btn w-full text-sm discipline-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="Inline">Inline</button>
                <button class="brutal-btn w-full text-sm discipline-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="Quad">Quad</button>
              </div>`;

html = html.replace(targetStr1, newStr1);

const targetStr2 = `<div class="flex flex-wrap gap-3">
                <button class="brutal-btn flex-1 text-sm level-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="First-timer">First-timer</button>
                <button class="brutal-btn flex-1 text-sm level-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="Beginner">Beginner</button>
                <button class="brutal-btn flex-1 text-sm level-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="Intermediate">Intermediate</button>
              </div>`;

const newStr2 = `<div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                <button class="brutal-btn w-full text-sm level-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="First-timer">First-timer</button>
                <button class="brutal-btn w-full text-sm level-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="Beginner">Beginner</button>
                <button class="brutal-btn w-full text-sm level-btn bg-kinetic-surface text-kinetic-text border-kinetic-border" data-val="Intermediate">Intermediate</button>
              </div>`;

html = html.replace(targetStr2, newStr2);

fs.writeFileSync('index.html', html);
console.log('done');
