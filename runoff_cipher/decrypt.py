

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = ALPHABET.upper()

def encrypt(plaintext):
    ciphertext = ""
    saved_offset = 0


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
        
        new_offset = (idx + saved_offset) % 26
        saved_offset = idx

        next_char = ALPHABET[new_offset]
        if upper:
            next_char = next_char.upper()

        ciphertext += next_char

    return ciphertext


def subtract_letters(letter_1, letter_2):
    idx_1 = ALPHABET.index(letter_1)
    idx_2 = ALPHABET.index(letter_2)
    
    # idx_1 - idx_2 (mod 26)
    subtracted = idx_1 - idx_2
    while subtracted < 0:
        subtracted += 26

    return ALPHABET[subtracted]



def decrypt(ciphertext):
    # Empty ciphertext is nothing
    if not ciphertext:
        return ""
    
    # The first character of the ciphertext is preserved,
    # this will be our starting off point
    plaintext = ciphertext[0]

    for i in range(len(ciphertext)):
        # first letter was already calculated
        if i == 0:
            continue
        
        # Ignore non alpha-numeric
        if ciphertext[i].lower() not in ALPHABET:
            plaintext += ciphertext[i]
            continue

        
        plaintext += subtract_letters(ciphertext[i], plaintext[i-1])

    return plaintext





def main():
    encrypted_flag = input("Encrypted: ")
    flag = decrypt(encrypted_flag)
    print(flag)
    


if __name__ == "__main__":
    main()

