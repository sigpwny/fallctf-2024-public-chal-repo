import time


def compare(left, right):
    # slow down our comparison to avoid hitting rate limit
    time.sleep(1)
    if len(left) != len(right):
        return False
    elif len(left) == 0 and len(right) == 0:
        return True
    elif left[0] != right[0]:
        return False
    else:
        return compare(left[1:], right[1:])


with open("/flag.txt") as f:
    flag = f.read().strip()
user_input = input("What is the flag?\n")

if (compare(user_input, flag)):
    print("That is correct!")
else:
    print("Wrong flag!")
