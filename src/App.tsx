/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "motion/react";
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
  QrCode
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
    <div className="min-h-screen selection:bg-burnt-orange selection:text-white">
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

      {/* Navigation */}
      <nav className="sticky top-0 z-50 bg-vintage-cream/80 backdrop-blur-md border-b-2 border-keyline transition-all">
        <div className="max-w-6xl mx-auto px-4 md:px-6 h-12 md:h-14 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <a href="./" className="font-serif text-base md:text-lg font-bold text-deep-teal hover:scale-105 transition-transform tracking-tight">UGH</a>
          </div>

          <div className="hidden md:flex items-center gap-5 lg:gap-6">
            <a href="#programs" className="font-serif text-xs lg:text-sm font-semibold hover:text-burnt-orange transition-colors tracking-wide">Programs</a>
            <a href="#leaderboard" className="font-serif text-xs lg:text-sm font-semibold hover:text-burnt-orange transition-colors tracking-wide">Summer Camp</a>
            <a href="#about" className="font-serif text-xs lg:text-sm font-semibold hover:text-burnt-orange transition-colors tracking-wide">About</a>
            
            <div className="h-5 w-[1px] bg-keyline/20"></div>

            <SignedOut>
              <SignInButton mode="modal">
                <button className="font-mono text-[8px] uppercase tracking-widest px-3 py-1.5 rounded-full border-2 border-keyline hover:bg-vintage-cream transition-all font-bold">
                  Sign In
                </button>
              </SignInButton>
            </SignedOut>
            <SignedIn>
              <UserButton afterSignOutUrl="/" />
            </SignedIn>

            <button 
              onClick={handleTrial}
              className="bg-burnt-orange text-white font-mono text-[8px] lg:text-[9px] uppercase tracking-widest px-4 lg:px-5 py-2 lg:py-2.5 rounded-full btn-tactical"
            >
              Secure Your Spot
            </button>
          </div>

          <button 
            className="md:hidden p-2 bg-burnt-orange text-white rounded-xl border-2 border-keyline shadow-[3px_3px_0_#1c1c18] active:translate-x-0.5 active:translate-y-0.5 active:shadow-none" 
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>
      </nav>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isMenuOpen && (
          <motion.div 
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="fixed inset-0 z-40 bg-vintage-cream/98 backdrop-blur-2xl md:hidden flex flex-col items-center justify-center p-6 border-b-4 border-keyline"
          >
            <div className="flex flex-col gap-8 items-center w-full max-w-sm">
              <a href="#programs" className="font-serif text-3xl font-bold tracking-[1px] hover:text-burnt-orange" onClick={() => setIsMenuOpen(false)}>Programs</a>
              <a href="#leaderboard" className="font-serif text-3xl font-bold tracking-[1px] hover:text-burnt-orange" onClick={() => setIsMenuOpen(false)}>Summer Camp</a>
              <a href="#about" className="font-serif text-3xl font-bold tracking-[1px] hover:text-burnt-orange" onClick={() => setIsMenuOpen(false)}>About</a>
              
              <div className="w-full h-[1px] bg-keyline/10 my-4"></div>

              <SignedOut>
                <SignInButton mode="modal">
                  <button className="w-full font-mono text-sm uppercase tracking-widest py-4 rounded-full border-2 border-keyline font-bold" onClick={() => setIsMenuOpen(false)}>
                    Sign In
                  </button>
                </SignInButton>
              </SignedOut>
              <SignedIn>
                <div className="flex items-center gap-4">
                  <UserButton afterSignOutUrl="/" />
                  <span className="font-mono text-xs uppercase tracking-widest font-bold">Account</span>
                </div>
              </SignedIn>

              <button 
                onClick={() => { handleTrial(); setIsMenuOpen(false); }}
                className="w-full bg-burnt-orange text-white font-mono text-sm uppercase tracking-widest py-5 rounded-full btn-tactical"
              >
                Secure Your Spot
              </button>

              <button 
                onClick={() => setIsMenuOpen(false)}
                className="mt-6 p-4 text-keyline/40 font-mono text-[10px] uppercase tracking-widest flex items-center gap-2"
              >
                <X size={16} /> Close Menu
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      <main>
        {/* Hero Section */}
        <section className="relative pt-8 md:pt-10 pb-12 md:pb-14 px-6 overflow-hidden">
          <div className="max-w-4xl mx-auto flex flex-col items-center text-center">
            <motion.div 
              initial={{ scale: 0.9, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ duration: 0.8 }}
              className="relative w-24 h-24 md:w-32 lg:w-40 md:h-32 lg:h-40 mb-5 md:mb-6"
            >
              <div className="absolute inset-0 bg-deep-teal rounded-full translate-x-1.5 translate-y-1.5 md:translate-x-3 md:translate-y-3 lg:translate-x-4 lg:translate-y-4" />
              <div className="relative w-full h-full rounded-full border-2 border-keyline overflow-hidden bg-white shadow-lg">
                <img 
                  src="https://lh3.googleusercontent.com/aida/ADBb0ui6K99eXFqSU6cl268hCSbrgfOAXdOfBdCrVFkqqH-6NvZ4N66OTbJwgkfodGmPiTaysIlbLIxZH6NwPsgiC7h5zmXSY5Q3xmzi1-fQcJlNM7xFAhSUINTvlVFEvooi8G7CNHYKsm1IC7MCd0MJlpB0AJAhRlkP1QywmITpc9gBQTKRoLOWseAxZWByrtIltlr2fqCAkPpqYij0TbAUoKPU2e0cGiyKKXr9Vv9pfZ-hqwUcXKydHBzCARlKTLW7vtDhDIE05btu" 
                  alt="UGH Logo" 
                  className="w-full h-full object-cover p-2.5"
                />
              </div>
            </motion.div>

            <motion.h1 
              initial={{ y: 20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.2 }}
              className="font-serif text-xl sm:text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-3 max-w-2xl tracking-tight leading-[1.05]"
            >
              Master the concrete waves of <span className="text-deep-teal">Hyderabad.</span>
            </motion.h1>

            <motion.p 
              initial={{ y: 20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.4 }}
              className="font-sans text-xs md:text-sm lg:text-base text-keyline/70 max-w-lg mb-5 md:mb-8 leading-relaxed"
            >
              Skateboarding is more than a sport; it&apos;s a tactical dialogue with urban architecture. We don&apos;t just teach skating; we master the concrete waves of Hyderabad.
            </motion.p>

            <motion.div
              initial={{ y: 20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.6 }}
              className="flex flex-col sm:flex-row gap-3 w-full sm:w-auto"
            >
              <button 
                onClick={handleTrial}
                className="bg-burnt-orange text-white font-mono text-[9px] sm:text-[10px] uppercase tracking-widest px-6 md:px-8 py-3 md:py-3.5 rounded-full btn-tactical shadow-lg w-full sm:w-auto font-bold"
              >
                SECURE YOUR SPOT
              </button>
              <a 
                href="#programs"
                className="bg-white text-keyline font-mono text-[9px] sm:text-[10px] uppercase tracking-widest px-6 md:px-8 py-3 md:py-3.5 rounded-full border-2 border-keyline hover:bg-vintage-cream transition-all text-center w-full sm:w-auto font-bold"
              >
                VIEW MODULES
              </a>
            </motion.div>
          </div>
          
          {/* Decorative Elements */}
          <div className="absolute top-1/2 left-0 -translate-y-1/2 -z-10 opacity-5 sm:opacity-8 translate-x-[-20%]">
            <div className="w-[180px] h-[180px] border-2 border-deep-teal rounded-full scale-150" />
          </div>
          <div className="absolute top-1/3 right-0 -translate-y-1/2 -z-10 opacity-5 sm:opacity-8 translate-x-[20%]">
            <div className="w-[120px] h-[120px] border-2 border-burnt-orange rounded-full scale-125" />
          </div>
        </section>

        {/* Training Modules */}
        <section id="programs" className="py-10 md:py-14 px-6 bg-white border-y-2 border-keyline relative">
          <div className="max-w-4xl mx-auto">
            <div className="flex flex-col items-center mb-6 md:mb-8 text-center">
              <span className="font-mono text-[8px] md:text-[9px] uppercase tracking-[2px] text-burnt-orange mb-2 font-bold">Tactical Training Ops</span>
              <h2 className="font-serif text-xl md:text-3xl font-bold mb-2 tracking-tight">Active Modules</h2>
              <div className="w-12 h-0.5 bg-keyline rounded-full" />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 lg:gap-6 items-stretch">
              {(Object.values(content.programs) as Program[]).map((program, idx) => (
                <motion.div 
                  key={program.id}
                  initial={{ y: 20, opacity: 0 }}
                  whileInView={{ y: 0, opacity: 1 }}
                  viewport={{ once: true, margin: "-100px" }}
                  transition={{ delay: idx * 0.1, duration: 0.6 }}
                  className={`bg-vintage-cream card-tactical p-5 md:p-6 flex flex-col relative overflow-hidden group hover:-translate-y-1 transition-all duration-500 ease-out fill-mode-forwards ${
                    program.id === "summer_camp" 
                      ? "border-burnt-orange ring-4 ring-burnt-orange/10 md:-translate-y-2 shadow-[8px_8px_0_#1c1c18]" 
                      : program.badge ? "border-deep-teal shadow-[6px_6px_0_#1c1c18]" : ""
                  }`}
                >
                  {program.id === "summer_camp" && (
                    <div className="absolute -right-12 -top-12 w-24 h-24 bg-burnt-orange rotate-45 flex items-end justify-center pb-2 z-20 shadow-lg">
                      <Star size={12} className="text-white animate-pulse" />
                    </div>
                  )}
                  <div className="absolute top-5 right-5 font-mono text-[8px] text-keyline/30 uppercase tracking-widest font-bold">
                    MOD-ID:{program.id.toUpperCase().substring(0, 3)}
                  </div>

                  <div className="border-b border-keyline/10 pb-5 mb-5">
                    <h3 className="font-serif text-lg md:text-xl font-bold text-deep-teal mb-2 leading-tight">{program.displayName}</h3>
                    {program.badge && (
                      <div className="flex items-center gap-2">
                        <span className="bg-burnt-orange text-white font-mono text-[8px] uppercase tracking-widest px-2.5 py-1 rounded-full border border-keyline font-bold">
                          {program.badge}
                        </span>
                      </div>
                    )}
                  </div>

                  <p className="font-sans text-[13px] text-keyline/70 mb-6 flex-grow leading-relaxed">
                    {program.description}
                  </p>

                  <div className="bg-white/50 rounded-[24px] p-4 mb-6 border border-keyline/5">
                    <p className="font-mono text-[9px] uppercase tracking-widest text-keyline/40 mb-2 font-bold">Objectives</p>
                    <ul className="space-y-2.5">
                      {program.features.map((feature, fidx) => (
                        <li key={fidx} className="flex items-start gap-2 text-[12px] font-bold leading-snug">
                          <ShieldCheck size={16} className="text-deep-teal shrink-0 mt-0.5" />
                          <span>{feature}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

                  <div className="mt-auto">
                    <div className="mb-5 flex items-end gap-1.5 px-1">
                       <span className="text-[10px] text-keyline/40 font-mono uppercase tracking-[2px] mb-1 font-bold">Fee:</span>
                       <span className="font-serif text-2xl font-bold italic text-deep-teal leading-none">₹{program.price.toLocaleString("en-IN")}</span>
                       <span className="text-[9px] text-keyline/40 font-mono italic mb-1">/{program.period}</span>
                    </div>
                    <button 
                      onClick={() => handleEnroll(program)}
                      className={`w-full font-mono text-[9px] uppercase tracking-[3px] py-3 rounded-lg border-2 border-keyline transition-all font-bold shadow-[4px_4px_0_#1c1c18] active:translate-y-1 active:shadow-none
                        ${program.badge ? "bg-burnt-orange text-white hover:bg-burnt-orange/90" : "bg-white text-keyline hover:bg-vintage-cream"}
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
        <section id="enroll" className="py-10 md:py-14 px-6 bg-vintage-cream relative overflow-hidden">
          <div className="max-w-3xl mx-auto bg-white border-2 border-keyline rounded-collector p-4 md:p-8 lg:p-10 shadow-[6px_6px_0_#1c1c18] relative z-10">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-5 mb-6">
              <div className="flex items-center gap-3">
                <div className="bg-burnt-orange p-2.5 rounded-lg border border-keyline text-white shadow-md">
                  <Star size={20} />
                </div>
                <div>
                  <span className="font-mono text-[8px] uppercase tracking-[1.5px] text-burnt-orange font-bold">Step-by-Step</span>
                  <h2 className="font-serif text-xl md:text-2xl font-bold tracking-tight">Enrollment Protocol</h2>
                </div>
              </div>
              <div className="hidden lg:block bg-vintage-cream px-5 py-3 rounded-xl border border-keyline font-mono text-[9px] uppercase tracking-widest font-bold">
                Verification Time: EST 30m
              </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-5 gap-8 lg:gap-12">
              <div className="lg:col-span-3">
                <p className="font-sans text-sm md:text-base text-keyline/70 mb-8 italic border-l-4 border-burnt-orange pl-5 leading-relaxed">
                  Manual verification ensures Coach Leela handles every enrollment with high-tactical personalized attention.
                </p>
                <div className="space-y-6">
                  {content.paymentInstructions.steps.map((step, idx) => (
                    <div key={idx} className="flex gap-4 group">
                      <div className="font-mono text-sm bg-vintage-cream text-burnt-orange border-2 border-keyline w-10 h-10 rounded-full flex items-center justify-center shrink-0 font-extrabold shadow-[3px_3px_0_#1c1c18] group-hover:scale-105 transition-transform">
                        {idx + 1}
                      </div>
                      <div className="pt-2">
                        <p className="font-sans text-[13px] md:text-sm font-bold leading-relaxed text-keyline/90">
                          {step.replace("{{price}}", "Calculated")}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              <div className="lg:col-span-2 space-y-6">
                <div className="bg-vintage-cream border-2 border-keyline rounded-collector p-6 md:p-8 flex flex-col justify-center items-center text-center relative overflow-hidden group shadow-inner-xl max-w-full">
                  <div className="absolute top-0 left-0 w-full h-1 bg-burnt-orange/10"></div>
                  <span className="font-mono text-[10px] uppercase tracking-[3px] text-keyline/50 mb-4 font-bold">Authorized UPI ID</span>
                  <div className="bg-white px-4 py-2 rounded-lg border border-keyline mb-6 w-full">
                    <span className="font-serif text-base md:text-lg lg:text-xl font-bold text-deep-teal select-all cursor-pointer break-all tracking-tighter block leading-tight overflow-wrap-anywhere">
                      {content.paymentInstructions.upiId}
                    </span>
                  </div>

                  <a 
                    href="upi://pay?pa=worldwide.leelamadhav@oksbi&pn=UGH%20Hyderabad&cu=INR"
                    className="w-full mb-6 bg-burnt-orange text-white border border-keyline px-5 py-4 rounded-xl font-mono text-[10px] md:text-xs uppercase tracking-widest font-bold flex items-center justify-center gap-2.5 hover:bg-deep-teal transition-all shadow-[4px_4px_0_#1c1c18] active:translate-y-1 active:shadow-none hover:scale-[1.02] animate-pulse-subtle"
                  >
                    TAP TO PAY (GPAY / PHONEPE)
                  </a>

                  <div className="grid grid-cols-1 w-full gap-3">
                    <div className="p-4 bg-white border border-keyline rounded-2xl shadow-sm text-center">
                      <p className="text-[9px] font-mono text-keyline/40 uppercase tracking-[2px] mb-1 font-bold">Response Window</p>
                      <p className="font-serif text-lg font-bold text-deep-teal">~30 Minutes</p>
                    </div>
                    <div className="p-2.5 bg-deep-teal/5 border border-deep-teal/10 rounded-lg text-center">
                       <p className="text-[8px] text-deep-teal/60 font-mono tracking-[2px] uppercase font-bold">
                        Systems active: 06:00 - 22:00 IST
                      </p>
                    </div>
                  </div>
                </div>
                
                <div className="text-center font-mono text-[8px] text-keyline/40 uppercase tracking-widest leading-relaxed px-4">
                  Transaction encryption managed by UPI standard protocol.<p className="mt-1">Screenshot receipt must be sent to Coach for activation.</p>
                </div>
              </div>
            </div>
          </div>
          
          {/* Background noise/pattern for tactical feel */}
          <div className="absolute inset-0 opacity-[0.03] pointer-events-none -z-10 bg-[radial-gradient(#00615f_1.5px,transparent_1.5px)] [background-size:24px_24px]"></div>
        </section>

        {/* Leaderboard Section */}
        <section id="leaderboard" className="py-12 md:py-14 px-6 bg-white border-y-2 border-keyline overflow-hidden">
          <div className="max-w-xl mx-auto">
            <div className="mb-8 md:mb-10 text-center">
              <span className="font-mono text-[8px] md:text-[9px] uppercase tracking-[3px] text-burnt-orange mb-2 font-bold block">Mission Rankings</span>
              <h2 className="font-serif text-xl md:text-3xl font-bold mb-3 tracking-tight">Summer Camp 2026</h2>
              <div className="inline-flex items-center gap-2 bg-vintage-cream px-4 py-1 rounded-full border border-keyline">
                <span className="w-1.5 h-1.5 bg-green-500 rounded-full animate-pulse"></span>
                <p className="font-mono text-[8px] text-keyline/70 uppercase tracking-widest font-bold">
                  Last Tactical Update: {new Date(content.leaderboard.lastUpdated).toLocaleDateString('en-IN', { day: '2-digit', month: 'short' })}
                </p>
              </div>
            </div>

            <div className="card-tactical overflow-hidden bg-white shadow-[6px_6px_0_#1c1c18] border-2 border-keyline rounded-collector">
              <div className="border-b border-keyline bg-deep-teal text-white px-5 md:px-8 py-3 flex justify-between items-center font-mono text-[9px] md:text-[10px] uppercase tracking-widest font-bold">
                <div className="flex items-center gap-2.5">
                  <ShieldCheck size={14} />
                  <span>Skater operative</span>
                </div>
                <span>Mission XP</span>
              </div>
              <div className="divide-y divide-keyline/5">
                {content.leaderboard.rankings.map((rank, idx) => (
                  <div key={idx} className="px-5 md:px-8 py-5 md:py-6 flex items-center justify-between hover:bg-vintage-cream/50 transition-all group">
                    <div className="flex items-center gap-5 md:gap-8">
                      <div className="relative">
                        <span className={`font-mono text-xl md:text-2xl font-black ${idx < 3 ? "text-burnt-orange" : "text-keyline/10"} transition-colors group-hover:text-burnt-orange w-8 md:w-12 inline-block`}>
                          #{idx + 1}
                        </span>
                      </div>
                      <div>
                        <p className="font-serif text-lg md:text-xl font-bold tracking-tight text-deep-teal mb-1">{rank.name}</p>
                        <div className={`inline-flex items-center gap-1.5 px-1.5 py-0.5 rounded-full border font-mono text-[8px] uppercase tracking-widest font-bold ${
                          rank.change === "up" ? "bg-green-50 border-green-100 text-green-700" : rank.change === "down" ? "bg-red-50 border-red-100 text-red-700" : "bg-gray-50 border-gray-100 text-gray-500"
                        }`}>
                          {rank.change === "up" ? <ArrowRight size={10} className="-rotate-45" /> : rank.change === "down" ? <ArrowRight size={10} className="rotate-45" /> : <div className="w-2 h-0.5 bg-gray-400" />}
                          {rank.change}
                        </div>
                      </div>
                    </div>
                    <div className="text-right">
                      <p className="font-mono text-xl md:text-2xl font-black text-keyline tracking-tighter">{rank.points.toLocaleString()}</p>
                      <p className="font-mono text-[8px] text-keyline/30 uppercase tracking-[2px] font-bold">XP earned</p>
                    </div>
                  </div>
                ))}
              </div>
              <div className="bg-deep-teal/5 p-5 text-center border-t-2 border-keyline/10">
                 <p className="font-mono text-[8px] text-keyline/40 uppercase tracking-widest font-bold">
                   End of current rankings.
                 </p>
              </div>
            </div>
          </div>
        </section>

        {/* About Section */}
        <section id="about" className="py-10 md:py-14 px-6 bg-vintage-cream border-b-2 border-keyline relative overflow-hidden">
          <div className="max-w-3xl mx-auto relative z-10">
            <div className="mb-10 md:mb-12">
              <span className="font-mono text-[8px] md:text-[9px] uppercase tracking-[2px] text-burnt-orange mb-2 font-bold block">Conceptual Framework</span>
              <h2 className="font-serif text-2xl md:text-4xl font-bold mb-3 tracking-tight text-deep-teal">About UGH</h2>
              <p className="font-sans text-xs md:text-sm text-keyline/80 leading-relaxed italic border-l-4 border-burnt-orange pl-4 md:pl-5 max-w-2xl">
                {content.about.description}
              </p>
            </div>

            <div className="mb-12">
              <div className="flex items-center gap-3 mb-8">
                 <div className="bg-keyline p-2.5 rounded-lg text-white">
                   <ShieldCheck size={20} />
                 </div>
                 <h3 className="font-serif text-xl md:text-2xl font-bold tracking-tight">2026 <span className="text-burnt-orange">Curriculum</span></h3>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 lg:gap-6">
                {content.about.curriculum.map((item, idx) => (
                  <motion.div 
                    key={idx}
                    initial={{ y: 30, opacity: 0 }}
                    whileInView={{ y: 0, opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ delay: idx * 0.1 }}
                    className="card-tactical p-6 md:p-8 relative overflow-hidden group bg-white shadow-[6px_6px_0_#1c1c18] border-2 border-keyline rounded-collector"
                  >
                    <div className="absolute top-0 left-0 w-full h-1.5 bg-deep-teal/10 group-hover:bg-deep-teal transition-all duration-500"></div>
                    <span className="font-mono text-[8px] uppercase tracking-widest text-deep-teal/40 mb-3 block font-bold">OP-0{idx+1}</span>
                    <h4 className="font-serif text-base md:text-lg font-bold mb-4 leading-tight">{item.title}</h4>
                    <ul className="space-y-3">
                      {item.points.map((p, pidx) => (
                        <li key={pidx} className="flex items-start gap-2.5 text-[12px] font-bold leading-snug">
                          <ArrowRight size={14} className="text-burnt-orange shrink-0 mt-1 transition-transform group-hover:translate-x-1" />
                          <span className="text-keyline/90">{p}</span>
                        </li>
                      ))}
                    </ul>
                  </motion.div>
                ))}
              </div>
            </div>
            
            <div className="mt-14 p-6 md:p-10 bg-deep-teal rounded-collector border-2 border-keyline text-white shadow-lg relative overflow-hidden">
               <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-6 text-center md:text-left">
                  <div className="max-w-md">
                    <h3 className="font-serif text-lg md:text-xl font-bold mb-3 italic leading-tight">&quot;We don&apos;t just glide; we command the urban terrain.&quot;</h3>
                    <p className="font-mono text-[9px] uppercase tracking-widest text-white/50 font-bold">- Leela Madhav</p>
                  </div>
                  <button 
                    onClick={handleTrial}
                    className="bg-burnt-orange text-white font-mono text-[9px] uppercase tracking-widest px-6 py-3 rounded-full border border-white font-bold hover:scale-105 active:scale-95 transition-all shadow-md shrink-0"
                  >
                    JOIN THE ELITE
                  </button>
               </div>
            </div>
          </div>
          
          {/* Decorative grid pattern */}
          <div className="absolute inset-x-0 bottom-0 h-64 bg-[linear-gradient(to_bottom,transparent,rgba(0,97,95,0.05))] -z-10"></div>
        </section>
      </main>

      {/* Footer */}
      <footer className="bg-keyline text-white py-10 px-6">
        <div className="max-w-5xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
            <div className="md:col-span-2">
              <h2 className="font-serif text-2xl font-bold mb-2">UGH</h2>
              <p className="font-sans text-white/60 max-w-xs mb-5 text-[13px]">
                Skateboarding is more than a sport; it&apos;s a tactical dialogue with urban architecture. Join us in Hyderabad.
              </p>
              <div className="flex gap-3">
                <a href="https://www.instagram.com/urbangliding.hyd?igsh=MWJubGk3OG42eHI2Zw==" target="_blank" rel="noreferrer" className="p-2.5 border border-white/20 rounded-full hover:bg-burnt-orange hover:border-burnt-orange transition-all">
                  <Instagram size={18} />
                </a>
                <a href={`mailto:${content.contact.email}`} className="p-2.5 border border-white/20 rounded-full hover:bg-deep-teal hover:border-deep-teal transition-all">
                  <Mail size={18} />
                </a>
                <a href={content.contact.whatsappGroup} target="_blank" rel="noreferrer" className="p-2.5 border border-white/20 rounded-full hover:bg-green-600 hover:border-green-600 transition-all">
                  <MessageCircle size={18} />
                </a>
              </div>
            </div>

            <div>
              <h3 className="font-mono text-[9px] uppercase tracking-widest text-white/40 mb-4">Quick Links</h3>
              <ul className="space-y-3">
                {["Safety Protocol", "Terms", "Privacy", "Contact"].map(item => (
                  <li key={item}>
                    <a href="#" className="font-sans text-xs text-white/60 hover:text-burnt-orange transition-colors">
                      {item}
                    </a>
                  </li>
                ))}
              </ul>
            </div>

            <div>
              <h3 className="font-mono text-[9px] uppercase tracking-widest text-white/40 mb-4">Community</h3>
              <div className="space-y-4">
                <button 
                  onClick={() => window.open(content.contact.googleBusiness, "_blank")}
                  className="group flex items-center gap-2 text-xs font-sans text-white/60 hover:text-white transition-all"
                >
                  Review Us
                  <ExternalLink size={12} className="group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
                </button>
                <div className="p-3 bg-white/5 border border-white/10 rounded-xl">
                  <p className="font-serif font-bold text-base">{content.contact.coachName}</p>
                  <p className="font-mono text-[9px] text-white/30 uppercase">IOC Certified</p>
                </div>
              </div>
            </div>
          </div>

          <div className="pt-6 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="font-mono text-[9px] text-white/40 uppercase tracking-widest">
              © 2026 Urban Gliding Hyderabad.
            </p>
            <div className="flex gap-4">
              <span className="font-mono text-[9px] text-white/40 uppercase tracking-widest">v{content.meta.version}</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
