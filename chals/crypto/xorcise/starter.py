import string

ciphertext_hex = your ciphertext goes here!
ciphertext = bytes.fromhex(ciphertext_hex)

# helpful function!
def is_printable_ascii(byte_array):
    try:
        message = byte_array.decode('utf-8')
        return all(c in string.printable for c in message)
    except UnicodeDecodeError:
        return False