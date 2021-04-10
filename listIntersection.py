
l = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]

print("First list is : ",l)
print("Second list is : ",l2)

l3 = [value for value in l if value in l2]

print("Final  list is : ",l3)