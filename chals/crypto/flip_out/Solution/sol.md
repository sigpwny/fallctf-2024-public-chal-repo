# Solution

Examining the chal setup shows that the iv is always connected to the front part of the token when it is first generated. Furthermore, the information about whether or not the user is an admin is also there in the next block. In addition, we also don't have any checks against username/passwords that are empty strings. Furthermore, the state of the padding after the admin info isn't checked. This makes it very easy to do a **bit flip** attack.


The idea is that we first generate a token against an empty username/password

This means that the token would be of the form

`iv|{"admin": 0}\x04\x04\x04\x04`

Due to the fact that `AES_CBC` uses fixed blocks of 16 bytes, and regular PKCS padding was used, `{"admin": 0}` being 12 bytes leaves `4` bytes of `\x04` remaining to be added as padding to the next block.


The idea of the attack is to modify the `IV` such that upon decryption/read of the token, the next block will have `{"admin": 1}` read.

Using `AES_CBC` rules, this goes down to calculating
`IV ^ original ^ target`. This will modify the IV in the bits that will correspond to the change rippling into the next block (admin field), turning the `0` into a `1`.

This is the main part of the attack from the solution file:

```py
token = bytes.fromhex(get_token())

iv = token[:16]
blocks = token[16:]

orig = b'{"admin": 0}\x04\x04\x04'
targ = b'{"admin": 1}\x04\x04\x04'

iv = xor(iv, orig, targ)
token = (iv + blocks).hex()
send_token(token)
```

