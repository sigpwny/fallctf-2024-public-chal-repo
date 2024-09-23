# Bug Bounty 4

## Guidance for admins/helpers giving hints
- No more print_flag function. They need to execute their own shellcode. I put a link to some shellcode in the hints, if they're confused/curious as to what is does, tell them it pops a shell (and explain what that means)
- The program leaks the address of the `name` buffer on the stack. This is helpful for figuring out what to overwrite the return address to
- They can generate the actual bytes for the shellcode using the pwntools `asm` function

# Solution
Put shellcode on the stack (in the `name` buffer) and overwrite the return address to point to that shellcode (as always, look at `solution.py` for reference)
