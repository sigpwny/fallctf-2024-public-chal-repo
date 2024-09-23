# Bug Bounty 2

## Guidance for admins/helpers giving hints
- This time, you need to overwrite `number` to be equal to `0xdeadbeef`
- Encourage them to play with different inputs, experimenting with how it looks in the printed stack visualization (gets displayed every time you run the challenge)
- The way the bytes of `number` are ordered is counterintuitive to beginners. This is because of endianness (x86 is little endian), which is also usually a difficult concept for beginners. You can try explaining endianness at a very high level. Also, the program prints the value of `number` at the end, so encourage people to observe a pattern with the bytes they overflow `name` with and the resulting number that gets printed (they can also see what `0xcafebabe` looks like on the stack in the initial stack visualization)
- The pwntools `p64` function can pack a number as 64-bit little endian (so instead of typing out `b'\xef\xbe\xad\xde\x00\x00\x00\x00'` you can just do `p64(0xdeadbeef)`

# Solution
Send 40 bytes to fill the name buffer followed by `p64(0xdeadbeef)` to overwrite `number` (reference `solution.py`)
