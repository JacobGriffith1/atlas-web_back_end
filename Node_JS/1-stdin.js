// 1. Using Process stdin


const readline = require('readline');

// createInterface
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Welcome message, name prompt
rl.question('Welcome to Atlas School, what is your name?\n', (name) => {
    console.log(`Your name is: ${name}`);

    rl.on('close', () => {
        console.log('This important software is now closing\n');
        process.exit(0); 
    });

    rl.close();
});
