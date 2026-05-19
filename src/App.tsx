/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { useEffect, useState, useRef } from "react";
import { motion, AnimatePresence, animate } from "motion/react";
import heroImage from "./assets/images/regenerated_image_1778859272387.png";
import navLogo from "./assets/images/regenerated_image_1778859275982.png";
import footerLogo from "./assets/images/regenerated_image_1778859278835.png";
import {
  Instagram,
  MessageCircle,
  Phone,
  ArrowRight,
  Menu,
  X,
  ExternalLink,
  ShieldCheck,
  Star,
  QrCode,
  Sun,
  Moon,
} from "lucide-react";
import {
  SignedIn,
  SignedOut,
  SignInButton,
  UserButton,
} from "@clerk/clerk-react";
import { ContentData, Program } from "./types";

function AnimatedPoints({
  points,
  change,
}: {
  points: number;
  change: string;
}) {
  const [currentPoints, setCurrentPoints] = useState(points);
  const [flashColor, setFlashColor] = useState("");
  const prevPointsRef = useRef(points);

  useEffect(() => {
    if (prevPointsRef.current !== points) {
      if (points > prevPointsRef.current) {
        setFlashColor(
          "text-green-500 scale-110 !font-black drop-shadow-[0_0_8px_rgba(34,197,94,0.5)]",
        );
      } else if (points < prevPointsRef.current) {
        setFlashColor("text-red-500 scale-90 opacity-75");
      }

      const controls = animate(prevPointsRef.current, points, {
        duration: 1.5,
        ease: "easeOut",
        onUpdate: (val) => {
          setCurrentPoints(Math.round(val));
        },
        onComplete: () => {
          setFlashColor("");
        },
      });

      prevPointsRef.current = points;
      return controls.stop;
    }
  }, [points]);

  return (
    <span className={`inline-block transition-all duration-700 ${flashColor}`}>
      {currentPoints.toLocaleString()}
    </span>
  );
}

export default function App() {
  const [content, setContent] = useState<ContentData | null>(null);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  useEffect(() => {
    const isDark =
      localStorage.getItem("theme") === "dark" ||
      (!localStorage.getItem("theme") &&
        window.matchMedia("(prefers-color-scheme: dark)").matches);
    setIsDarkMode(isDark);
    if (isDark) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, []);

  const toggleDarkMode = () => {
    setIsDarkMode((prev) => {
      const next = !prev;
      if (next) {
        document.documentElement.classList.add("dark");
        localStorage.setItem("theme", "dark");
      } else {
        document.documentElement.classList.remove("dark");
        localStorage.setItem("theme", "light");
      }
      return next;
    });
  };

  useEffect(() => {
    const fetchContent = () => {
      fetch(`assets/content.json?t=${new Date().getTime()}`)
        .then((res) => res.json())
        .then((data) => setContent(data))
        .catch((err) => console.error("Failed to load content", err));
    };

    fetchContent();
    const interval = setInterval(fetchContent, 10000); // Check for updates every 10 seconds
    return () => clearInterval(interval);
  }, []);

  const handleEnroll = (program: Program) => {
    if (!content) return;
    const message = content.whatsapp.preFillTemplate
      .replace("{{programName}}", program.displayName)
      .replace("{{price}}", program.price.toLocaleString("en-IN"));

    const url = `https://wa.me/${content.contact.phone}?text=${encodeURIComponent(message)}`;
    window.open(url, "_blank");
  };

  const handleTrial = () => {
    if (!content) return;
    const url = `https://wa.me/${content.contact.phone}?text=${encodeURIComponent(content.whatsapp.freeTrialTemplate)}`;
    window.open(url, "_blank");
  };

  if (!content) {
    return (
      <div className="min-h-screen bg-vintage-cream flex items-center justify-center">
        <div className="animate-pulse flex flex-col items-center">
          <div className="w-16 h-16 border-4 border-deep-teal rounded-full border-t-transparent animate-spin mb-4" />
          <p className="font-mono text-xs uppercase tracking-widest text-deep-teal">
            Initializing Mission 2026...
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen selection:bg-vibrant-orange selection:text-white overflow-x-hidden">
      {/* Google Analytics */}
      <script
        async
        src="https://www.googletagmanager.com/gtag/js?id=G-K2PYP4J4DZ"
      ></script>
      <script>
        {`
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', 'G-K2PYP4J4DZ');
        `}
      </script>

      <nav
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-700 ${
          scrolled ? "py-2 md:py-4" : "py-4 md:py-8"
        }`}
      >
        <div className="max-w-7xl mx-auto px-4 md:px-6">
          <div
            className={`flex items-center justify-between px-4 md:px-8 py-2 md:py-4 rounded-full transition-all duration-700 ${
              scrolled ? "glass-premium shadow-premium" : "bg-transparent"
            }`}
          >
            <div className="flex items-center gap-2 md:gap-3">
              <div className="w-9 h-9 md:w-10 md:h-10 rounded-full bg-white dark:bg-zinc-800 overflow-hidden border border-border-gray dark:border-white/10 flex items-center justify-center shrink-0 shadow-sm">
                <img
                  src={navLogo}
                  alt="Logo"
                  className="w-full h-full object-cover p-1"
                />
              </div>
              <a
                href="./"
                className="font-display text-sm md:text-xl font-extrabold text-charcoal dark:text-off-white tracking-tighter whitespace-nowrap"
              >
                URBAN GLIDING{" "}
                <span className="hidden sm:inline">HYDERABAD</span>
              </a>
            </div>

            <div className="hidden md:flex items-center gap-6 lg:gap-10">
              <a
                href="#programs"
                className="font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange transition-colors"
              >
                Programs
              </a>
              <a
                href="#leaderboard"
                className="font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange transition-colors"
              >
                Leaderboard
              </a>
              <a
                href="#about"
                className="font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] text-charcoal/50 dark:text-off-white/50 hover:text-vibrant-orange transition-colors"
              >
                About
              </a>

              <div className="h-4 w-[1px] bg-charcoal/10 dark:bg-white/10"></div>

              <button
                onClick={toggleDarkMode}
                className="w-10 h-10 rounded-full border border-border-gray dark:border-white/20 flex items-center justify-center text-charcoal dark:text-off-white hover:bg-charcoal dark:hover:bg-off-white dark:hover:text-charcoal hover:text-white transition-all transform-gpu hover:scale-105 active:scale-95"
              >
                {isDarkMode ? <Sun size={16} /> : <Moon size={16} />}
              </button>

              <SignedOut>
                <SignInButton mode="modal">
                  <button className="font-sans text-[11px] font-bold uppercase tracking-[0.2em] text-charcoal dark:text-off-white hover:text-vibrant-orange transition-all">
                    Sign In
                  </button>
                </SignInButton>
              </SignedOut>
              <SignedIn>
                <UserButton afterSignOutUrl="/" />
              </SignedIn>

              <button
                onClick={handleTrial}
                className="bg-vibrant-orange text-white font-sans text-[11px] font-bold uppercase tracking-[0.2em] px-8 py-4 rounded-full btn-premium shadow-lg shadow-vibrant-orange/20 hover:-translate-y-0.5 hover:shadow-xl active:translate-y-0"
              >
                Secure Access
              </button>
            </div>

            <div className="flex items-center gap-2 md:hidden">
              <button
                onClick={toggleDarkMode}
                className="w-10 h-10 rounded-full border border-border-gray dark:border-white/20 flex items-center justify-center text-charcoal dark:text-off-white tap-target-min hover:bg-charcoal dark:hover:bg-off-white dark:hover:text-charcoal hover:text-white transition-all transform-gpu"
              >
                {isDarkMode ? <Sun size={18} /> : <Moon size={18} />}
              </button>
              <button
                className="tap-target-min bg-vibrant-orange text-white rounded-full shadow-lg active:scale-95 transition-all flex items-center justify-center"
                onClick={() => setIsMenuOpen(!isMenuOpen)}
              >
                {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isMenuOpen && (
          <motion.div
            initial={{ opacity: 0, x: "100%" }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: "100%" }}
            transition={{ type: "spring", damping: 25, stiffness: 120 }}
            className="fixed inset-0 z-[60] bg-white dark:bg-zinc-950 p-6 flex flex-col transition-colors duration-500"
          >
            <div className="flex justify-between items-center mb-12">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-white dark:bg-zinc-800 overflow-hidden border border-border-gray dark:border-white/10 flex items-center justify-center shrink-0">
                  <img
                    src={navLogo}
                    alt="Logo"
                    className="w-full h-full object-cover p-1"
                  />
                </div>
                <span className="font-display text-xl font-extrabold text-charcoal dark:text-off-white tracking-tighter">
                  URBAN GLIDING
                </span>
              </div>
              <button
                onClick={() => setIsMenuOpen(false)}
                className="w-12 h-12 bg-charcoal text-white rounded-full shadow-xl flex items-center justify-center"
              >
                <X size={20} />
              </button>
            </div>

            <div className="flex flex-col gap-6 flex-grow">
              {["Programs", "Leaderboard", "About"].map((item, i) => (
                <motion.a
                  key={item}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.2 + i * 0.1 }}
                  href={`#${item.toLowerCase().replace(" ", "")}`}
                  onClick={() => setIsMenuOpen(false)}
                  className="font-display text-4xl font-black text-charcoal dark:text-off-white tracking-tighter hover:text-vibrant-orange transition-colors"
                >
                  {item}
                </motion.a>
              ))}
            </div>

            <div className="mt-auto space-y-6">
              <div className="h-px bg-border-gray" />
              <div className="flex justify-between items-center">
                <div>
                  <p className="font-sans text-[10px] font-bold uppercase tracking-widest text-charcoal/50 dark:text-off-white/50 mb-2">
                    Primary Hub
                  </p>
                  <p className="font-sans text-sm font-bold text-charcoal dark:text-off-white">
                    Hyderabad, Telangana
                  </p>
                </div>
                <div className="flex gap-4">
                  <a
                    href="https://www.instagram.com/urbangliding.hyd?igsh=MWJubGk3OG42eHI2Zw=="
                    target="_blank"
                    rel="noreferrer"
                    className="w-10 h-10 rounded-full border border-border-gray flex items-center justify-center text-charcoal dark:text-off-white hover:bg-charcoal hover:text-white dark:hover:bg-white dark:hover:text-charcoal transition-all"
                  >
                    <Instagram size={18} />
                  </a>
                </div>
              </div>
              <button
                onClick={() => {
                  handleTrial();
                  setIsMenuOpen(false);
                }}
                className="w-full bg-vibrant-orange text-white py-6 rounded-full font-sans text-xs uppercase tracking-[0.3em] font-extrabold shadow-2xl"
              >
                Secure Trial Access
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      <main>
        {/* Hero Strategic Zone */}
        <section className="relative min-h-[85vh] flex items-center justify-center pt-24 pb-12 overflow-hidden bg-white dark:bg-zinc-900 transition-colors duration-500">
          {/* Crisp Background Elements */}
          <div className="absolute inset-0 z-0 overflow-hidden pointer-events-none">
            <div
              className="absolute inset-0 opacity-[0.03]"
              style={{
                backgroundImage:
                  "radial-gradient(#1a1a1a 1px, transparent 1px)",
                backgroundSize: "32px 32px",
              }}
            />
          </div>

          <div className="max-w-7xl mx-auto px-6 relative z-10 w-full grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
            <div className="text-left">
              <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
              >
                <span className="inline-flex items-center gap-2 py-2 px-5 bg-deep-teal/5 dark:bg-deep-teal/10 text-deep-teal dark:text-deep-teal/90 font-sans text-[10px] md:text-xs uppercase tracking-[0.3em] rounded-full mb-6 font-bold border border-deep-teal/10">
                  <span className="w-1.5 h-1.5 bg-deep-teal rounded-full animate-pulse" />
                  IOC Certified · Hyderabad's Premier Skate Community
                </span>
                <h1 className="text-balance mb-6">
                  Master the <br />
                  <span className="text-vibrant-orange italic">Pavement</span>
                </h1>
              </motion.div>

              <motion.p
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{
                  delay: 0.1,
                  duration: 1,
                  ease: [0.16, 1, 0.3, 1],
                }}
                className="font-sans text-base md:text-lg text-charcoal/50 dark:text-off-white/50 max-w-lg mb-10 leading-relaxed font-medium text-balance"
              >
                World-class skate education delivered to your doorstep. Join
                250+ gliders progressing across 6+ residential societies with
                IOC-certified coaching.
              </motion.p>

              <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{
                  delay: 0.2,
                  duration: 1,
                  ease: [0.16, 1, 0.3, 1],
                }}
                className="flex flex-col sm:flex-row gap-4"
              >
                <button
                  onClick={handleTrial}
                  className="bg-vibrant-orange text-white font-sans text-xs md:text-sm uppercase tracking-[0.2em] px-8 md:px-10 py-5 rounded-full btn-premium shadow-xl shadow-vibrant-orange/10 font-bold flex items-center justify-center gap-3 group w-full sm:w-auto"
                >
                  Book Private Trial
                  <ArrowRight
                    size={18}
                    className="group-hover:translate-x-2 transition-transform duration-500"
                  />
                </button>
                <a
                  href="#programs"
                  className="bg-white dark:bg-transparent text-charcoal dark:text-off-white font-sans text-xs md:text-sm uppercase tracking-[0.2em] px-8 md:px-10 py-5 rounded-full border border-border-gray dark:border-white/10 hover:border-charcoal dark:hover:border-white hover:bg-charcoal dark:hover:bg-white hover:text-white dark:hover:text-charcoal transition-all text-center font-bold shadow-soft flex items-center justify-center w-full sm:w-auto min-h-[52px]"
                >
                  Curriculum
                </a>
              </motion.div>
            </div>

            <div className="relative flex items-center justify-center lg:justify-end mt-12 lg:mt-0">
              <motion.div
                initial={{ scale: 0.9, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                transition={{ duration: 1.5, ease: [0.16, 1, 0.3, 1] }}
                className="relative w-full max-w-[440px] aspect-square group"
              >
                <div className="absolute inset-0 bg-gradient-to-br from-deep-teal/5 to-vibrant-orange/5 rounded-[60px] blur-3xl opacity-50 transition-all duration-1000 scale-110" />
                <div className="relative w-full h-full rounded-[60px] border border-border-gray dark:border-white/10 bg-white/40 dark:bg-zinc-900/40 backdrop-blur-xl p-10 md:p-12 shadow-xl overflow-hidden shadow-charcoal/5">
                  <img
                    src={heroImage}
                    alt="UGH Logo"
                    className="w-full h-full object-contain transition-transform duration-[3s] group-hover:scale-105 p-6"
                  />
                </div>

                {/* Floating Stats */}
                <motion.div
                  initial={{ x: 30, opacity: 0 }}
                  animate={{ x: 0, opacity: 1 }}
                  transition={{ delay: 0.6, duration: 1 }}
                  className="absolute -bottom-6 -left-6 glass-premium p-6 rounded-2xl shadow-xl border border-border-gray max-w-[200px]"
                >
                  <p className="font-display text-3xl font-black text-deep-teal leading-none mb-1">
                    250+
                  </p>
                  <p className="font-sans text-[9px] uppercase tracking-widest text-charcoal/50 dark:text-off-white/50 font-bold">
                    Active Students
                  </p>
                </motion.div>

                {/* floating badge */}
                <motion.div
                  animate={{ y: [0, -8, 0] }}
                  transition={{
                    duration: 4,
                    repeat: Infinity,
                    ease: "easeInOut",
                  }}
                  className="absolute -top-4 -right-4 glass-premium px-5 py-3 rounded-xl shadow-xl border border-border-gray flex items-center gap-2"
                >
                  <Star
                    size={14}
                    className="text-vibrant-orange fill-vibrant-orange"
                  />
                  <p className="font-sans text-[9px] font-bold uppercase tracking-widest text-charcoal dark:text-off-white">
                    IOC Certified
                  </p>
                </motion.div>
              </motion.div>
            </div>
          </div>
        </section>

        {/* Training Modules */}
        <section
          id="programs"
          className="py-16 md:py-24 px-6 bg-white dark:bg-zinc-900 relative overflow-hidden transition-colors duration-500"
        >
          <div className="max-w-7xl mx-auto relative z-10">
            <div className="flex flex-col lg:flex-row lg:items-end justify-between mb-12 md:mb-16 gap-8">
              <div className="max-w-2xl">
                <span className="font-sans text-[10px] uppercase tracking-[0.4em] text-vibrant-orange mb-3 font-extrabold block">
                  Expert Coaching
                </span>
                <h2 className="mb-4 text-charcoal dark:text-off-white">
                  Active Modules
                </h2>
                <p className="font-sans text-base md:text-lg text-charcoal/50 dark:text-off-white/50 font-medium text-balance">
                  Specialized training systems designed for rapid progression
                  across all skill levels.
                </p>
              </div>
              <div className="flex items-center gap-2 bg-light-sand dark:bg-white/5 p-1.5 rounded-full border border-border-gray dark:border-white/10 w-full sm:w-auto overflow-x-auto no-scrollbar">
                <button className="px-6 py-2.5 rounded-full bg-charcoal text-white font-sans text-[10px] font-bold uppercase tracking-widest whitespace-nowrap min-h-[40px]">
                  Monthly Mastery
                </button>
                <button className="px-6 py-2.5 rounded-full text-charcoal/50 dark:text-off-white/50 font-sans text-[10px] font-bold uppercase tracking-widest hover:text-charcoal dark:hover:text-off-white transition-colors whitespace-nowrap min-h-[40px]">
                  Seasonal Camps
                </button>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-stretch">
              {(Object.values(content.programs) as Program[]).map(
                (program, idx) => (
                  <motion.div
                    key={program.id}
                    initial={{ y: 50, opacity: 0 }}
                    whileInView={{ y: 0, opacity: 1 }}
                    viewport={{ once: true, margin: "-50px" }}
                    transition={{
                      delay: idx * 0.1,
                      duration: 1,
                      ease: [0.16, 1, 0.3, 1],
                    }}
                    className={`card-premium p-6 md:p-10 flex flex-col relative group hover:-translate-y-4 hover:shadow-[0_40px_100px_-20px_rgba(0,97,95,0.1)] ${
                      program.id === "summer_camp"
                        ? "bg-light-sand dark:bg-zinc-800 border-none"
                        : ""
                    }`}
                  >
                    <div className="flex justify-between items-start mb-8 md:mb-10">
                      <div
                        className={`w-12 h-12 rounded-xl flex items-center justify-center border transition-all duration-700 ${
                          program.id === "summer_camp"
                            ? "bg-vibrant-orange text-white border-vibrant-orange"
                            : "bg-deep-teal/5 text-deep-teal border-deep-teal/10 group-hover:bg-deep-teal group-hover:text-white"
                        }`}
                      >
                        {program.id === "summer_camp" ? (
                          <Star size={20} />
                        ) : (
                          <ShieldCheck size={20} />
                        )}
                      </div>
                      {program.badge && (
                        <span className="bg-charcoal text-[white] font-sans text-[8px] uppercase tracking-[0.2em] px-3 py-1 rounded-full font-bold">
                          {program.badge}
                        </span>
                      )}
                    </div>

                    <div className="mb-8 flex-grow">
                      <h3 className="mb-3 transition-colors group-hover:text-deep-teal text-2xl">
                        {program.displayName}
                      </h3>
                      <p className="font-sans text-[15px] text-charcoal/50 dark:text-off-white/50 leading-relaxed font-medium">
                        {program.description}
                      </p>
                    </div>

                    <div className="space-y-3 mb-10">
                      {program.features.slice(0, 4).map((feature, fidx) => (
                        <div key={fidx} className="flex items-center gap-3">
                          <div className="w-1 h-1 rounded-full bg-charcoal/20 group-hover:bg-vibrant-orange transition-colors" />
                          <span className="text-[12px] font-bold text-charcoal/50 dark:text-off-white/50 group-hover:text-charcoal dark:text-off-white transition-colors tracking-tight">
                            {feature}
                          </span>
                        </div>
                      ))}
                    </div>

                    <div className="mt-auto pt-8 border-t border-border-gray">
                      <div className="mb-6 flex items-baseline gap-2">
                        <span className="text-3xl font-display font-black text-charcoal dark:text-off-white tracking-tighter italic">
                          ₹{program.price.toLocaleString("en-IN")}
                        </span>
                        <span className="text-[9px] text-charcoal/50 dark:text-off-white/50 font-sans uppercase tracking-[0.2em] font-bold">
                          / {program.period}
                        </span>
                      </div>
                      <button
                        onClick={() => handleEnroll(program)}
                        className={`w-full font-sans text-[10px] uppercase tracking-[0.2em] py-3.5 rounded-full border transition-all duration-700 font-extrabold btn-premium
                        ${program.id === "summer_camp" ? "bg-deep-teal text-white border-deep-teal" : "bg-transparent border-charcoal dark:border-white text-charcoal dark:text-off-white hover:bg-charcoal dark:hover:bg-off-white hover:text-white dark:hover:text-charcoal"}
                      `}
                      >
                        {program.ctaText}
                      </button>
                    </div>
                  </motion.div>
                ),
              )}
            </div>
          </div>
        </section>

        {/* Leaderboard Section */}
        <section
          id="leaderboard"
          className="py-16 md:py-24 px-6 bg-white dark:bg-zinc-900 overflow-hidden text-center transition-colors duration-500"
        >
          <div className="max-w-4xl mx-auto">
            <div className="mb-12 md:mb-16 px-4">
              <span className="font-sans text-[10px] uppercase tracking-[0.4em] text-vibrant-orange mb-4 font-extrabold block">
                Community Impact
              </span>
              <h2 className="mb-4 text-charcoal dark:text-off-white">
                UGH Leaderboard
              </h2>
            </div>

            <div className="glass-premium rounded-[28px] md:rounded-[40px] overflow-hidden border border-border-gray shadow-xl mx-2 md:mx-0 text-left">
              <div className="bg-charcoal text-white px-6 md:px-10 py-5 flex justify-between items-center font-sans text-[9px] font-bold uppercase tracking-[0.34em]">
                <div className="flex items-center gap-3">
                  <ShieldCheck size={16} />
                  <span className="hidden sm:inline">Skater Recognition</span>
                  <span className="sm:hidden">Skater</span>
                </div>
                <span>Points</span>
              </div>
              <div className="divide-y divide-border-gray/50 dark:divide-white/10">
                {[...content.leaderboard.rankings]
                  .sort((a, b) => b.points - a.points)
                  .map((rank, idx) => (
                    <motion.div
                      layout
                      key={rank.name}
                      initial={{ opacity: 0, y: 10 }}
                      whileInView={{ opacity: 1, y: 0 }}
                      viewport={{ once: true }}
                      transition={{ delay: idx * 0.04 }}
                      className="px-6 md:px-10 py-4 md:py-6 flex items-center justify-between hover:bg-light-sand dark:hover:bg-white/5 transition-all duration-500 group"
                    >
                      <div className="flex items-center gap-4 md:gap-10">
                        <div className="relative shrink-0">
                          <span
                            className={`font-display text-xl md:text-2xl font-black ${idx < 3 ? "text-vibrant-orange" : "text-charcoal/50 dark:text-off-white/50"} transition-colors group-hover:text-vibrant-orange w-6 md:w-10 block`}
                          >
                            0{idx + 1}
                          </span>
                        </div>
                        <div>
                          <p className="font-display text-lg md:text-xl font-bold tracking-tighter text-charcoal dark:text-off-white mb-0.5 md:mb-1 group-hover:translate-x-1 transition-transform duration-500">
                            {rank.name}
                          </p>
                          <div
                            className={`inline-flex items-center gap-2 px-2 py-0.5 rounded-full border font-sans text-[8px] uppercase tracking-widest font-bold ${
                              rank.change === "up"
                                ? "bg-green-500/5 border-green-500/10 text-green-600 dark:text-green-400"
                                : rank.change === "down"
                                  ? "bg-red-500/5 border-red-500/10 text-red-600 dark:text-red-400"
                                  : "bg-gray-50 dark:bg-white/5 border-gray-100 dark:border-white/10 text-gray-400"
                            }`}
                          >
                            {rank.change === "up" ? (
                              <ArrowRight size={10} className="-rotate-45" />
                            ) : rank.change === "down" ? (
                              <ArrowRight size={10} className="rotate-45" />
                            ) : (
                              <div className="w-2 h-0.5 bg-gray-400" />
                            )}
                            {rank.change === "stable"
                              ? "Constant"
                              : rank.change.toUpperCase()}
                          </div>
                        </div>
                      </div>
                      <div className="text-right shrink-0">
                        <p className="font-display text-xl md:text-3xl font-black text-deep-teal tracking-tighter transition-all duration-700 group-hover:scale-105">
                          <AnimatedPoints
                            points={rank.points}
                            change={rank.change}
                          />
                        </p>
                      </div>
                    </motion.div>
                  ))}
              </div>
            </div>

            <div className="mt-10 flex justify-center items-center gap-3">
              <span className="w-1.5 h-1.5 rounded-full bg-vibrant-orange animate-pulse" />
              <p className="font-sans text-[9px] font-extrabold uppercase tracking-widest text-charcoal/50 dark:text-off-white/50">
                Sync Cycle: 24h Protocol
              </p>
            </div>
          </div>
        </section>

        {/* About Section */}
        <section
          id="about"
          className="py-16 md:py-24 px-6 bg-white dark:bg-zinc-900 relative overflow-hidden transition-colors duration-500"
        >
          <div className="max-w-7xl mx-auto relative z-10">
            <div className="max-w-4xl mx-auto items-center mb-16 lg:mb-24 text-center">
              <div>
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.8 }}
                >
                  <span className="font-sans text-[10px] uppercase tracking-[0.4em] text-vibrant-orange mb-4 font-extrabold block">
                    The Framework
                  </span>
                  <h2 className="mb-6 md:mb-8 text-charcoal dark:text-off-white text-4xl md:text-5xl lg:text-5xl tracking-tighter sm:leading-none">
                    About UGH
                  </h2>
                  <p className="font-sans text-lg md:text-xl font-medium text-charcoal/50 dark:text-off-white/50 leading-[1.6] text-balance mb-12">
                    Skate education, delivered to your doorstep. UGH transforms Hyderabad's residential complexes into private training grounds using IOC-certified methodologies.
                  </p>
                </motion.div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 text-left">
                  <motion.div 
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5, delay: 0.1 }}
                    className="p-6 md:p-8 rounded-[24px] bg-white dark:bg-zinc-900 border border-border-gray dark:border-white/10 hover:-translate-y-1 transition-all duration-500 hover:shadow-premium group"
                  >
                    <h4 className="font-display text-lg font-bold text-charcoal dark:text-off-white tracking-tight mb-2">
                      IOC Precision
                    </h4>
                    <p className="font-sans text-sm text-charcoal/50 dark:text-off-white/50 font-medium leading-relaxed">
                      Olympic-grade standards brought directly to your pavement.
                    </p>
                  </motion.div>
                  
                  <motion.div 
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5, delay: 0.2 }}
                    className="p-6 md:p-8 rounded-[24px] bg-white dark:bg-zinc-900 border border-border-gray dark:border-white/10 hover:-translate-y-1 transition-all duration-500 hover:shadow-premium group"
                  >
                    <h4 className="font-display text-lg font-bold text-charcoal dark:text-off-white tracking-tight mb-2">
                      Society Access
                    </h4>
                    <p className="font-sans text-sm text-charcoal/50 dark:text-off-white/50 font-medium leading-relaxed">
                      On-site coaching strictly within your residence for all ages.
                    </p>
                  </motion.div>
                </div>
              </div>
            </div>

            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
              className="p-10 md:p-20 bg-charcoal dark:bg-zinc-900 border dark:border-white/10 rounded-[40px] md:rounded-[60px] text-white shadow-2xl relative overflow-hidden group text-center"
            >
              <div className="absolute inset-0 opacity-[0.03] pointer-events-none bg-[radial-gradient(#ffffff_1px,transparent_1px)] [background-size:32px_32px]"></div>

              {/* Highlight Orbs */}
              <div className="absolute -top-1/2 -left-1/4 w-full h-full bg-vibrant-orange/20 blur-[120px] rounded-full pointer-events-none" />
              <div className="absolute -bottom-1/2 -right-1/4 w-full h-full bg-deep-teal/30 blur-[120px] rounded-full pointer-events-none" />

              <div className="relative z-10 max-w-3xl mx-auto flex flex-col items-center">
                <h3 className="mb-6 italic leading-[1] tracking-tighter text-balance text-white md:text-5xl lg:text-5xl">
                  Start your journey with{" "}
                  <span className="text-vibrant-orange">UGH</span>
                </h3>
                <p className="font-sans text-sm md:text-lg text-white/70 font-medium mb-10 max-w-lg mx-auto leading-relaxed">
                  By clicking on the video about the SB series to start your
                  journey. Share and tag UGH to get on our leaderboard! For any
                  inquiries, feel free to DM us.
                </p>
                <a
                  href="https://www.instagram.com/reel/DYYldtwB0ze/?igsh=MWJuZmU0b3RjNHN1eg=="
                  target="_blank"
                  rel="noreferrer"
                  className="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-vibrant-orange text-white font-sans text-[10px] md:text-xs uppercase tracking-[0.25em] px-10 md:px-14 py-4 md:py-5 rounded-full font-extrabold hover:scale-105 transition-all duration-700 shadow-xl shadow-vibrant-orange/30 btn-premium"
                >
                  <Instagram size={18} />
                  Watch SB Series
                </a>
              </div>
            </motion.div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="py-20 md:py-28 px-6 bg-charcoal text-white relative overflow-hidden">
        <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-deep-teal via-vibrant-orange to-deep-teal opacity-30" />
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-16 mb-20 md:mb-28">
            <div className="lg:col-span-3">
              <div className="flex items-center gap-4 mb-8">
                <div className="w-10 h-10 rounded-full bg-white overflow-hidden border border-white/10 flex items-center justify-center shrink-0">
                  <img
                    src={footerLogo}
                    alt="Logo"
                    className="w-full h-full object-cover p-1"
                  />
                </div>
                <span className="font-display text-xl md:text-2xl font-extrabold tracking-tighter">
                  URBAN GLIDING HYDERABAD
                </span>
              </div>
              <p className="font-sans text-base md:text-lg text-white/40 max-w-sm leading-relaxed font-medium mb-8">
                Making sports accessible for all.
              </p>
              <div className="flex gap-5">
                <a
                  href="https://www.instagram.com/urbangliding.hyd?igsh=MWJubGk3OG42eHI2Zw=="
                  target="_blank"
                  rel="noreferrer"
                  className="w-10 h-10 rounded-full border border-white/10 flex items-center justify-center hover:bg-white hover:text-charcoal transition-all duration-700"
                >
                  <Instagram size={18} />
                </a>
                <a
                  href={content.contact.whatsappGroup}
                  target="_blank"
                  rel="noreferrer"
                  className="w-10 h-10 rounded-full border border-white/10 flex items-center justify-center hover:bg-white hover:text-charcoal transition-all duration-700"
                >
                  <MessageCircle size={18} />
                </a>
              </div>
            </div>

            <div>
              <p className="font-sans text-[10px] font-bold uppercase tracking-[0.3em] text-white/10 mb-6">
                Explore
              </p>
              <ul className="space-y-4">
                {["Programs", "Leaderboard", "About", "Contact"].map((link) => (
                  <li key={link}>
                    <a
                      href={`#${link.toLowerCase()}`}
                      className="font-sans text-sm font-bold text-white/50 hover:text-vibrant-orange transition-colors tracking-tight italic"
                    >
                      {link}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          <div className="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6 text-center md:text-left">
            <p className="font-sans text-[9px] font-bold text-white/10 uppercase tracking-[0.3em]">
              © 2026 Urban Gliding Hyderabad. All rights reserved.
            </p>
            <div className="flex gap-8">
              <a
                href="#"
                className="font-sans text-[9px] font-bold text-white/10 uppercase tracking-[0.3em] hover:text-white transition-colors"
              >
                Terms
              </a>
              <a
                href="#"
                className="font-sans text-[9px] font-bold text-white/10 uppercase tracking-[0.3em] hover:text-white transition-colors"
              >
                Privacy
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
