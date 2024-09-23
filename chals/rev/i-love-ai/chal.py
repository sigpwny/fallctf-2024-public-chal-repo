import random
import time
import hashlib
import tensorflow as tf
import torch
import numpy as np

while True:
    lucky = int(input("What's your lucky number? "))
    if lucky >= 1:
        break
    else:
        print("Your number is too small. Try again")

prompt = "Please validate your flag here: "
for char in prompt:
    time.sleep(lucky)
    print(char,end="",flush=True)

input_flag = input()

mat1 = np.array([[12,23,34],[45,56,67]])
mat2 = tf.constant(mat1)
mat3 = torch.Tensor(mat1 - 10)
newmat = mat2+mat3


list1 = []

for char in input_flag:
    list1.append(ord(char))

num1 = 0

for i in range(len(list1)):
    num1 *= 1337
    num1 += list1[len(list1)-i-1]
    num1 += int(hashlib.sha256(str(i).encode()).hexdigest(),16) % 1111

num1 = num1 + np.sum(newmat)

if num1 == 10602469122775137520271714710689700036283511162045136025617737553145049925831233503427787459248513684058256:
    print("Your flag is correct.")
else:
    print("Your flag is wrong")
