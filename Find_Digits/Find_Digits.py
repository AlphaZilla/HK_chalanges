N = int(input())

for _ in range(N):
    cNr = int(input())
    count = 0
    for digit in str(cNr):
        # print(digit)
        try:
            if cNr % int(digit) == 0:
                # print("Is even")
                count +=  1
        except ZeroDivisionError:
            # print("Not even")
            pass
    print(count)
