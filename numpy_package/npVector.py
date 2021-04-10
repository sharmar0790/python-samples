import numpy as np
import random as rn

arr = [0 for i in range(30)]

for i in range(30):
    arr[i] = rn.randint(1,1000)

print(arr)

data = np.mean(arr)

print("Mean === ",data)