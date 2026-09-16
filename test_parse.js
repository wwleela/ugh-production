const fs = require('fs');
const content = fs.readFileSync('src/App.tsx', 'utf8');
try {
  // basic check - this might not work if it's TSX unless we use a parser
} catch (e) {}
