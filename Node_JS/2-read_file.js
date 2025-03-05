// 2. Reading a file synchronously with Node JS

const fs = require('fs');

function countStudents(path) {
    try {
        // Read the file synchronously
        const data = fs.readFileSync(path, 'utf8');
        //console.log('FILE DATA LOADED SUCCESSFULLY.')

        // Split the data into an array of lines
        const lines = data.split('\r').filter(line => line.trim() !== '', '\n'); // Remove empty lines
        //console.log('Lines:', lines);

        // Ensure file has a header and at least one data row
        if (lines.length <= 1) {
            throw new Error('Cannot load the database')
        }

        // Extract the header row (column names)
        const headers = lines[0].replace(/^\uFEFF/, '').split(',');

        // Identify the index of the required columns
        const firstNameIndex = headers.indexOf('firstname');
        const fieldIndex = headers.indexOf('field');

        if (firstNameIndex === -1 || fieldIndex === -1) {
            throw new Error('Cannot load the database');
        }

        // Create an objectto store the students grouped by field
        const fieldCounts = {};

        // Loop through each student (skip first row since it's a header)
        for (let i = 1; i < lines.length; i++) {
            const studentData = lines[i].split(',');

            // Ensure the row has the required number of columns
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

        // Compute the total number of students
        const totalStudents = Object.values(fieldCounts).reduce((acc, arr) => acc + arr.length, 0);
        console.log(`Number of students: ${totalStudents}`);

        // Print students per field
        for (const [field, names] of Object.entries(fieldCounts)) {
            console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;