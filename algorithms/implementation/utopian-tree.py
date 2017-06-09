def hightCycler(nr):
    hight = 1
    if nr >= 1:
        # hight = 2
        for x in range(0, nr):
            if x % 2 == 0:
                hight *= 2
            else:
                hight += 1
        return hight
    else:
        return hight


# number of tests. This is the first input
nr = int(input("numarul de teste :"))

for x in range(0, nr):

    test = int(input("cate cicluri :"))
    res = hightCycler(test)
    print("inaltimea este :", res, "m")
