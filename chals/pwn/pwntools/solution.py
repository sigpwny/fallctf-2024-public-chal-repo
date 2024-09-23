from pwn import *

# Connect to the instance
conn = remote('chal.fallctf.com', 5000)
# Use process() for local challenge files.
# conn = process('./challenge')

# Receive the prompt
conn.recvuntil(b'> ')

# Send the payload
conn.sendline(b'\xde\xca\xfb\xad')

# Interact with the challenge
conn.interactive()

# can also solve with: echo -e "\xde\xca\xfb\xad" | nc chal.fallctf.com 5000