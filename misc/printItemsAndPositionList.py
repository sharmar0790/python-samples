

n1 = int(input("Enter the count of the numbers to be entered : "))

l = list()
for i in range(1,n1+1):
    n2 = int(input("Enter the numbers for the list : "))
    l.append(n2)

print("final list as : ", l)

for j in l:
    print("This number - %d is present at location %d" %(j,l.index(j)))


