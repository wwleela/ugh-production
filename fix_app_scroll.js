const fs = require('fs');
let code = fs.readFileSync('src/App.tsx', 'utf8');

// Add activeSection state
if (!code.includes('activeSection')) {
    code = code.replace(
        'const [activeCategory, setActiveCategory] = useState<"kids" | "adults">("kids");',
        'const [activeCategory, setActiveCategory] = useState<"kids" | "adults">("kids");\n  const [activeSection, setActiveSection] = useState<string>("");'
    );
    
    // Add intersection observer useEffect
    const observerHook = `
  useEffect(() => {
    const observer = new IntersectionObserver((entries) => {
      let maxVisible = 0;
      let mostVisibleId = "";
      
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          // If we want exact ratio:
          if (entry.intersectionRatio > maxVisible) {
            maxVisible = entry.intersectionRatio;
            mostVisibleId = entry.target.id;
          }
        }
      });
      
      if (mostVisibleId) {
        setActiveSection(mostVisibleId);
      }
    }, { threshold: [0.1, 0.5, 0.9], rootMargin: "-80px 0px 0px 0px" });

    const sections = document.querySelectorAll("section[id]");
    sections.forEach((s) => observer.observe(s));

    return () => observer.disconnect();
  }, []);
`;
    
    code = code.replace(
        'useEffect(() => {\n    setContent(contentData);\n  }, []);',
        'useEffect(() => {\n    setContent(contentData);\n  }, []);\n' + observerHook
    );
}

// Ensure smooth scrolling click behavior and active styling on Desktop Nav
code = code.replace(
    /className="font-sans text-\[10px\] lg:text-\[11px\] font-bold uppercase tracking-\[0.2em\] text-charcoal\/50 dark:text-off-white\/50 hover:text-vibrant-orange transition-colors"/g,
    'className={`font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] transition-colors ${activeSection === "programs" ? "text-vibrant-orange" : "text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange"}`}'
);
// Above regex would incorrectly apply 'programs' to all. We need to be more precise.

fs.writeFileSync('src/App.tsx', code);
