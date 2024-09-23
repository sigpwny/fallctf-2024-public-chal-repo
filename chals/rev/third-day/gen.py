flag = "fallctf{610_jellybean_jira_ticket}"

import random

def gen():
    assert len(flag) == 34
    seq1 = []
    flag2 = []
    seq3 = []
    seq4 = []

    # solve: (seq1 ^ seq2) << seq3 == seq4

    # program: (seq4 >> seq3 == (key ^ flag)) ^ seq1 ^ flag == 0

    for i in range(len(flag)):
        key = random.randint(0, 255)
        seq1.append(key)
        flag2.append(ord(flag[i]))
        seq3.append(random.randint(1, 4))
        seq4.append((seq1[i] ^ flag2[i]) << seq3[i])


    seq3 = seq3[::-1]
    new_seq1 = [None for _ in range(34)]
    for i in range(len(seq1)):
        new_seq1[(3*i)%34] = seq1[i]
    # for i in range(len(seq4)):
    #     print(chr((seq4[i] >> seq3[33 - i]) ^ seq1[i]), end='')
    
    # (3 * i) % 34
    # new seq1 

    
    print(f'const int seq1[] = {{{", ".join(map(str, new_seq1))}}};')
    # print(f'const int flag2[] ={{{", ".join(map(str, flag2))}}};')
    print(f'const int seq3[] = {{{", ".join(map(str, seq3))}}};')
    print(f'const int seq4[] = {{{", ".join(map(str, seq4))}}};')

    # print(len(new_seq1), len(seq3), len(seq4))
    # for i in range(len(seq4)):
    #     print(chr((seq4[i] >> seq3[33 - i]) ^ new_seq1[(3 * i) % 34]))
gen()