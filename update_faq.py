import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Remove old FAQ section
old_faq_pattern = r'<!-- FAQS -->.*?</section>'
content = re.sub(old_faq_pattern, '<!-- FAQS moved to floating modal -->', content, flags=re.DOTALL)

# 2. Append new floating button and modal before <!-- Footer -->
new_faq_html = """
    <!-- Floating FAQ Button -->
    <button onclick="document.getElementById('faq-modal').classList.remove('hidden')" class="fixed bottom-6 right-6 md:bottom-10 md:right-10 z-[90] w-14 h-14 bg-kinetic-text text-kinetic-bg rounded-full shadow-[4px_4px_0px_var(--kinetic-accent)] flex items-center justify-center hover:-translate-y-1 hover:shadow-[6px_6px_0px_var(--kinetic-accent)] transition-all focus:outline-none focus-visible:ring-4 focus-visible:ring-kinetic-accent group border-2 border-transparent hover:border-kinetic-accent">
      <span class="material-symbols-outlined text-3xl">help_outline</span>
    </button>

    <!-- FAQ Modal -->
    <div id="faq-modal" class="hidden fixed inset-0 z-[100] flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-kinetic-bg/80 backdrop-blur-sm" onclick="document.getElementById('faq-modal').classList.add('hidden')"></div>
      <div class="relative bg-kinetic-surface border-2 border-kinetic-border shadow-[12px_12px_0px_var(--kinetic-shadow)] p-8 max-w-2xl w-full max-h-[90vh] overflow-y-auto text-left">
        <div class="flex justify-between items-center mb-6 border-b-2 border-kinetic-border pb-4">
          <h3 class="text-3xl font-display font-bold uppercase">FAQ <span class="text-kinetic-accent">Skating Classes</span></h3>
          <button onclick="document.getElementById('faq-modal').classList.add('hidden')" class="material-symbols-outlined hover:text-kinetic-accent text-3xl">close</button>
        </div>
        <div class="space-y-4">
          <details class="group bg-kinetic-surface-alt border-2 border-kinetic-border focus-within:ring-2 focus-within:ring-kinetic-accent">
            <summary class="font-bold text-lg p-4 cursor-pointer list-none flex justify-between items-center outline-none">
              What gear is mandatory for classes?
              <span class="material-symbols-outlined group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <div class="px-4 pb-4 text-kinetic-muted border-t border-kinetic-border pt-3">
              A certified helmet, wrist guards, elbow pads, and knee pads are required for every class &mdash; no exceptions.
            </div>
          </details>
          <details class="group bg-kinetic-surface-alt border-2 border-kinetic-border focus-within:ring-2 focus-within:ring-kinetic-accent">
            <summary class="font-bold text-lg p-4 cursor-pointer list-none flex justify-between items-center outline-none">
              What's the age limit?
              <span class="material-symbols-outlined group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <div class="px-4 pb-4 text-kinetic-muted border-t border-kinetic-border pt-3">
              UGH coaches Junior (5&ndash;12 yrs), Senior (13&ndash;17 yrs), and Adult riders/skaters. Everyone is welcome to learn.
            </div>
          </details>
          <details class="group bg-kinetic-surface-alt border-2 border-kinetic-border focus-within:ring-2 focus-within:ring-kinetic-accent">
            <summary class="font-bold text-lg p-4 cursor-pointer list-none flex justify-between items-center outline-none">
              What happens if it rains?
              <span class="material-symbols-outlined group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <div class="px-4 pb-4 text-kinetic-muted border-t border-kinetic-border pt-3">
              Rained-out sessions are rescheduled to a make-up day so you don't lose your training time.
            </div>
          </details>
          <details class="group bg-kinetic-surface-alt border-2 border-kinetic-border focus-within:ring-2 focus-within:ring-kinetic-accent">
            <summary class="font-bold text-lg p-4 cursor-pointer list-none flex justify-between items-center outline-none">
              What should I bring to my first session?
              <span class="material-symbols-outlined group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <div class="px-4 pb-4 text-kinetic-muted border-t border-kinetic-border pt-3">
              Comfortable athletic clothing and closed-toe shoes. Protective gear is provided, or you can bring your own per our mandatory safety policy.
            </div>
          </details>
          <details class="group bg-kinetic-surface-alt border-2 border-kinetic-border focus-within:ring-2 focus-within:ring-kinetic-accent">
            <summary class="font-bold text-lg p-4 cursor-pointer list-none flex justify-between items-center outline-none">
              Does UGH offer workshops at Aparna Serene Park?
              <span class="material-symbols-outlined group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <div class="px-4 pb-4 text-kinetic-muted border-t border-kinetic-border pt-3">
              Yes &mdash; a weekly skateboarding workshop has actually been run at Aparna Serene Park, Kondapur.
            </div>
          </details>
          <details class="group bg-kinetic-surface-alt border-2 border-kinetic-border focus-within:ring-2 focus-within:ring-kinetic-accent">
            <summary class="font-bold text-lg p-4 cursor-pointer list-none flex justify-between items-center outline-none">
              Does UGH offer workshops at Gachibowli schools?
              <span class="material-symbols-outlined group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <div class="px-4 pb-4 text-kinetic-muted border-t border-kinetic-border pt-3">
              Yes, as part of our Noble Practices initiative &mdash; a real outreach program that has taught 60+ students free skateboarding instruction.
            </div>
          </details>
          <details class="group bg-kinetic-surface-alt border-2 border-kinetic-border focus-within:ring-2 focus-within:ring-kinetic-accent">
            <summary class="font-bold text-lg p-4 cursor-pointer list-none flex justify-between items-center outline-none">
              Does UGH offer workshops at Aparna Heights 1?
              <span class="material-symbols-outlined group-open:rotate-180 transition-transform">expand_more</span>
            </summary>
            <div class="px-4 pb-4 text-kinetic-muted border-t border-kinetic-border pt-3">
              We are currently booking workshops for Aparna Heights 1, Kondapur &mdash; available on request.
            </div>
          </details>
        </div>
      </div>
    </div>
"""

content = content.replace('<!-- Footer -->', new_faq_html + '\n    <!-- Footer -->')

with open('index.html', 'w') as f:
    f.write(content)

