

nbr = int(input("Enter the number of words you want to enter and sorted : "))

l = list()
for i in range(1 , nbr + 1):
    n = input("Enter the string : ")
    l.append(n)

print("The entered list is : ", l)

#sorting the list in ascending order
l.sort()
print("The sorted list is : ", l)

