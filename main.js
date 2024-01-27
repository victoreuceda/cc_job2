const { exec } = require('child_process');

exec('sudo id', (error, stdout, stderr) => {
    if (error) {
        console.log('This container does not have sudo privileges.');
        return;
    }
    console.log('This container has sudo privileges.');
});