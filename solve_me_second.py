def solveMeSecond(a, b):
    return a + b

n = int(input("input number of lines (test cases) :"))

for t in range(0, n):
    a, b = input().split()
    a, b = int(a), int(b)
    res = solveMeSecond(a, b)
    print(res)
