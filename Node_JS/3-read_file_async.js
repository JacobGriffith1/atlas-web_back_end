// 3. Reading a File Asynchronously with Node JS

const fs = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        // console.log('Promise made')
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                // If there's an error, reject Promise with specified error
                return reject(new Error('Cannot load the database'));
            }

            // Split the data into lines
            // Use a regex to support Unix (\n) and Windows (\r\n) line endings.
            const lines = data.split(/\r?\n/).filter(line => line.trim() !== '');

            // Check for header and data
            if (lines.length <= 1) {
                return reject(new Error('Cannot load the database'));
            }

            // Extract the header row
            // Remove any potential BOM and split by comma.
            const headers = lines[0].replace(/^\uFEFF/, '').split(',');

            // Find the indexes for 'firstname' and 'field'
            const firstNameIndex = headers.indexOf('firstname');
            const fieldIndex = headers.indexOf('field');

            if (firstNameIndex === -1 || fieldIndex === -1) {
                return reject(new Error('Cannot load the database'));
            }

            // Object to group students by field
            const fieldCounts = {};

            //Process each student entry (skip header)
            for (let i = 1; i < lines.length; i++) {
                const studentData = lines[i].split(',');
                // console.log(`Lines: ${i}`);

                // Skip lines that do not have the correct numer of columns
                if (studentData.length < headers.length) continue;

                const firstName = studentData[firstNameIndex].trim();
                const field = studentData[fieldIndex].trim();

                if (firstName && field) {
                    if (!fieldCounts[field]) {
                        fieldCounts[field] = [];
                    }
                    fieldCounts[field].push(firstName);
                }
            }

            // Count the total number of students
            const totalStudents = Object.values(fieldCounts)
                .reduce((acc, names) => acc + names.length, 0);

            // Log the overall student count
            console.log(`Number of students: ${totalStudents}`);

            // Log each field with its count and list of first names
            for (const [field, names] of Object.entries(fieldCounts)) {
                console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
            }

            // Resolve the Promise once processing is complete
            resolve();
            // console.log('Promise resolved');
        });
    });
}

module.exports = countStudents;