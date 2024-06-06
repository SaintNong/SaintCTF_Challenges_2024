#include <stdio.h>
#include <string.h>

void access_granted() {
    char encoded_flag[] = {
        120,
        102,
        110,
        115,
        121,
        128,
        105,
        54,
        105,
        100,
        126,
        53,
        122,
        100,
        105,
        54,
        120,
        120,
        57,
        120,
        56,
        114,
        103,
        113,
        56,
        100,
        114,
        56,
        68,
        130,
    };  // Encoded flag
    int length = sizeof(encoded_flag) / sizeof(encoded_flag[0]);
    char decoded_flag[length + 1]; // +1 for the null terminator

    // Decode each character by subtracting 5 from its ASCII value
    for (int i = 0; i < length; i++) {
        decoded_flag[i] = encoded_flag[i] - 5;
    }
    decoded_flag[length] = '\0'; // Null-terminate the string

    // Print the decoded flag
    printf("%s\n", decoded_flag);
}

int main() {
    char password[] = "Eromanga Sensei is 10/10";
    char user_input[256];

    printf("Enter password: ");
    fgets(user_input, sizeof(user_input), stdin);

    // Strip the newline character fgets stores at the end of input
    user_input[strlen(user_input) - 1] = '\0';
    
    // Check password
    if (strcmp(user_input, password) == 0) {
        puts("Access granted.");
        puts("Here is your flag:");

        access_granted();
    } else {
        puts("Access denied.");
        puts("The password is wrong!");
    }

    return 0;
}

