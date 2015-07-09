# number of space-separated integers
N = int(input())

# create a list from the input. Convert input to integer
N2 = list(int(x) for x in input().strip().split(" "))

tup = tuple(N2)

print(hash(tup))
