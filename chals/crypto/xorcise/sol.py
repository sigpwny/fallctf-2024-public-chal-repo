import string

ciphertext_hex = "5b5c51515e495b464e54504d51586245524f40"
ciphertext = bytes.fromhex(ciphertext_hex)

def is_printable_ascii(byte_array):
    try:
        message = byte_array.decode('utf-8')
        return all(c in string.printable for c in message)
    except UnicodeDecodeError:
        return False

for key in range(256):  
    decrypted_message = bytes([c ^ key for c in ciphertext])
    
    # Check if the decrypted message is readable
    if is_printable_ascii(decrypted_message):
        print(f"Key: 0x{key:02X}")
        print(f"Decrypted message: {decrypted_message.decode()}")
        print("-" * 40)