import binascii 

c = int('612c0496141e3bb1fae92923929ba5f8', 16)

# You can find these however you want (factordb, wolfram alpha, brute force, etc)
p = 17378651858107286503
q = 12428326454008306487

# public key
n = p*q
e = 17

totient = (p-1)*(q-1)

# this is "fast" in sage, use pow(e, -1, totient) in python 3.8+, cry in python < 3.8
d = pow(e, -1, totient)
print(d)

solved_m = pow(c, d, n)
print(binascii.unhexlify(hex(int(solved_m))[2:]))