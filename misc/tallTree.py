length_of_tree = input("Enter the length of the tree : ")
length_of_tree = int(length_of_tree)

spaces = length_of_tree - 1
hashes = length_of_tree - spaces
actual_length = length_of_tree
while length_of_tree != 0:
    for i in range(spaces):
        print(" ", end="")
    for j in range(hashes):
        print("#", end="")
    print()
    spaces -= 1
    hashes += 2
    length_of_tree -= 1

spaces = 0
hashes -= 2
while length_of_tree <= actual_length:
    for i in range(spaces):
        print(" ", end="")
    for j in range(hashes):
        print("#", end="")
    print()
    spaces += 1
    hashes -= 2
    length_of_tree += 1



