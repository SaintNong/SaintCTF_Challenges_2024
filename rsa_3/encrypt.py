from Crypto.Util.number import getPrime, bytes_to_long

with open("flag.txt", "r") as file:
    msg = file.read().strip().encode("utf-8")
    m = bytes_to_long(msg)

# Key-gen
e = 3
p, q = getPrime(512), getPrime(512)
N = p*q

# Get ciphertext
c = pow(m, e, N)

# Print public key
print("e =", e)
print("c =", c)
print("N =", N)

