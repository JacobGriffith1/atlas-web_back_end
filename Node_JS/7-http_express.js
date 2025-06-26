// 7. Create a more complex HTTP server using Express

const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;
const databaseFile = process.argv[2]; // Get the database file from command-line arguments

app.get('/', (req, res) => {
  res.send('Hello Atlas School!');
});

app.get('/students', async (req, res) => {
  let responseText = 'This is the list of our students\n';

  try {
    // Await the promise returned by countStudents to get the data
    const data = await countStudents(databaseFile);

    // Extract total students and field counts from the resolved data
    const { totalStudents, fieldCounts } = data;

    // Append the number of students to the response text
    responseText += `Number of students: ${totalStudents}\n`;

    // Loop through the fields and append student data to the response
    for (const [field, names] of Object.entries(fieldCounts)) {
      responseText += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }

    // Send the formatted response text to the client
    res.send(responseText.trim());
  } catch (error) {
    res.status(500).send('Cannot load the database');
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}\n`);
});

module.exports = app;