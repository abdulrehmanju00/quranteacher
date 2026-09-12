import express from 'express';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;
const HOST = '0.0.0.0';

const publicDir = path.join(__dirname, 'public');

// Serve static files with proper MIME types
app.use(express.static(publicDir, {
  extensions: ['html', 'htm']
}));

// Route handler for clean URLs and safety
app.get('*', (req, res) => {
  const reqPath = req.path.replace(/^\/+|\/+$/g, '');
  
  if (!reqPath || reqPath === '') {
    return res.sendFile(path.join(publicDir, 'index.html'));
  }

  // Check direct file
  const directFile = path.join(publicDir, reqPath);
  if (fs.existsSync(directFile) && fs.statSync(directFile).isFile()) {
    return res.sendFile(directFile);
  }

  // Check with .html extension
  const htmlFile = path.join(publicDir, `${reqPath}.html`);
  if (fs.existsSync(htmlFile) && fs.statSync(htmlFile).isFile()) {
    return res.sendFile(htmlFile);
  }

  // Handle common variations
  if (reqPath === 'even') {
    return res.sendFile(path.join(publicDir, 'even.html'));
  }
  if (reqPath === 'service') {
    return res.sendFile(path.join(publicDir, 'service.html'));
  }
  if (reqPath === 'event') {
    return res.sendFile(path.join(publicDir, 'event.html'));
  }

  // Fallback to 404 or index
  const notFoundFile = path.join(publicDir, '404.html');
  if (fs.existsSync(notFoundFile)) {
    return res.status(404).sendFile(notFoundFile);
  }

  res.sendFile(path.join(publicDir, 'index.html'));
});

app.listen(PORT, HOST, () => {
  console.log(`Server running at http://${HOST}:${PORT}`);
});

