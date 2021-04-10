

x,y = 3,5

r = list()
for i in range(0,x):
    l = list()
    for j in range(0,y):
        if 0 < j < y and 0 < i < x:
            l.append(j*i)
        else:
            l.append(0)

    r.append(l)

print(r)
