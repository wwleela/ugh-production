const fs = require('fs');
let code = fs.readFileSync('src/App.tsx', 'utf8');

const oldMobile = `className="font-display text-4xl font-black text-charcoal dark:text-off-white tracking-tighter hover:text-vibrant-orange transition-colors"`;
const newMobile = `className={\`font-display text-4xl font-black tracking-tighter transition-colors \${activeSection === item.toLowerCase().replace(" ", "") ? "text-vibrant-orange" : "text-charcoal dark:text-off-white hover:text-vibrant-orange"}\`}`;

code = code.replace(oldMobile, newMobile);

fs.writeFileSync('src/App.tsx', code);
