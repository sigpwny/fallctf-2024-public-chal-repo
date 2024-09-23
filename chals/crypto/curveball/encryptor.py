from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib
import os

def encrypt_flag(shared_secret: int, iv: str, flag: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    
    # Encrypt the flag
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(flag.encode('ascii'), 16))
    
    return ciphertext.hex()

shared_secret = 'df700d2f1344ef3bdc60394e643af298fe7983f34f73da973797ecfb4a790575'  # Replace with your actual shared secret
iv = os.urandom(16)  # Randomly generate a 16-byte IV

# Flag to encrypt
flag = "fallctf{n0t_s0_s3cr3t_anYm0r3}"

# Encrypt the flag
ciphertext = encrypt_flag(shared_secret, iv, flag)

# Print the IV and encrypted flag in hexadecimal format
print("IV:", iv.hex())
print("Encrypted flag:", ciphertext)