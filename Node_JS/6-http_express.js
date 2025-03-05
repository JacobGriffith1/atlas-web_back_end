// 6. Create a small HTTP server using Express

const express = require('express');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
    res.send('Hello Atlas School!\n');
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

module.exports = app;