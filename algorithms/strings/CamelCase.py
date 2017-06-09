#!/bin/python3

# string = input().strip()
string = "testCamelCase"

nr = 0

for x in string:
    if (x.istitle()):
        nr += 1

if (string[0]):
    nr += 1

print(nr)
