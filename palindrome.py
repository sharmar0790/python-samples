

n1 = int(input("Enter the number to be verified as a palindrome : "))

print("Entered number is : ", n1)

splittedNumberList = list(str(n1))

reversedStr = ""
for i in reversed(splittedNumberList):
    reversedStr += i

print(reversedStr)
if reversedStr == str(n1):
    print("Number is a palindrome")
else:
    print("Number is a not a palindrome")