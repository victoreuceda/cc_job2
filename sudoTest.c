#include <stdlib.h>
#include <stdio.h>

int main() {
    // Attempt to execute a harmless command with sudo, such as 'id'
    int result = system("sudo id");

    // Check the result of the system call
    if (result == 0) {
        // If the result is 0, the command executed successfully
        printf("This container has sudo privileges.\n");
    } else {
        // A non-zero result indicates a failure, likely due to lack of privileges
        printf("This container does not have sudo privileges.\n");
    }

    return 0;
}