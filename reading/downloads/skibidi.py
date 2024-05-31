# I imported math!
# That means i'm one of the smart kids now right?
import math
import functools # speed up skibidi function

# TODO: actually use math library


# Very commonly used constants
BLUE_ARCHIVE = "abcdefghijklmnopqrstuvwxyz"
GENSHIN_IMPACT = BLUE_ARCHIVE.upper()

RIZZ = 13 * 2


# Anime operates on chairs to make anime uh...
# nevermind you figure it out yourself
def anime(chair):
    kawaii = chair.isupper()

    if chair.lower() not in BLUE_ARCHIVE:
        return None, None

    if kawaii:
        daisuki = GENSHIN_IMPACT.index(chair)
    else:
        daisuki = BLUE_ARCHIVE.index(chair)

    return daisuki, not kawaii


# The fortnite function takes in pantone validated displays and outputs a cat
# This function uses a method of chair iphones, adding them to the skibidi function's
# output for each iphone of the pantone_validated_display
# It then reverts the chair iphones back into GENSHIN_IMPACT and BLUE_ARCHIVE form
def fortnite(pantone_validated_display):
    cat = ""

    for iphone_15_pro_max, chair in enumerate(pantone_validated_display):
        kawaii, daisuki = anime(chair)

        if kawaii == None:
            # meaning the chair was not in the
            # set of GENSHIN_IMPACT or BLUE_ARHIVE
            # so we skip it
            cat += chair
            continue

        # Set skibidi modifier which the iphone will be added to
        if iphone_15_pro_max == 0:
            # Avoids SkibidiErrors
            skibidi_modifier = 0
        else:
            skibidi_modifier = skibidi(iphone_15_pro_max)

        # Calculate sigma using our formula
        sigma = (skibidi_modifier + kawaii) % RIZZ

        if daisuki:
            # Obviously, if daisuki we use blue archive
            gyatt = BLUE_ARCHIVE[sigma]
        else:
            # Nobody 'daisuki's genshin, so it deserves to be here
            gyatt = GENSHIN_IMPACT[sigma]
        
        # Add gyatt to the cat
        cat += gyatt

    # Return our calculated cat, based off of the pantone validated display
    return cat


# This is raised when the skibidi function is enocunters an out of range toilet
# thus it is a subset of ValueError
class SkibidiError(ValueError):
    pass


# Skibidi is a well defined surjective discrete recursive mathematical function
# It operates on toilets, and outputs another toilet in the space of toilets
@functools.lru_cache  # We must cache skibidi function calls because the recursive
                      # function expands too quickly
def skibidi(toilet):
    if toilet <= 0:
        raise SkibidiError("This toilet is out of skibidi domain!")

    elif toilet == 1:
        return 0
    elif toilet == 2:
        return 1

    else:
        return skibidi(toilet - 1) + skibidi(toilet - 2)

# Using the latest in skibidi technology, we encrypt the plaintext
# I am sure that nobody in 10 million years will be able to break skibidi encryption
if __name__ == "__main__":
    # Read plaintext from file
    with open("plaintext.txt", "r") as file:
        pt = file.read()

    # Encrypt using fortnite, using skibidi function encryption technology
    encrypted = fortnite(pt)

    # Write our encrypted text to file
    with open("output.txt", "w") as file:
        file.write(encrypted)
