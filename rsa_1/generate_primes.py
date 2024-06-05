import random
import math


# Primality test
# Test prime n for k tests
# Read: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    # Write n-1 as d*2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        d >>= 1
        r += 1
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Finds the first prime by scanning upwards from n
def find_prime(n, k, n_tests):

    # Scan upwards until prime test succeeds
    i = 0
    while True:
        number = n + i
        if miller_rabin(number, n_tests):
            # Prime found!!
            return number

        i += 1


# Close-ish n1 and n2
# differing around the second half of the digits
n1 = 2 ** 512
n2 = 2 ** 512 + 2 ** 259 + 2 ** 169 + 2 ** 69 + 420 + 69 + 161660

k = 1000
n_tests = 1000

# Find p and q (which will be close to each other)
p = find_prime(n1, k, n_tests)
q = find_prime(n2, k, n_tests)
n = p * q

# Print
print("p:", p)
print("q:", q)
print("n:", n)
