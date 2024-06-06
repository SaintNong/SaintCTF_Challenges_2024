import string
import random

def generate_key():
    alphabet = string.ascii_lowercase
    
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

def encrypt(plaintext):
    key = generate_key()

    ciphertext = ""

    for character in plaintext:
        next_char = character
        if character in string.ascii_uppercase:
            next_char = key[character.lower()].upper()
        elif character in string.ascii_lowercase:
            next_char = key[character]

        ciphertext += next_char

    return ciphertext

PLAINTEXT = """
According to all known laws of aviation, there is no way a bee should be able to fly.
Its wings are too small to get its fat little body off the ground.
The bee, of course, flies anyway because bees don't care what humans think is impossible.
Yellow, black. Yellow, black. Yellow, black. Yellow, black.
Ooh, black and yellow!
Let's shake it up a little.
Barry! Breakfast is ready!
Coming!
Hang on a second.
Hello?
Barry?
Adam?
Can you believe this is happening?
I can't.
I'll pick you up.
Looking sharp.
Use the stairs, Your father paid good money for those.
Sorry. I'm excited.
Here's the graduate.
We're very proud of you, son.
A perfect report card, all B's.
Very proud.
Ma! I got a thing going here.
You got lint on your fuzz.
Ow! That's me!
Wave to us! We'll be in row 118,000.
Bye!
Barry, I told you, stop flying in the house!
Hey, Adam.
Hey, Barry.
Is that fuzz gel?
A little. Special day, graduation.
Never thought I'd make it.
Three days grade school, three days high school.
Those were awkward.
Three days college. I'm glad I took a day and hitchhiked around The Hive.

saint{bet_you_used_some_online_tool_lol!_also_this_is_peak_cinema}
"""
OUTFILE = "ciphertext.txt"

if __name__ == "__main__":
    ciphertext = encrypt(PLAINTEXT)

    with open(OUTFILE, "w") as file:
        file.write(ciphertext)
    


