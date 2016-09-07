#!/usr/bin/py
# Head ends here

def lonelyinteger(b):
    ans = 0
    for x in b:
        if b.count(x) == 1:
            ans = x
    return int(ans)
# Tail starts here


if __name__ == '__main__':
    a = int(input())
    # b = map(int, input().strip().split(" "))
    b = input().strip().split(" ")
    print(lonelyinteger(b))
    # print(b, type(b[0]))
