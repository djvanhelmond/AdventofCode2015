#! /usr/bin/python

input = "1321131112"
n = 40
input = input[::-1]

def lookandsay( str ):
  newstr = ""
  i = 0
  c = 1
  while (i<len(str)-1):
    if (str[i] == str[i+1]):
      c += 1
    else: 
      newstr = newstr + str[i] + `c`
      c = 1
    i += 1 
  newstr = newstr + str[i] + `c`
  return newstr

for r in range(n):
  input = lookandsay ( input )
print len(input)

