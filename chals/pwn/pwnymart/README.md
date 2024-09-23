# PwnyMart

Welcome to pwn! In many pwn challenges (and in real world pwn), the ultimate goal is to achieve _Remote Code Execution (RCE)_ or arbitrary code execution. At a high level, this means that we get the vulnerable program or process to execute code that we want, rather than the code it's ordinarily meant to execute. Since our malicious code will often run with the same privilege and access given to the the original program, this can be a very powerful attack technique. 

While this is a bit of an oversimplification, in a lot of pwn, RCE is achieved in the same broad way: we leak the value of some function pointer, write the function pointer to a memory location that's supposed to store another function pointer, and then get the program to call our malicious function pointer. 

These individual steps are usually achieved by using pwn _primitives_ gained from exploiting vulnerabilities like buffer overflows, heap vulnerabilities, etc. in the target program. In the rest of the pwn suite you will practice exploiting some of these vulnerabilties, but this challenge is meant to give you the chance to carry out the overall three-step process. 

So, to solve this challenge, you should do the following:

1. Leak the address of a useful function. Your ultimately goal is to be able to read the flag.txt file, so this should help you figure out what a useful function looks like. 

2. Find a memory location that contains a function pointer where you can write the address of the function you found in Step 1, and write the address to that location. 

3. Get the program to jump to the address stored in the memory location you found in Step 2. That is, get the program to call your useful fuction from Step 1. 

If you are unfamiliar with function pointers, here are a couple of resources:

- https://en.wikipedia.org/wiki/Function_pointer
- https://stackoverflow.com/questions/840501/how-do-function-pointers-in-c-work

TL; DR: a function pointer stores the starting address of a function in memory. 
