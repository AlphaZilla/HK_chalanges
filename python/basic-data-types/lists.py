N = int(input())  # Nr. of lines for input()

L = []

for x in range(N):

    line = list(input().strip().split(" "))

    if line[0] == "insert":
        L.insert(int(line[1]), int(line[2]))
        # print(L, "<<<insert")

    elif line[0] == "append":
        L.append(int(line[1]))
        # print(L, "<<<append")

    elif line[0] == "remove":
        L.remove(int(line[1]))
        # print(L, "<<<remove")

    elif line[0] == "pop":
        L.pop()
        # print(L, "<<<pop")

    elif line[0] == "index":
        print(L.index(int(line[1])))
        # print(L.index(int(line[1])), "<<<index")

    elif line[0] == "count":
        print(L.count(int(line[1])))

    elif line[0] == "sort":
        L.sort()
        # print(L, "<<<append")

    elif line[0] == "print":
        print(L)
        # print(L, "<<<print")

    elif line[0] == "reverse":
        L.reverse()
        # print(L, "<<<reverse")
