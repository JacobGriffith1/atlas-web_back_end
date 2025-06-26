// 4. Create a more complex HTTP server using Node's HTTP module

const http = require('http');
const countstudents = require('./3-read_file_async');
const fs = require('fs');

// Get database file path from command line arguments
const databaseFile = process.argv[2];

// Create the HTTP server and assign it to the variable 'app'
const app = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/plain'); // Set the response content type to plain text

    if (req.url === '/') {
        res.statusCode = 200; // Set HTTP status to OK
        res.end('Hello Atlas School!'); // Send the response body
    } else if (req.url === '/students') {
        res.statusCode = 200;
        res.write('This is the list of our students\n');

        // Check for database
        if (!databaseFile || !fs.existsSync(databaseFile)) {
            res.end('Cannot load the database');
        } else {
            // Capture the logs by overriding console.log;
            const originalConsoleLog = console.log;
            let logOutput = '';

            console.log = (...args) => {
                logOutput += args.join (' ') + '\n';
                originalConsoleLog(...args); // Keep normal logging behavior
            };

            countstudents(databaseFile)
                .then(() => {
                    res.end(logOutput); // Ends response after countStudents logs output
                    console.log = originalConsoleLog; // Restore console.log
                })
                .catch(() => {
                    res.end('Cannot load the database');
                    console.log = originalConsoleLog; // Restore console.log in case of errors
                });
        }
    } else {
        res.statusCode = 404;
        res.end('Not Found');
    }
});

app.listen(1245);

module.exports = app;