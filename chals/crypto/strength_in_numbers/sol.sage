from Crypto.Util.number import long_to_bytes
from output import e, n, c

# You could also use this: https://www.alpertron.com.ar/ECM.HTM
factors = ecm.factor(n)
phi_n = 1
for f in factors:
    phi_n *= f - 1
d = pow(e, -1, phi_n)
m = pow(c, d, n)
FLAG_bytes = long_to_bytes(m)
print(FLAG_bytes.decode("utf-8"))

