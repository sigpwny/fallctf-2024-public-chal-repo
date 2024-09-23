message = b"fallctf{fake_flag}" # Note: this is a fake flag, you need to find the real flag from the ciphertext
key = 0x??  

ciphertext = bytes([m ^ key for m in message])
ciphertext_hex = ciphertext.hex()
print(ciphertext_hex)