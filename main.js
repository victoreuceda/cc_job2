const fs = require('fs');
const { exec } = require('child_process');
const net = require('net');

function checkFileAccess() {
    console.log("\nChecking File Access:");
    const sensitiveFiles = ["/etc/passwd", "/root/.ssh/", "/var/run/docker.sock"];
    sensitiveFiles.forEach(file => {
        fs.access(file, fs.constants.F_OK, (err) => {
            console.log(`${file} access: ${err ? 'not possible' : 'possible'}`);
        });
    });
}

function checkPermissionChange() {
    console.log("\nChecking Permission Change:");
    const testFile = "/etc/passwd";
    exec(`sudo chmod 777 ${testFile}`, (error, stdout, stderr) => {
        console.log(`Permission change on ${testFile}: ${error ? 'not possible' : 'successful'}`);
        // Revert permission change for safety
        exec(`sudo chmod 644 ${testFile}`, () => {});
    });
}

function checkPrivilegedPortBinding() {
    console.log("\nChecking Privileged Port Binding:");
    const privilegedPort = 80;
    const server = net.createServer();
    server.listen(privilegedPort, () => {
        console.log(`Binding to privileged port ${privilegedPort} successful.`);
        server.close();
    }).on('error', (err) => {
        console.log(`Binding to privileged port ${privilegedPort} failed.`);
    });
}

checkFileAccess();
checkPermissionChange();
checkPrivilegedPortBinding();
