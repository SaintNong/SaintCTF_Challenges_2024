from Crypto.Util.number import bytes_to_long
import math

# Load flag to be encrypted
with open("flag.txt", "r") as file:
    flag = file.read() # Get flag

# Encode flag to be a number
m = bytes_to_long(flag.encode())


# Begin RSA-ing
n = 179769313486231590772930519078902473361797697894230657273430081157732675805513383277446882993888727857037846813333674683106592539325607511279964508299045249288187728675124326542901861119507442246935883558453107746437341710670564148205252095331183806257742567461705578993551762233272971788549927725822310484299
# You don't get p and q this time hahahaha
# I wrote my own prime generator!
# I'm sure it is secure :P

# A very commonly used modulus, part 1 of public key
e = 65537
print("e:", e)

# The modulus, part of 2 public key
print("n:", n)

# Perform encryption to get the ciphertext
c = pow(m, e, n)
print("c:", c)


# Good luck finding the message :)
print("m: ?")
