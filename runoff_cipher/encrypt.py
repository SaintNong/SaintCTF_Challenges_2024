ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = ALPHABET.upper()

def encrypt(plaintext):
    ciphertext = ""
    runoff = 0


    for char in plaintext:
        if char.lower() not in ALPHABET:
            ciphertext += char

            continue

        if char.islower():
            idx = ALPHABET.index(char)
            upper = False
        else:
            idx = ALPHABET_UPPER.index(char)
            upper = True
        
        new_offset = (idx + runoff) % 26
        runoff = idx

        next_char = ALPHABET[new_offset]
        if upper:
            next_char = next_char.upper()

        ciphertext += next_char

    return ciphertext


def main():
    with open("flag.txt", "r") as file:
        flag = file.read().strip()

    encrypted_flag = encrypt(flag)
    
    with open("output.txt", "w") as file:
        file.write(encrypted_flag)


if __name__ == "__main__":
    main()

