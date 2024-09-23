# Bug Bounty 3

## Guidance for admins/helpers giving hints
- Need to overwrite the return address this time (tell them to look at pwn guides if they don't know what that is). Is there a function we can make the return address point to in order to print the flag?
- They can use gdb or objdump to find the address of `print_flag`, this is in the challenge hints though so they should already know the commands. There's no PIE, so the address of `print_flag` is always the same
- After figuring out that address, this challenge becomes pretty similar to the previous one. They can use the stack visualization to determine the number of bytes to overflow

# Solution
Overwrite the return address to `0x401216` (addr of win func) so that the program prints the flag after the main function completes
 
