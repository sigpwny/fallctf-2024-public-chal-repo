from Crypto.Util.number import getPrime, bytes_to_long
from secret import FLAG

def main():
    # For those unfamiliar with RSA:
    # https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Operation

    e = 65537
    n = 1
    for _ in range(10):
        n *= getPrime(64)

    FLAG_bytes = FLAG.encode("utf-8")   # string -> bytes
    m = bytes_to_long(FLAG_bytes)       # bytes -> number
    c = pow(m, e, n)                    # c = m^e (mod n)

    with open("output.py", "a") as out:
        out.write(f"e = {e}\n")
        out.write(f"n = {n}\n")
        out.write(f"c = {c}\n")

if __name__ == "__main__":
    main()
