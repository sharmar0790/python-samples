#find the number of upper and lower case characters

str = "Hello World!!"

l = 0
u=0
for i in str:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    else:
        print("ignore")

print("Lower = %d, upper = %d" %(l,u))