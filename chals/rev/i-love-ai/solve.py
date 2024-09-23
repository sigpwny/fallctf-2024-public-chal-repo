import hashlib
large_num = 10602469122775137520271714710689700036283511162045136025617737553145049925831233503427787459248513684058256
large_num -= 414 #stupid matrix lol

for num_char in range(1,100):
    this_answer = ""
    this_num = large_num
    for i in range(num_char-1,-1,-1):
        try:
            this_loop = this_num % 1337
            this_num = this_num // 1337
            this_loop -= (int(hashlib.sha256(str(i).encode()).hexdigest(),16) % 1111)
            this_answer += chr(this_loop)
        except:
            break

    if this_answer.startswith("fallctf"):
        print(this_answer)
