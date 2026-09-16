const fs = require('fs');
let code = fs.readFileSync('src/App.tsx', 'utf8');

code = code.replace(
  'href="#leaderboard"\n                className={`font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] transition-colors ${activeSection === "programs" ? "text-vibrant-orange" : "text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange"}`}',
  'href="#leaderboard"\n                className={`font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] transition-colors ${activeSection === "leaderboard" ? "text-vibrant-orange" : "text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange"}`}'
);

code = code.replace(
  'href="#about"\n                className={`font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] transition-colors ${activeSection === "programs" ? "text-vibrant-orange" : "text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange"}`}',
  'href="#about"\n                className={`font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] transition-colors ${activeSection === "about" ? "text-vibrant-orange" : "text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange"}`}'
);

// We should also handle smooth scrolling via an onClick handler to offset the sticky header. Let's write a generic function and add it.

fs.writeFileSync('src/App.tsx', code);
