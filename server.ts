import express from "express";
import cors from "cors";
import path from "path";
import { fileURLToPath } from "url";
import { Resend } from "resend";
import { createServer as createViteServer } from "vite";
import fs from "fs";
import crypto from "crypto";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function startServer() {
  const app = express();
  const PORT = 3000;

  app.use(express.json());
  
  // Restricted CORS
  app.use(cors({
    origin: ["https://ugh.co.in", "http://localhost:3000", /\.asia-east1\.run\.app$/],
    methods: ["GET", "POST"],
    credentials: true
  }));

  // Security Headers
  app.use((req, res, next) => {
    res.setHeader('X-Content-Type-Options', 'nosniff');
    res.setHeader('X-Frame-Options', 'DENY');
    res.setHeader('X-XSS-Protection', '1; mode=block');
    next();
  });

  const resend = process.env.RESEND_API_KEY ? new Resend(process.env.RESEND_API_KEY) : null;

  // API Routes
  app.get("/api/health", (req, res) => {
    res.json({ status: "healthy", timestamp: new Date().toISOString() });
  });

  // Admin enrollment endpoint
  app.post("/admin/enroll", async (req, res) => {
    try {
      const adminSecret = req.headers['x-admin-secret'] as string || "";
      const expectedSecret = process.env.ADMIN_SECRET_KEY || "";

      // Security: Use timingSafeEqual to prevent timing attacks
      const isAuthorized = adminSecret.length === expectedSecret.length && 
                           crypto.timingSafeEqual(
                             Buffer.from(adminSecret), 
                             Buffer.from(expectedSecret)
                           );

      if (!isAuthorized) {
        return res.status(401).json({ 
          error: 'Unauthorized', 
          message: 'Invalid admin secret' 
        });
      }

      const { studentEmail, studentName, programType, amount, transactionId, notes } = req.body;
      if (!studentEmail || !studentName || !programType) {
        return res.status(400).json({ 
          error: 'Bad Request', 
          message: 'Missing required fields' 
        });
      }

      const enrollmentId = `ENR-${Date.now()}-${Math.random().toString(36).substring(2, 11).toUpperCase()}`;

      let emailSent = false;
      let emailId = null;

      if (resend) {
        try {
          const { data, error } = await resend.emails.send({
            from: 'UGH Mission 2026 <onboarding@resend.dev>', // Should be a verified domain in prod
            to: [studentEmail],
            cc: ['worldwide.leelamadhav@gmail.com'],
            subject: `✅ Welcome to UGH — ${programType}`,
            html: `
              <div style="font-family: sans-serif; padding: 20px; max-width: 600px; border: 1px solid #00615f;">
                <h1 style="color: #00615f;">Welcome to Urban Gliding Hyderabad!</h1>
                <p>Hi ${studentName},</p>
                <p>Your payment for <strong>${programType}</strong> has been verified.</p>
                <div style="background: #f1ede7; padding: 15px; border-radius: 8px; margin: 20px 0;">
                  <p><strong>Enrollment ID:</strong> ${enrollmentId}</p>
                  <p><strong>Amount Paid:</strong> ₹${amount}</p>
                  <p><strong>Transaction ID:</strong> ${transactionId}</p>
                </div>
                <p>Coach Leela will reach out within 24 hours to schedule your first session.</p>
                <p>Stay Tactical,<br>Team UGH</p>
              </div>
            `
          });
          if (error) {
            console.error('Resend error:', error);
          } else {
            emailSent = true;
            emailId = data?.id;
          }
        } catch (err) {
          console.error('Email delivery exception:', err);
        }
      }

      // Simple Logging (in a real app, this would go to a DB or file)
      const logEntry = {
        enrollmentId,
        studentEmail,
        studentName,
        programType,
        amount,
        transactionId,
        emailSent,
        emailId,
        notes,
        timestamp: new Date().toISOString()
      };
      
      // For this environment, we just log to console or a virtual audit log
      console.log('ENROLLMENT_LOG:', JSON.stringify(logEntry));

      res.status(200).json({
        success: true,
        message: 'Student enrolled successfully',
        enrollment: logEntry
      });

    } catch (error: any) {
      console.error('Enrollment error:', error);
      res.status(500).json({ 
        error: 'Internal Server Error', 
        message: error.message 
      });
    }
  });

  // Vite middleware for development
  if (process.env.NODE_ENV !== "production") {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), 'dist');
    if (fs.existsSync(distPath)) {
      app.use(express.static(distPath));
      app.get('*', (req, res) => {
        res.sendFile(path.join(distPath, 'index.html'));
      });
    }
  }

  app.listen(PORT, "0.0.0.0", () => {
    console.log(`🚀 UGH Backend running on http://0.0.0.0:${PORT}`);
  });
}

startServer();
