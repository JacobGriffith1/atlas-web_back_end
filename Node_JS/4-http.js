// 4. Create a small HTTP server using Node's HTTP module

const http = require('http');

// Create the HTTP server and assign it to the variable 'app'
const app = http.createServer((req, res) => {
    res.statusCode = 200; // Set HTTP status to OK
    res.setHeader('Content-Type', 'text/plain') // Set the response content type to plain text
    res.end('Hello Atlas School!'); // Send the response body
});

// Start the server listening on port 1245
app.listen(1245);

module.exports = app;