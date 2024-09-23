## The solution file.
import hashlib
def modinv(a, p):
    """ Return the modular inverse of a mod p using the extended Euclidean algorithm """
    if a == 0:
        return 0
    lm, hm = 1, 0
    low, high = a % p, p
    while low > 1:
        ratio = high // low
        nm, new = hm - lm * ratio, high - low * ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % p

def elliptic_curve_add(P, Q, a, p):
    """ Add two points P and Q on an elliptic curve with given parameters """
    if P is None:
        return Q
    if Q is None:
        return P
    if P == Q:  # Point doubling
        x1, y1 = P
        if y1 == 0:
            return None  # Point at infinity
        lam = (3 * x1**2 + a) * modinv(2 * y1, p) % p
    else:  # General point addition
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and y1 != y2:
            return None  # P + Q = O (point at infinity)
        lam = (y2 - y1) * modinv(x2 - x1, p) % p

    x3 = (lam**2 - x1 - (x2 if P != Q else x1)) % p
    y3 = (lam * (x1 - x3) - (y1 if P != Q else y1)) % p

    return (x3, y3)

def legendre_symbol(a, p):
    """ Compute the Legendre symbol a|p. Returns 1 if a is a quadratic residue mod p, -1 otherwise """
    return pow(a, (p - 1) // 2, p)

# calculate modular square root from y using legendre symbol
def mod_sqrt(a, p):
    """ Compute the modular square root of a mod p, if it exists """
    if legendre_symbol(a, p) != 1:
        return None  # no sqrt exists
    if a == 0:
        return 0
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    # For general case where p % 4 != 3, use Tonelli-Shanks or other methods
    raise NotImplementedError("General modular square root not implemented")

def elliptic_curve_mult(P, k, a=123001240123101920407, p=269123855285160332211801709888382470147):
    """ Perform scalar multiplication using the double-and-add method """
    result = None  # Start with the point at infinity
    addend = P

    while k > 0:
        if k & 1:
            result = elliptic_curve_add(result, addend, a, p)
        addend = elliptic_curve_add(addend, addend, a, p)
        k >>= 1

    return result

# Curve parameters
a = 123001240123101920407
b = 2390490212093
p = 269123855285160332211801709888382470147
G = (141223464919893415164492319302044521923, 105945507900846830121381021840356606089)


Q_a_x = 19299658936035824596857706134874824001
y_squared = (Q_a_x**3 + a * Q_a_x + b) % p
y = mod_sqrt(y_squared, p)
Q_a = (Q_a_x, y)

#secret:
n_B = 853735663
S = elliptic_curve_mult(Q_a, n_B)
print(f"The shared secret S(x, y) = {S}")
secret = hashlib.sha256(f"{S[0]}".encode('utf-8')).hexdigest()
print(f"Shared secret to use: {secret}")
