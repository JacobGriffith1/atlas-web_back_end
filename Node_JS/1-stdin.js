// 1. Using Process stdin

// Import readline
const readline = require('readline');

// createInterface
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Welcome message, name prompt
rl.question('Welcome to Atlas School, what is your name?\n', (name) => {
    // Display name
    console.log(`Your name is: ${name}`);

    // Close handler
    rl.on('close', () => {
        console.log('This important software is now closing\n');
        process.exit(0); 
    });

    // Close interface
    rl.close();
});
