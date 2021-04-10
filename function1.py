def solve_eq(equation):
    x,add,num_1,equal,num_2=equation.split()
    num_1,num_2=int(num_1),int(num_2)
    return "x = " + str(num_2 - num_1)


print(solve_eq("x + 4 = 9"))