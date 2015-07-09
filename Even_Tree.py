NM = map(int, input().strip().split(" "))

edges = []

for x in range(NM[1]):
    edges.append(map(int, input().strip().split(" ")))

for edge in edges:
    print(edge)
