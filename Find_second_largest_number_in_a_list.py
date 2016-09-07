N = int(input().strip())

# use a List Comprehensions method to convert to int all the numbers
L = list(int(x) for x in input().strip().split(" "))

# find the biggest int in original list
# loop till all the occurrence are removed
for x in range(L.count(max(L))):
    L.remove(max(L))

# print the biggest int from the original list
print(max(L))

