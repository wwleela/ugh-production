/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "motion/react";
import heroImage from "./assets/images/regenerated_image_1778859272387.png";
import navLogo from "./assets/images/regenerated_image_1778859275982.png";
import footerLogo from "./assets/images/regenerated_image_1778859278835.png";
import { 
  Instagram, 
  Mail, 
  MessageCircle, 
  Phone, 
  ArrowRight, 
  Menu, 
  X,
  ExternalLink,
  ShieldCheck,
  Star,
  QrCode,
  Globe
} from "lucide-react";
import { 
  SignedIn, 
  SignedOut, 
  SignInButton, 
  UserButton 
} from "@clerk/clerk-react";
import { ContentData, Program } from "./types";

export default function App() {
  const [content, setContent] = useState<ContentData | null>(null);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  useEffect(() => {
    fetch("assets/content.json")
      .then((res) => res.json())
      .then((data) => setContent(data))
      .catch((err) => console.error("Failed to load content", err));
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
          <p className="font-mono text-xs uppercase tracking-widest text-deep-teal">Initializing Mission 2026...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen selection:bg-vibrant-orange selection:text-white overflow-x-hidden">
      {/* Google Analytics */}
      <script async src="https://www.googletagmanager.com/gtag/js?id=G-K2PYP4J4DZ"></script>
      <script>
        {`
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', 'G-K2PYP4J4DZ');
        `}
      </script>

      <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-700 ${
        scrolled ? "py-2 md:py-4" : "py-4 md:py-8"
      }`}>
        <div className="max-w-7xl mx-auto px-4 md:px-6">
          <div className={`flex items-center justify-between px-4 md:px-8 py-2 md:py-4 rounded-full transition-all duration-700 ${
            scrolled ? "glass-premium shadow-premium" : "bg-transparent"
          }`}>
              <div className="flex items-center gap-2 md:gap-3">
                <div className="w-9 h-9 md:w-10 md:h-10 rounded-full bg-white overflow-hidden border border-border-gray flex items-center justify-center shrink-0 shadow-sm">
                  <img src={navLogo} alt="Logo" className="w-full h-full object-cover p-1" />
                </div>
                <a href="./" className="font-display text-sm md:text-xl font-extrabold text-charcoal tracking-tighter whitespace-nowrap">URBAN GLIDING <span className="hidden sm:inline">HYDERABAD</span></a>
              </div>

            <div className="hidden md:flex items-center gap-6 lg:gap-10">
              <a href="#programs" className="font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] text-charcoal/60 hover:text-vibrant-orange transition-colors">Programs</a>
              <a href="#leaderboard" className="font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] text-charcoal/60 hover:text-vibrant-orange transition-colors">Leaderboard</a>
              <a href="#about" className="font-sans text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] text-charcoal/60 hover:text-vibrant-orange transition-colors">About</a>
              
              <div className="h-4 w-[1px] bg-charcoal/10"></div>

              <SignedOut>
                <SignInButton mode="modal">
                  <button className="font-sans text-[11px] font-bold uppercase tracking-[0.2em] text-charcoal hover:text-vibrant-orange transition-all">
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

            <button 
              className="md:hidden tap-target-min bg-vibrant-orange text-white rounded-full shadow-lg active:scale-95 transition-all flex items-center justify-center" 
              onClick={() => setIsMenuOpen(!isMenuOpen)}
            >
              {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
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
            className="fixed inset-0 z-[60] bg-white p-6 flex flex-col"
          >
            <div className="flex justify-between items-center mb-12">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-white overflow-hidden border border-border-gray flex items-center justify-center shrink-0">
                  <img src={navLogo} alt="Logo" className="w-full h-full object-cover p-1" />
                </div>
                <span className="font-display text-xl font-extrabold text-charcoal tracking-tighter">URBAN GLIDING</span>
              </div>
              <button 
                onClick={() => setIsMenuOpen(false)}
                className="w-12 h-12 bg-charcoal text-white rounded-full shadow-xl flex items-center justify-center"
              >
                <X size={20} />
              </button>
            </div>

            <div className="flex flex-col gap-6 flex-grow">
              {['Programs', 'Leaderboard', 'About'].map((item, i) => (
                <motion.a 
                  key={item}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.2 + i * 0.1 }}
                  href={`#${item.toLowerCase().replace(' ', '')}`}
                  onClick={() => setIsMenuOpen(false)}
                  className="font-display text-4xl font-black text-charcoal tracking-tighter hover:text-vibrant-orange transition-colors"
                >
                  {item}
                </motion.a>
              ))}
            </div>

            <div className="mt-auto space-y-6">
              <div className="h-px bg-border-gray" />
              <div className="flex justify-between items-center">
                 <div>
                   <p className="font-sans text-[10px] font-bold uppercase tracking-widest text-charcoal/40 mb-2">Primary Hub</p>
                   <p className="font-sans text-sm font-bold text-charcoal">Hyderabad, Telangana</p>
                 </div>
                 <div className="flex gap-4">
                    <div className="w-10 h-10 rounded-full border border-border-gray flex items-center justify-center text-charcoal">
                      <Instagram size={18} />
                    </div>
                    <div className="w-10 h-10 rounded-full border border-border-gray flex items-center justify-center text-charcoal">
                      <Globe size={18} />
                    </div>
                 </div>
              </div>
              <button 
                onClick={() => { handleTrial(); setIsMenuOpen(false); }}
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
        <section className="relative min-h-[85vh] flex items-center justify-center pt-24 pb-12 overflow-hidden bg-white">
          {/* Crisp Background Elements */}
          <div className="absolute inset-0 z-0 overflow-hidden pointer-events-none">
            <div className="absolute inset-0 opacity-[0.03]" style={{ backgroundImage: 'radial-gradient(#1a1a1a 1px, transparent 1px)', backgroundSize: '32px 32px' }} />
          </div>

          <div className="max-w-7xl mx-auto px-6 relative z-10 w-full grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
            <div className="text-left">
              <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
              >
                  <span className="inline-flex items-center gap-2 py-2 px-5 bg-deep-teal/5 text-deep-teal font-sans text-[10px] md:text-xs uppercase tracking-[0.3em] rounded-full mb-6 font-bold border border-deep-teal/10">
                  <span className="w-1.5 h-1.5 bg-deep-teal rounded-full animate-pulse" />
                  Elite Hyderabad Community
                </span>
                <h1 className="text-balance mb-6">
                  Command the <br />
                  <span className="text-vibrant-orange italic">Urban</span> Terrain.
                </h1>
              </motion.div>
              
              <motion.p 
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.1, duration: 1, ease: [0.16, 1, 0.3, 1] }}
                className="font-sans text-base md:text-lg text-charcoal/50 max-w-lg mb-10 leading-relaxed font-medium text-balance"
              >
                India's elite skating concierge. IOC-certified instructors delivering mastery directly to your doorstep.
              </motion.p>

              <motion.div 
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.2, duration: 1, ease: [0.16, 1, 0.3, 1] }}
                className="flex flex-col sm:flex-row gap-4"
              >
                <button 
                  onClick={handleTrial}
                  className="bg-vibrant-orange text-white font-sans text-xs md:text-sm uppercase tracking-[0.2em] px-8 md:px-10 py-5 rounded-full btn-premium shadow-xl shadow-vibrant-orange/10 font-bold flex items-center justify-center gap-3 group w-full sm:w-auto"
                >
                  Book Private Trial
                  <ArrowRight size={18} className="group-hover:translate-x-2 transition-transform duration-500" />
                </button>
                <a 
                  href="#programs"
                  className="bg-white text-charcoal font-sans text-xs md:text-sm uppercase tracking-[0.2em] px-8 md:px-10 py-5 rounded-full border border-border-gray hover:border-charcoal hover:bg-charcoal hover:text-white transition-all text-center font-bold shadow-soft flex items-center justify-center w-full sm:w-auto min-h-[52px]"
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
                <div className="relative w-full h-full rounded-[60px] border border-border-gray bg-white/40 backdrop-blur-xl p-10 md:p-12 shadow-xl overflow-hidden shadow-charcoal/5">
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
                  <p className="font-display text-3xl font-black text-deep-teal leading-none mb-1">160+</p>
                  <p className="font-sans text-[9px] uppercase tracking-widest text-charcoal/40 font-bold">Active Students</p>
                </motion.div>
                
                {/* floating badge */}
                <motion.div 
                  animate={{ y: [0, -8, 0] }}
                  transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
                  className="absolute -top-4 -right-4 glass-premium px-5 py-3 rounded-xl shadow-xl border border-border-gray flex items-center gap-2"
                >
                  <Star size={14} className="text-vibrant-orange fill-vibrant-orange" />
                  <p className="font-sans text-[9px] font-bold uppercase tracking-widest">IOC Certified</p>
                </motion.div>
              </motion.div>
            </div>
          </div>
        </section>

        {/* Training Modules */}
        <section id="programs" className="py-16 md:py-24 px-6 bg-white relative overflow-hidden">
          <div className="max-w-7xl mx-auto relative z-10">
            <div className="flex flex-col lg:flex-row lg:items-end justify-between mb-12 md:mb-16 gap-8">
              <div className="max-w-2xl">
                <span className="font-sans text-[10px] uppercase tracking-[0.4em] text-vibrant-orange mb-3 font-extrabold block">Expert Coaching</span>
                <h2 className="mb-4 text-charcoal">Active Modules</h2>
                <p className="font-sans text-base md:text-lg text-charcoal/40 font-medium text-balance">Specialized training systems designed for rapid progression across all skill levels.</p>
              </div>
              <div className="flex items-center gap-2 bg-light-sand p-1.5 rounded-full border border-border-gray w-full sm:w-auto overflow-x-auto no-scrollbar">
                <button className="px-6 py-2.5 rounded-full bg-charcoal text-white font-sans text-[10px] font-bold uppercase tracking-widest whitespace-nowrap min-h-[40px]">Monthly Mastery</button>
                <button className="px-6 py-2.5 rounded-full text-charcoal/40 font-sans text-[10px] font-bold uppercase tracking-widest hover:text-charcoal transition-colors whitespace-nowrap min-h-[40px]">Seasonal Camps</button>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-stretch">
              {(Object.values(content.programs) as Program[]).map((program, idx) => (
                <motion.div 
                  key={program.id}
                  initial={{ y: 50, opacity: 0 }}
                  whileInView={{ y: 0, opacity: 1 }}
                  viewport={{ once: true, margin: "-50px" }}
                  transition={{ delay: idx * 0.1, duration: 1, ease: [0.16, 1, 0.3, 1] }}
                  className={`card-premium p-6 md:p-10 flex flex-col relative group hover:-translate-y-4 hover:shadow-[0_40px_100px_-20px_rgba(0,97,95,0.1)] ${
                    program.id === "summer_camp" ? "bg-light-sand border-none" : ""
                  }`}
                >
                  <div className="flex justify-between items-start mb-8 md:mb-10">
                    <div className={`w-12 h-12 rounded-xl flex items-center justify-center border transition-all duration-700 ${
                      program.id === "summer_camp" ? "bg-vibrant-orange text-white border-vibrant-orange" : "bg-deep-teal/5 text-deep-teal border-deep-teal/10 group-hover:bg-deep-teal group-hover:text-white"
                    }`}>
                      {program.id === "summer_camp" ? <Star size={20} /> : <ShieldCheck size={20} />}
                    </div>
                    {program.badge && (
                      <span className="bg-charcoal text-[white] font-sans text-[8px] uppercase tracking-[0.2em] px-3 py-1 rounded-full font-bold">
                        {program.badge}
                      </span>
                    )}
                  </div>

                  <div className="mb-8 flex-grow">
                    <h3 className="mb-3 transition-colors group-hover:text-deep-teal text-2xl">{program.displayName}</h3>
                    <p className="font-sans text-[15px] text-charcoal/40 leading-relaxed font-medium">
                      {program.description}
                    </p>
                  </div>

                  <div className="space-y-3 mb-10">
                    {program.features.slice(0, 4).map((feature, fidx) => (
                      <div key={fidx} className="flex items-center gap-3">
                        <div className="w-1 h-1 rounded-full bg-charcoal/20 group-hover:bg-vibrant-orange transition-colors" />
                        <span className="text-[12px] font-bold text-charcoal/60 group-hover:text-charcoal transition-colors tracking-tight">{feature}</span>
                      </div>
                    ))}
                  </div>

                  <div className="mt-auto pt-8 border-t border-border-gray">
                    <div className="mb-6 flex items-baseline gap-2">
                       <span className="text-3xl font-display font-black text-charcoal tracking-tighter italic">₹{program.price.toLocaleString("en-IN")}</span>
                       <span className="text-[9px] text-charcoal/30 font-sans uppercase tracking-[0.2em] font-bold">/ {program.period}</span>
                    </div>
                    <button 
                      onClick={() => handleEnroll(program)}
                      className={`w-full font-sans text-[10px] uppercase tracking-[0.2em] py-3.5 rounded-full border transition-all duration-700 font-extrabold btn-premium
                        ${program.id === "summer_camp" ? "bg-deep-teal text-white border-deep-teal" : "bg-transparent border-charcoal text-charcoal hover:bg-charcoal hover:text-white"}
                      `}
                    >
                      {program.ctaText}
                    </button>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* Enrollment Protocol */}
        <section id="enroll" className="py-16 md:py-24 px-6 bg-light-sand relative overflow-hidden">
          <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
            <div className="relative z-10">
              <span className="font-sans text-[10px] uppercase tracking-[0.4em] text-vibrant-orange mb-4 font-extrabold block">Activation</span>
              <h2 className="mb-6 text-charcoal">Frictionless <br />Concierge Entry</h2>
              <p className="font-sans text-base md:text-lg text-charcoal/40 mb-10 leading-relaxed font-medium text-balance">Direct activation path via Coach Leela for precision tactical support. No complex forms—just pure service.</p>
              
              <div className="space-y-8">
                {content.paymentInstructions.steps.map((step, idx) => (
                  <motion.div 
                    key={idx}
                    initial={{ x: -20, opacity: 0 }}
                    whileInView={{ x: 0, opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ delay: idx * 0.1, duration: 1, ease: [0.16, 1, 0.3, 1] }}
                    className="flex gap-6 group"
                  >
                    <div className="font-display text-lg bg-charcoal text-white w-12 h-12 rounded-xl flex items-center justify-center shrink-0 font-black shadow-lg group-hover:bg-vibrant-orange transition-colors duration-500">
                      0{idx + 1}
                    </div>
                    <div className="pt-2">
                      <p className="font-sans text-[14px] md:text-base font-bold leading-relaxed text-charcoal/70">
                        {step.replace("{{price}}", "Your Module Fee")}
                      </p>
                    </div>
                  </motion.div>
                ))}
              </div>
            </div>

            <div className="relative">
              <motion.div 
                initial={{ y: 30, opacity: 0 }}
                whileInView={{ y: 0, opacity: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
                className="bg-white p-6 md:p-16 rounded-[40px] md:rounded-[50px] shadow-xl border border-border-gray text-center relative overflow-hidden"
              >
                <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-deep-teal to-vibrant-orange" />
                <div className="w-14 h-14 md:w-16 md:h-16 bg-deep-teal/5 rounded-xl md:rounded-2xl flex items-center justify-center text-deep-teal mx-auto mb-8">
                  <QrCode size={28} className="md:w-8 md:h-8" />
                </div>
                <h3 className="font-display text-lg md:text-xl font-bold mb-3 tracking-tighter uppercase tracking-[0.2em]">Authorized Gateway</h3>
                <p className="font-sans text-[9px] text-charcoal/30 uppercase tracking-[0.3em] font-bold mb-6">Verification: ~30min</p>
                
                <div className="px-4 py-4 rounded-xl bg-light-sand/40 border border-border-gray mb-8 group transition-all hover:bg-white hover:shadow-lg overflow-hidden text-ellipsis">
                  <span className="font-display text-xs md:text-lg font-extrabold text-deep-teal select-all cursor-pointer tracking-tighter block truncate">
                    {content.paymentInstructions.upiId}
                  </span>
                </div>

                <a 
                  href="upi://pay?pa=worldwide.leelamadhav@oksbi&pn=UGH%20Hyderabad&cu=INR"
                  className="w-full inline-flex md:w-auto bg-vibrant-orange text-white px-8 md:px-12 py-4 rounded-full font-sans text-[10px] uppercase tracking-[0.3em] font-extrabold flex items-center justify-center gap-3 hover:bg-charcoal transition-all duration-700 shadow-xl shadow-vibrant-orange/10 group btn-premium min-h-[52px]"
                >
                  Initiate Secure Pay
                  <ArrowRight size={18} className="group-hover:translate-x-2 transition-transform duration-500 hidden sm:block" />
                </a>

                <div className="mt-12 flex items-center justify-center gap-2">
                  <div className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse" />
                  <p className="font-sans text-[10px] font-bold uppercase tracking-widest text-charcoal/40">Secure Transaction Channel</p>
                </div>
              </motion.div>
              
              {/* Decorative side element */}
              <div className="absolute -right-20 top-1/2 -translate-y-1/2 w-40 h-80 bg-vibrant-orange/5 blur-[100px] pointer-events-none" />
            </div>
          </div>
        </section>

        {/* Leaderboard Section */}
        <section id="leaderboard" className="py-16 md:py-24 px-6 bg-white overflow-hidden text-center">
          <div className="max-w-4xl mx-auto">
            <div className="mb-12 md:mb-16 px-4">
              <span className="font-sans text-[10px] uppercase tracking-[0.4em] text-vibrant-orange mb-4 font-extrabold block">Community Impact</span>
              <h2 className="mb-4 text-charcoal">UGH Leaderboard</h2>
              <p className="font-sans text-base md:text-lg text-charcoal/40 font-medium text-balance">Live performance metrics of talented skaters across our training modules.</p>
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
              <div className="divide-y divide-border-gray">
                {content.leaderboard.rankings.map((rank, idx) => (
                  <motion.div 
                    key={idx}
                    initial={{ opacity: 0, y: 10 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ delay: idx * 0.04 }}
                    className="px-6 md:px-10 py-4 md:py-6 flex items-center justify-between hover:bg-light-sand transition-all duration-500 group"
                  >
                    <div className="flex items-center gap-4 md:gap-10">
                      <div className="relative shrink-0">
                        <span className={`font-display text-xl md:text-2xl font-black ${idx < 3 ? "text-vibrant-orange" : "text-charcoal/5"} transition-colors group-hover:text-vibrant-orange w-6 md:w-10 block`}>
                          0{idx + 1}
                        </span>
                      </div>
                      <div>
                        <p className="font-display text-lg md:text-xl font-bold tracking-tighter text-charcoal mb-0.5 md:mb-1 group-hover:translate-x-1 transition-transform duration-500">{rank.name}</p>
                        <div className={`inline-flex items-center gap-2 px-2 py-0.5 rounded-full border font-sans text-[8px] uppercase tracking-widest font-bold ${
                          rank.change === "up" ? "bg-green-500/5 border-green-500/10 text-green-600" : rank.change === "down" ? "bg-red-500/5 border-red-500/10 text-red-600" : "bg-gray-50 border-gray-100 text-gray-400"
                        }`}>
                          {rank.change === "up" ? <ArrowRight size={10} className="-rotate-45" /> : rank.change === "down" ? <ArrowRight size={10} className="rotate-45" /> : <div className="w-2 h-0.5 bg-gray-400" />}
                          {rank.change === "stable" ? "Constant" : rank.change.toUpperCase()}
                        </div>
                      </div>
                    </div>
                    <div className="text-right shrink-0">
                      <p className="font-display text-xl md:text-3xl font-black text-deep-teal tracking-tighter transition-all duration-700 group-hover:scale-105">{rank.points.toLocaleString()}</p>
                    </div>
                  </motion.div>
                ))}
              </div>
            </div>
            
            <div className="mt-10 flex justify-center items-center gap-3">
              <span className="w-1.5 h-1.5 rounded-full bg-vibrant-orange animate-pulse" />
              <p className="font-sans text-[9px] font-extrabold uppercase tracking-widest text-charcoal/20">Sync Cycle: 24h Protocol</p>
            </div>
          </div>
        </section>

        {/* About Section */}
        <section id="about" className="py-16 md:py-24 px-6 bg-off-white relative overflow-hidden">
          <div className="max-w-7xl mx-auto relative z-10">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-20 items-start mb-16 lg:mb-24">
            <div className="lg:col-span-1">
                <span className="font-sans text-[10px] uppercase tracking-[0.4em] text-vibrant-orange mb-4 font-extrabold block">Framework</span>
                <h2 className="mb-6 text-charcoal">About UGH</h2>
                <p className="font-sans text-lg md:text-2xl font-medium text-charcoal/40 leading-[1.5] text-balance">
                  {content.about.description}
                </p>
              </div>
              <div className="hidden lg:block relative">
                <div className="aspect-[4/3] rounded-[40px] bg-charcoal/5 border border-border-gray overflow-hidden flex items-center justify-center p-16 opacity-30">
                  <img src={heroImage} alt="UGH Branding" className="w-full h-full object-contain grayscale" />
                </div>
              </div>
            </div>

            <div className="mb-20 lg:mb-24">
              <div className="flex flex-col md:flex-row md:items-center justify-between mb-10 md:mb-12 gap-4">
                 <h3 className="tracking-tighter">Our <span className="text-vibrant-orange italic">Curriculum</span></h3>
                 <div className="h-px bg-border-gray flex-grow mx-8 hidden lg:block"></div>
                 <div className="bg-charcoal px-4 py-1.5 rounded-full text-white font-sans text-[8px] font-bold uppercase tracking-widest self-start md:self-auto">v2.6 Stable</div>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {content.about.curriculum.map((item, idx) => (
                  <motion.div 
                    key={idx}
                    initial={{ y: 20, opacity: 0 }}
                    whileInView={{ y: 0, opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ delay: idx * 0.1, duration: 1, ease: [0.16, 1, 0.3, 1] }}
                    className="card-premium p-10 relative overflow-hidden group hover:-translate-y-1.5"
                  >
                    <div className="w-10 h-10 rounded-xl bg-charcoal/5 flex items-center justify-center text-charcoal mb-6 group-hover:bg-vibrant-orange group-hover:text-white transition-all duration-700">
                      <ShieldCheck size={18} />
                    </div>
                    <span className="font-sans text-[9px] uppercase tracking-[0.4em] text-charcoal/20 mb-4 block font-bold">MODULE-0{idx+1}</span>
                    <h4 className="mb-6 leading-tight text-xl">{item.title}</h4>
                    <ul className="space-y-3">
                      {item.points.map((p, pidx) => (
                        <li key={pidx} className="flex items-start gap-3 text-[13px] font-bold leading-relaxed text-charcoal/50 group-hover:text-charcoal transition-colors">
                          <div className="w-1.5 h-1.5 rounded-full bg-vibrant-orange mt-1.5 shrink-0" />
                          <span>{p}</span>
                        </li>
                      ))}
                    </ul>
                  </motion.div>
                ))}
              </div>
            </div>
            
            <motion.div 
              initial={{ opacity: 0 }}
              whileInView={{ opacity: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 1.5, ease: [0.16, 1, 0.3, 1] }}
              className="p-10 md:p-24 bg-charcoal rounded-[40px] md:rounded-[60px] text-white shadow-xl relative overflow-hidden group text-center"
            >
               <div className="absolute inset-0 opacity-10 pointer-events-none bg-[radial-gradient(#ffffff_1px,transparent_1px)] [background-size:60px_60px]"></div>
               <div className="relative z-10 max-w-3xl mx-auto">
                  <h3 className="mb-8 md:mb-10 italic leading-[1] tracking-tighter text-balance text-white md:text-5xl">
                    &quot;We don&apos;t just glide; <br />
                    we command the <span className="text-vibrant-orange">urban</span> terrain.&quot;
                  </h3>
                  <p className="font-sans text-[10px] md:text-xs uppercase tracking-[0.4em] text-white/30 font-extrabold mb-8">- LEELA MADHAV, IOC CHIEF</p>
                  <button 
                    onClick={handleTrial}
                    className="bg-vibrant-orange text-white font-sans text-[10px] md:text-xs uppercase tracking-[0.25em] px-10 md:px-14 py-4 md:py-5 rounded-full font-extrabold hover:scale-105 transition-all duration-700 shadow-xl shadow-vibrant-orange/30 btn-premium mx-auto"
                  >
                    Elevate Your Skillset
                  </button>
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
                  <img src={footerLogo} alt="Logo" className="w-full h-full object-cover p-1" />
                </div>
                <span className="font-display text-xl md:text-2xl font-extrabold tracking-tighter">URBAN GLIDING HYDERABAD</span>
              </div>
              <p className="font-sans text-base md:text-lg text-white/40 max-w-sm leading-relaxed font-medium mb-8">
                The leading skating community in Hyderabad, India. Elite doorstep coaching for children and adults.
              </p>
              <div className="flex gap-5">
                <a href="https://www.instagram.com/urbangliding.hyd?igsh=MWJubGk3OG42eHI2Zw==" target="_blank" rel="noreferrer" className="w-10 h-10 rounded-full border border-white/10 flex items-center justify-center hover:bg-white hover:text-charcoal transition-all duration-700">
                  <Instagram size={18} />
                </a>
                <a href="#" className="w-10 h-10 rounded-full border border-white/10 flex items-center justify-center hover:bg-white hover:text-charcoal transition-all duration-700">
                  <Globe size={18} />
                </a>
                <a href={`mailto:${content.contact.email}`} className="w-10 h-10 rounded-full border border-white/10 flex items-center justify-center hover:bg-white hover:text-charcoal transition-all duration-700">
                  <Mail size={18} />
                </a>
                <a href={content.contact.whatsappGroup} target="_blank" rel="noreferrer" className="w-10 h-10 rounded-full border border-white/10 flex items-center justify-center hover:bg-white hover:text-charcoal transition-all duration-700">
                  <MessageCircle size={18} />
                </a>
              </div>
            </div>
            
            <div>
              <p className="font-sans text-[10px] font-bold uppercase tracking-[0.3em] text-white/10 mb-6">Explore</p>
              <ul className="space-y-4">
                {['Programs', 'Leaderboard', 'About', 'Contact'].map(link => (
                  <li key={link}>
                    <a href={`#${link.toLowerCase()}`} className="font-sans text-sm font-bold text-white/50 hover:text-vibrant-orange transition-colors tracking-tight italic">
                      {link}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          </div>
          
          <div className="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6 text-center md:text-left">
            <p className="font-sans text-[9px] font-bold text-white/10 uppercase tracking-[0.3em]">© 2026 Urban Gliding Hyderabad. Professional Coaching.</p>
            <div className="flex gap-8">
              <a href="#" className="font-sans text-[9px] font-bold text-white/10 uppercase tracking-[0.3em] hover:text-white transition-colors">Terms</a>
              <a href="#" className="font-sans text-[9px] font-bold text-white/10 uppercase tracking-[0.3em] hover:text-white transition-colors">Privacy</a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
