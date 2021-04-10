
number = "0100,0011,1010,1001"

arr = number.split(",")

re = list()
for i in arr:
    a = int(i,2)
    if a%5==0:
        re.append(a)

re1 = list()
for j in re:
    re1.append(format(j,'b'))

print(re1)
