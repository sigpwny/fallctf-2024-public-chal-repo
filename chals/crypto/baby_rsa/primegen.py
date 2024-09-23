from Crypto.Util.number import long_to_bytes, bytes_to_long
import random

#use the miller-rabin primality test to generate 2 random large primes
def miller_rabin(n, k=40):
    if n in [2, 3]: return True
    if n < 2 or n % 2 == 0: return False
    r, d = 0, n - 1
    while d % 2 == 0: r, d = r + 1, d // 2
    def witness(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1: return True
        return any(pow(x, 2**i, n) == n - 1 for i in range(r-1))
    return all(witness(random.randint(2, n - 2)) for _ in range(k))
def generate_large_prime(bits):
    gen_candidate = lambda : random.getrandbits(bits) | 1 | (1 << bits - 1)
    return next(filter(miller_rabin, iter(lambda: gen_candidate(), None)))

# Generate two 1024-bit primes for RSA
prime1 = generate_large_prime(64)
prime2 = generate_large_prime(64)

print(f"p = {prime1}")
print(f"q = {prime2}")