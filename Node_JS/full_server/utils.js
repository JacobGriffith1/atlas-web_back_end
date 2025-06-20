import { rejects } from 'assert';
import { error } from 'console';
import fs from 'fs';
import { resolve } from 'path';

export function readDatabase(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf-8', (err, data) => {
            if (err) return reject(Error('Cannot load the database'));

            const lines = data.trim().split('\n').slice(1);
            const students = {};

            for (const line of lines) {
                const [, , , field] = line.split(',');
                const firstname = line.split(',')[0];
                if (!students[field]) students[field] = [];
                students[field].push(firstname);
            }

            resolve(students);
        });
    });
}