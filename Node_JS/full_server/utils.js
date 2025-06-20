import fs from 'fs';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) return reject(Error('Cannot load the database'));

      const lines = data.trim().split('\n').slice(1);
      const students = {};

      for (const line of lines) {
        const parts = line.split(',');
        const firstname = parts.length > 0 ? parts[0].trim() : null;
        const field = parts.length > 3 ? parts[3].trim() : null;

        if (!firstname || !field) continue;

        if (!students[field]) students[field] = [];
        students[field].push(firstname);
      }

      resolve(students);
    });
  });
}