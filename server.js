require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { verifyWeather } = require('./src/routes/weather');

const app = express();
app.use(cors());
app.use(express.json());

// Serve static files
app.use(express.static(__dirname));

// API Routes
app.post('/api/verify-weather', verifyWeather);

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
