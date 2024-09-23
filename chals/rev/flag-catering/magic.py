import sys

def magic(n):
    return 1 if n == 0 else sum([
        magic(i) * magic(n - i - 1) for i in range(n)
    ])

offsets = [-101, -96, -106, -103, -85, -74, 30, 306, 1331, 4765, 16680, 58689, 207896, 742789, 2674330, 9694740, 35357571, 129644693, 477638592, 1767263082, 6564120299, 24466266925, 91482563525, 343059613542, 1289904147213, 4861946401333, 18367353072057, 69533550915905, 263747951750263, 1002242216651260, 3814986502092205, 14544636039226792, 55534064877048090, 212336130412243013, 812944042149730648, 3116285494907301157, 11959798385860453381, 45950804324621742254, 176733862787006701275]

def main():
    print('The flag is: ', end="")
    for i in range(len(offsets)):
        print(chr(magic(i) - offsets[i]), end="")
        # flush stdout
        sys.stdout.flush()

if __name__ == '__main__':
    main()