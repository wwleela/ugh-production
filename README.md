# Urban Gliding Hyderabad (UGH)

India's elite skating community. Premium doorstep coaching and IOC-certified training.

## Architecture & Deployment

This application follows a **Global Standard Architecture** for modern web applications:

1.  **Framework**: React 19 + Vite (High-performance SPA).
2.  **Styling**: Tailwind CSS 4 (Utility-first, minimal footprint).
3.  **Authentication**: Clerk Integration for secure user sessions.
4.  **Typography**: Inter (Body) & Space Grotesk (Display) for a clean, technical feel.
5.  **Single Source of Truth**: All pages (About, Leaderboard) are consolidated into the main React application.

### Important: Hosting Your Domain

The "old design" you might see on your domain is likely because your hosting is pointing to the previous `static-export` files. We have removed those redundant files to ensure a "crisp and simple" architecture.

**To update your website:**
1.  **Build**: Run `npm run build`. This generates a `dist/` folder.
2.  **Deploy**: Upload the **entire contents of the `dist/` folder** to your hosting root.
3.  **Pathing**: Ensure your domain is pointed to `index.html` inside that `dist` output.

## Mission protocol
Stay Tactical. Command the Urban Terrain.
