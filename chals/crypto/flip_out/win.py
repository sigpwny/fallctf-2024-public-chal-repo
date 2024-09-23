from pwn import *

def get_token():
    uname = ""
    pword = ""
    p = remote('chal.fallctf.com', 6000)
    p.recvuntil(b": ")
    p.sendline(b"1") #log in with creds
    p.recvuntil(b": ")
    p.sendline(uname.encode())
    p.recvuntil(b": ")
    p.sendline(pword.encode())
    p.recvuntil(b": ")
    token = p.recvline()[:-1].decode()
    p.close()

    return token

def send_token(token):
    p = remote('chal.fallctf.com', 6000)
    p.recvuntil(b": ")
    p.sendline(b"2")
    p.recvuntil(b": ")
    p.sendline(token.encode())
    p.recvline()
    print(p.clean().decode())
    p.close()


token = bytes.fromhex(get_token())

iv = token[:16]
blocks = token[16:]

orig = b'{"admin": 0}\x04\x04\x04'
targ = b'{"admin": 1}\x04\x04\x04'

iv = xor(iv, orig, targ)
token = (iv + blocks).hex()
send_token(token)
