import time
from Crypto.Util.number import bytes_to_long



def long_to_bytes(data):
    message_bytes = data.to_bytes((data.bit_length() + 7) // 8, 'big')
    return message_bytes.decode()
    

# Get message from file
with open("redact.txt", "r") as file:
    msg = file.read().strip()

# Process known parts of message to m_0
m0 = bytes_to_long(msg.replace("X", "\x00").encode("utf-8"))

# Insert flags
e = 3
c = 71864217135137708992392634250454877135167974386857209692296652483223474398571286595142143507760696539557718383726560248230902947395309631317124838239302352527527836928616814325165776437437482016873949855126380800934857166406087752368296802525608589871991415095441256563882042600803488384825351320059497469052
N = 93819257989829571430664208183713951831975055753964162947526176998466113750259232571208125649000642389398166642060616112688288011600946399691703059644459388992441400878305027931479485983780500803912757250487057810250168702297243860033071920490077615110671213670757041229901954139146958933264829956048861122263

# Create polynomial ring
P.<x> = PolynomialRing(Zmod(N), implementation="NTL")

# Start timer
start_time = time.time()

# Polynomial ring over N is defined as
# (m0 + x)^e - c (mod N)
pol = (m0 + x) ^ e - c
roots = pol.small_roots(epsilon=1/30)

if not roots:
    raise ValueError("oops look like it no work")

# Check time elapsed
time_elapsed = time.time() - start_time
print(f"Root found in: {time_elapsed:.3g}s")


for root in roots:
    print(f"Flag: {long_to_bytes(int(root))}")



