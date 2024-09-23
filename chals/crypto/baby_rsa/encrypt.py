import binascii

flag = "small_n_bad"
flag = binascii.hexlify(flag.encode("utf-8"))
m = int(flag, 16)

p = 17378651858107286503
q = 12428326454008306487
n = p*q
print(n)

e = 17
c = pow(m, e, n)

print(hex(int(c)))