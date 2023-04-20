class Dog:
    @staticmethod
    def print_sum(*args):
        sum_1=0
        for i in args:
            sum_1 += i
        return sum_1

    
def main():
    sum_2 = Dog.print_sum(1,2,3,4,7,8,9)
    print(sum_2)


main()