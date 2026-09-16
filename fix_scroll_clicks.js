const fs = require('fs');
let code = fs.readFileSync('src/App.tsx', 'utf8');

const scrollHandlerStr = `
  const handleScroll = (e: React.MouseEvent<HTMLAnchorElement>, targetId: string) => {
    e.preventDefault();
    const target = document.getElementById(targetId);
    if (target) {
      // 100px is the height of the fixed navbar
      const offsetTop = target.getBoundingClientRect().top + window.scrollY - 100;
      window.scrollTo({
        top: offsetTop,
        behavior: 'smooth'
      });
      // Also update URL hash without jump
      window.history.pushState(null, '', \`#\${targetId}\`);
      // Optimistically update active section
      setActiveSection(targetId);
    }
    setIsMenuOpen(false); // Close mobile menu if open
  };
`;

if (!code.includes('handleScroll')) {
    // insert handleScroll right after the useEffect observer
    code = code.replace(
        'return () => observer.disconnect();\n  }, []);',
        'return () => observer.disconnect();\n  }, []);\n' + scrollHandlerStr
    );
}

// Update desktop links
code = code.replace(
    /href="#programs"\n\s*className={`font-sans text-\[10px\] lg:text-\[11px\] font-bold uppercase tracking-\[0.2em\] transition-colors \${activeSection === "programs" \? "text-vibrant-orange" : "text-charcoal\/50 dark:text-off-white\/50 hover:text-vibrant-orange"}`}/g,
    'href="#programs"\n                onClick={(e) => handleScroll(e, "programs")}\n                className={`font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] transition-colors ${activeSection === "programs" ? "text-vibrant-orange" : "text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange"}`}'
);

code = code.replace(
    /href="#leaderboard"\n\s*className={`font-sans text-\[10px\] lg:text-\[11px\] font-bold uppercase tracking-\[0.2em\] transition-colors \${activeSection === "leaderboard" \? "text-vibrant-orange" : "text-charcoal\/50 dark:text-off-white\/50 hover:text-vibrant-orange"}`}/g,
    'href="#leaderboard"\n                onClick={(e) => handleScroll(e, "leaderboard")}\n                className={`font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] transition-colors ${activeSection === "leaderboard" ? "text-vibrant-orange" : "text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange"}`}'
);

code = code.replace(
    /href="#about"\n\s*className={`font-sans text-\[10px\] lg:text-\[11px\] font-bold uppercase tracking-\[0.2em\] transition-colors \${activeSection === "about" \? "text-vibrant-orange" : "text-charcoal\/50 dark:text-off-white\/50 hover:text-vibrant-orange"}`}/g,
    'href="#about"\n                onClick={(e) => handleScroll(e, "about")}\n                className={`font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] transition-colors ${activeSection === "about" ? "text-vibrant-orange" : "text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange"}`}'
);

// Update mobile links
const oldMobileRender = `{["Programs", "Leaderboard", "About"].map((item, i) => (
                <motion.a
                  key={item}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.2 + i * 0.1 }}
                  href={\`#\${item.toLowerCase().replace(" ", "")}\`}
                  onClick={() => setIsMenuOpen(false)}
                  className={\`font-display text-4xl font-black tracking-tighter transition-colors \${activeSection === item.toLowerCase().replace(" ", "") ? "text-vibrant-orange" : "text-charcoal dark:text-off-white hover:text-vibrant-orange"}\`}
                >
                  {item}
                </motion.a>
              ))}`;
              
const newMobileRender = `{["Programs", "Leaderboard", "About"].map((item, i) => (
                <motion.a
                  key={item}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.2 + i * 0.1 }}
                  href={\`#\${item.toLowerCase().replace(" ", "")}\`}
                  onClick={(e) => handleScroll(e, item.toLowerCase().replace(" ", ""))}
                  className={\`font-display text-4xl font-black tracking-tighter transition-colors \${activeSection === item.toLowerCase().replace(" ", "") ? "text-vibrant-orange" : "text-charcoal dark:text-off-white hover:text-vibrant-orange"}\`}
                >
                  {item}
                </motion.a>
              ))}`;

code = code.replace(oldMobileRender, newMobileRender);

fs.writeFileSync('src/App.tsx', code);
