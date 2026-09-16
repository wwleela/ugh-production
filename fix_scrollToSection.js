const fs = require('fs');
let code = fs.readFileSync('src/App.tsx', 'utf8');

const scrollHandlerStr = `
  const scrollToSection = (e: React.MouseEvent<HTMLAnchorElement>, targetId: string) => {
    e.preventDefault();
    const target = document.getElementById(targetId);
    if (target) {
      const offsetTop = target.getBoundingClientRect().top + window.scrollY - 100;
      window.scrollTo({
        top: offsetTop,
        behavior: 'smooth'
      });
      window.history.pushState(null, '', \`#\${targetId}\`);
      setActiveSection(targetId);
    }
    setIsMenuOpen(false);
  };
`;

// Insert it right after setActiveSection state definition
code = code.replace(
    'const [activeSection, setActiveSection] = useState<string>("");',
    'const [activeSection, setActiveSection] = useState<string>("");\n' + scrollHandlerStr
);

// Replace handleScroll with scrollToSection in all onClick handlers we added
code = code.replace(/onClick=\{\(e\) => handleScroll\(e/g, 'onClick={(e) => scrollToSection(e');

fs.writeFileSync('src/App.tsx', code);
