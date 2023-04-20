

s = input("Enter the string: ")

print("Entered string is : ",s)
l = list(s)
newString = ""
for temp in l:
    if temp.isalpha() and l.index(temp) % 2 == 0:
        newString+=temp

print("Reversed string into list is as : ",newString)

