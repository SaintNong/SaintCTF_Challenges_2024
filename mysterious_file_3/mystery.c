#include <stdio.h>
#include <string.h>

void xor_encrypt(char *input, const char *key, size_t key_len) {
    size_t input_len = strlen(input);

    // Perform XOR operation, repeating the key if necessary
    for (size_t i = 0; i < input_len; i++) {
        input[i] ^= key[i % key_len];
    }
}

int main() {
    char input_text[] = "\xad\xcc\xd7\x81\xaa\xd6\xf9\xab\x9c\xf2\x8d\x97\xae\x9e\xcc\x9b\x81\xce\x8e\x81\xb8\x9c\xcc\x82\xed\xc9\x81\xce\xe1\xd0";
    char key[] = "\xde\xad\xbe\xef";     // XOR key
    size_t key_len = strlen(key);

    // Encrypt the input
    xor_encrypt(input_text, key, key_len);

    // Make some funny
    puts("Try a breakpoint here?");

    puts("(btw disassembling is quite the hassle with this one)");
    puts("(trust me, dynamic analysis is the way to go here)");


    return 0;
}
