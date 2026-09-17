import re

with open('index.html', 'r') as f:
    content = f.read()

new_impact_content = """<!-- IMPACT TAB -->
<div id="tab-impact" class="hidden main-tab-content">
  <section class="pt-8 md:pt-16 pb-12 px-[clamp(1.25rem,5vw,4rem)] border-b border-kinetic-border">
    <div class="max-w-4xl mx-auto text-center">
      <h2 class="text-[clamp(1.75rem,5vw,3.5rem)] leading-tight font-display font-bold mb-6 uppercase tracking-tight focus:outline-none focus-visible:ring-4 focus-visible:ring-kinetic-accent focus-visible:ring-offset-4 focus-visible:ring-offset-kinetic-bg" tabindex="0">Action Sports Programs for <span class="text-kinetic-accent">Hyderabad Schools</span></h2>
      <p class="text-lg text-kinetic-muted mb-12">
        UGH offers structured action sports classes and workshops for schools across Hyderabad &mdash; introducing students to skateboarding, inline skating, and BMX.
      </p>
      
      <div class="bg-kinetic-surface border-2 border-kinetic-border shadow-[8px_8px_0px_var(--kinetic-shadow)] p-8 md:p-12 text-left mb-12 focus:outline-none focus-visible:ring-4 focus-visible:ring-kinetic-accent focus-visible:ring-offset-4 focus-visible:ring-offset-kinetic-bg" tabindex="0">
        <h3 class="text-2xl font-bold uppercase mb-4 text-kinetic-accent">Noble Practices Initiative</h3>
        <p class="mb-6 font-medium">A free program that has already taught 60+ students in Gachibowli foundational skateboarding instruction and safety gear at no cost.</p>
        <p class="text-kinetic-muted text-sm">Action sports offer kids physical development, discipline, competitive pathways, and even the chance to represent India at national and international levels.</p>
      </div>
      
      <div class="inline-block p-6 bg-kinetic-surface-alt border border-kinetic-border text-center w-full max-w-2xl focus:outline-none focus-visible:ring-4 focus-visible:ring-kinetic-accent focus-visible:ring-offset-4 focus-visible:ring-offset-kinetic-bg" tabindex="0">
         <h4 class="font-bold text-lg uppercase mb-2">Want this at your school?</h4>
         <p class="text-sm text-kinetic-muted">Reach out to your school management to bring a UGH action sports program to your students.</p>
      </div>
    </div>
  </section>
  <section class="py-12 px-[clamp(1.25rem,5vw,4rem)] border-b border-kinetic-border bg-kinetic-surface-alt">
    <div class="max-w-5xl mx-auto">
      <h2 class="text-[clamp(1.5rem,4vw,2.5rem)] leading-tight font-display font-bold mb-6 text-center uppercase tracking-tight focus:outline-none focus-visible:ring-4 focus-visible:ring-kinetic-accent focus-visible:ring-offset-4 focus-visible:ring-offset-kinetic-bg" tabindex="0">Doorstep Skateboarding <span class="text-kinetic-accent">Workshops</span></h2>
      <p class="text-center text-lg text-kinetic-muted mb-12 max-w-3xl mx-auto">UGH runs free introductory workshops at residential communities across Hyderabad to give families hands-on experience with action sports, right at their doorstep.</p>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-12">
        <div tabindex="0" class="p-4 bg-kinetic-surface border border-kinetic-border flex items-center gap-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-kinetic-accent"><span class="material-symbols-outlined text-kinetic-accent">location_on</span> <span class="font-bold">Aparna Serene Park</span>, Kondapur</div>
        <div tabindex="0" class="p-4 bg-kinetic-surface border border-kinetic-border flex items-center gap-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-kinetic-accent"><span class="material-symbols-outlined text-kinetic-accent">location_on</span> <span class="font-bold">Aparna Sarovar Zenith</span>, Nallagandla</div>
        <div tabindex="0" class="p-4 bg-kinetic-surface border border-kinetic-border flex items-center gap-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-kinetic-accent"><span class="material-symbols-outlined text-kinetic-accent">location_on</span> <span class="font-bold">Aparna Sarovar Grande</span>, Nallagandla</div>
        <div tabindex="0" class="p-4 bg-kinetic-surface border border-kinetic-border flex items-center gap-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-kinetic-accent"><span class="material-symbols-outlined text-kinetic-accent">location_on</span> <span class="font-bold">Aparna Heights 1</span>, Kondapur</div>
        <div tabindex="0" class="p-4 bg-kinetic-surface border border-kinetic-border flex items-center gap-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-kinetic-accent"><span class="material-symbols-outlined text-kinetic-accent">location_on</span> <span class="font-bold">PBEL City</span>, Peerancheru</div>
        <div tabindex="0" class="p-4 bg-kinetic-surface border border-kinetic-border flex items-center gap-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-kinetic-accent"><span class="material-symbols-outlined text-kinetic-accent">location_on</span> <span class="font-bold">Prestige Beverly Hills</span>, Hyderabad</div>
        <div tabindex="0" class="p-4 bg-kinetic-surface border border-kinetic-border flex items-center gap-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-kinetic-accent"><span class="material-symbols-outlined text-kinetic-accent">location_on</span> <span class="font-bold">Ananda Bay Hills</span>, Narsingi</div>
        <div tabindex="0" class="p-4 bg-kinetic-surface border border-kinetic-border flex items-center gap-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-kinetic-accent"><span class="material-symbols-outlined text-kinetic-accent">location_on</span> <span class="font-bold">My Home Tarkshya</span>, Kokapet</div>
        <div tabindex="0" class="p-4 bg-kinetic-surface border border-kinetic-border flex items-center gap-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-kinetic-accent"><span class="material-symbols-outlined text-kinetic-accent">location_on</span> <span class="font-bold">My Home Navadweepa</span>, Madhapur / HITEC City</div>
        <div tabindex="0" class="p-4 bg-kinetic-surface border border-kinetic-border flex items-center gap-3 focus:outline-none focus-visible:ring-2 focus-visible:ring-kinetic-accent"><span class="material-symbols-outlined text-kinetic-accent">location_on</span> <span class="font-bold">The Botanika</span>, Gachibowli</div>
      </div>
      
      <div tabindex="0" class="text-center p-8 bg-kinetic-surface border-2 border-kinetic-border shadow-[4px_4px_0px_var(--kinetic-shadow)] focus:outline-none focus-visible:ring-4 focus-visible:ring-kinetic-accent focus-visible:ring-offset-2 focus-visible:ring-offset-kinetic-bg">
         <h3 class="text-2xl font-bold uppercase mb-4">Is your apartment missing?</h3>
         <p class="text-kinetic-muted mb-6 max-w-2xl mx-auto">Tap below to bring a free doorstep skateboarding, inline skating, or BMX workshop to your residential apartment in Hyderabad.</p>
         <button onclick="document.getElementById('wizard-modal').classList.remove('hidden')" class="inline-flex px-8 py-4 bg-kinetic-text text-kinetic-bg font-bold uppercase tracking-wider hover:scale-105 active:scale-95 transition-all shadow-[6px_6px_0px_var(--kinetic-accent)] border-2 border-kinetic-text items-center justify-center gap-2 focus:outline-none focus-visible:ring-4 focus-visible:ring-kinetic-accent focus-visible:ring-offset-2 focus-visible:ring-offset-kinetic-bg">
            Book a Free Workshop <span class="material-symbols-outlined">arrow_forward</span>
         </button>
      </div>
    </div>
  </section>
</div>"""

new_venues_content = """<!-- VENUES TAB -->
<div id="tab-venues" class="hidden main-tab-content">
  <section class="pt-8 md:pt-16 pb-fluid-xl px-[clamp(1.25rem,5vw,4rem)] border-b border-kinetic-border">
    <div class="max-w-5xl mx-auto">
      <h2 class="text-[clamp(1.75rem,5vw,3.5rem)] leading-tight font-display font-bold mb-6 text-center uppercase tracking-tight focus:outline-none focus-visible:ring-4 focus-visible:ring-kinetic-accent focus-visible:ring-offset-4 focus-visible:ring-offset-kinetic-bg" tabindex="0">Hyderabad <span class="text-kinetic-accent">Skate Parks</span></h2>
      <p class="text-center text-lg text-kinetic-muted mb-12 max-w-3xl mx-auto">Explore the premier skateboarding and action sports facilities available in Hyderabad, offering dedicated spaces for progression and community.</p>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12">
        <!-- Wallride Park -->
        <div class="bg-kinetic-surface border-2 border-kinetic-border shadow-[8px_8px_0px_var(--kinetic-shadow)] flex flex-col group focus-within:ring-4 focus-within:ring-kinetic-accent focus-within:ring-offset-2 focus-within:ring-offset-kinetic-bg" tabindex="0">
           <div class="h-64 bg-kinetic-surface-alt border-b-2 border-kinetic-border overflow-hidden relative">
              <img src="/src/assets/images/regenerated_image_1789593359927.jpg" alt="Wallride Park Logo" class="absolute inset-0 w-full h-full object-contain p-8 mix-blend-multiply dark:mix-blend-normal group-hover:scale-105 transition-transform duration-500" />
           </div>
           <div class="p-8 flex flex-col flex-grow">
              <div class="flex items-center gap-2 mb-2 text-kinetic-accent font-bold uppercase tracking-wider text-sm">
                 <span class="material-symbols-outlined text-base">location_on</span> Peeran Cheruvu
              </div>
              <h3 class="text-2xl font-display font-bold uppercase mb-4">WallRide Park</h3>
              <p class="text-kinetic-muted mb-6 flex-grow">Opened in 2017, WallRide Park is India's first asphalt pump track and Telangana's first concrete skatepark. Built to foster action sports in Hyderabad, it features a diverse environment for riders of all skill levels, including quarter pipes, banks, transitions, a funbox, manual pads, and a central pyramid.</p>
              <a href="https://wallridepark.com" target="_blank" class="inline-flex py-3 px-6 bg-transparent border-2 border-kinetic-text font-bold uppercase tracking-wider hover:bg-kinetic-text hover:text-kinetic-bg transition-colors items-center justify-center gap-2 w-full mt-auto">
                 Visit Website <span class="material-symbols-outlined text-sm">open_in_new</span>
              </a>
           </div>
        </div>

        <!-- Emptyhead Skatepark -->
        <div class="bg-kinetic-surface border-2 border-kinetic-border shadow-[8px_8px_0px_var(--kinetic-shadow)] flex flex-col group focus-within:ring-4 focus-within:ring-kinetic-accent focus-within:ring-offset-2 focus-within:ring-offset-kinetic-bg" tabindex="0">
           <div class="h-64 bg-kinetic-surface-alt border-b-2 border-kinetic-border flex items-center justify-center relative overflow-hidden">
              <span class="material-symbols-outlined text-6xl text-kinetic-border opacity-50 group-hover:scale-110 group-hover:text-kinetic-accent transition-all duration-500">skateboarding</span>
           </div>
           <div class="p-8 flex flex-col flex-grow">
              <div class="flex items-center gap-2 mb-2 text-kinetic-accent font-bold uppercase tracking-wider text-sm">
                 <span class="material-symbols-outlined text-base">location_on</span> Hyderabad
              </div>
              <h3 class="text-2xl font-display font-bold uppercase mb-4">Emptyhead Skatepark</h3>
              <p class="text-kinetic-muted mb-6 flex-grow">A dedicated space for the skateboarding community in Hyderabad. Built for skaters, by skaters, Emptyhead provides essential features like ledges, rails, and smooth flatground for practicing tricks, finding flow, and building local action sports culture.</p>
              <button class="inline-flex py-3 px-6 bg-kinetic-surface-alt border-2 border-kinetic-border text-kinetic-muted font-bold uppercase tracking-wider cursor-not-allowed items-center justify-center gap-2 w-full mt-auto">
                 More Info Soon
              </button>
           </div>
        </div>
      </div>
      
    </div>
  </section>
</div>
"""

# Replace the sections using regex
content = re.sub(r'<!-- IMPACT TAB -->.*?<!-- EVENTS TAB -->', new_impact_content + '\n\n<!-- EVENTS TAB -->', content, flags=re.DOTALL)
content = re.sub(r'<!-- VENUES TAB -->.*?</main>', new_venues_content + '\n</main>', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
