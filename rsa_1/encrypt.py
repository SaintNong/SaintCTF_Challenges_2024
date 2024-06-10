from Crypto.Util.number import getPrime, bytes_to_long
import math

# Load flag to be encrypted
with open("flag.txt", "r") as file:
    flag = file.read() # Get flag

# Encode flag to be a number
m = bytes_to_long(flag.encode())

# p and q are safe
p = getPrime(1024)
q = getPrime(1024)

# Begin RSA-ing
n = p*q

# 3 is safe right?
e = 3
print("e:", e)
print("n:", n)


# Perform encryption to get the ciphertext
c = pow(m, e, n)
print("c:", c)


# Good luck finding the message :)
print("m: ?")
