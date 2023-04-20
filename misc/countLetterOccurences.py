
s = input("Enter the string : ")

print("Entered string is : ",s)
d = {}
l = list(s)
for i in l:
    if i in d:
        d[i] = d.get(i)+1
    else:
        d[i]=1

for k,v in d.items():
    print(k,v)

