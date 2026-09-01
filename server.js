require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { GoogleGenAI } = require('@google/genai');

const app = express();
app.use(cors());
app.use(express.json());

// Serve static files
app.use(express.static(__dirname));

// Initialize Gemini
let ai = null;
if (process.env.GEMINI_API_KEY) {
  ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
} else {
  console.warn("GEMINI_API_KEY is not set.");
}

app.post('/api/verify-weather', async (req, res) => {
  if (!ai) {
    return res.status(500).json({ error: "Gemini API key is not configured." });
  }

  const { venue, date_time, discipline } = req.body;
  if (!venue || !date_time) {
    return res.status(400).json({ error: "Venue and date_time are required." });
  }

  const prompt = `You are the UGH Session Matcher, an action-sports professional. 
The user wants to book a ${discipline} session at "${venue}" on ${date_time}.
Use Google Search to check the weather forecast for Hyderabad, India on that date and time.
Determine if the venue is outdoor and if the rain probability is > 50%.
If rain probability > 50% for an outdoor venue, say: "Rain risk high for ${venue}. Flagging our indoor backup slot at Decathlon Atrium."
Otherwise, say: "Weather looks clear for ${venue}. You're good to go."
Keep your response to a maximum of 2 short sentences. Direct and sharp tone.`;

  try {
    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: prompt,
      config: {
        tools: [{ googleSearch: {} }],
        temperature: 0.2
      }
    });

    const reply = response.text;
    const requiresBackup = reply.toLowerCase().includes('backup slot') || reply.toLowerCase().includes('rain risk high');

    res.json({ reply, requiresBackup });
  } catch (error) {
    console.error("Gemini Error:", error);
    res.status(500).json({ error: "Failed to verify weather." });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
