import random

print(random.random)
r,c=10,10
arr = [[0 for x in range(r)] for y in range(c)]
for i in range(0,r-1):
    for j in range(0,c-1):
        arr[i][j] = random.randint(5,100)

print(arr)