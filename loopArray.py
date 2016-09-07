def loopArray(l, r):
  global nr, value
  dif = (r - l) + 1

  for x in range(l, r + 1):
    nr.append(x)

  for x in range(0, dif):
    for i in range(0, dif):
      if nr[x] == nr[i]:
        value += "0"
      else:
        value += "1"

  return nr, value

value = ""
nr = list()

print(loopArray(10, 15))
