import re

s = input("Enter the string: ")

print("Entered string is : ",s)
flag = 0
while True:
    if not re.search("[a-z]",s):
        flag=-1
        break
    elif not re.search("[0-9]",s):
        flag = -1
        break
    elif not re.search("[A-Z]",s):
        flag=-1
        break
    elif not re.search("[$@#]",s):
        flag=-1
        break
    elif len(s) <= 6 or len(s) > 12:
        flag=-1
        break
    else:
        flag=0
        print("Valid Password")
        break

if flag==-1:
    print("Invalid password")



