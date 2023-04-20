
sentence = input("Enter the input sequence : ")

splittedData = list(sentence)
print(splittedData)
letter = 0
digit = 0
for temp in splittedData:
    if temp.isdigit():
        digit += 1
    else:
        letter += 1


print("Letter count : ", letter)
print("Digit count : " , digit)


