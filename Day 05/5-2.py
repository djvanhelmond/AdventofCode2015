#! /usr/bin/python

filename = './input'

naughty = 0
nice = 0

def isnice ( line ):
  vowels = ['a', 'e', 'u', 'i', 'o']
  doubles = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
  disallowed = ['ab', 'cd', 'pq', 'xy']
  
  # contains three vowels (aeiuo)
  j = 0
  for i in range(0, len(line)):
    if line[i] in vowels: 
      j += 1
  if j < 3:
    print "no 3 vowels"
    return False
    
  # at least one letter twice in a row
  if sum([st in line for st in doubles]) == 0:
    print "no doubles"
    return False
    
  # does not contain 'ab', 'cd', 'pq' or 'xy'
  if sum([st in line for st in disallowed]) > 0:
    print "disallowed combination"
    return False

  print "3 vowels"
  print "double"
  print "no disallowed (ab, cd, pq, xy)"
  return True



with open(filename) as f:
  for linen in f:
    line = linen.rstrip('\n')
    if isnice(line):
      print "%s is nice" % line
      nice += 1
    else:
      print "%s is naughty" % line
      naughty += 1
    print "--"


print "naughty strings: %d" % naughty
print "nice strings %d" % nice
    
