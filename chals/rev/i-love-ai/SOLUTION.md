pyc is compiled python file. https://pylingual.io/ is a good onliner decompiler that decompile the file perfectly.

Many excessive lines can be removed, including the lucky number part and tensorflow and torch part. The matrices can be calculated by hand.

The length needs to be bruteforced, but the algorithm stays the same.
Notice the algorithm * 1337, then add character ascii, then add a predicable hex number % 1111
Since ascii + < 1111 is always smaller than 1337, we can savely extract each character by % 1337
Then subtract the given hash

To check if we get the flag, we can check if the string begins with fallctf