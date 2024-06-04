import math
"""
This time (hopefully) the only solution is to use math your way out
We will be using Fermat factorization
"""

# Set variables from txt file
e = 65537
n = 179769313486231590772930519078902473361797697894230657273430081157732675805513383277446882993888727857037846813333674683106592539325607511279964508299045249288187728675124326542901861119507442246935883558453107746437341710670564148205252095331183806257742567461705578993551762233272971788549927725822310484299
c = 172596549687106679413360254320186990709746394718552747980517271337165139408990524768148398011175925933687030437347090265804024118517722415894183394338638575078418870729738512514817760513469860485559808441762370732866049335513331825450542774706808672211633553807601562978250502081019197879738492061336591923319

print("n:", n)
print("c:", c)

""" New stuff here! """
# This time we aren't so lucky as to recieve p and q for free.
# The challenge description suggests that the p and q are close together
# This suggests that fermat factorization might work!
# Read: https://en.wikipedia.org/wiki/Fermat's_factorization_method

def is_square(number):
    root = math.isqrt(number)
    return root ** 2 == number


def is_square(number):
    # Use math.isqrt because the number is large
    root = math.isqrt(number)
    return root * root == number

def fermat_factorize(n, max_attempts):
    # Begin from the ceiling of square root of n and scan up
    x = math.isqrt(n) + 1

    for attempt in range(1, max_attempts + 1):
        print(f"Attempt #{attempt} - ", end="")

        # Calculate the difference of squares (x^2 - n)
        # then check if the result is a perfect square
        difference_of_squares = x * x - n

        if is_square(difference_of_squares):
            # Factorization found :D
            print("SUCCESS!!!!")

            # Factorized as (x+a)(x-a)
            a = math.isqrt(difference_of_squares)
            p = x + a
            q = x - a
            return (p, q) # return p and q
        x += 1
        print("Failed")


    raise ValueError("primes are not close enough :(")

# Factorize p and q within 10000 attempts
p, q = fermat_factorize(n, 10000)

print("p found:", p)
print("q found:", q)


""" End of new stuff """


# Find totient of n = pq
# which is equal to (p-1) * (q-1)
# (proof is left as an exercise to the reader)
phi = (p-1) * (q-1)

# Find private key d using totient
# d is the modular multiplicative inverse of e, mod phi
# this is now much easier in python 3.8+ (thanks python!)
d = pow(e, -1, phi)

# Decode ciphertext using private key d
m = pow(c, d, n)

# Convert message back to bytes
# Insert here
message_bytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')
print(message_bytes.decode())
