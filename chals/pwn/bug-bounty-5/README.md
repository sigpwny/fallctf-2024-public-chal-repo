# Bug Bounty 5

## Guidance for admins/helpers giving hints
- I'll assume they already know how the shellcode stuff works since they probably solved Bug Bounty 4 before this (if not, tell them to solve that first)
- New vulnerability! This time, we don't just print a stack address for them, they have to leak it using a format string exploit.
- They can send `b"%p %p %p %p %p %p %p ..."`to format things off the stack as pointers. Could one of these be a stack address? Encourage them to compare the pointers printed by the format string to what shows up in the stack visualization (this time, there's only a stack visualization at the end of the program to prevent leaking anything for them).
- To access a the `n`'th format string argument (or in this case, the `n`'th thing off the stack) and format as a pointer, they can send `%<n>$p` (for example, `%5$p`)

# Solution
First send `%14$p` to leak a stack address with the format string. Specifically, this is the saved base pointer for the current stack frame. Then, with the stack leak, you can do a shellcode exploit as normal, i.e. overwrite the return address to point to your shellcode, as in the previous challenge. 
