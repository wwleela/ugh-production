import {StrictMode} from 'react';
import {createRoot} from 'react-dom/client';
import { ClerkProvider } from '@clerk/clerk-react';
import App from './App.tsx';
import './index.css';

let key = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY;

// Clerk Configuration Guard: Ensure we use a Publishable Key (pk_...) on the frontend.
// If a Secret Key (sk_...) is accidentally provided, we fall back to a safe default to prevent crashes.
if (key && key.startsWith('sk_')) {
  console.warn("Clerk Auth Notice: VITE_CLERK_PUBLISHABLE_KEY contains a Secret Key (sk_...). Frontend authentication requires a Publishable Key (pk_...). Using fallback development key.");
  key = null;
}

const PUBLISHABLE_KEY = key || "pk_test_cG93ZXJmdWwtcmVkZmlzaC01MC5jbGVyay5hY2NvdW50cy5kZXYk";

if (!PUBLISHABLE_KEY) {
  console.warn("Clerk Publishable Key is missing. Please set VITE_CLERK_PUBLISHABLE_KEY in your environment.");
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ClerkProvider publishableKey={PUBLISHABLE_KEY} afterSignOutUrl="/">
      <App />
    </ClerkProvider>
  </StrictMode>,
);
