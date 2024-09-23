from math import factorial

def black_magic(n):
    # catalan number (2n+1 choose n)
    return ((factorial(2 * n + 1) // (factorial(n + 1) * factorial(n))) // (2 * n + 1))

flag = 'fallctf{catatonically_slow_calculation}'
def main():
    offsets = []
    for i in range(len(flag)):
        print(i, black_magic(i))
        offsets.append(black_magic(i) - ord(flag[i]))
    print(offsets)
main()