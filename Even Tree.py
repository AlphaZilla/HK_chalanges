NM = input()
# NM = input().strip().split(" ")
# NM = input().split(" ")

print(NM)
print(type(NM))

list1 = []

for x in range(int(NM[1])):
    list1.append(input().strip().split(" "))
    # print(int(input().strip().split(" ")[0]))

print(list1)
