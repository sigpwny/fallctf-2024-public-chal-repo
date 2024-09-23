# pwntools - beginner

## Guidance for admins/helpers giving hints

- You just have to input the value of `password` to get the flag (defined in `challenge.c`)
- However, people might find it difficult to enter it into the terminal manually, as the bytes aren't alphanumeric. Tell them to send it using pwntools (reference `starter.py`)

## Solution
Send b'\xde\xca\xfb\xad' over pwntools. This requires modifying one line in the starter script.
