import fs from 'fs';
import path from 'path';

// Проверь, идет ли билд или dev
const isDev = process.env.NODE_ENV !== 'production';

export default {
  server: isDev
    ? {
        host: '0.0.0.0',
        https: {
          key: fs.readFileSync(path.resolve('/home/ubuntu/EasyMPNN/nginx/ssl/key.pem')),
          cert: fs.readFileSync(path.resolve('/home/ubuntu/EasyMPNN/nginx/ssl/cert.pem')),
        },
        port: 4000,
      }
    : {},
};