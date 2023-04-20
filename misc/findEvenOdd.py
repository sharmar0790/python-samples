

n1 = int(input("Enter First number : "))
n2 = int(input("Enter Second number : "))

for i in range(n1, n2+1):
    if i % 2 == 0:
        print(" %d is a even number." %(i))
    else:
        print(" %d is a odd number." %(i))