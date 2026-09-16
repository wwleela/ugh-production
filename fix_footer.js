const fs = require('fs');
let code = fs.readFileSync('src/App.tsx', 'utf8');

const oldFooter = `{["Programs", "Leaderboard", "About", "Contact"].map((link) => (
                  <li key={link}>
                    <a
                      href={\`#\${link.toLowerCase()}\`}
                      className="font-sans text-sm font-bold text-white/50 hover:text-vibrant-orange transition-colors tracking-tight italic"
                    >
                      {link}
                    </a>
                  </li>
                ))}`;
                
const newFooter = `{["Programs", "Leaderboard", "About"].map((link) => (
                  <li key={link}>
                    <a
                      href={\`#\${link.toLowerCase()}\`}
                      onClick={(e) => handleScroll(e, link.toLowerCase())}
                      className={\`font-sans text-sm font-bold transition-colors tracking-tight italic \${activeSection === link.toLowerCase() ? "text-vibrant-orange" : "text-white/50 hover:text-vibrant-orange"}\`}
                    >
                      {link}
                    </a>
                  </li>
                ))}`;

code = code.replace(oldFooter, newFooter);

fs.writeFileSync('src/App.tsx', code);
