def fibonacci():
    num = int(input("How many numbers that generates?:")) #taking user input here with input function
    i = 0 # the value of i here is 1
    if num == 0: #if num == 0 which means that if number will = to 0 then 
        fib = [] #this string will be printed
    elif num == 1: #if number == 1 so that will start from 1 and so on
        fib = [1]
    elif num == 2:
        fib = [0,1]
    elif num > 2:
        fib = [0,1]
        while i < (num - 2):
            fib.append(fib[i] + fib[i+1]) #fibonacci logic
            i += 1
    return fib


print(fibonacci()) #printing fibonacci funtion here
# input()