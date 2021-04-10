# prog to remove the duplicate and sort the sequence

input = "hello world and practice makes perfect and hello world again"

l = input.split(" ")
print(l)
b = set(l)
print(' '.join(sorted(b)))
