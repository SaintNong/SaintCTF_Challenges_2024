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
    char input_text[] = "\x8a\xc5\xdb\xcf\xb8\xc1\xdf\x88\xfe\xc4\xcd\xd5\xfe\xde\xdf\x86\xb0\xd9\xc5\x8b\xef\xde\xcd\xdb\xad\xde\x8d\x82\xbc\x9c\xc7\xb0\xea\xc3\xda\xb0\xa6\x9d\xcc\xce\xa3";
    char key[] = "\xde\xad\xbe\xef";     // XOR key
    size_t key_len = strlen(key);

    // Encrypt the input
    xor_encrypt(input_text, key, key_len);

    // Make some funny
    puts("Put a breakpoint on me!");
    puts("(or just disassemble/decompile me idc)");


    return 0;
}
