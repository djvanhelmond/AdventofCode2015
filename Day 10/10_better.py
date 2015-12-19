#! /usr/bin/python

from itertools import groupby

input = "1321131112"
n = 40

def lookandsay( instr ):
  newstr = ""
  repeats = [list(g) for k, g in groupby(str( instr ))]
  for group in repeats:
    newstr += str(len(group)) + str(group[0])
  return newstr

for r in range(n):
  input = lookandsay ( input )
print len(input)

