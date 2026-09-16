const fs = require('fs');
let code = fs.readFileSync('src/App.tsx', 'utf8');

code = code.replace(
  'href="#programs"\n                  className="bg-white dark:bg-transparent text-charcoal dark:text-off-white font-sans text-xs md:text-sm uppercase tracking-[0.2em] px-8 md:px-10 py-5 rounded-full border border-border-gray dark:border-white/10 hover:border-charcoal dark:hover:border-white hover:bg-charcoal dark:hover:bg-white hover:text-white dark:hover:text-charcoal transition-all text-center font-bold shadow-soft flex items-center justify-center w-full sm:w-auto min-h-[52px]"',
  'href="#programs"\n                  onClick={(e) => handleScroll(e, "programs")}\n                  className="bg-white dark:bg-transparent text-charcoal dark:text-off-white font-sans text-xs md:text-sm uppercase tracking-[0.2em] px-8 md:px-10 py-5 rounded-full border border-border-gray dark:border-white/10 hover:border-charcoal dark:hover:border-white hover:bg-charcoal dark:hover:bg-white hover:text-white dark:hover:text-charcoal transition-all text-center font-bold shadow-soft flex items-center justify-center w-full sm:w-auto min-h-[52px]"'
);

fs.writeFileSync('src/App.tsx', code);
