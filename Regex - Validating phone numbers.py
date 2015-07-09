'''
Validating phone numbers
"YES" if it is a valid number "NO" if it isn't.
using the regular expresion
'''
import re


tests = int(input())  # how many numbers test
line_input = ""

for x in range(tests):

    # take a line of text\numbers
    line_input = input()
    print(line_input)
    print(type(line_input))

    # comp = re.compile(r"[789]\d{9}")
    comp = re.compile(r"[789]\d{9}$")

    found = comp.match(str(line_input))

    if found:

        print("YES")

    else:

        print("NO")
