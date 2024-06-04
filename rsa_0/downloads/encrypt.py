from Crypto.Util.number import getPrime, bytes_to_long
import math

# Load flag to be encrypted
with open("flag.txt", "r") as file:
    flag = file.read() # Get flag

# Encode flag to be a number
m = bytes_to_long(flag.encode())


# Begin RSA-ing
p = getPrime(512) # 512-bit prime
q = getPrime(512) # 512-bit prime


n = p * q

# A very commonly used modulus, part 1 of public key
e = 65537
print("e:", e)


# Debug code, will definitely be deleted in prod
# WARNING: This MUST be deleted in production
# If this is not deleted we are in big trouble!
print("p:", format(p))
print("q:", format(q))

# The modulus, part of 2 public key
print("n:", n)

# Perform encryption to get the ciphertext
c = pow(m, e, n)
print("c:", c)


# Good luck finding the message :)
# The factorization (the hard pard) has already been done for you!
print("m: ?")
