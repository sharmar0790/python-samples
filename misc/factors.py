

nbr = int(input("Enter the number to find the factors : "))

for i in range(1, nbr+ 1 ):
    if (nbr % i == 0):
        if i % 2 == 0:
            print("Factor is :", i , " and it is : Even")
        else:
            print("Factor is :",  i , " and it is : Odd")
