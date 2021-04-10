import sys


class BankSystem:
    amount = 0
    password = ""

    def __init__(self,am, p):
        self.amount = am
        self.password = p

    def display(self):
        print("Amount : ", self.amount)
        print("Password : ", self.password)

    def maintainAccount(self, op, am, p):
        if op == 'W':
            if self.amount <= 0 or self.amount < am:
                print("In Sufficient Balance")
            else:
                self.amount -= am
                print("Amount Withdrawn")
                print("Final Amount after withdrawn is : ", self.amount)
        elif op == 'C':
            self.amount += am
            print("Amount Creditted")
            print("Final Amount after credit is : ", self.amount)
        elif op == 'P':
            self.password = p
            print("Final Password after change is : ", self.password)
        else:
            print("Invalid option")
            sys.exit(-1)


operation = str(input("Enter the Operation to be Performed : "))

if operation == "W":
    amount = int(input("Enter the operation details : "))
    obj1 = BankSystem(1234,'pass')
    obj1.display()
    obj1.maintainAccount(operation,amount,'')
elif operation == "C":
    amount = int(input("Enter the operation details : "))
    obj1 = BankSystem(1234,'pass')
    obj1.display()
    obj1.maintainAccount(operation,amount,'')
elif operation == "P":
    password = str(input("Enter the password to be updated : "))
    obj1 = BankSystem(1234,'pass')
    obj1.display()
    obj1.maintainAccount(operation, 0, password)
else:
    print("Invalid option")
    sys.exit(-1)
